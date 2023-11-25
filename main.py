# Author: Guson Ulysse
# Date: 11/24/2023
import requests
import os

STOCK = "CVS"

# Load sensitive data from environment variables
stock_market_api_key = os.getenv('ALPHAVANTAGE_API_KEY')  # API key for alpha
news_api_key = os.getenv('NEWSAPI_API_KEY')  # API key for newsapi
bot_token = os.getenv('BOT_TOKEN')  # Token for telegram messaging bot
chat_id = os.getenv('CHAT_ID')  # Token for telegram chat id

# API endpoints for Alpha Vantage and NewsAPI
alpha_endpoint = 'https://www.alphavantage.co/query'
news_api_endpoint = 'https://newsapi.org/v2/everything'

# Setting up the parameters for the API requests
alpha_params = {
    'function': 'TIME_SERIES_DAILY',
    'symbol': 'CVS',
    'apikey': stock_market_api_key,
}

news_params = {
    'q': 'cvs',
    'searchin': 'title',
    'sortby': 'publishedAt',
    'apiKey': news_api_key,
    'pageSize': 1,
}

# Performing API requests to get stock data and news data
stock_data = requests.get(url=alpha_endpoint, params=alpha_params)
news_data = requests.get(url=news_api_endpoint, params=news_params)

# Raise an exception for HTTP errors
stock_data.raise_for_status()
news_data.raise_for_status()

# Parsing the JSON response to extract relevant information
stocks_info = stock_data.json()
news_info = news_data.json()
headline = news_info['articles'][0]['title']
news_description = news_info['articles'][0]['description']

# Extracting the recent and previous closing prices of the stock
recent_ending_price = stocks_info['Time Series (Daily)']['2023-11-24']['4. close']
previous_ending_price = stocks_info['Time Series (Daily)']['2023-11-22']['4. close']

# Computing the percentage change in stock price
change_in_stock_price = (float(recent_ending_price) - float(previous_ending_price)) / float(previous_ending_price) * 100
num_rounded = format(change_in_stock_price, ".1f")


def telegram_bot_sendtext(bot_message):
    # Construct the URL for the Telegram sendMessage API
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + chat_id + '&parse_mode=Markdown&text=' + bot_message

    # Send the request to Telegram API and get the response
    response = requests.get(send_text)

    # Return the JSON response
    return response.json()


# Constructing the message based on stock performance
if change_in_stock_price >= 0:
    message = f"{STOCK}: 🔺{num_rounded}%\nHeadline: {headline}\nBrief: {news_description}"
else:
    message = f"{STOCK}: 🔻{num_rounded}%\nHeadline: {headline}\nBrief: {news_description}"

# Sending the message via Telegram bot
telegram_bot_sendtext(message)



