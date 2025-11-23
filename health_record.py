'''
File: health_record.py
Description: Defines the HealthRecord class for tracking animal health, issues, treatments, and medical notes.
Author: Sina Mardani Mehrabad
ID: 110471492
Username: marsy127
This is my own work as defined by the University's Academic Integrity Policy.
'''


class HealthRecord:
    """
    This class represents a single health record entry for an animal.

    It stores details about a medical issue, including when it was reported,
    its severity, any treatment plans, and additional notes. This class helps
    zoo staff and veterinarians monitor animal well-being over time.
    """

    def __init__(self, issue: str, date_reported: str, severity: str,
                 treatment_plan: str = "Pending", notes: str = "") -> None:
        """
        This function initializes a new HealthRecord object that keeps track of a
        health issue or illness experienced by an animal.

        Parameters:
            issue (str): The name or description of the health issue (e.g., 'Infection', 'Broken Wing').
            date_reported (str): The date when the issue was first reported or diagnosed.
            severity (str): The severity level of the issue (e.g., 'Low', 'Medium', 'High').
            treatment_plan (str): The current or planned treatment (default: 'Pending').
            notes (str): Any extra observations, progress notes, or comments (default: empty).

        Returns:
            None
        """
        # Store the main health-related details as public attributes for easy access
        self.issue = issue
        self.date_reported = date_reported
        self.severity = severity
        self.treatment_plan = treatment_plan
        self.notes = notes

    def __str__(self) -> str:
        """
        This function returns a readable string summary of the health record details.
        It allows the record to be displayed neatly when printed.

        Returns:
            str: A formatted string showing the issue, date, severity, treatment, and notes.
        """
        return (
            "Issue: " + self.issue +
            " | Date: " + self.date_reported +
            " | Severity: " + self.severity +
            " | Treatment: " + self.treatment_plan +
            " | Notes: " + self.notes
        )
