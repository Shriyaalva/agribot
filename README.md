 # 🌱 AgriBot – Intelligent Chatbot for Farmers

AgriBot is a full-stack AI-powered web application designed to assist farmers with
crop selection, plant disease detection, and agricultural guidance using Machine Learning and Deep Learning models.

---

## 🚀 Features

### 1. Crop Recommendation System
- Inputs: Nitrogen, Phosphorus, Potassium, pH, temperature, humidity, rainfall
- Model: XGBoost Classifier
- Output: Best recommended crop

### 2. Crop Disease Prediction
- Input: Leaf image uploaded by user
- Model: CNN (TensorFlow / Keras)
- Dataset: Rice Leaf Disease Dataset
- Output: Disease name with basic remedy suggestion

### 3. Agricultural Chatbot
- Intent-based chatbot
- Handles greetings, crop queries, disease help, and soil-related questions
- Routes queries to relevant ML models

### 4. Web Application
- Backend: Django
- Frontend: HTML, CSS, JavaScript
- REST APIs for ML model inference

---

User (Browser)
|
v
Frontend (HTML/CSS/JS)
|
v
Django Backend (REST APIs)
| |
| ├── Crop Recommendation (XGBoost)
| └── Disease Prediction (CNN)
|
v
Prediction Result → User


---

## 🛠️ Tech Stack

- Python 3.10
- Django
- XGBoost
- TensorFlow / Keras
- Scikit-learn
- HTML, CSS, JavaScript
- SQLite

---

## ⚙️ How to Run the Project

```bash
# Create virtual environment
python -m venv venv
venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run server
python manage.py runserver


## 🏗️ System Architecture

