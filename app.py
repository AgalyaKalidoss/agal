import streamlit as st
import joblib

# Load trained model
model = joblib.load("placement_model.pkl")

# Title
st.title("🎓 Placement Prediction App")
st.write("Enter your CGPA to check placement status.")

# Input from user
cgpa_value = st.number_input("Enter your CGPA:", min_value=0.0, max_value=10.0, step=0.01)

# Prediction logic
if st.button("Check Placement Status"):
    predicted_value = model.predict([[cgpa_value]])[0]
    cgpa_cutoff = 7.0  # fixed threshold, change if needed

    if cgpa_value >= cgpa_cutoff:
        st.success("✅ You can get placed!")
    else:
        st.warning("⚠️ Do more best to rise the CGPA.")
