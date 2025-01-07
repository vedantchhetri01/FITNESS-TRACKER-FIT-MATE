# Fit-Mate - Fitness Tracker App
Fit-Mate is an interactive fitness tracking app designed to help users stay motivated and track their progress. With a user-friendly interface powered by Streamlit, the app offers a variety of features aimed at enhancing the fitness journey.


https://github.com/user-attachments/assets/df09e9fe-ab61-4784-8d27-061b53f91864




Features:-
Motivational Quotes: Get inspired with random daily quotes to keep you motivated.

Step Counter: Simulate your daily steps with a random step count, helping you track your physical activity.

Calorie Tracker: Calculate the calories burned based on activity type (e.g., running, walking, cycling), weight, and duration.

Daily Fitness Challenges: Complete daily fitness challenges and mark them as completed for extra motivation.

Polls and Feedback: Vote on future feature requests and give feedback for improving the app.

Unlock Rewards: Unlock random rewards like fitness gear discounts, exclusive badges, or bonus steps.

Activity Graph: Visualize your fitness progress over 10 days with a chart showing steps and calories burned.

Set Fitness Goals: Set a fitness goal for steps per day and track your progress.

Fitness Horoscope: Receive a personalized fitness horoscope based on your zodiac sign, with exercise recommendations.

Reminders: Set workout reminders to stay on track and get notified at your chosen time.

Stress and Sleep Monitoring: Assess your stress level and receive suggestions for relaxation exercises based on your stress rating.

Key Components and Technologies:
Streamlit:
          
     Streamlit is the main framework used to create the interactive web application. It simplifies the process of building web apps with Python, providing a clean and easy-to-use               interface for users.
          Streamlit allows for real-time updates of visual components like charts, text, and interactive widgets (such as buttons, sliders, and selectboxes) with minimal code.
NumPy:

      NumPy is used for numerical operations. In this app, it is used to generate random numbers for the daily steps and for creating the data arrays (e.g., steps and calories burned) displayed in the activity graph.
      It is also useful in generating random values for the simulated steps taken and calories burned over the course of several days.
Plotly:

      Plotly is a graphing library that creates interactive visualizations. It is used in the app to plot the activity graph, which shows the steps and calories burned over the last 10 days.
      Plotly charts are highly customizable and allow for hover effects, tooltips, and other interactive features to engage users.
Plyer:

      Plyer is used to send desktop notifications to users. The app leverages this library to notify users of reminders to work out, providing a simple notification system to help users stay on track with their fitness goals.
      Notifications are simulated for the purpose of user interaction and to promote healthy habits.
Random Module:

      The random module is used throughout the app to simulate step counts, calorie burns, daily challenges, rewards, and other elements that provide users with a fun, engaging experience.
      For example, it generates random motivational quotes and fitness challenges, as well as random rewards when users "unlock gifts."
Datetime:

      Datetime is used to manage and display date and time-based elements. It helps with calculating goal deadlines, setting reminders, and displaying activity over time.
      The timedelta function is used to add 30 days to the current date when setting fitness goals.
