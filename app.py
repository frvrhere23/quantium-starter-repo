from dash import Dash, html, dcc, Input, Output, callback # We bring in our tools to build the website and make it interactive
import plotly.express as px # Plotly is our artist for drawing the line charts
import pandas as pd # Pandas is our super-smart spreadsheet assistant

# --- STEP 1: LOAD AND PREPARE THE DATA ---
# This part is like opening our book of sales and making sure it's ready to read.

# We read the 'formatted_data.csv' file that has all our Pink Morsel sales info.
df = pd.read_csv("formatted_data.csv")

# We tell the computer that the 'Date' column is about time, not just random text.
# This helps it put everything in the right calendar order!
df["Date"] = pd.to_datetime(df["Date"])

# We sort the dates from the oldest to the newest so the chart flows smoothly from left to right.
df = df.sort_values(by="Date")

# --- STEP 2: BUILD THE APP LAYOUT ---
# Think of this as the 'Skeleton' or the 'Blueprint' of our website.
app = Dash(__name__)
app.title = "Pink Morsel Sales Visualizer"

# 'app.layout' is where we define what goes where on the screen.
app.layout = html.Div(id="app-container", children=[
    
    # 1. THE HEADER: The title at the top of the page.
    # We wrap it in a 'glass-card' Div to give it that cool frosted-glass look!
    html.Div(className="glass-card", children=[
        html.H1(children='Pink Morsel Sales Visualizer'),
        html.P(children='Use the buttons below to switch between different sales regions.')
    ]),

    # 2. THE CONTROL PANEL: This is where the user can click buttons.
    # We use 'dcc.RadioItems' for our list of regions.
    html.Div(className="glass-card", children=[
        html.Label("Select Region:", style={'fontWeight': 'bold', 'marginBottom': '10px', 'display': 'block'}),
        dcc.RadioItems(
            id='region-filter', # This is the ID so the callback (the brain) can find it!
            options=[
                {'label': 'North', 'value': 'north'},
                {'label': 'East', 'value': 'east'},
                {'label': 'South', 'value': 'south'},
                {'label': 'West', 'value': 'west'},
                {'label': 'All', 'value': 'all'}
            ],
            value='all', # We start with 'all' so the user seeing everything at first.
            className='radio-group', # This connects to our style.css file!
            labelStyle={'display': 'inline-block', 'marginRight': '20px'},
            inputClassName='radio-input', # Styles the little circle button
            labelClassName='radio-label'  # Styles the text next to the button
        )
    ]),

    # 3. THE GRAPH AREA: A big box where our chart will live.
    html.Div(className="glass-card", children=[
        # 'dcc.Graph' is like a blank canvas waiting for our callback to draw on it.
        dcc.Graph(id='sales-line-chart', className='chart-container')
    ])
])

# --- STEP 3: THE BRAIN (Interactivity) ---
# This is a 'Callback' - it's like a rule that says: 
# "Whenever the user clicks a button, run this code and update the chart!"

@callback(
    # Output: We want to change the 'figure' (the chart) of the 'sales-line-chart'.
    Output('sales-line-chart', 'figure'),
    # Input: We are watching the 'value' of the 'region-filter' buttons.
    Input('region-filter', 'value')
)
def update_graph(selected_region):
    # This function runs every single time a radio button is clicked!
    
    # A. Filtering: We only keep the data the user asked for.
    if selected_region == 'all':
        filtered_df = df # If they pick 'all', we don't change anything.
    else:
        # If they pick a region (like 'north'), we only keep the rows for that region.
        filtered_df = df[df["Region"] == selected_region]

    # B. Drawing: We create a new line chart with the chosen data.
    fig = px.line(
        filtered_df, 
        x="Date", 
        y="Sales", 
        title=f"Pink Morsel Sales: {selected_region.capitalize()}"
    )

    # C. Adding the Marker: We add the red dotted line at Jan 15, 2021.
    # This is when the price went up, so we want to see what happened before and after!
    fig.add_vline(x="2021-01-15", line_width=2, line_dash="dash", line_color="#ff4d4d")
    
    # D. Styling the Chart: We make sure the chart matches our beautiful website design.
    fig.update_layout(
        plot_bgcolor='rgba(0,0,0,0)',  # Makes the chart background see-through
        paper_bgcolor='rgba(0,0,0,0)', # Makes the paper background see-through
        font_color='#f8fafc',          # Sets the text to a nice off-white color
        xaxis=dict(showgrid=False),    # Removes the vertical lines from the chart
        yaxis=dict(showgrid=True, gridcolor='rgba(255,255,255,0.1)'), # Subtly keeps horizontal lines
        margin=dict(l=40, r=40, t=60, b=40)
    )

    return fig # We send the finished chart back to the website!

# --- STEP 4: RUN THE APP ---
if __name__ == '__main__':
    # This starts our local web server so we can visit the site in our browser.
    app.run(debug=True)


