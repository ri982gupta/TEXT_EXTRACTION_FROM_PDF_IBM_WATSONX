import os
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

# Configure IBM Watson NLU service
authenticator = IAMAuthenticator(apikey=os.environ.get("WATSON_APIKEY"))
nlu = NaturalLanguageUnderstandingV1(
    version='2021-03-10',
    authenticator=authenticator
)
nlu.set_service_url(os.environ.get("WATSON_URL"))
