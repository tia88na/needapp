"""
Nutrition Grade Prediction System
A Streamlit web application for predicting nutrition grades of food products
"""

import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="Nutrition Grade Prediction",
    page_icon="🍎",
    layout="wide"
)

# Title and description
st.title("🍎 Nutrition Grade Prediction System")
st.markdown("""
This application predicts the **nutrition grade** (A, B, C, D, or E) of a food product 
based on its nutritional values per 100g.

- **Grade A**: Best nutritional quality
- **Grade B**: Good nutritional quality  
- **Grade C**: Average nutritional quality
- **Grade D**: Poor nutritional quality
- **Grade E**: Lowest nutritional quality

Simply enter the nutritional values below and click **Predict** to get the nutrition grade.
""")

st.divider()

# Load the model
@st.cache_resource
def load_model():
    """Load the trained Random Forest model"""
    try:
        model = joblib.load('model.pkl')
        return model
    except Exception as e:
        st.error(f"Error loading model: {e}")
        return None

# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("📊 Enter Nutritional Values (per 100g)")
    
    # Create two columns for input fields
    input_col1, input_col2 = st.columns(2)
    
    with input_col1:
        energy = st.number_input(
            "Energy (kcal/100g)",
            min_value=0.0,
            max_value=5000.0,
            value=250.0,
            step=10.0,
            help="Energy content in kilocalories per 100g"
        )
        
        fat = st.number_input(
            "Fat (g/100g)",
            min_value=0.0,
            max_value=100.0,
            value=5.0,
            step=0.1,
            help="Total fat content in grams per 100g"
        )
        
        saturated_fat = st.number_input(
            "Saturated Fat (g/100g)",
            min_value=0.0,
            max_value=100.0,
            value=2.0,
            step=0.1,
            help="Saturated fat content in grams per 100g"
        )
        
        sugars = st.number_input(
            "Sugars (g/100g)",
            min_value=0.0,
            max_value=100.0,
            value=10.0,
            step=0.1,
            help="Sugar content in grams per 100g"
        )
    
    with input_col2:
        salt = st.number_input(
            "Salt (g/100g)",
            min_value=0.0,
            max_value=100.0,
            value=0.5,
            step=0.01,
            help="Salt content in grams per 100g"
        )
        
        protein = st.number_input(
            "Protein (g/100g)",
            min_value=0.0,
            max_value=100.0,
            value=8.0,
            step=0.1,
            help="Protein content in grams per 100g"
        )
        
        fiber = st.number_input(
            "Fiber (g/100g)",
            min_value=0.0,
            max_value=100.0,
            value=3.0,
            step=0.1,
            help="Fiber content in grams per 100g"
        )
        
        carbohydrates = st.number_input(
            "Carbohydrates (g/100g)",
            min_value=0.0,
            max_value=100.0,
            value=15.0,
            step=0.1,
            help="Carbohydrate content in grams per 100g"
        )

with col2:
    st.subheader("📋 Input Summary")
    
    # Display input summary in a nice format
    summary_data = {
        "Nutrient": ["Energy", "Fat", "Saturated Fat", "Sugars", "Salt", "Protein", "Fiber", "Carbohydrates"],
        "Value": [
            f"{energy} kcal",
            f"{fat} g",
            f"{saturated_fat} g",
            f"{sugars} g",
            f"{salt} g",
            f"{protein} g",
            f"{fiber} g",
            f"{carbohydrates} g"
        ]
    }
    
    summary_df = pd.DataFrame(summary_data)
    st.dataframe(summary_df, hide_index=True, use_container_width=True)

st.divider()

# Predict button
if st.button("🔮 Predict Nutrition Grade", type="primary", use_container_width=True):
    # Load model
    model = load_model()
    
    if model is not None:
        # Prepare input data
        # Order: energy, fat, saturated_fat, sugars, salt, protein, fiber, carbohydrates
        input_features = np.array([[energy, fat, saturated_fat, sugars, salt, protein, fiber, carbohydrates]])
        
        try:
            # Make prediction
            prediction_numeric = model.predict(input_features)[0]
            
            # Convert numeric prediction to letter grade
            # Model outputs: 0=a, 1=b, 2=c, 3=d, 4=e
            grade_mapping = {0: 'a', 1: 'b', 2: 'c', 3: 'd', 4: 'e'}
            prediction = grade_mapping.get(prediction_numeric, str(prediction_numeric).lower())
            
            # Display result
            st.success("✅ Prediction Complete!")
            
            # Create a large, centered display for the grade
            result_col1, result_col2, result_col3 = st.columns([1, 2, 1])
            
            with result_col2:
                # Color coding for grades
                grade_colors = {
                    'a': '#038141',  # Dark green
                    'b': '#85BB2F',  # Light green
                    'c': '#FECB02',  # Yellow
                    'd': '#EE8100',  # Orange
                    'e': '#E63E11'   # Red
                }
                
                # Normalize grade to lowercase for comparison
                grade_lower = prediction.lower() if isinstance(prediction, str) else str(prediction).lower()
                color = grade_colors.get(grade_lower, '#888888')
                
                st.markdown(f"""
                <div style="
                    background-color: {color};
                    padding: 40px;
                    border-radius: 15px;
                    text-align: center;
                    box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                ">
                    <h1 style="color: white; font-size: 80px; margin: 0; font-weight: bold;">
                        {prediction.upper()}
                    </h1>
                    <p style="color: white; font-size: 24px; margin: 10px 0 0 0;">
                        Nutrition Grade
                    </p>
                </div>
                """, unsafe_allow_html=True)
            
            # Add explanation
            st.markdown("---")
            st.subheader("📖 What does this grade mean?")
            
            grade_explanations = {
                'a': "**Excellent!** This product has the best nutritional quality. It's low in unhealthy nutrients and high in beneficial ones.",
                'b': "**Good!** This product has good nutritional quality. It's a healthy choice for most people.",
                'c': "**Average.** This product has moderate nutritional quality. Consider consuming in moderation.",
                'd': "**Poor.** This product has poor nutritional quality. Consider healthier alternatives when possible.",
                'e': "**Very Poor.** This product has the lowest nutritional quality. Limit consumption and opt for healthier choices."
            }
            
            explanation = grade_explanations.get(grade_lower, "Grade information not available.")
            st.info(explanation)
            
            # Display feature values used for prediction
            with st.expander("🔍 View Input Details"):
                st.write("The prediction was based on the following nutritional values:")
                feature_df = pd.DataFrame({
                    'Feature': ['Energy (kcal/100g)', 'Fat (g/100g)', 'Saturated Fat (g/100g)', 
                               'Sugars (g/100g)', 'Salt (g/100g)', 'Protein (g/100g)', 
                               'Fiber (g/100g)', 'Carbohydrates (g/100g)'],
                    'Value': [energy, fat, saturated_fat, sugars, salt, protein, fiber, carbohydrates]
                })
                st.table(feature_df)
                
        except Exception as e:
            st.error(f"Error making prediction: {e}")
            st.write("Please check your input values and try again.")

# Footer
st.divider()
st.markdown("""
<div style="text-align: center; color: #666; padding: 20px;">
    <p>Built with ❤️ using Streamlit | Random Forest Classifier Model</p>
    <p style="font-size: 12px;">Note: This is a prediction tool and should not replace professional nutritional advice.</p>
</div>
""", unsafe_allow_html=True)
