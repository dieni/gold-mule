import time
import os

from tensorflow import keras

from models import Observation

MODEL_PATH = os.getenv('MODEL_PATH')


def predict_ltc(observation: Observation) -> float:
    """Predicts the LTC delta for a given observation."""
    model = keras.models.load_model(MODEL_PATH, compile=False)
    predictions = model.predict(observation.as_tensor())
    return predictions[0][0]
    