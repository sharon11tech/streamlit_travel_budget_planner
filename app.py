

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# ========== Custom CSS for clean font and layout ==========
st.markdown(
    """
    <style>
    html, body, [class*="css"] {
        font-family: 'Georgia', serif;
        background-color: #FAFAFA;
    }
    .centered-title {
        text-align: center;
        font-size: 36px;
        font-weight: bold;
        padding-top: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ========== Centered Title ==========
st.markdown('<div class="centered-title">Travel Budget Planner</div>', unsafe_allow_html=True)

# ========== Sidebar Inputs ==========
st.sidebar.header("Trip Details")

destination = st.sidebar.selectbox("Destination", ["Dubai", "Paris", "Bali", "New York", "Tokyo"])
days = st.sidebar.slider("Number of Days", 1, 30, 5)
travelers = st.sidebar.number_input("Number of Travelers", min_value=1, max_value=10, value=1)
budget_type = st.sidebar.radio("Budget Level", ["Low", "Medium", "Luxury"])
include_activities = st.sidebar.checkbox("Include Sightseeing & Activities", value=True)

# ========== Budget Values ==========
costs = {
    "Low": {"accommodation": 20, "food": 15, "transport": 10, "activities": 10},
    "Medium": {"accommodation": 50, "food": 30, "transport": 20, "activities": 25},
    "Luxury": {"accommodation": 120, "food": 70, "transport": 50, "activities": 60}
}

# ========== Calculations ==========
selected = costs[budget_type]

total_accommodation = selected["accommodation"] * days * travelers
total_food = selected["food"] * days * travelers
total_transport = selected["transport"] * days * travelers
total_activities = selected["activities"] * days * travelers if include_activities else 0

total_cost = total_accommodation + total_food + total_transport + total_activities

# ========== Display Results ==========
st.subheader("Estimated Budget Summary")
st.write(f"**Destination:** {destination}")
st.write(f"**Duration:** {days} days")
st.write(f"**Travelers:** {travelers}")
st.write(f"**Budget Level:** {budget_type}")
st.write(f"**Include Activities:** {'Yes' if include_activities else 'No'}")

# Budget breakdown
st.markdown("### Cost Breakdown")
st.write(f"**Accommodation:** ${total_accommodation}")
st.write(f"**Food:** ${total_food}")
st.write(f"**Transport:** ${total_transport}")
st.write(f"**Activities:** ${total_activities}")
st.markdown(f"### **Total Estimated Cost: ${total_cost}**")

# ========== Pie Chart ==========
labels = ['Accommodation', 'Food', 'Transport']
sizes = [total_accommodation, total_food, total_transport]

if include_activities:
    labels.append('Activities')
    sizes.append(total_activities)

colors = ['#88AB8E', '#C7B7A3', '#A4907C', '#EEE3CB']

fig, ax = plt.subplots(figsize=(6, 6))
wedges, texts, autotexts = ax.pie(
    sizes,
    labels=labels,
    autopct='%1.1f%%',
    startangle=90,
    shadow=True,
    colors=colors,
    wedgeprops={'edgecolor': 'black', 'linewidth': 1}
)
ax.axis('equal')
plt.setp(autotexts, size=10, weight='bold')
st.pyplot(fig)
