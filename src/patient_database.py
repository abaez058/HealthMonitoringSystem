"""
patient_database.py
--------------------------------
Simulates a simple patient database for storing vital thresholds and information.
In a real-world application, this would connect to a SQL or cloud-based database.
"""

class PatientDatabase:
    def __init__(self):
        # Example in-memory data for demo purposes
        self.patient_data = {
            "P001": {
                "heart_rate": (60, 100),
                "temperature": (97.0, 99.0),
                "blood_pressure": (90, 120)
            }
        }

    def get_vital_thresholds(self, patient_id):
        """
        Retrieves the threshold ranges for a given patient.
        """
        return self.patient_data.get(patient_id, {})

    def update_vital_thresholds(self, patient_id, new_thresholds):
        """
        Updates the vital thresholds for a patient.
        """
        if patient_id not in self.patient_data:
            self.patient_data[patient_id] = {}

        self.patient_data[patient_id].update(new_thresholds)
        print(f"[DB] Updated thresholds for {patient_id}: {new_thresholds}")
