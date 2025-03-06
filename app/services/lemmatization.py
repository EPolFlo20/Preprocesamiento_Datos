# Instalar spaCy y descargar el modelo para español (si aún no está instalado)
import os

# Importar spaCy
try:
    import spacy
except ImportError:
    os.system("pip install spacy")
    import spacy

# Cargar el modelo en español
try:
    nlp = spacy.load("es_core_news_sm")
except OSError:
    # Descargar el modelo de español
    os.system("python -m spacy download es_core_news_sm")
    nlp = spacy.load("es_core_news_sm")


def lemmatize(inputText):
    doc = nlp(inputText)
    # Crear una lista con los detalles de cada token
    lematization_results = {
        "Lemas" : {}
    }
    for token in doc:
        lematization_results["Lemas"][token.text] = {
            "Lema": token.lemma_,
            "Etiqueta": token.pos_,
            "Dependencia": token.dep_ 
        }

    return lematization_results