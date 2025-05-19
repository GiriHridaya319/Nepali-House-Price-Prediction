import streamlit as st
import pickle
import numpy as np

# Load the saved objects
with open('scaler.pkl', 'rb') as f:
    scaler = pickle.load(f)

with open('label_encoder.pkl', 'rb') as f:
    label_encoder = pickle.load(f)

with open('linear_regression_model.pkl', 'rb') as f:
    linear_regression_model = pickle.load(f)

with open('random_forest_model.pkl', 'rb') as f:
    random_forest_model = pickle.load(f)

# Define the prediction functions
def predict_price(floor, bedroom, bathroom, road, land, age, city):
    # Calculate LAND_squared
    land_squared = land ** 2
    
    # Create input data with features in the correct order
    input_data = np.array([[floor, bedroom, bathroom, road, land, age, city, land_squared]])
    
    # Scale the input data (if scaling is required)
    input_scaled = scaler.transform(input_data)
    
    # Make the prediction
    predicted_price = linear_regression_model.predict(input_scaled)
    
    return predicted_price[0]

def predict_price_rf(floor, bedroom, bathroom, road, land, age, city):
    # Calculate LAND_squared
    land_squared = land ** 2
    
    # Create input data with features in the correct order
    input_data = np.array([[floor, bedroom, bathroom, road, land, age, city, land_squared]])
    
    # Make the prediction
    predicted_price_rf = random_forest_model.predict(input_data)
    
    return predicted_price_rf[0]

# Streamlit app
st.title("House Price Prediction")

# Input fields for features
st.header("Enter House Features")
floor = st.number_input("FLOOR", min_value=0)
bedroom = st.number_input("BEDROOM", min_value=0)
bathroom = st.number_input("BATHROOM", min_value=0)
road = st.number_input("ROAD (in feet)", min_value=0)
land = st.number_input("LAND (in aana)", min_value=0.0)
age = st.number_input("AGE", min_value=0)

# Restrict Cities input to only 5 specific cities
allowed_cities = ["kathmandu", "bhaktapur", "chitwan", "kaski", "lalitpur"]
city = st.selectbox("Cities", options=allowed_cities)

# Preprocess the city input (strip and lowercase)
city = city.strip().lower()

# Encode the city
try:
    city_encoded = label_encoder.transform([city])[0]
except ValueError as e:
    st.error(f"Error: {e}. The selected city is not recognized by the model.")
    st.stop()

# Model selection
model_choice = st.selectbox("Select Model", ("Linear Regression", "Random Forest"))

# Predict button
if st.button("Predict"):
    if model_choice == "Linear Regression":
        predicted_price = predict_price(floor, bedroom, bathroom, road, land, age, city_encoded)
        st.success(f"The predicted price using Linear Regression is: NRs {predicted_price:,.2f} Cr")
    else:
        predicted_price_rf = predict_price_rf(floor, bedroom, bathroom, road, land, age, city_encoded)
        st.success(f"The predicted price using Random Forest is: NRs {predicted_price_rf:,.2f} Cr")