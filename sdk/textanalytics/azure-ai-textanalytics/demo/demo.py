import os
from .models import Patient, HealthcareFile
from typing import List
from azure.ai.formrecognizer import FormRecognizerClient
from azure.identity import DefaultAzureCredential
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

# client = FormRecognizerClient(
#     endpoint=os.environ["FORMRECOGNIZER_ENDPOINT"],
#     credential=DefaultAzureCredential()
# )

# with open("Contoso_Health.pdf", "rb") as f:
#     poller = client.begin_recognize_content(f)

# form = poller.result()



patient = Patient(name="Jane Doe", age=70, birthday="04/10/1990")

from azure.ai.textanalytics import TextAnalyticsClient
from azure.core.credentials import AzureKeyCredential

client = TextAnalyticsClient(
    endpoint=os.environ["TEXTANALYTICS_ENDPOINT"],
    credential=AzureKeyCredential(os.environ["TEXTANALYTICS_KEY"])
)

provider_notes = "The patient is a 70-year-old with a history of hypertensive borderline hypercholesterolemia, and hypercoagulability with multiple pulmonary emboli in the past who presented asymptomatically with a wide complex tachycardia that could not rule out ventricular tachycardia in the recovery phase of a full Bruce exercise tolerance test. The patient was admitted for Holter monitoring times 48 hours. He was ruled out for a myocardial infarction. He was started on a cholesterol lowering agent, his Coumadin was held, and Heparin was started in the case of an invasive procedure."

analyzed_docs = client.begin_analyze_healthcare_entities(documents=[provider_notes]).result()
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
