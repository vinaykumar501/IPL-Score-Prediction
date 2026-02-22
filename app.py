import streamlit as st
import pickle
import numpy as np
import pandas as pd

model = pickle.load(open('model.pkl', 'rb'))
transformer = pickle.load(open('transformer.pkl', 'rb'))

st.title("IPL Score Prediction")

teams = [
'Sunrisers Hyderabad',
'Royal Challengers Bangalore',
'Mumbai Indians',
'Rising Pune Supergiant',
'Gujarat Lions',
'Kolkata Knight Riders',
'Kings XI Punjab',
'Delhi Daredevils',
'Chennai Super Kings',
'Rajasthan Royals',
'Deccan Chargers',
'Kochi Tuskers Kerala',
'Pune Warriors',
'Rising Pune Supergiants',
'Delhi Capitals'
]

batting_team = st.selectbox("Batting Team", teams)

bowling_teams = [team for team in teams if team != batting_team]
bowling_team = st.selectbox("Bowling Team", bowling_teams)

current_score = st.number_input("Current Score", min_value=0)
balls_left = st.number_input("Balls Left", min_value=1, max_value=120)
wickets_left = st.number_input("Wickets Left", min_value=0, max_value=10)
current_run_rate = st.number_input("Current Run Rate", min_value=0.0)

if st.button("Predict Score"):

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
