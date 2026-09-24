# 🌦️ AI Weather Chatbot

An NLP-based weather chatbot that uses an **LSTM model** to understand user intents and the **OpenWeather API** to provide real-time weather information through a **Streamlit** interface.

## 🚀 Features

- Natural-language weather queries
- LSTM-based intent classification
- NLP preprocessing, tokenization & padding
- Location extraction
- Real-time weather data using OpenWeather API
- Context-aware follow-up questions
- Concise, intent-based responses
- Streamlit chatbot interface
- API error handling

## 🧠 How It Works

```text
User Query
    ↓
NLP Preprocessing
    ↓
LSTM Intent Classification
    ↓
Location Extraction
    ↓
OpenWeather API
    ↓
Weather Data
    ↓
Chatbot Response
```

**LSTM** understands what the user is asking, while the **OpenWeather API** provides the actual weather data.

## 🛠️ Tech Stack

- Python
- TensorFlow / Keras
- LSTM
- NLP
- OpenWeather API
- Streamlit
- NumPy
- Pandas
- scikit-learn

## ⚙️ Setup

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add your OpenWeather API key:

```text
OPENWEATHER_API_KEY=your_api_key_here
```

Run the application:

```bash
streamlit run app.py
```

## 💬 Example

**User:**  
"What is the temperature in Visakhapatnam?"

**Bot:**  
"The current temperature in Visakhapatnam is 26°C."

The chatbot returns **only the information requested by the user** instead of displaying unnecessary weather details.

## 🔮 Future Improvements

- Transformer-based intent classification
- Better location/entity recognition
- Weather forecasting
- Voice interaction
- Multilingual support
- Improved conversational memory

## 📌 Purpose

Built as an **AI/ML portfolio project** to demonstrate NLP, LSTM-based intent classification, API integration, and Streamlit application development.
