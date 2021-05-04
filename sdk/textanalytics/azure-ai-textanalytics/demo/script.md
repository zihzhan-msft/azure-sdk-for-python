# Our script

- Hey, we're going to be showing you guys a quick demo that walks you through how to access some of Azure's Cognitive Services offerings
using our Python SDKs
- We're newly hired by a hospital to digitize their billing process. We'll be going through patient invoices and doctor's notes
to extract billing information.
- Then we show the 2 forms. First, we'll take a look at unstructured doctor's notes from patient visits. We specifically want to get
billing codes found within the "history of present illness" section.
- We'll use Azure's Form Recognizer service to extract the text from this file
- With our Python SDKs, authentication is now a lot easier. TODO: ask Charles for AAD snippet
