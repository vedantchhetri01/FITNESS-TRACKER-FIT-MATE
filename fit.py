import streamlit as st
import numpy as np
import plotly.graph_objects as go
from datetime import datetime, timedelta
from plyer import notification
import random
import time


def calculate_calories(activity_type, weight, duration):
    activity_factor = {
        'Running': 0.063,
        'Walking': 0.029,
        'Cycling': 0.045,
        'Swimming': 0.06,
        'Yoga': 0.02
    }
    return weight * activity_factor.get(activity_type, 0) * duration
MOTIVATIONAL_QUOTES = [
    "The journey of a thousand miles begins with a single step.",
    "You don’t have to be great to start, but you have to start to be great.",
    "Don’t limit your challenges, challenge your limits!",
    "Push yourself because no one else is going to do it for you.",
    "Take care of your body. It’s the only place you have to live."
]
DAILY_CHALLENGES = [
    "Walk an extra 1,000 steps today!",
    "Take a 5-minute stretch break after every hour of work.",
    "Drink 8 glasses of water today.",
    "Do 10 push-ups before lunch.",
    "Take the stairs instead of the elevator!"
]

st.set_page_config(page_title="Fit-Mate", page_icon="🏋️", layout="wide")

st.markdown("<h1 style='text-align: center;'>🏋️ Fit-Mate </h1>", unsafe_allow_html=True)

st.markdown("<h3 style='text-align: center;'>Stay fit and track your progress effortlessly!</h3>", unsafe_allow_html=True)

st.markdown("<div style='height: 100px;'></div>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.subheader("💡 Motivational Quote")
    st.info(random.choice(MOTIVATIONAL_QUOTES))

    steps_today = np.random.randint(500, 10000)
    st.subheader("🚶 Step Counter")
    st.metric("Steps Today", f"{steps_today} steps")
    st.subheader("🔥 Calorie Tracker")
    activity_type = st.selectbox("Activity Type", ['Running', 'Walking', 'Cycling', 'Swimming', 'Yoga'])
    weight = st.number_input("Weight (kg)", min_value=30, max_value=200, value=70)
    duration = st.number_input("Duration (min)", min_value=1, max_value=120, value=30)
    if st.button("Calculate Calories"):
        calories = calculate_calories(activity_type, weight, duration)
        st.success(f"Calories burned: **{calories:.2f} kcal**")
with col2:
    st.subheader("🎯 Daily Challenge")
    daily_challenge = random.choice(DAILY_CHALLENGES)
    st.info(f"Today's Challenge: {daily_challenge}")
    if st.button("Mark Challenge as Completed"):
        st.success("🎉 Challenge Completed! Great Job!")
    st.subheader("📊 Interactive Poll")
    poll_question = "Which feature would you like us to add next?"
    poll_options = [
        "Integration with fitness devices (Fitbit/Google Fit)",
        "Advanced calorie tracking for food intake",
        "Gamification: Badges and rewards",
        "Weekly progress reports"
    ]
    user_vote = st.radio(poll_question, poll_options)
    if st.button("Submit Vote"):
        st.success(f"Thanks for voting! You selected: **{user_vote}**")

    st.subheader("🎁 Unlock Today's Gift")
    if st.button("Unlock Gift"):
        st.balloons()
        reward = random.choice(["10% off on fitness gear", "Exclusive Badge: Calorie Crusher", "Free Yoga Class", "Extra 500 Steps Added"])
        st.success(f"Congratulations! You unlocked: {reward}")


st.markdown("---")

col3, col4 = st.columns([1, 1])

with col3:

    st.subheader("📈 Activity Graph")
    days = np.arange(1, 11)
    steps = np.random.randint(4000, 12000, size=10)
    calories_burned = np.random.randint(200, 800, size=10)
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=days,
        y=steps,
        mode='lines+markers',
        name='Steps',
        line=dict(color='blue', width=3),
        marker=dict(size=8, color='blue')
    ))

   
    fig.add_trace(go.Scatter(
        x=days,
        y=calories_burned,
        mode='lines+markers',
        name='Calories Burned',
        line=dict(color='orange', width=3, dash='dash'),
        marker=dict(size=8, color='orange')
    ))

  
    fig.update_layout(
        title="Activity Progress Over 10 Days",
        xaxis=dict(title='Day', tickmode='linear', tick0=1, dtick=1),
        yaxis=dict(title='Value'),
        legend=dict(title="Metrics"),
        template='plotly_dark',
        plot_bgcolor='rgba(0, 0, 0, 0)',
        paper_bgcolor='rgba(0, 0, 0, 0)',
    )
    peak_day = days[np.argmax(steps)]
    peak_steps = max(steps)
    fig.add_trace(go.Scatter(
        x=[peak_day],
        y=[peak_steps],
        mode='markers+text',
        text=['🏆 Peak Day'],
        textposition="top center",
        marker=dict(size=12, color='green', symbol='star')
    ))
    st.plotly_chart(fig, use_container_width=True)

with col4:
    st.subheader("🎯 Set Fitness Goals")
    goal_date = st.date_input("Select Goal Date", datetime.today() + timedelta(days=30))
    goal_steps = st.number_input("Target Steps per Day", min_value=1, max_value=50000, value=10000)
    if st.button("Set Fitness Goal"):
        progress = steps_today / goal_steps
        progress = min(progress, 1.0)  # Ensure value is between 0 and 1
        st.success(f"Fitness Goal Set: {goal_steps} steps per day by {goal_date}")
        st.progress(progress)

    st.subheader("🔮 Fitness Horoscope")
    zodiac_signs = [
    "Aries", "Taurus", "Gemini", "Cancer", "Leo", "Virgo",
    "Libra", "Scorpio", "Sagittarius", "Capricorn", "Aquarius", "Pisces"
]
    user_zodiac = st.selectbox("Select Your Zodiac Sign:", zodiac_signs)
    fitness_horoscopes = {
    "Aries": "Your energy is unstoppable today! Focus on cardio for a great workout.",
    "Taurus": "Strength training suits you today. Build that foundation!",
    "Gemini": "Variety is key—try a mix of yoga and cycling today.",
    "Cancer": "Relaxation is important. A calming yoga session will refresh you.",
    "Leo": "The spotlight is on you! Join a group workout and shine.",
    "Virgo": "Precision matters. Work on form and technique in your exercises.",
    "Libra": "Balance is key. Mix strength training with light stretches.",
    "Scorpio": "Your intensity will drive results. Focus on interval training.",
    "Sagittarius": "Adventure awaits! Take a hike or try a new outdoor activity.",
    "Capricorn": "Discipline will lead to success. Stick to your planned workout.",
    "Aquarius": "Innovation inspires you—explore a dance or fitness class.",
    "Pisces": "Go with the flow. A swim or water-based workout will suit you."
}

    if st.button("Get My Fitness Horoscope"):
        
        st.success(f"**{user_zodiac} Horoscope:** {fitness_horoscopes.get(user_zodiac)}")


col5, col6 = st.columns([1, 1])

with col5:
    st.subheader("⏰ Set Reminders")
    reminder_time = st.time_input("Reminder Time", datetime.now().time())
    if st.button("Set Reminder"):
        reminder_message = f"Reminder: Time to work out! 🏋️"
        st.info(f"Simulated Notification: '{reminder_message}' at {reminder_time}")
        notification.notify(
            title="Fitness Reminder",
            message=reminder_message,
            timeout=10
        )

with col6:
    st.subheader("🧘 Stress and Sleep Monitoring")
    stress_level = st.slider("How stressed are you feeling today? (0 = Relaxed, 10 = Very Stressed)", 0, 10, 5)

    if stress_level > 7:
        st.info("You're feeling highly stressed. Here are some relaxation exercises:")
        relaxation_exercises = [
            "Take 5 deep breaths, holding each for 4 seconds.",
            "Spend 10 minutes doing light yoga or stretching.",
            "Listen to calming music or nature sounds for 10 minutes.",
            "Practice progressive muscle relaxation: tense and release each muscle group."
        ]
        st.write(random.choice(relaxation_exercises))
    elif stress_level > 3:
        st.info("Moderate stress detected. Consider trying this:")
        st.write("Take a short walk outside or do 5 minutes of meditation.")
    else:
        st.success("You seem relaxed today! Keep up the good work.")


st.markdown("<div style='height: 50px;'></div>", unsafe_allow_html=True)


message = "Thank you for being connected !"
scroll_speed = 0.1 

placeholder = st.empty()
st.markdown("<div style='height: 300px;'></div>", unsafe_allow_html=True)

while True:
    for i in range(len(message)):
      
        animated_message = message[i:] + message[:i]
        
        
        centered_message = " " * (len(message) // 2) + animated_message
        with placeholder.container():
            st.write(f"<h3 style='text-align: center;'>{animated_message}</h3>", unsafe_allow_html=True)
            time.sleep(scroll_speed)
	