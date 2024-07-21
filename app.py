# from flask import Flask, jsonify, request
# from flask_cors import CORS
# from ibm_watson import NaturalLanguageUnderstandingV1
# from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
# import os

# # Set the environment variables
# os.environ["WATSON_APIKEY"] = "cUAOZe81kVuhSVudBOGHSQHyORnpMPHZzL1bwwVUEuFT"
# os.environ["WATSON_URL"] = "https://us-south.nl.cloud.ibm.com"


# app = Flask(__name__)
# CORS(app)

# # Configure IBM Watson NLU service
# authenticator = IAMAuthenticator(apikey=os.environ.get("WATSON_APIKEY"))
# nlu = NaturalLanguageUnderstandingV1(
#     version='2021-03-10',
#     authenticator=authenticator
# )
# nlu.set_service_url(os.environ.get("WATSON_URL"))

# @app.route('/analyze-document', methods=['POST'])
# def analyze_document():
#     print("Analyzing document...")
#     # Check if document file is provided
#     if 'document' not in request.files:
#         return jsonify({'error': 'No document file provided'}), 400

#     document_file = request.files['document']
#     document_text = document_file.read().decode('utf-8')

#     print("Document received:", document_text)  # Check if the document text is received correctly

#     # Analyze the document using IBM Watson NLU
#     try:
#         response = nlu.analyze(
#             text=document_text,
#             features={'entities': {}, 'keywords': {}}
#         ).get_result()
#         print("Analysis completed successfully:", response)  # Check the response from IBM Watson NLU
#         return jsonify(response), 200
#     except Exception as e:
#         print("Error during analysis:", e)  # Print any errors that occur during analysis
#         return jsonify({'error': str(e)}), 500
    

# # if __name__ == '__main__':
# #     app.run(port=3000)
