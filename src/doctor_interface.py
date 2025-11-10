"""
doctor_interface.py
--------------------------------
Allows doctors to customize patient vital thresholds.
Interacts with the patient database to retrieve and update ranges.
"""

from patient_database import PatientDatabase


class DoctorInterface:
    def __init__(self):
        self.db = PatientDatabase()

    def update_vital_thresholds(self, patient_id, new_thresholds):
        """
        Updates vital thresholds for a specific patient.
        :param patient_id: str
        :param new_thresholds: dict - example: {"heart_rate": (60, 100)}
        """
        self.db.update_vital_thresholds(patient_id, new_thresholds)
        print(f"[UPDATE] Thresholds updated for patient {patient_id}.")

    def view_patient_thresholds(self, patient_id):
        """
        Displays the current thresholds for a patient.
        """
        thresholds = self.db.get_vital_thresholds(patient_id)
        print(f"\n[INFO] Current thresholds for patient {patient_id}:")
        for vital, (low, high) in thresholds.items():
            print(f" - {vital}: {low}-{high}")
