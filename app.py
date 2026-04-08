from dash import Dash, html, dcc # We import Dash tools to build our website layout
import plotly.express as px # Plotly is the artist that draws our pretty charts
import pandas as pd # Pandas is our spreadsheet manager

# --- STEP 1: LOAD AND PREPARE THE DATA ---
# We load our clean 'formatted_data.csv' that we made in the last task.
df = pd.read_csv("formatted_data.csv")

# We need to make sure the computer knows the "Date" column is actually about calendar time!
# Otherwise, it might just see it as words.
df["Date"] = pd.to_datetime(df["Date"])

# We sort the dates from oldest to newest so the line chart flows correctly.
# It's like putting your baby photos in order from birth to today!
df = df.sort_values(by="Date")

# --- STEP 2: CREATE THE CHART ---
# We use 'px.line' to create a line chart.
# x="Date": The timeline goes across the bottom.
# y="Sales": The money goes up and down the side.
# title="Pink Morsel Sales": A clear name for our chart.
fig = px.line(df, x="Date", y="Sales", title="Pink Morsel Sales Over Time")

# We want to highlight Jan 15, 2021, because that's when the price changed!
# We add a vertical line (vline) to the chart like a "Before/After" marker.
fig.add_vline(x="2021-01-15", line_width=3, line_dash="dash", line_color="red")
fig.add_annotation(x="2021-01-15", y=max(df["Sales"]), text="Price Increase", showarrow=True, arrowhead=1)

# We add clear labels for the axes so anyone reading it knows what the lines mean.
fig.update_layout(
    xaxis_title="Date (Timeline)",
    yaxis_title="Total Sales (Money Made)",
    font=dict(family="Arial", size=14, color="black")
)

# --- STEP 3: BUILD THE APP LAYOUT ---
# This is how we organize things on the screen.
app = Dash(__name__)

# 'app.layout' is like the blueprint for our webpage.
# html.Div is like a 'container' or 'box' holding everything together.
app.layout = html.Div(children=[
    # html.H1 is a 'Header 1' - it's the biggest, boldest text at the top!
    html.H1(children='Pink Morsel Visualizer', style={'textAlign': 'center', 'color': '#003366'}),
    
    # html.P is a 'Paragraph' for adding a little explanation.
    html.P(children='A chart showing when sales were highest for Soul Foods.', style={'textAlign': 'center'}),

    # dcc.Graph is where our Plotly figure (fig) gets displayed.
    dcc.Graph(
        id='sales-line-chart',
        figure=fig
    )
])

# --- STEP 4: RUN THE APP ---
# This part tells Python to actually start the web server so we can see the app!
if __name__ == '__main__':
    # 'debug=True' is a helper mode that lets us see errors easily if something goes wrong.
    app.run(debug=True)
