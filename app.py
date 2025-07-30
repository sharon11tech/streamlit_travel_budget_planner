import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Great+Vibes&display=swap');

    .main-title {
        text-align: center;
        font-size: 48px;
        font-family: 'Great Vibes', cursive;
        color: #5D3A00;
        margin-bottom: 10px;
        padding-top: 10px;
    }

    .cost-highlight {
        font-size: 24px;
        font-weight: bold;
        color: #2F4F4F;
        background-color: #F5F5F5;
        padding: 10px;
        border-radius: 8px;
        width: fit-content;
    }

    html, body, [class*="css"] {
        font-family: 'Georgia', serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="main-title">Travel Budget Planner</div>', unsafe_allow_html=True)

st.sidebar.header("Trip Details")
destination = st.sidebar.selectbox("Destination", ["Dubai", "Paris", "Bali", "New York", "Tokyo"])
days = st.sidebar.slider("Number of Days", 1, 30, 5)
travelers = st.sidebar.number_input("Number of Travelers", min_value=1, max_value=10, value=1)
budget_type = st.sidebar.radio("Budget Level", ["Low", "Medium", "Luxury"])
include_activities = st.sidebar.checkbox("Include Sightseeing & Activities", value=True)

costs = {
    "Low": {"accommodation": 20, "food": 15, "transport": 10, "activities": 10},
    "Medium": {"accommodation": 50, "food": 30, "transport": 20, "activities": 25},
    "Luxury": {"accommodation": 120, "food": 70, "transport": 40, "activities": 60}
}

daily = costs[budget_type]
total = {
    "Accommodation": daily["accommodation"] * days * travelers,
    "Food": daily["food"] * days * travelers,
    "Transport": daily["transport"] * days * travelers,
    "Activities": (daily["activities"] * days * travelers) if include_activities else 0
}

df = pd.DataFrame(list(total.items()), columns=["Category", "Cost"])
total_cost = df["Cost"].sum()

st.subheader(f"Estimated Budget for {destination} ({days} days, {travelers} traveler{'s' if travelers > 1 else ''})")

fig, ax = plt.subplots()
colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']
ax.pie(df["Cost"], labels=df["Category"], autopct='%1.1f%%', startangle=90, colors=colors)
ax.axis("equal")
st.pyplot(fig)

st.markdown(f'<div class="cost-highlight">Total Estimated Cost: ${total_cost:,.2f}</div>', unsafe_allow_html=True)
