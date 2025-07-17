import dash
from dash import dcc, html, Input, Output
from extract import fetch_stock_data
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# Top 10 Companies
top_10_tickers = ['AAPL', 'MSFT', 'GOOGL', 'AMZN', 'TSLA', 'META', 'NVDA', 'NFLX', 'JPM', 'INTC']

# === Dash App ===
app = dash.Dash(__name__)
app.title = "📈 Stock Analytics Dashboard"

# === Layout ===
app.layout = html.Div([
    html.Div([
        html.H1("📊Live Stock Price Analytics", style={
            'textAlign': 'center',
            'color': '#1a1a1a',
            'marginBottom': '10px',
            'fontWeight': 'bold',
            'fontSize': '36px'
        }),

        html.P("Compare Line Chart & Candlestick Data", style={
            'textAlign': 'center',
            'color': '#555',
            'marginTop': '0px',
            'marginBottom': '40px',
            'fontSize': '18px'
        }),

        html.Div([
            html.Label("📌 Select a Top Company:", style={'fontWeight': 'bold', 'marginRight': '10px'}),
            dcc.Dropdown(
                id='stock-dropdown',
                options=[{'label': sym, 'value': sym} for sym in top_10_tickers],
                placeholder='Choose from Top 10...',
                style={'flex': '1', 'marginRight': '15px'}
            ),
            html.Label("Or enter a custom symbol:", style={'marginLeft': '10px'}),
            dcc.Input(id='stock-input', type='text', placeholder='E.g. INFY, NFLX', debounce=True,
                      style={'flex': '1', 'padding': '10px', 'borderRadius': '5px', 'border': '1px solid #ccc'})
        ], style={
            'display': 'flex', 'flexDirection': 'row', 'flexWrap': 'wrap',
            'gap': '10px', 'marginBottom': '20px'
        }),

        html.Div([
            html.Label("🕒 Select Period:", style={'fontWeight': 'bold', 'marginRight': '10px'}),
            dcc.Dropdown(
                id='period-dropdown',
                options=[
                    {'label': '1 Month', 'value': '1mo'},
                    {'label': '3 Months', 'value': '3mo'},
                    {'label': '6 Months', 'value': '6mo'},
                    {'label': '1 Year', 'value': '1y'},
                    {'label': '2 Years', 'value': '2y'},
                    {'label': '5 Years', 'value': '5y'}
                ],
                value='1mo',
                style={'width': '150px', 'marginRight': '30px'}
            ),
            html.Label("⏱ Interval:", style={'fontWeight': 'bold', 'marginRight': '10px'}),
            dcc.Dropdown(
                id='interval-dropdown',
                options=[
                    {'label': '1 Day', 'value': '1d'},
                    {'label': '1 Hour', 'value': '1h'},
                    {'label': '30 Minutes', 'value': '30m'},
                    {'label': '15 Minutes', 'value': '15m'},
                    {'label': '5 Minutes', 'value': '5m'}
                ],
                value='1d',
                style={'width': '150px'}
            ),
        ], style={'display': 'flex', 'flexDirection': 'row', 'marginBottom': '30px'}),

    ], style={
        'padding': '30px',
        'maxWidth': '1000px',
        'margin': 'auto',
        'backgroundColor': '#ffffff',
        'borderRadius': '15px',
        'boxShadow': '0 4px 20px rgba(0,0,0,0.08)'
    }),

    dcc.Graph(id='stock-graph', style={'marginTop': '40px'}),
    html.Div(id='stats-output', style={
        'textAlign': 'center',
        'fontWeight': 'bold',
        'fontSize': '18px',
        'marginTop': '20px',
        'color': '#2c3e50'
    }),

], style={'backgroundColor': '#f4f6f9', 'minHeight': '100vh', 'paddingTop': '30px'})


# === Callback ===
@app.callback(
    [Output('stock-graph', 'figure'),
     Output('stats-output', 'children')],
    [Input('stock-dropdown', 'value'),
     Input('stock-input', 'value'),
     Input('interval-dropdown', 'value'),
     Input('period-dropdown', 'value')]
)
def update_graph(dropdown_ticker, input_ticker, interval, period):
    ticker = input_ticker.upper() if input_ticker else dropdown_ticker
    if not ticker:
        return go.Figure(), "Please select or enter a stock symbol."

    try:
        df = fetch_stock_data(ticker=ticker, interval=interval, period=period)
        if df.empty:
            return go.Figure(), f"No data available for {ticker}."

        fig = make_subplots(
            rows=2, cols=1,
            shared_xaxes=True,
            vertical_spacing=0.15,
            row_heights=[0.4, 0.6],
            subplot_titles=[f"{ticker} Price Line Chart", f"{ticker} Candlestick Chart"]
        )

        # Line chart (Adj Close fallback to Close if needed)
        line_col = 'Adj Close' if 'Adj Close' in df.columns else 'Close'
        fig.add_trace(go.Scatter(
            x=df['Date'],
            y=df[line_col],
            mode='lines+markers',
            name='Line Chart',
            line=dict(color='royalblue')
        ), row=1, col=1)

        # Candlestick chart
        fig.add_trace(go.Candlestick(
            x=df['Date'],
            open=df['Open'],
            high=df['High'],
            low=df['Low'],
            close=df['Close'],
            name='Candlesticks'
        ), row=2, col=1)

        fig.update_layout(
            template='plotly_dark',
            height=700,
            showlegend=False,
            xaxis_title='Date',
            yaxis_title='Price'
        )

        latest = df.iloc[-1]
        stats = f"Latest Close: ${latest[line_col]:.2f} | High: ${latest['High']:.2f} | Low: ${latest['Low']:.2f} | Volume: {int(latest['Volume'])}"
        return fig, stats

    except Exception as e:
        return go.Figure(), f"⚠️ Error fetching data for '{ticker}': {str(e)}"


# === Run Server ===
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080, debug=True)
