import streamlit as st
import numpy as np
import pickle

# Load model

with open("Randomforestmodel.pkl","rb") as file:
    Randomforestmodel=pickle.load(file)

st.title("🍇 Raisin Prediction App")

st.write("Enter the raisin features below.")

Area = st.number_input("Area", min_value=0.0)
MajorAxisLength = st.number_input("Major Axis Length")
MinorAxisLength = st.number_input("Minor Axis Length")
Eccentricity = st.number_input("Eccentricity")
ConvexArea = st.number_input("Convex Area")
Extent = st.number_input("Extent")
Perimeter = st.number_input("Perimeter")

if st.button("Predict"):

    features = np.array([[Area,
                          MajorAxisLength,
                          MinorAxisLength,
                          Eccentricity,
                          ConvexArea,
                          Extent,
                          Perimeter]])

   

    prediction = Randomforestmodel.predict(features)

    if prediction[0] == 0:
        st.success("Prediction: Kecimen")
    else:
        st.success("Prediction: Besni")