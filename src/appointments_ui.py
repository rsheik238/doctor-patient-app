import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import DateEntry
import requests
import sqlite3
import sys, os
from app.infrastructure.db.sqlite_repo import SQLiteDoctorRepository, SQLitePatientRepository

API_BASE = "http://localhost:5000"
DB_PATH = "hospital.db"

root = tk.Tk()
root.title("Doctor Appointment Booking")
root.geometry("950x600")

doctor_var = tk.StringVar()
patient_var = tk.StringVar()
slot_var = tk.StringVar()
date_var = tk.StringVar()

doctor_map = {}
patient_map = {}

frame = ttk.Frame(root, padding=12)
frame.pack(fill=tk.BOTH, expand=True)

# ------------------ Data Loaders ------------------
def load_doctors():
    with sqlite3.connect(DB_PATH) as conn:
        repo = SQLiteDoctorRepository(conn)
        doctors = repo.get_all()
    doctor_map.clear()
    for doc in doctors:
        name = f"{doc.first_name} {doc.last_name}"
        doctor_map[name] = doc.id
    doctor_combo["values"] = list(doctor_map.keys())

def load_patients():
    with sqlite3.connect(DB_PATH) as conn:
        repo = SQLitePatientRepository(conn)
        patients = repo.get_all()
    patient_map.clear()
    for pat in patients:
        name = f"{pat.first_name} {pat.last_name}"
        patient_map[name] = pat.id
    patient_combo["values"] = list(patient_map.keys())

# ------------------ Appointment Logic ------------------
def fetch_slots():
    slot_listbox.delete(0, tk.END)
    appointment_table.delete(*appointment_table.get_children())

    doctor_id = doctor_map.get(doctor_var.get())
    date = date_picker.get_date().strftime("%Y-%m-%d")

    if not doctor_id:
        messagebox.showerror("Missing Info", "Please select a doctor.")
        return

    try:
        res = requests.get(f"{API_BASE}/slots/available", params={"doctor_id": doctor_id, "date": date})
        res.raise_for_status()
        slots = res.json()["available_slots"]
        for s in slots:
            slot_listbox.insert(tk.END, s)
    except Exception as e:
        messagebox.showerror("Error", f"Could not fetch slots: {e}")
        return

    try:
        booked_res = requests.get(f"{API_BASE}/appointments", params={"doctor_id": doctor_id, "date": date})
        booked_res.raise_for_status()
        visits = booked_res.json()
        for visit in visits:
            appointment_table.insert("", tk.END, values=(visit["time"], visit["patient_id"]))
    except Exception as e:
        print("Could not load existing appointments:", e)

def on_slot_select(event):
    selected = slot_listbox.curselection()
    if selected:
        slot_var.set(slot_listbox.get(selected[0]))

def book_slot():
    doctor_id = doctor_map.get(doctor_var.get())
    patient_id = patient_map.get(patient_var.get())
    date = date_picker.get_date().strftime("%Y-%m-%d")
    time = slot_var.get()

    if not all([doctor_id, patient_id, date, time]):
        messagebox.showerror("Missing Info", "Please select doctor, patient, date, and slot.")
        return

    try:
        res = requests.post(f"{API_BASE}/slots/book", json={
            "doctor_id": doctor_id,
            "patient_id": patient_id,
            "date": date,
            "time": time
        })
        if res.status_code == 200:
            messagebox.showinfo("Success", f"Slot {time} booked for {date}.")
            fetch_slots()
        else:
            messagebox.showerror("Failed", res.json().get("error", "Unknown error"))
    except Exception as e:
        messagebox.showerror("Error", f"Booking failed: {e}")

# ------------------ Widgets ------------------
ttk.Label(frame, text="Doctor:").grid(row=0, column=0, sticky="w")
doctor_combo = ttk.Combobox(frame, textvariable=doctor_var, state="readonly", width=30)
doctor_combo.grid(row=0, column=1, padx=5, pady=5)

ttk.Label(frame, text="Patient:").grid(row=1, column=0, sticky="w")
patient_combo = ttk.Combobox(frame, textvariable=patient_var, state="readonly", width=30)
patient_combo.grid(row=1, column=1, padx=5, pady=5)

ttk.Label(frame, text="Date:").grid(row=2, column=0, sticky="w")
date_picker = DateEntry(frame, textvariable=date_var, width=20, date_pattern='yyyy-mm-dd')
date_picker.grid(row=2, column=1, padx=5, pady=5, sticky="w")

ttk.Button(frame, text="Show Available Slots", command=fetch_slots).grid(row=3, column=0, columnspan=2, pady=10)

slot_listbox = tk.Listbox(frame, height=7, width=30)
slot_listbox.grid(row=4, column=0, columnspan=2, padx=5, pady=5)
slot_listbox.bind("<<ListboxSelect>>", on_slot_select)

ttk.Label(frame, text="Selected Slot:").grid(row=5, column=0, sticky="w")
ttk.Entry(frame, textvariable=slot_var, state="readonly", width=20).grid(row=5, column=1, sticky="w")

ttk.Button(frame, text="Book Slot", command=book_slot).grid(row=6, column=0, columnspan=2, pady=15)

ttk.Label(frame, text="Booked Appointments:").grid(row=7, column=0, columnspan=2, pady=(10, 0), sticky="w")

columns = ("Time", "Patient ID")
appointment_table = ttk.Treeview(frame, columns=columns, show="headings", height=8)
for col in columns:
    appointment_table.heading(col, text=col)
    appointment_table.column(col, width=150)
appointment_table.grid(row=8, column=0, columnspan=2, pady=5)

# ------------------ Init ------------------
load_doctors()
load_patients()
root.mainloop()
