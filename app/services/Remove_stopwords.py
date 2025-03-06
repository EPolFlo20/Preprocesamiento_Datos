# Instalación de NLTK y descarga de recursos necesarios
import os

# Importar NLTK
try:
    import nltk
except ImportError:
    os.system("pip install nltk")
    import nltk

# Descarga de las stopwords
nltk.download('stopwords')
nltk.download('punkt')  # Para tokenización

from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def remove_stopwords(inputText):
    # Tokenización del texto
    tokens = word_tokenize(inputText.lower())  # Convertimos a minúsculas y tokenizamos

    # Lista de stopwords en español
    stop_words = set(stopwords.words('spanish'))

    # Eliminación de stopwords
    filtered_tokens = [word for word in tokens if word not in stop_words]
    filtered_text = " ".join(filtered_tokens)
    
    filtered_text_dict = {
        "filtered_text" : filtered_text
    }

    #return filtered_text
    return filtered_text_dict