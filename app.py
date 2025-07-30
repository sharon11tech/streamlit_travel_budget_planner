import streamlit as st
import matplotlib.pyplot as plt
from datetime import date

st.set_page_config(page_title="Travel Budget Planner", layout="centered")

st.markdown("<h1 style='text-align: center; font-family: Brush Script MT, cursive; color:#2E4053;'>Travel Budget Planner</h1>", unsafe_allow_html=True)
st.markdown("### Plan your trip with cost estimates")

destination = st.selectbox("Choose Destination", ["Tokyo", "Paris", "New York", "Dubai", "Cape Town"])

start_date = st.date_input("Start Date", value=date.today())
end_date = st.date_input("End Date", value=date.today())

if end_date < start_date:
    st.warning("End date must be after start date.")
    st.stop()

num_days = (end_date - start_date).days + 1

accommodation = st.number_input("Accommodation (per day)", value=100)
food = st.number_input("Food (per day)", value=50)
transport = st.number_input("Transport (per day)", value=30)
activities = st.number_input("Activities (total)", value=100)

total_cost = num_days * (accommodation + food + transport) + activities


summaries = {
    "Tokyo": {
        "summary": "A vibrant blend of tradition and tech. Prepare for an efficient, fast-paced experience.",
        "tips": [
            "Use a Suica or Pasmo card for public transport.",
            "Many places only accept cash — carry some yen.",
            "Try sushi at Tsukiji Market early in the morning!"
        ]
    },
    "Paris": {
        "summary": "Romantic charm, rich culture, and world-class cuisine.",
        "tips": [
            "Book Eiffel Tower tickets in advance to skip long lines.",
            "Consider a museum pass if visiting multiple attractions.",
            "Watch out for pickpockets in crowded areas."
        ]
    },
    "New York": {
        "summary": "The city that never sleeps — dynamic, diverse, and thrilling.",
        "tips": [
            "Use the subway for quick and cheap travel.",
            "Central Park is beautiful year-round.",
            "Tipping is customary — usually 15–20%."
        ]
    },
    "Dubai": {
        "summary": "A modern oasis with luxury shopping and desert adventures.",
        "tips": [
            "Dress modestly in public places.",
            "Public transport is clean and efficient.",
            "Visit in winter (Nov–Feb) for cooler weather."
        ]
    },
    "Cape Town": {
        "summary": "Spectacular nature meets vibrant culture.",
        "tips": [
            "Table Mountain closes during bad weather — check ahead.",
            "Tap water is safe to drink.",
            "Use Uber or Bolt for safe transportation."
        ]
    }
}

st.markdown("### 🧳 Trip Summary")
st.markdown(f"You're planning a **{num_days}-day** trip to **{destination}**.")
st.markdown(f"**Overview:** {summaries[destination]['summary']}")
st.markdown("**Did you know?**")
for tip in summaries[destination]['tips']:
    st.markdown(f"- {tip}")


labels = ['Accommodation', 'Food', 'Transport', 'Activities']
values = [accommodation * num_days, food * num_days, transport * num_days, activities]

fig, ax = plt.subplots()
colors = ['#7FB3D5', '#F7DC6F', '#82E0AA', '#F1948A']
ax.pie(values, labels=labels, autopct='%1.1f%%', colors=colors, startangle=140)
ax.axis('equal')
st.pyplot(fig)


st.markdown("---")
st.markdown(f"<h3 style='color:#1A5276;'>Total Estimated Cost: <span style='color:#148F77;'>${total_cost:,.2f}</span></h3>", unsafe_allow_html=True)
