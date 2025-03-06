from app.services.language_detection import *
from app.services.lemmatization import *
from app.services.Remove_stopwords import remove_stopwords
from app.services.thesaurus_construction import *

from flask import Flask, render_template, jsonify

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

from flask import request
@app.route("/preprocessing", methods=['POST', 'GET'])
def Chosen_Preprocessing():
    try:
        inputText = request.args.get('inputText', '')
        option = request.args.get('operation', '')

        if  option == 'language_detection':
            detected_language_data = detect_language(inputText)
            detected_language_json = jsonify(detected_language_data)
            return detected_language_json
        
        elif option == 'remove_stopwords':
            filtered_text_data = remove_stopwords(inputText)
            filtered_text_json = jsonify(filtered_text_data)
            return filtered_text_json
        
        elif option == 'lemmatization':
            lematization_results_data = lemmatize(inputText)
            lematization_results_json = jsonify(lematization_results_data)
            return lematization_results_json
        
        elif option == 'preprocess':
            preprocessed_text_data = preprocess_text(inputText)
            preprocessed_text_json = jsonify(preprocessed_text_data)
            return preprocessed_text_json
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def preprocess_text(inputText):
    # 1. Detección de idioma
    detect_language_data = detect_language(inputText)

    # 2. Eliminación de stopwords
    filtered_text_data = remove_stopwords(inputText)

    # 3. Lematización de palabras restantes
    filtered_text_value = filtered_text_data["filtered_text"]
    lematization_results_data = lemmatize(filtered_text_value)

    # 4. Selección de palabras clave
    lemas_data = lematization_results_data["Lemas"]
    keywords_data = {
        "keywords": [token["Lema"] for token in lemas_data.values()]
    }

    # 5. Construcción del tesauro
    tesauro_data = thesaurus_construction(keywords_data, lemas_data)

    response_data = detect_language_data
    response_data.update(filtered_text_data)
    response_data.update(lematization_results_data)
    response_data.update(keywords_data)
    response_data.update(tesauro_data)

    return response_data