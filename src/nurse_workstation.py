"""
nurse_workstation.py
--------------------------------
Handles alert notifications and nurse interactions.
Simulates how alerts are received, displayed, and acknowledged.
"""

class NurseWorkstation:
    def send_alert(self, patient_id, alerts):
        """
        Displays alerts for a patient.
        :param patient_id: str
        :param alerts: list of alert messages
        """
        print(f"\n[ALERT] Patient {patient_id} requires attention!")
        for msg in alerts:
            print(f" - {msg}")
        self.acknowledge_alert(patient_id)

    def acknowledge_alert(self, patient_id):
        """
        Simulates nurse acknowledgment.
        """
        print(f"[ACK] Nurse acknowledged alert for patient {patient_id}.")
