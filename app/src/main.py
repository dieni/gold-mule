import time

from tensorflow import keras

from models import Observation

MODEL_PATH = "model.h5"


def predict_cryptomajor_delta() -> float:
    """Predicts the CryptoMajor delta for a given observation."""
    model = keras.models.load_model(MODEL_PATH, compile=False)
    observation = Observation(19036, 286.91, 594.47, 85.83, 0.608,
                              3.02, 0.18073, 293.22, 0.009999999999991)
    predictions = model.predict(observation.as_tensor())
    return predictions[0][0]


if __name__ == '__main__':
    start = time.time()
    predicted_delta = predict_cryptomajor_delta()
    end = time.time()
    print(f"\nThe prediction took {round(end - start, 2)} seconds.")
    print("The prediction for the next CryptoMajor delta is:")
    print(predicted_delta)
