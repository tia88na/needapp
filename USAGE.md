# Quick Start Guide

## Running the Application

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Extract the Model (if needed)
If the `model.pkl` file is not present in the root directory:
```bash
unzip model.pkl.zip
```

### Step 3: Run the Streamlit App
```bash
streamlit run app.py
```

The app will automatically open in your default browser at `http://localhost:8501`

## Using the Application

1. **Enter Nutritional Values**: Fill in all 8 nutritional values for your food product (per 100g)
   - Energy (kcal)
   - Fat (g)
   - Saturated Fat (g)
   - Sugars (g)
   - Salt (g)
   - Protein (g)
   - Fiber (g)
   - Carbohydrates (g)

2. **Review Your Inputs**: Check the "Input Summary" panel on the right to verify your values

3. **Get Prediction**: Click the "🔮 Predict Nutrition Grade" button

4. **View Results**: 
   - The predicted grade (A-E) will be displayed in a large, color-coded box
   - Read the explanation of what the grade means
   - Expand "View Input Details" to see the values used for prediction

## Example Values

### Healthy Food (likely Grade A or B)
- Energy: 100 kcal
- Fat: 1.0 g
- Saturated Fat: 0.5 g
- Sugars: 2.0 g
- Salt: 0.1 g
- Protein: 15.0 g
- Fiber: 10.0 g
- Carbohydrates: 5.0 g

### Average Food (likely Grade C)
- Energy: 300 kcal
- Fat: 8.0 g
- Saturated Fat: 3.0 g
- Sugars: 12.0 g
- Salt: 1.0 g
- Protein: 10.0 g
- Fiber: 4.0 g
- Carbohydrates: 35.0 g

### Unhealthy Food (likely Grade D or E)
- Energy: 500 kcal
- Fat: 25.0 g
- Saturated Fat: 12.0 g
- Sugars: 40.0 g
- Salt: 2.5 g
- Protein: 5.0 g
- Fiber: 1.0 g
- Carbohydrates: 60.0 g

## Nutrition Grade Scale

- **A** (Dark Green): Best nutritional quality - Excellent choice
- **B** (Light Green): Good nutritional quality - Healthy option
- **C** (Yellow): Average nutritional quality - Consume in moderation
- **D** (Orange): Poor nutritional quality - Consider healthier alternatives
- **E** (Red): Lowest nutritional quality - Limit consumption

## Troubleshooting

### Model Loading Error
- Make sure `model.pkl` exists in the root directory
- Extract it from `model.pkl.zip` if needed

### Missing Dependencies
- Run `pip install -r requirements.txt` to install all required packages

### Port Already in Use
- If port 8501 is already in use, run: `streamlit run app.py --server.port=8502`

### Browser Doesn't Open Automatically
- Manually navigate to the URL shown in the terminal (usually `http://localhost:8501`)

## Notes

- This is a prediction tool based on machine learning
- It should not replace professional nutritional advice
- Predictions are based on the trained Random Forest model
- The model was trained on food nutritional data and may not be 100% accurate
