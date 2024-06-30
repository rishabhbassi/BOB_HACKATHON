import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Set page config
st.set_page_config(page_title="Welcome to your Financial Dashboard", layout="wide")

# Custom CSS for styling
st.markdown(
    """
    <style>
    body {
        background-color: #FFD700; /* Yellow background */
        color: #FFA500; /* Orange text */
    }
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }
    .stButton>button {
        background-color: #FFA500; /* Orange button */
        color: #00000; /* Yellow text */
        border: none;
        padding: 0.5rem 1rem;
        border-radius: 0.25rem;
        font-size: 1rem;
    }
    .sidebar .sidebar-content {
        background-color: #FFA500; /* Orange sidebar */
    }
    .sidebar .sidebar-content .sidebar-item {
        color: #FFD700; /* Yellow sidebar text */
    }
    h1, h2, h3, h4 {
        color: #FFA500; /* Orange headings */
    }
    .card {
        background-color: #FFD700; /* Lighter shade of orange */
        color: #FFA500; /* Orange text */
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Generate dummy financial data with more variability
np.random.seed(42)
dates = pd.date_range(start="2023-01-01", periods=100)
aapl = (np.random.randn(100).cumsum() * 50 + 1500).round(2)  # Increased variability
googl = (np.random.randn(100).cumsum() * 80 + 28000).round(2)  # Increased variability
msft = (np.random.randn(100).cumsum() * 30 + 3000).round(2)  # Increased variability

data = pd.DataFrame({"Date": dates, "AAPL": aapl, "GOOGL": googl, "MSFT": msft})

# Home Page
def home_page():
    st.title("Welcome to your Financial Dashboard")
    st.header("Overview")
    st.write("### Total Assets: $500,000")
    st.write("### Investment Performance: 12%")

    st.markdown("### Key Metrics")
    col1, col2, col3 = st.columns(3)
    col1.metric("Monthly Growth", "2%")
    col2.metric("Annual Growth", "12%")
    col3.metric("Risk Level", "Moderate")

    st.markdown("### Upcoming Tasks")
    st.write("- Review investment portfolio")
    st.write("- Schedule meeting with financial advisor")
    st.write("- Rebalance assets for Q2")

# Dashboard
def dashboard_page():
    st.title("Investment Dashboard")

    st.markdown("### Investment Overview")
    fig = px.line(data, x="Date", y=["AAPL", "GOOGL", "MSFT"], labels={"value": "Price", "variable": "Company"})
    fig.update_traces(line=dict(width=2))  # Adjust line width for better visibility
    fig.update_layout(
        plot_bgcolor="#FFA500", paper_bgcolor="#FFA500",  # Yellow background
        font_color="#000000", title_font_color="#000000",  # Orange text
        legend_title_font_color="#000000"
    )
    st.plotly_chart(fig, use_container_width=True)

    st.markdown("### Financial Recommendations")
    st.write("Based on your financial goals and market analysis, we recommend:")
    st.markdown(
        """
        - Adjusting your portfolio allocation.
        - Exploring new investment opportunities.
        - Saving more for retirement.
        - Diversifying into international markets.
        """
    )

    st.markdown("### Account Settings")
    st.write("Manage your account settings here.")
    col1, col2, col3 = st.columns(3)
    col1.button("Edit Profile")
    col2.button("Change Password")
    col3.button("Log Out")

# Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Dashboard"])

if page == "Home":
    home_page()
else:
    dashboard_page()
