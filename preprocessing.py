
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

nltk.download('punkt')
nltk.download('stopwords')

def procesar_texto(texto):
    texto = texto.lower()
    
    palabras = word_tokenize(texto)
    
    palabras_comunes = set(stopwords.words('english'))
    palabras_sin_comunes = [palabra for palabra in palabras if palabra not in palabras_comunes]
    
    stemmer = PorterStemmer()
    palabras_raiz = [stemmer.stem(palabra) for palabra in palabras_sin_comunes]
    
    texto_procesado = ' '.join(palabras_raiz)
    
    return texto_procesado


