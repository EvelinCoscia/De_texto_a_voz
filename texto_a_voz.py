import nltk
from newspaper import Article
from gtts import gTTS
from gtts import gTTS
import os

nltk.download('punkt')
nltk.download('punkt_tab')


def obtener_texto_articulo(url):
    articulo = Article(url)
    articulo.download()
    articulo.parse()
    articulo.nlp()
    return articulo.text

def convertir_texto_a_audio(texto, nombre_archivo="articulo.mp3"):
    tts = gTTS(text=texto, lang='es')
    tts.save(nombre_archivo)
    print(f"Audio guardado como {nombre_archivo}")

def articulo_a_audio(url, nombre_archivo="articulo.mp3"):
    texto = obtener_texto_articulo(url)
    print("Texto extraído:")
    print(texto[:500], '...')  
    convertir_texto_a_audio(texto, nombre_archivo)

def reproducir_audio(nombre_archivo="articulo.mp3"):
    os.system(f"start {nombre_archivo}")

# Ejecutar
url = "https://rockcontent.com/es/blog/textos-digitales"  # Usa una URL válida
articulo_a_audio(url)

reproducir_audio()
