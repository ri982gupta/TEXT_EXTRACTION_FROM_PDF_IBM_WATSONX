from flask import jsonify, request
from app.watson import nlu

@app.route('/analyze-document', methods=['POST'])
def analyze_document():
    if 'document' not in request.files:
        return jsonify({'error': 'No document file provided'}), 400

    document_file = request.files['document']
    document_text = document_file.read().decode('utf-8')

    try:
        response = nlu.analyze(
            text=document_text,
            features={'entities': {}, 'keywords': {}}
        ).get_result()
        return jsonify(response), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
