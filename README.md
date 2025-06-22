# Visit Scheduler API (Flask + Clean Architecture)

A modular Python backend project for scheduling doctor-patient appointments. Built with Flask, SQLite (extensible to MySQL), and structured using Clean Architecture.

---

## Project Structure

```
doctor-patient-app/
├── src/
│   ├── app/                 # Application logic
│   └── main.py              # Entry point
├── tests/                   # Unit & Integration tests
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/rsheik238/doctor-patient-app.git
cd doctor-patient-app
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
# OR
.venv\Scripts\activate       # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

```bash
cd src
python main.py
```

Visit the API at: [http://localhost:5000](http://localhost:5000)

### Available Endpoints

| Method | URL          | Description           |
| ------ | ------------ | --------------------- |
| GET    | `/doctors/`  | List all doctors      |
| POST   | `/doctors/`  | Add a new doctor      |
| GET    | `/patients/` | List all patients     |
| POST   | `/patients/` | Add a new patient     |
| GET    | `/visits/`   | List scheduled visits |
| POST   | `/visits/`   | Schedule a new visit  |

---

## Running Tests

### Run Unit Tests

```bash
pytest tests/unit
```

### Run Integration Tests

```bash
pytest tests/integration
```

All tests are self-contained and use an in-memory SQLite database.

---

## Hosting on AWS (EC2)

### 1. Create an EC2 Instance

- Choose Ubuntu 22.04 LTS
- Allow ports: 22 (SSH), 5000 (Flask), 80/443 (optional)

### 2. SSH into the Instance

```bash
ssh -i your-key.pem ubuntu@<your-ec2-ip>
```

### 3. Install Requirements

```bash
sudo apt update
sudo apt install python3-pip python3-venv git -y
git clone https://github.com/your-username/hospital_scheduler.git
cd hospital_scheduler
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### 4. Start the Flask App

```bash
cd src
nohup python main.py &
```

You can now access the app at `http://<your-ec2-ip>:5000/`

> Optionally use a reverse proxy like Nginx and set up Gunicorn for production hosting.

---

## Switching to MySQL

Replace the `SQLite*Repository` classes in `core/container.py` with MySQL-based implementations (can be added under `infrastructure/db/mysql_repo.py`).

---

## Notes

- Modular and extensible for any frontend (React, Tkinter, etc.)
- Use `blueprints` in `routes/__init__.py` for scalable API structure
- Clean Architecture ensures testability and maintainability

---

## Author

Shahida Begum
