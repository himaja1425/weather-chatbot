# weather-chatbot
An NLP-based weather chatbot that uses an LSTM model to classify user intents and OpenWeather API to provide real-time weather information through a Streamlit interface.



# 🌦️ Weather Chatbot

An AI-powered conversational weather chatbot that uses **Natural Language Processing (NLP)** and an **LSTM neural network** to understand user weather queries and the **OpenWeather API** to retrieve real-time weather information.

The application provides a simple conversational interface using **Streamlit** and responds specifically to the information requested by the user.

---

## 📌 Project Overview

The AI Weather Chatbot allows users to ask weather-related questions using natural language.

For example:

- "What is the temperature in Visakhapatnam?"
- "What is the humidity in Chennai?"
- "Is it raining in Hyderabad?"
- "What is the wind speed in Mumbai?"
- "When is sunrise in Bangalore?"

The chatbot first identifies **what the user is asking for** using an LSTM-based intent classification model. It then identifies the requested location and retrieves the latest available weather information from the OpenWeather API.

### Important Design Principle

The **LSTM does not predict the actual weather**.

Its responsibility is to understand the user's query and classify the intent.

The **OpenWeather API is the source of current weather data**.

---

## 🚀 Features

- Natural-language weather queries
- LSTM-based intent classification
- NLP text preprocessing
- Tokenization and sequence padding
- Location extraction
- Real-time weather data through OpenWeather API
- Context-aware follow-up questions
- Concise responses based on the user's request
- Streamlit conversational interface
- API error handling
- Low-confidence intent handling
- Secure API-key management using environment variables

---

## 🧠 System Architecture

```text
                 User Query
                     │
                     ▼
              Streamlit Chat UI
                     │
                     ▼
            Text Preprocessing
                     │
                     ▼
                Tokenizer
                     │
                     ▼
              LSTM Classifier
                     │
                     ▼
              Intent Detection
                     │
                     ▼
             Location Extraction
                     │
                     ▼
          OpenWeather API Request
                     │
                     ▼
             Current Weather Data
                     │
                     ▼
          Intent-based Response
                     │
                     ▼
              Chatbot Response
```

---

## 🤖 Machine Learning Model

The project uses an **LSTM (Long Short-Term Memory)** neural network for intent classification.

### Model Architecture

```text
Input Text
    ↓
Tokenization
    ↓
Padding
    ↓
Embedding Layer
    ↓
LSTM Layer
    ↓
Dropout
    ↓
Dense Layer
    ↓
Softmax
    ↓
Predicted Intent
```

The model learns different ways users can ask for the same type of weather information.

For example:

```text
"What is the temperature in Chennai?"
"How hot is it in Chennai?"
"Tell me the current temperature in Chennai."
```

These queries can be classified into the same `temperature` intent.

---

## 🎯 Supported Intents

The chatbot can be designed to recognize intents such as:

- `current_weather`
- `temperature`
- `feels_like`
- `min_temperature`
- `max_temperature`
- `humidity`
- `wind_speed`
- `wind_direction`
- `wind_gust`
- `pressure`
- `visibility`
- `cloudiness`
- `rain`
- `snow`
- `sunrise`
- `sunset`

The intent determines which information should be extracted from the weather API response.

---

## 🌐 OpenWeather API

After identifying the user's intent and location, the application sends a request to the **OpenWeather API**.

The API can provide information such as:

- Temperature
- Feels-like temperature
- Humidity
- Atmospheric pressure
- Wind speed
- Wind direction
- Visibility
- Cloudiness
- Rainfall
- Snowfall
- Sunrise
- Sunset

The chatbot does not use the LSTM to generate or predict current weather values.

Instead:

```text
LSTM
→ Understands the question

OpenWeather API
→ Provides current weather data

Response Generator
→ Returns the requested information
```

---

## 💬 Conversational Behavior

The chatbot is designed to answer the **specific question asked by the user** rather than displaying every available weather parameter.

### Example

**User:**

```text
What is the temperature in Visakhapatnam?
```

**Bot:**

```text
The current temperature in Visakhapatnam is 26°C.
```

It should not unnecessarily return humidity, pressure, wind speed, visibility, etc.

### Follow-up Example

**User:**

```text
What is the temperature in Visakhapatnam?
```

**Bot:**

```text
The current temperature in Visakhapatnam is 26°C.
```

**User:**

```text
What about humidity?
```

**Bot:**

```text
The current humidity in Visakhapatnam is XX%.
```

The chatbot can use the previous location as conversational context while retrieving fresh weather data.

---

## 🛠️ Technologies Used

### Programming Language
- Python

### Machine Learning
- TensorFlow
- Keras
- LSTM
- scikit-learn

### NLP
- Tokenization
- Sequence Padding
- Label Encoding
- Text Preprocessing

### API
- OpenWeather API

### Frontend
- Streamlit

### Data Processing
- NumPy
- Pandas

---

## 📂 Project Structure

```text
ai-weather-chatbot/
│
├── data/
│   └── intents.json
│
├── models/
│   ├── chatbot.keras
│   ├── tokenizer.pkl
│   └── label_encoder.pkl
│
├── api/
│   └── weather_api.py
│
├── chatbot/
│   ├── predict.py
│   └── response.py
│
├── notebooks/
│   ├── data_preprocessing.ipynb
│   └── model_training.ipynb
│
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/ai-weather-chatbot.git
```

```bash
cd ai-weather-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 OpenWeather API Configuration

Create an API key through OpenWeather and create a `.env` file in the project root.

Add:

```text
OPENWEATHER_API_KEY=your_api_key_here
```

Never commit the `.env` file to GitHub.

The `.gitignore` should contain:

```text
.env
venv/
__pycache__/
.ipynb_checkpoints/
```

A `.env.example` file can be included:

```text
OPENWEATHER_API_KEY=your_api_key_here
```

---

## ▶️ Running the Application

Start the Streamlit application:

```bash
streamlit run app.py
```

The application will open in the browser and provide a conversational weather interface.

---

## 📊 Model Training

The LSTM model is trained using the intent dataset stored in:

```text
data/intents.json
```

The training process includes:

1. Loading the intent dataset
2. Text preprocessing
3. Tokenization
4. Sequence conversion
5. Padding
6. Label encoding
7. Train/validation split
8. LSTM model training
9. Model evaluation
10. Saving the trained model

The trained model is saved as:

```text
models/chatbot.keras
```

The tokenizer and label encoder are also saved for inference.

---

## 📈 Model Evaluation

The model can be evaluated using:

- Training accuracy
- Validation accuracy
- Training loss
- Validation loss
- Classification report
- Confusion matrix

These metrics help evaluate how well the model distinguishes between different weather-related intents.

---

## 🛡️ Error Handling

The application handles common issues such as:

- Invalid city names
- Missing API key
- API request failures
- Network errors
- Empty queries
- Unsupported questions
- Low-confidence intent predictions
- Missing location information

The chatbot should provide a meaningful message instead of crashing when an error occurs.

---

## ⚠️ Limitations

- Intent classification depends on the quality and variety of the training dataset.
- The chatbot supports predefined weather-related intents.
- Location extraction may not correctly identify every possible place name.
- Weather information depends on the availability and accuracy of the OpenWeather API.
- LSTM-based intent classification may require additional training data as the range of user queries grows.

---

## 🔮 Future Improvements

Possible future enhancements include:

- Transformer-based intent classification
- Named Entity Recognition (NER) for better location extraction
- Multi-city weather comparison
- Extended weather forecasts
- Voice-based interaction
- Multilingual weather queries
- Improved conversational memory
- Weather alerts and notifications
- Mobile-friendly deployment
- Integration with additional weather APIs

---

## 🎓 Key Learning Outcomes

This project demonstrates practical understanding of:

- Natural Language Processing
- Text preprocessing
- Tokenization
- Sequence modeling
- LSTM neural networks
- Intent classification
- Model training and evaluation
- REST API integration
- Real-time data retrieval
- Error handling
- Streamlit application development
- AI/ML project deployment

---

## 👩‍💻 Project Purpose

This project was developed as an **AI/ML portfolio project** to demonstrate the integration of a machine learning model with a real-world API and an interactive application.

The focus is on building an understandable end-to-end pipeline:

```text
Machine Learning
        +
NLP
        +
Real-Time API
        +
Conversational Interface
        =
AI Weather Chatbot
```

---

## 📜 License

This project is intended for educational and portfolio purposes.
