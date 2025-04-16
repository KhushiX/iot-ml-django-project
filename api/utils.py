import joblib
import os

# Load the model from the correct path
model_path = os.path.join(os.path.dirname(__file__), 'model.pkl')
model = joblib.load(model_path)

def fetch_sensor_data():
    # Dummy values for now (replace with ThingSpeak data later)
    return 45, 300

def predict_behavior(soil, ldr, time):
    # Convert to correct shape for prediction
    input_data = [[soil, ldr, time]]
    prediction = model.predict(input_data)
    return prediction[0]
