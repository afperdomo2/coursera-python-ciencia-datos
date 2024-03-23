"""
Este módulo define un servidor Flask para predecir emociones a partir de texto proporcionado.
"""
from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_predictor

app = Flask("Emotion Detection")


@app.route("/emotionDetector")
def sent_prediction():
    """
    Realiza la predicción de la emoción para el texto proporcionado
    y devuelve los resultados en formato JSON.

    Returns:
        dict: Un diccionario JSON que contiene las emociones detectadas y la emoción dominante.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    response = emotion_predictor(text_to_analyze)

    if response["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    message = {
        "anger": response["anger"],
        "disgust": response["disgust"],
        "fear": response["fear"],
        "joy": response["joy"],
        "sadness": response["sadness"],
        "dominant_emotion": response["dominant_emotion"]
    }
    return jsonify(message)


@app.route("/")
def render_index_page():
    """
    Renderiza la página de índice HTML.

    Returns:
        str: El contenido HTML de la página de índice.
    """
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
