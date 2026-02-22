import streamlit as st
import pickle  
import numpy as np
model = pickle.load(open('model.pkl', 'rb'))
transformer = pickle.load(open('transformer.pkl', 'rb'))
st.title("IPL Score Prediction")
teams = [
    'Chennai Super Kings',
    'Mumbai Indians',
    'Royal Challengers Bangalore',
    'Kolkata Knight Riders',
    'Sunrisers Hyderabad',
    'Delhi Capitals',
    'Punjab Kings',
    'Rajasthan Royals',
    'Lucknow Super Giants',
    'Gujarat Titans'
]
batting_team = st.selectbox("Batting Team", teams)
bowling_team = st.selectbox("Bowling Team", teams)
current_score = st.number_input("Current Score", min_value=0)
balls_left = st.number_input("Balls Left", min_value=0, max_value=120)
wickets_left = st.number_input("Wickets Left", min_value=0, max_value=10)
current_run_rate = st.number_input("Current Run Rate", min_value=0.0)
if st.button("Predict Score"):
    import pandas as pd
    input_data = pd.DataFrame([{
        'batting_team': batting_team,
        'bowling_team': bowling_team,
        'current_score': current_score,
        'balls_left': balls_left,
        'wickets_left': wickets_left,
        'current_run_rate': current_run_rate
    }])
    input_transformed = transformer.transform(input_data)
    prediction = model.predict(input_transformed)
    st.success(f"Predicted Final Score: {int(prediction[0])}")