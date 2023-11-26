<h1>"Stock Info and News Update Bot"</h1>
<br />
</br>

<h2>Overview</h2>

This Python-based application monitors CVS stock prices, retrieves relevant news articles, and sends updates via a Telegram bot. 
It utilizes the Alpha Vantage API for stock data and the NewsAPI for news articles.
<br />


<h2>Features</h2>

1. **Automated Stock Monitoring:** The bot automatically monitors the stock price of CVS using the Alpha Vantage API. This feature provides real-time tracking of stock performance, which is essential for investors and financial analysts.

2. **Daily Stock Price Change Calculation:** The application calculates the daily percentage change in the CVS stock price. This is a crucial metric for users tracking stock market movements and making investment decisions.

3. **Real-time News Updates:** Integrates with the NewsAPI to fetch the latest news articles related to CVS. This feature helps users stay informed about recent developments that might impact the stock's performance.

4. **Telegram Bot Integration:** The project features a Telegram bot that sends customized notifications to users. These notifications include stock price updates and relevant news headlines, providing a convenient way to receive timely information.

5. **Environment Variable-Based Configuration:** The application uses environment variables for sensitive information like API keys and Telegram bot credentials, enhancing security and making it easier to manage different deployment environments.

6. **Error Handling:** Implements robust error handling for API requests, ensuring the application runs smoothly even if there are issues with data retrieval.

7. **User-Friendly Notifications:** The Telegram messages are formatted for clarity and ease of understanding, delivering concise and relevant information directly to the user's mobile device.

8. **Scalability and Extendibility:** Designed to be easily extendable to monitor additional stocks or integrate with other news sources or messaging platforms.

9. **Minimal Dependencies:** The project has minimal external dependencies, making it lightweight and easy to set up.

<h2>Prerequisites </h2>
To run this project, you will need:

+ **Python:** The application is written in Python(3.6 and above), a recent version of [Python](https://www.python.org/downloads/).
+ **Pip:** Python's package installer, pip, should be installed for managing Python packages. It usually comes with Python installation.
+ **API keys:** for Alpha Vantage, NewsAPI, and a Telegram bot token. These should be stored as environment variables.

<h2>Installation</h2>

- **Clone the Repository:** git clone https://github.com/SonnyGU/AlphaVantage-CVS-MarketWatcher.git
- **Install the Requests library using pip:** pip install requests
- **Run the Application:** python main.py 

<h2>Setup</h2>

Store your API keys and Telegram bot token in environment variables:
- **ALPHAVANTAGE_API_KEY:** Your Alpha Vantage API key.
- **NEWSAPI_API_KEY:** Your NewsAPI key.
- **BOT_TOKEN:** Your Telegram bot token.
- **CHAT_ID:** Your Telegram chat ID.

<h2>Program walk-through:</h2>

<p align="center">
Launch the utility: <br/>
<img src="https://i.imgur.com/5zAX0wk.png" height="80%" width="80%" alt="Stock Steps"/>
<br />
<br />
Before Running Application:  <br/>
<img src="https://i.imgur.com/6QT5t64.jpg" height="50%" width="50%" alt="Stock Steps"/>
<br />
<br /> 
After Running Application:    <br/>
<img src="https://i.imgur.com/MLOwr74.jpg" height="50%" width="50%" alt="Stock Steps"/>
<br />
<br />



<!--
 ```diff
- text in red
+ text in green
! text in orange
# text in gray
@@ text in purple (and bold)@@
```
--!>
