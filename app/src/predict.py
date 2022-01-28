import time
import os

from tensorflow import keras

from models import Observation

MODEL_PATH = os.getenv('MODEL_PATH')


def predict_ltc(observation: Observation) -> float:
    """Predicts the LTC delta for a given observation."""
    print("Try to predict ..")
    
    model = keras.models.load_model(MODEL_PATH, compile=False)
    
    print(f"Type: {type(observation.as_tensor())}")
    
    predictions = model.predict(observation.as_tensor())
    return predictions[0][0]
    