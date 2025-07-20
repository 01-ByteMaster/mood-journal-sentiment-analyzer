
from flask import Flask, request, jsonify
import pickle
from clean_text import clean_text_with_stopwords
from flask_cors import CORS

# Initialize the app
app = Flask(__name__)
CORS(app)

# Loading  model components 
try:
    with open("sentiment_components.pkl", "rb") as f:
        components = pickle.load(f)

    model = components["model"]
    tfidf = components["tfidf"]
    le = components["label_encoder"]

    print("Model components loaded successfully.")
except Exception as e:
    model = tfidf = le = None
    print(f'Failed to load model components. Error : ',{e})
    print(f'Error: {e}')

# Route for sentiment prediction
@app.route("/predict", methods=["POST"])
def predict():
    if not model or not tfidf or not le:
        return jsonify({"error": "Model not loaded properly."}), 500

    data = request.get_json()

    if not data or 'text' not in data:
        return jsonify({"error": "No text provided in request."}), 400

    try:
        input_text = data['text']
        cleaned = clean_text_with_stopwords(input_text)
        vector_label = tfidf.transform([cleaned])
        prediction = model.predict(vector_label)
        mood = le.inverse_transform(prediction)[0]

        return jsonify({
            "input": input_text,
            "cleaned_text": cleaned,
            "predicted_mood": mood
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
