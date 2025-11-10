"""
health_monitoring_system.py
--------------------------------
Core module for processing and analyzing patient vital signs.
It receives input from sensors, checks thresholds, and triggers alerts if needed.
"""

from nurse_workstation import NurseWorkstation
from patient_database import PatientDatabase


class HealthMonitoringSystem:
    def __init__(self):
        self.db = PatientDatabase()
        self.nurse_station = NurseWorkstation()

    def process_vitals(self, patient_id, vitals):
        """
        Processes new patient vital readings and checks for alerts.
        :param patient_id: str - unique patient identifier
        :param vitals: dict - example: {"heart_rate": 110, "temperature": 101.5}
        """
        thresholds = self.db.get_vital_thresholds(patient_id)
        alerts = []

        for vital, value in vitals.items():
            low, high = thresholds.get(vital, (None, None))
            if low is not None and high is not None:
                if value < low or value > high:
                    alerts.append(f"{vital} out of range: {value} (Normal: {low}-{high})")

        if alerts:
            self.nurse_station.send_alert(patient_id, alerts)
        else:
            print(f"[INFO] All vitals normal for patient {patient_id}.")


if __name__ == "__main__":
    system = HealthMonitoringSystem()
    vitals_sample = {"heart_rate": 120, "temperature": 98.6, "blood_pressure": 130}
    system.process_vitals("P001", vitals_sample)
