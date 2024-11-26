from flask import Flask, request, jsonify, render_template
import joblib
import numpy as np

# Initialize Flask app
app = Flask(__name__)

# Load the pre-trained model
MODEL_PATH = "iris_model.pkl"
model = joblib.load(MODEL_PATH)

# Define the index-to-class mapping
CLASS_MAPPING = {
    0: "Iris-setosa",
    1: "Iris-versicolor",
    2: "Iris-virginica"
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse input data
        data = request.json
        features = data.get("features")
        if not features or len(features) != 4:
            return jsonify({"error": "Invalid input. Provide a list of 4 features."}), 400

        # Convert to numpy array and reshape for the model
        input_features = np.array(features).reshape(1, -1)

        # Make prediction
        prediction = model.predict(input_features)[0]
        predicted_class = CLASS_MAPPING[prediction]

        # Return prediction
        return jsonify({
            "prediction": predicted_class,
            "class_index": int(prediction)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
