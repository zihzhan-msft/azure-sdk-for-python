import os
from models import Patient, HealthcareFile
from typing import List
from azure.ai.formrecognizer import FormRecognizerClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

client = FormRecognizerClient(
    endpoint=os.environ["FORMRECOGNIZER_ENDPOINT"],
    credential=DefaultAzureCredential()
)

with open("Contoso_Health_Medical_Record.pdf", "rb") as fd:
    myfile = fd.read()
poller = client.begin_recognize_content(myfile)
content = poller.result()[0]
notes = ""
for idx, line in enumerate(content.lines):
    if line.text == "HISTORY OF PRESENT ILLNESS:":
        for note in content.lines[idx+1:]:
            notes += f"{note.text} "



patient = Patient(name="Jane Doe", age=70, birthday="04/10/1990")

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

client = TextAnalyticsClient(
    endpoint=os.environ["TEXTANALYTICS_ENDPOINT"],
    credential=AzureKeyCredential(os.environ["TEXTANALYTICS_KEY"])
)

analyzed_docs = client.begin_analyze_healthcare_entities(documents=[notes]).result()
good_docs = [d for d in analyzed_docs if not d.is_error]


for doc in good_docs:
    for entity in doc.entities:
        if entity.category == "Diagnosis":
            patient.diagnoses.append(entity.text)
        elif entity.category == "MedicationName":
            patient.medications.append(entity.text)
        elif entity.category == "SymptomOrSign":
            patient.symptoms.append(entity.text)
        elif entity.category == "ExaminationName":
            patient.examinations.append(entity.text)
