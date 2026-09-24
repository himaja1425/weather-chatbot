# ==========================================================
# Weather Chatbot - Intent Prediction
# File: chatbot/predict.py
# ==========================================================

# ==========================
# Import Libraries
# ==========================

import re
import pickle
import numpy as np
import nltk

from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences


# ==========================
# Download NLTK Resources
# ==========================

nltk.download("punkt")
nltk.download("wordnet")


# ==========================
# Initialize Lemmatizer
# ==========================

lemmatizer = WordNetLemmatizer()


# ==========================
# Load Trained Model
# ==========================

import os
import pickle
from tensorflow.keras.models import load_model

# ==========================================================
# Get Project Root Directory
# ==========================================================

# Current file:
# weather chatbot/chatbot/predict.py

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

# Move one level up to:
# weather chatbot/

BASE_DIR = os.path.dirname(CURRENT_DIR)

print("Project Directory :", BASE_DIR)

# ==========================================================
# Model Path
# ==========================================================

MODEL_PATH = os.path.join(BASE_DIR, "models", "chatbot.keras")

print("Model Path :", MODEL_PATH)
print("Model Exists :", os.path.exists(MODEL_PATH))

model = load_model(MODEL_PATH)

print("✅ LSTM Model Loaded Successfully")

# ==========================================================
# Tokenizer Path
# ==========================================================

TOKENIZER_PATH = os.path.join(BASE_DIR, "models", "tokenizer.pkl")

print("Tokenizer Path :", TOKENIZER_PATH)
print("Tokenizer Exists :", os.path.exists(TOKENIZER_PATH))

with open(TOKENIZER_PATH, "rb") as file:
    tokenizer = pickle.load(file)

print("✅ Tokenizer Loaded Successfully")

# ==========================================================
# Label Encoder Path
# ==========================================================

LABEL_ENCODER_PATH = os.path.join(BASE_DIR, "models", "label_encoder.pkl")

print("Label Encoder Path :", LABEL_ENCODER_PATH)
print("Label Encoder Exists :", os.path.exists(LABEL_ENCODER_PATH))

with open(LABEL_ENCODER_PATH, "rb") as file:
    label_encoder = pickle.load(file)

print("✅ Label Encoder Loaded Successfully")

# ==========================================================
# Text Cleaning Function
# ==========================================================

def clean_text(sentence):
    """
    Clean user sentence exactly the same way
    as done during model training.
    """

    # Convert to lowercase
    sentence = sentence.lower()

    # Remove punctuation and numbers
    sentence = re.sub(r"[^a-zA-Z\s]", "", sentence)

    # Tokenize
    words = word_tokenize(sentence)

    # Lemmatize
    words = [lemmatizer.lemmatize(word) for word in words]

    # Join words
    cleaned_sentence = " ".join(words)

    return cleaned_sentence


# ==========================================================
# Predict Intent
# ==========================================================

def predict_intent(sentence):
    """
    Predict intent from user sentence.

    Parameters
    ----------
    sentence : str

    Returns
    -------
    predicted_tag : str

    confidence : float
    """

    # --------------------------------
    # Clean text
    # --------------------------------

    cleaned_sentence = clean_text(sentence)

    # --------------------------------
    # Convert text to sequence
    # --------------------------------

    sequence = tokenizer.texts_to_sequences([cleaned_sentence])

    # --------------------------------
    # Padding
    # --------------------------------

    padded_sequence = pad_sequences(
        sequence,
        maxlen=model.input_shape[1],
        padding="post"
    )

    # --------------------------------
    # Prediction
    # --------------------------------

    prediction = model.predict(
        padded_sequence,
        verbose=0
    )

    # --------------------------------
    # Highest Probability
    # --------------------------------

    predicted_index = np.argmax(prediction)

    # --------------------------------
    # Confidence Score
    # --------------------------------

    confidence = float(prediction[0][predicted_index])

    # --------------------------------
    # Confidence Threshold
    # --------------------------------

    CONFIDENCE_THRESHOLD = 0.70

    if confidence < CONFIDENCE_THRESHOLD:

        return "unknown", confidence

    # --------------------------------
    # Convert Index to Intent
    # --------------------------------

    predicted_tag = label_encoder.inverse_transform(
        [predicted_index]
    )[0]

    return predicted_tag, confidence


# ==========================================================
# Predict Intent Probabilities
# (Optional - Useful for Debugging)
# ==========================================================

def predict_all_intents(sentence):
    """
    Returns probability of every intent.
    """

    cleaned_sentence = clean_text(sentence)

    sequence = tokenizer.texts_to_sequences([cleaned_sentence])

    padded_sequence = pad_sequences(
        sequence,
        maxlen=model.input_shape[1],
        padding="post"
    )

    prediction = model.predict(
        padded_sequence,
        verbose=0
    )[0]

    results = {}

    for i, probability in enumerate(prediction):

        tag = label_encoder.inverse_transform([i])[0]

        results[tag] = round(float(probability), 4)

    return results


# ==========================================================
# Main Function
# ==========================================================

if __name__ == "__main__":

    print("=" * 60)
    print("       WEATHER CHATBOT INTENT PREDICTOR")
    print("=" * 60)
    print("Type 'exit' to quit.")
    print("=" * 60)

    while True:

        user_input = input("\nYou : ")

        if user_input.lower() == "exit":

            print("\nGoodbye!")

            break

        tag, confidence = predict_intent(user_input)

        print("\nPredicted Intent :", tag)

        print("Confidence       : {:.2f}%".format(confidence * 100))

        if tag == "unknown":

            print("Bot : Sorry, I couldn't understand your question.")

        # Uncomment to see all probabilities
        # print(predict_all_intents(user_input))