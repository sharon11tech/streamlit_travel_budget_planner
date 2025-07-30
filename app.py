import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

st.set_page_config(page_title="Travel Budget Planner", layout="centered")

st.markdown("<h1 style='text-align: center; font-family: Brush Script MT; color: #3B3B98;'>Travel Budget Planner</h1>", unsafe_allow_html=True)

with st.sidebar:
    st.header("Trip Preferences")
    destination = st.selectbox("Choose your destination", ["Paris", "Tokyo", "New York", "Dubai", "Bali", "Rome", "Istanbul"])
    start_date = st.date_input("Trip Start Date")
    end_date = st.date_input("Trip End Date")
    trip_style = st.selectbox("Trip Style", ["Adventure", "Relaxation", "Business", "Family"])
    accommodation_type = st.selectbox("Accommodation Type", ["Hostel", "Hotel", "Airbnb", "Resort"])
    food_cost = st.slider("Daily food cost ($)", 10, 100, 30)
    transport_cost = st.slider("Daily transport cost ($)", 5, 80, 20)
    shopping_cost = st.slider("Total shopping/extra cost ($)", 0, 1000, 150)

if end_date < start_date:
    st.error("End date must be after start date.")
else:
    num_days = (end_date - start_date).days + 1

    accommodation_multipliers = {
        "Hostel": 20,
        "Hotel": 50,
        "Airbnb": 40,
        "Resort": 80
    }

    daily_accommodation_cost = accommodation_multipliers[accommodation_type]
    total_food = food_cost * num_days
    total_transport = transport_cost * num_days
    total_accommodation = daily_accommodation_cost * num_days
    total_cost = total_food + total_transport + total_accommodation + shopping_cost

    st.subheader("Trip Summary")
    st.write(f"**Destination:** {destination}")
    st.write(f"**Trip Style:** {trip_style}")
    st.write(f"**Accommodation Type:** {accommodation_type}")
    st.write(f"**Duration:** {num_days} days ({start_date.strftime('%b %d')} to {end_date.strftime('%b %d')})")

    tips = {
        "Paris": ["Buy a museum pass to save money.", "Use metro to get around cheaply."],
        "Tokyo": ["Get a prepaid IC card for transport.", "Many restaurants offer budget lunch boxes."],
        "New York": ["Use the subway instead of taxis.", "Many museums have free entry days."],
        "Dubai": ["Travel during shoulder season for cheaper rates.", "Use Nol card for metro and buses."],
        "Bali": ["Eat at warungs for cheap local food.", "Rent a scooter for local travel."],
        "Rome": ["Drink from public fountains—it’s clean.", "Walking is the best way to explore the city."],
        "Istanbul": ["Buy a museum card to save on entry fees.", "Try ferries for scenic and cheap transport."]
    }

    st.markdown("---")
    st.subheader("Travel Tips ✨")
    for tip in tips[destination]:
        st.info(tip)

    st.markdown("---")
    st.subheader("Expense Breakdown")
    expenses = pd.Series({
        "Accommodation": total_accommodation,
        "Food": total_food,
        "Transport": total_transport,
        "Shopping/Extras": shopping_cost
    })

    fig, ax = plt.subplots()
    colors = ["#E59866", "#58D68D", "#5DADE2", "#AF7AC5"]
    ax.pie(expenses, labels=expenses.index, autopct='%1.1f%%', startangle=90, colors=colors)
    ax.axis('equal')
    st.pyplot(fig)

    st.markdown("---")
    st.markdown(f"<h3 style='color:#1F618D;'>Total Estimated Cost: <span style='color:#117864;'>${total_cost:,.2f}</span></h3>", unsafe_allow_html=True)
