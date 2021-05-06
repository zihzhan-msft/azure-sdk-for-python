# Our script

- Hey, we're going to be showing you guys a quick demo that walks you through how to access some of Azure's Cognitive Services offerings using our Python SDKs
- I'm going to show you guys how to use our Text Analytics and Form Recognizer SDKs to build up a healthcare patient's profile,
and Krista's going to show you how to use Form Recognizer to automate processing of healthcare invoices.

- We want to build a patient profile from this patient health record.
- First, I'm going to use Form Recognizer to extract the content from this form.
- I'm going to create a client with our SDKs to query the service with. Once I authenticate to my client, I can start making calls to the service and don't have to think about authentication again. Here I'm using azure-identity
- `begin_recognize_content` will get all of the content in this file, no need for pre-training. For this demo, I'm actually going to be focusing on this free-form
documentation section, which we're going to send to Text Analytics to do healthcare analysis
- As you see here, I'm going to be iterating through all of the lines in the form until I reach here.
- Check the `notes` variable

- Now that I have this free-form provider note section, I'm going to be sending this off to Text Analytics to analyze.
- Creating our Text Analytics Client is very similar to creating our FormRecognizer Client. Our SDKs offer different ways to authenticate,
depending on the service, so the only difference here is that I'm authenticating with a key credential.
- Where Text Analytics's healthcare analysis offering really shines is in unstructured provider notes, like the one here.
- In building up this patient's profile, we're interested in extracted entities that fall into the following categories, so I'm going to loop through entities and grab the ones I care about to create my patient profile.
- Now, we can see the following diagnoses from this unstructured text block, and the patient's profile has been built. Off to Krista
