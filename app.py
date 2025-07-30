import streamlit as st
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import date

st.set_page_config(page_title="Travel Budget Planner", layout="centered")

st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&display=swap');

    .main-title {
        text-align: center;
        font-size: 56px;
        font-family: 'Playfair Display', serif;
        color: #5DADE2;
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
        text-align: center;
        margin: auto;
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
destination = st.sidebar.selectbox("Destination", ["Dubai", "Paris", "Bali", "New York", "Tokyo", "Iceland", "Rome"])
start_date = st.sidebar.date_input("Start Date", value=date.today())
end_date = st.sidebar.date_input("End Date", value=date.today())
travelers = st.sidebar.number_input("Number of Travelers", min_value=1, max_value=10, value=1)

trip_style = st.sidebar.selectbox("Trip Style", ["Relaxing", "Adventure", "Cultural", "Romantic", "Solo"])
accommodation_type = st.sidebar.selectbox("Accommodation Type", ["Hostel", "Hotel", "Resort", "Airbnb"])

daily_food_cost = st.sidebar.slider("Daily Food Cost per Person ($)", 5, 100, 30)
daily_transport_cost = st.sidebar.slider("Daily Transport Cost per Person ($)", 5, 100, 20)
extra_cost = st.sidebar.slider("Extra Costs (Fixed Amount, $)", 0, 1000, 50)


num_days = (end_date - start_date).days + 1 if end_date >= start_date else 0


if num_days > 0:
    cost = {
        "Accommodation": {"Hostel": 25, "Hotel": 60, "Resort": 120, "Airbnb": 50}[accommodation_type] * num_days * travelers,
        "Food": daily_food_cost * num_days * travelers,
        "Transport": daily_transport_cost * num_days * travelers,
        "Extras": extra_cost
    }

    df = pd.DataFrame(list(cost.items()), columns=["Category", "Cost"])
    total_cost = df["Cost"].sum()

    fig, ax = plt.subplots()
    colors = ['#FF9999', '#66B3FF', '#99FF99', '#FFCC99']
    ax.pie(df["Cost"], labels=df["Category"], autopct='%1.1f%%', startangle=90, colors=colors)
    ax.axis("equal")
    st.pyplot(fig)

    st.markdown(f'<div class="cost-highlight">Total Estimated Cost: ${total_cost:,.2f}</div>', unsafe_allow_html=True)

    
    travel_tips = {
        "Dubai": [
            "Dubai has one of the world’s most efficient metro systems.",
            "Visit during November to March for cooler weather.",
            "Many attractions offer discounts for booking online."
        ],
        "Paris": [
            "Parisians appreciate when tourists try speaking French.",
            "The Paris Museum Pass can save you a lot of money.",
            "Public transport is faster than taxis during rush hour."
        ],
        "Bali": [
            "Tap water isn’t safe to drink in Bali — stick to bottled water.",
            "Use Blue Bird taxis for reliable service.",
            "Ubud is great for culture; Seminyak for beaches."
        ],
        "New York": [
            "Subway is the fastest and cheapest way to get around.",
            "Museums often have pay-what-you-wish days.",
            "Download a city pass to save on major attractions."
        ],
        "Tokyo": [
            "Public transport is punctual and efficient.",
            "Cash is still widely used, even in big cities.",
            "Visit convenience stores — they’re surprisingly good!"
        ],
        "Iceland": [
            "Tap water is among the cleanest in the world.",
            "Weather can change fast — always layer up.",
            "Gas and food are pricey; plan accordingly."
        ],
        "Rome": [
            "Book Vatican tours in advance to avoid long lines.",
            "Many museums are free on the first Sunday of each month.",
            "Try local eateries away from tourist hubs for better food."
        ]
    }

    tips = travel_tips.get(destination, [])
    st.subheader(f"Did You Know? Travel Tips for {destination}")
    for tip in tips[:3]:
        st.markdown(f"- {tip}")
else:
    st.warning("Please ensure your end date is after your start date.")
