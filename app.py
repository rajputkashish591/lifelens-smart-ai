import streamlit as st
import pandas as pd
import os
import datetime

# Page Config
st.set_page_config(page_title="LifeLens AI", layout="centered")

st.title("🧠 LifeLens AI - Smart Life Predictor")

# ---------------- INPUT ----------------
st.subheader("📊 Enter Your Daily Data")

study = st.slider("📚 Study Hours", 0, 12)
phone = st.slider("📱 Phone Usage (hrs)", 0, 12)
sleep = st.slider("😴 Sleep Hours", 0, 12)

# ---------------- AI LOGIC ----------------
def predict_risk(study, phone, sleep):
    score = 0
    
    if study < 3:
        score += 2
    if phone > 5:
        score += 2
    if sleep < 6:
        score += 2
    
    if score <= 2:
        return "Low Risk ✅"
    elif score <= 4:
        return "Medium Risk ⚠️"
    else:
        return "High Risk ❌"

def give_solution(risk):
    if "High" in risk:
        return "⚠️ High Risk! Reduce phone usage, study at least 4-6 hrs, and sleep 7-8 hrs."
    
    elif "Medium" in risk:
        return "⚡ Medium Risk. Improve consistency and reduce distractions."
    
    else:
        return "✅ Excellent! Keep maintaining your routine."

def generate_plan(risk):
    if "High" in risk:
        return """
📅 **Daily Plan:**
- Study: 4-6 hrs  
- Phone: < 3 hrs  
- Sleep: 7-8 hrs  
- Breaks: Every 1 hr  
"""
    elif "Medium" in risk:
        return """
📅 **Daily Plan:**
- Study: 3-5 hrs  
- Phone: < 4 hrs  
- Sleep: 7 hrs  
"""
    else:
        return """
📅 **Daily Plan:**
- Maintain your current routine 👍  
"""

# ---------------- FILE ----------------
file = "data.csv"

# ---------------- ANALYZE ----------------
if st.button("🚀 Analyze My Life"):

    result = predict_risk(study, phone, sleep)

    st.subheader("📊 Result")
    st.success(result)

    st.subheader("💡 Suggestion")
    st.info(give_solution(result))

    st.subheader("📅 Smart Plan")
    st.markdown(generate_plan(result))

    # Save Data with Date
    today = datetime.date.today()

    new_data = pd.DataFrame({
        "Date": [today],
        "Study": [study],
        "Phone": [phone],
        "Sleep": [sleep]
    })

    if os.path.exists(file):
        old_data = pd.read_csv(file)
        data = pd.concat([old_data, new_data], ignore_index=True)
    else:
        data = new_data

    data.to_csv(file, index=False)

# ---------------- HISTORY ----------------
if os.path.exists(file):

    st.subheader("📈 Progress Dashboard")

    data = pd.read_csv(file)

    st.line_chart(data[["Study", "Phone", "Sleep"]])

    st.dataframe(data)

# ---------------- CHATBOT ----------------
st.subheader("🤖 AI Mentor (Basic)")

user_input = st.text_input("Ask anything about study, focus, routine...")

def chatbot_reply(msg):
    msg = msg.lower()
    
    if "study" in msg:
        return "Try Pomodoro technique: 25 min study + 5 min break."
    elif "focus" in msg:
        return "Keep your phone away and use distraction blockers."
    elif "sleep" in msg:
        return "Sleep at least 7-8 hours daily for better performance."
    elif "phone" in msg:
        return "Limit social media and use apps like Digital Wellbeing."
    else:
        return "Stay consistent and disciplined 👍"

if user_input:
    st.write("💬 AI:", chatbot_reply(user_input))

# ---------------- MOTIVATION ----------------
st.subheader("🔥 Daily Motivation")

st.success("“Small improvements daily lead to big success.” 🚀")