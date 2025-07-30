import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("✈️ Travel Budget Planner")

# Sidebar Inputs
st.sidebar.header("Enter Your Trip Details")

destination = st.sidebar.selectbox("Destination", ["Dubai", "Paris", "Bali", "New York", "Tokyo"])
days = st.sidebar.slider("Number of Days", 1, 30, 5)
travelers = st.sidebar.number_input("Number of Travelers", min_value=1, max_value=10, value=1)
budget_type = st.sidebar.radio("Budget Preference", ["Low", "Medium", "Luxury"])
include_activities = st.sidebar.checkbox("Include Activities/Sightseeing", value=True)

# Cost per day per person (in USD)
costs = {
    "Low": {"accommodation": 20, "food": 15, "transport": 10, "activities": 10},
    "Medium": {"accommodation": 50, "food": 30, "transport": 20, "activities": 25},
    "Luxury": {"accommodation": 120, "food": 70, "transport": 50, "activities": 60}
}

# Get selected cost values
selected = costs[budget_type]

# Calculate totals
total_accommodation = selected["accommodation"] * days * travelers
total_food = selected["food"] * days * travelers
total_transport = selected["transport"] * days * travelers
total_activities = selected["activities"] * days * travelers if include_activities else 0

total_cost = total_accommodation + total_food + total_transport + total_activities

# Display results
st.header("Estimated Trip Budget")

st.write(f"🌍 **Destination:** {destination}")
st.write(f"🗓️ **Duration:** {days} days")
st.write(f"👥 **Travelers:** {travelers}")
st.write(f"💼 **Budget Type:** {budget_type}")
st.write(f"🎡 **Activities Included:** {'Yes' if include_activities else 'No'}")

st.subheader("💰 Cost Breakdown:")
st.write(f"🏨 Accommodation: ${total_accommodation}")
st.write(f"🍽️ Food: ${total_food}")
st.write(f"🚗 Transport: ${total_transport}")
st.write(f"🎟️ Activities: ${total_activities}")
st.success(f"**Total Estimated Cost: ${total_cost}**")

# Pie Chart
labels = ['Accommodation', 'Food', 'Transport']
sizes = [total_accommodation, total_food, total_transport]

if include_activities:
    labels.append('Activities')
    sizes.append(total_activities)

fig, ax = plt.subplots()
ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
ax.axis('equal')
st.pyplot(fig)
