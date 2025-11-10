"""
main.py
--------------------------------
Entry point for the Health Monitoring System simulation.
Demonstrates interactions between doctors, the monitoring system, and the nurse workstation.
"""

from health_monitoring_system import HealthMonitoringSystem
from doctor_interface import DoctorInterface

if __name__ == "__main__":
    print("=== Health Monitoring System Simulation ===")

    # Initialize main components
    system = HealthMonitoringSystem()
    doctor = DoctorInterface()

    patient_id = "P001"

    # Step 1: Doctor reviews current thresholds
    doctor.view_patient_thresholds(patient_id)

    # Step 2: Doctor updates the patient's thresholds
    new_thresholds = {"heart_rate": (55, 95), "temperature": (96.5, 99.5)}
    doctor.update_vital_thresholds(patient_id, new_thresholds)

    # Step 3: System processes new vital readings
    vitals_sample = {"heart_rate": 102, "temperature": 100.2, "blood_pressure": 110}
    system.process_vitals(patient_id, vitals_sample)

    print("\n=== Simulation Complete ===")
