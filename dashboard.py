import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import time
from datetime import datetime, timedelta
import csv
import numpy as np

# Create Dash app
app = dash.Dash(__name__)


# Initialize variables
with open('dogecoin_price.txt', 'r') as f:
        price = float(f.read())
prices = [price]
times = [time.time()]

# Define function to update prices and times
def update_prices():
    with open('dogecoin_price.txt', 'r') as f:
        price = float(f.read())
        prices.append(price)
        times.append(time.time())
    # Write the new data to a CSV file
        with open('dogecoin_price.csv', 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([times[-1], prices[-1]])

# Define function to calculate daily metrics
def calculate_daily_metrics():
    now = datetime.now()
    #Check if 8pm or past 8 pm and Next day
    if now.hour == 20 and now.minute == 0 :
        print("Generating Daily Report")

        # Load data from CSV file
        with open('dogecoin_price.csv', 'r') as csvfile:
            reader = csv.reader(csvfile)
            data = [(datetime.fromtimestamp(float(row[0])), float(row[1])) for row in reader]

        # Filter data from the last 24 hours
        today_data = [d for d in data if d[0] > datetime.now() - timedelta(hours=24)]

        # Extract prices from data
        prices = [d[1] for d in today_data]

        # Calculate daily volatility as standard deviation of prices
        daily_volatility = round(np.std(prices), 4)

        # Calculate open and close price as first and last price of the day
        open_price = round(prices[0], 4)
        close_price = round(prices[-1], 4)

        # Calculate evolution as percentage change from open to close price
        evolution = round((close_price - open_price) / open_price * 100, 4)

        # Save report to CSV file
        with open('daily_report.csv', 'w') as file:
            file.write(f'{now},{daily_volatility},{open_price},{close_price},{evolution}\n')

    with open('daily_report.csv', 'r') as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            daily_volatility = float(row[1])
            open_price = float(row[2])
            close_price = float(row[3])
            evolution = float(row[4])
    return daily_volatility, open_price, close_price, evolution


# Define app layout
app.layout = html.Div(children=[
    html.H1(children='Dogecoin Price'),

    html.Div(id='price-div'),

    dcc.Graph(
        id='price-chart',
        figure={
            'data': [
                {'x': times, 'y': prices, 'type': 'line', 'name': 'Price'},
            ],
            'layout': {
                'title': 'Dogecoin Price',
                'xaxis': {'title': 'Time'},
                'yaxis': {'title': 'Price (USD)','range': [0, max(prices)*1.1]}
            }
        }
    ),

    dcc.Interval(
        id='interval-component',
        interval=60*1000, # in milliseconds
        n_intervals=0
    ),

    html.Div(id='daily-report')
])

# Define callback to update price and chart
@app.callback(Output('price-div', 'children'),
              Output('price-chart', 'figure'),
              Input('interval-component', 'n_intervals'))
def update_price_chart(n):
    update_prices()
    price = prices[-1]
    times_readable = [datetime.fromtimestamp(t).strftime('%Y-%m-%d %H:%M:%S') for t in times]
    return f'Current price: ${price:.4f}', {
            'data': [
                {'x': times_readable, 'y': prices, 'type': 'line', 'name': 'Price'},
            ],
            'layout': {
                'title': 'Dogecoin Price',
                'xaxis': {'title': 'Time'},
                'yaxis': {'title': 'Price (USD)'}
            }
        }

# Define callback to update daily report
@app.callback(Output('daily-report', 'children'),
              Input('interval-component', 'n_intervals'))
def update_daily_report(n):
    # Check if it's 8pm
    now = datetime.now()
    # Calculate daily metrics
    daily_volatility, open_price, close_price, evolution = calculate_daily_metrics()
    # Format daily report
    report = f'Daily report ({now.strftime("%Y-%m-%d")}):\n'
    report += f'Daily volatility: {daily_volatility:.4f}\n'
    report += f'Open price: {open_price:.4f}\n'
    report += f'Close price: {close_price:.4f}\n'
    report += f'Evolution: {evolution:.4f}%'
    return html.Pre(report)

if __name__ == '__main__':
    app.run_server(debug=True)