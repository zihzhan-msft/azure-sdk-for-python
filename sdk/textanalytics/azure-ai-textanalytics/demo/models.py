import datetime

class Patient:
    def __init__(
        self,
        name: str,
        age: int,
        birthday: datetime.date
    ) -> None:
        self.name = name
        self.age = age
        self.birthday = birthday
        self.medications = []
        self.diagnoses = []
        self.symptoms = []
        self.examinations = []

class HealthcareFile:
    def __init__(
        self,
        patient: Patient,
        date: datetime.datetime,
        provider_notes: str,
    ) -> None:
        self.patient = patient
        self.date = date
        self.provider_notes = provider_notes

PATH_TO_INVOICE = ""
PATH_TO_MEDICAL_RECORD = "/Users/isabellacai/Desktop/github_repos/azure-sdk-for-python/sdk/textanalytics/azure-ai-textanalytics/demo/Contoso_Health_Medical_Record.pdf"