# Import necessary libraries
import streamlit as st
import yfinance as yf

# Page configuration
st.set_page_config(page_title="Stock Futures Pricing App", page_icon="📈")

# Title
st.title("Stock Futures Pricing App")

# Sidebar for user input
symbol = st.sidebar.text_input("Enter Stock Symbol", "AAPL")
expiration_date = st.sidebar.date_input("Select Expiration Date", value=None)
strike_price = st.sidebar.number_input("Enter Strike Price", value=0.0)
option_type = st.sidebar.radio("Select Option Type", ("Call", "Put"))

# Fetch stock data
stock_data = yf.Ticker(symbol)
stock_price = stock_data.history(period='1d')['Close'][0]

# Calculate option price (you may need a more sophisticated pricing model)
if option_type == "Call":
    option_price = max(stock_price - strike_price, 0)
else:
    option_price = max(strike_price - stock_price, 0)

# Display results
st.write(f"Stock Price: ${stock_price}")
st.write(f"Option Price: ${option_price}")

# Additional features can be added based on your requirements
