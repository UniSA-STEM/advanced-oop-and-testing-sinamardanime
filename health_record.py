'''
File: health_record.py
Description: Defines the HealthRecord class for tracking animal health and treatments.
Author: Sina Mardani Mehrabad
ID: 110100110
Username: marsy127
This is my own work as defined by the University's Academic Integrity Policy.
'''


class HealthRecord:
    """
    Represents one health report for an animal.
    Stores details about an issue, the date reported, its severity, treatment, and notes.
    """

    def __init__(self, issue, date_reported, severity, treatment_plan="Pending", notes=""):
        self.issue = issue
        self.date_reported = date_reported
        self.severity = severity
        self.treatment_plan = treatment_plan
        self.notes = notes

    def __str__(self):
        """Readable text summary of the health record."""
        return (
            "Issue: " + self.issue +
            " | Date: " + self.date_reported +
            " | Severity: " + self.severity +
            " | Treatment: " + self.treatment_plan +
            " | Notes: " + self.notes
        )