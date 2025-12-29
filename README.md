# Nutrition Grade Prediction System 🍎

A machine learning web application that predicts the nutrition grade (A-E) of food products based on their nutritional values.

## Overview

This project uses a **Random Forest Classifier** trained on nutritional data to predict the nutrition grade of food products. The grades range from A (best) to E (worst) and are based on the nutritional composition per 100g of product.

## Features

- 🎯 Predict nutrition grades (A, B, C, D, E) based on 8 nutritional features
- 🖥️ Clean and intuitive Streamlit web interface
- 📊 Real-time predictions with visual grade display
- 📋 Input summary and detailed explanations
- 🎨 Color-coded grade visualization

## Installation

1. Clone this repository:
```bash
git clone https://github.com/tia88na/needapp.git
cd needapp
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Extract the model (if not already extracted):
```bash
unzip model.pkl.zip
```

## Usage

Run the Streamlit app:
```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`

## Input Features

The model requires the following nutritional values per 100g:

- **Energy** (kcal/100g): Energy content in kilocalories
- **Fat** (g/100g): Total fat content
- **Saturated Fat** (g/100g): Saturated fat content
- **Sugars** (g/100g): Sugar content
- **Salt** (g/100g): Salt content
- **Protein** (g/100g): Protein content
- **Fiber** (g/100g): Fiber content
- **Carbohydrates** (g/100g): Carbohydrate content

## Nutrition Grades

- **Grade A**: Best nutritional quality
- **Grade B**: Good nutritional quality
- **Grade C**: Average nutritional quality
- **Grade D**: Poor nutritional quality
- **Grade E**: Lowest nutritional quality

## Model Details

- **Algorithm**: Random Forest Classifier
- **Framework**: scikit-learn
- **Input Features**: 8 numerical features
- **Output**: Nutrition grade (A, B, C, D, or E)
- **Model File**: `model.pkl` (compressed in `model.pkl.zip`)

## Files

- `app.py`: Main Streamlit application
- `model.pkl.zip`: Trained Random Forest model (compressed)
- `nutrients_csvfile.csv`: Dataset with nutritional information
- `requirements.txt`: Python dependencies

## Technologies Used

- Python 3.12+
- Streamlit
- scikit-learn
- pandas
- numpy
- joblib

## License

MIT License

## Author

Created for nutrition grade prediction