"""
Este módulo implementa una aplicación Flask para detección de emociones.
"""

from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_adetector():
    """
    Endpoint para analizar emociones en un texto.
    """
    # Recupera el texto a analizar de los argumentos de la solicitud
    text_to_analyze = request.args.get('textToAnalyze')

    # Verifica si el texto está vacío
    if not text_to_analyze:
        return "¡Entrada inválida! El texto no puede estar vacío."

    # Pasa el texto a la función y almacena la respuesta
    response = emotion_detector(text_to_analyze)

    if response is None:
        return "¡Error al analizar el texto! Intenta de nuevo."

    # Extrae el label y el score de la respuesta
    dominant_emotion = response.get('dominant_emotion', 'N/A')
    anger = response.get('anger', 0.0)
    disgust = response.get('disgust', 0.0)
    fear = response.get('fear', 0.0)
    joy = response.get('joy', 0.0)
    sadness = response.get('sadness', 0.0)

    # Verifica si el label es N/A
    if dominant_emotion == 'N/A':
        return "¡Texto inválido! ¡Por favor, inténtalo de nuevo!"

    # Devuelve una cadena formateada con el label de sentimiento y el score
    return (
        f"Para la frase dada, la respuesta del sistema es "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} y 'sadness': {sadness}. "
        f"La emoción dominante es {dominant_emotion}."
    )

@app.route("/")
def render_index_page():
    """
    Renderiza la página principal de la aplicación.
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
