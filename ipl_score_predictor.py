# Redesigned IPL Score Predictor UI
import math
import numpy as np
import pickle
import streamlit as st

# PAGE CONFIG
st.set_page_config(
    page_title='IPL SCORE PREDICTOR',
    layout="centered"
)

# LOAD MODEL
filename = 'ml_model.pkl'
model = pickle.load(open(filename, 'rb'))

# NEW CLEAN MINIMALISTIC UI STYLE
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #020024, #090979, #00d4ff);
        background-attachment: fixed;
    }
    .card {
        background: rgba(255, 255, 255, 0.18);
        padding: 28px;
        border-radius: 18px;
        backdrop-filter: blur(12px);
        -webkit-backdrop-filter: blur(12px);
        border: 1px solid rgba(255, 255, 255, 0.25);
        margin-bottom: 22px;
    }
    h1 {
        color: #00eaff;
        text-shadow: 0px 0px 12px #00eaff;
        font-weight: 900;
    }
    label, .st-bx, .stNumberInput label {
        color: white !important;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# 🔹 UPDATED HEADING
st.markdown("<h1 style='text-align:center;'>🏏 IPL SCORE PREDICTOR</h1>", unsafe_allow_html=True)

# TEAMS
teams = [
    'Chennai Super Kings',
    'Delhi Capitals',
    'Punjab Kings',
    'Kolkata Knight Riders',
    'Mumbai Indians',
    'Rajasthan Royals',
    'Royal Challengers Bangalore',
    'Sunrisers Hyderabad'
]

# MAIN INPUT CARD
st.markdown("<div class='card'>", unsafe_allow_html=True)

colA, colB = st.columns(2)
with colA:
    batting_team = st.selectbox('🏏 Select Batting Team', teams, index=None)
with colB:
    bowling_team = st.selectbox('🎯 Select Bowling Team', teams, index=None)

prediction_array = []

# Encoding batting team
for t in teams:
    prediction_array.append(1 if batting_team == t else 0)

# Error if same team selected
if batting_team == bowling_team and batting_team is not None:
    st.error("Batting and Bowling teams must be different")

# Encoding bowling team
for t in teams:
    prediction_array.append(1 if bowling_team == t else 0)

# NUMERIC INPUT SECTION
st.markdown("### 🔢 Match Details", unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)
with col1:
    overs = st.number_input('Overs Completed', min_value=0.0, max_value=20.0, step=0.1)

with col2:
    runs = st.number_input('Total Runs Scored', min_value=0, max_value=400, step=1)

with col3:
    # ✅ Wickets as slider
    wickets = st.slider('Wickets Fallen', min_value=0, max_value=10, value=0, step=1)

# VALIDATION FOR OVERS
if overs - math.floor(overs) > 0.5:
    st.error("Invalid over format. Valid examples: 10.0 to 10.5")

st.markdown("### 📊 Last 5 Overs Stats", unsafe_allow_html=True)
col4, col5 = st.columns(2)
with col4:
    runs_in_prev_5 = st.number_input('Runs in Last 5 Overs', min_value=0, max_value=200, step=1)
with col5:
    wickets_in_prev_5 = st.slider('Wickets in Last 5 Overs', min_value=0, max_value=10, value=0, step=1)

st.markdown("</div>", unsafe_allow_html=True)

# FINAL PREDICTION
prediction_array = prediction_array + [runs, wickets, overs, runs_in_prev_5, wickets_in_prev_5]
prediction_array = np.array([prediction_array])
predict = model.predict(prediction_array)

# PREDICT BUTTON
st.markdown("<div class='card'>", unsafe_allow_html=True)
if st.button('🔮 Predict Final Score'):
    score = int(round(predict[0]))
    st.success(f"🏆 **Predicted Score Range:** {score - 5} to {score + 5}")
st.markdown("</div>", unsafe_allow_html=True)
