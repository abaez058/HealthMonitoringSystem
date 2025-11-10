# Health Monitoring System – Sequence Diagrams

This project presents UML sequence diagrams for a **Health Monitoring System** that tracks patient vitals and manages real-time alerts.  
It highlights how medical staff and system components interact to ensure patient safety and efficient monitoring.

---

## 📊 Diagrams

### 1. Monitor and Alert on Vital Signs
Illustrates how patient sensors send vital data (heart rate, blood pressure, temperature, etc.) to the monitoring system.  
When readings exceed set thresholds, alerts are sent to the nurse workstation for acknowledgment and logging.

### 2. Set Personalized Vital Ranges
Shows how doctors can personalize patient vital sign thresholds.  
The system retrieves current settings, updates new ranges, and confirms the changes in the patient database.

---

## 📁 Project Structure

src/
├── health_monitoring_system.py # Processes and analyzes patient vitals
├── nurse_workstation.py # Displays alerts and records nurse acknowledgments
├── doctor_interface.py # Allows doctors to customize vital sign thresholds
└── patient_database.py # Stores patient data and vital range settings


---

## 🧠 Key Skills Demonstrated
- System design and UML documentation  
- Real-time data monitoring and alert workflows  
- Database interaction and user-role integration  
- Clear technical documentation for software projects

---

## 💻 How to View
All sequence diagrams are located in the `diagrams/` folder.  
They can be viewed directly on GitHub or downloaded for presentation and documentation purposes.

---

## 👤 Author
**Andrew Baez**  
Designed as part of a portfolio project to demonstrate system design and documentation skills for healthcare technology applications.

---
