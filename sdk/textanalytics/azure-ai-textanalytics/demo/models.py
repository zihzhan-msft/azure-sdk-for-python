import datetime

class Patient:
    def __init__(self) -> None:
        self.medications = []
        self.diagnoses = []
        self.symptoms = []
        self.examinations = []

PATH_TO_INVOICE = ""
PATH_TO_MEDICAL_RECORD = "/Users/isabellacai/Desktop/github_repos/azure-sdk-for-python/sdk/textanalytics/azure-ai-textanalytics/demo/Contoso_Health_Medical_Record.pdf"