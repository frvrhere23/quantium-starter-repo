from dash.testing.composite import DashComposite # This is the tool that helps us 'see' our app through a browser
from app import app # We import our app so the tester can open it

# --- WELCOME TO THE TEST LAB! ---
# Imagine this file is like a safety inspector. It opens our app in a secret
# browser window and checks if everything is where it belongs.

def test_header_present(dash_duo):
    # 1. Open the app!
    # 'dash_duo' is like a pair of hands that controls our secret browser.
    dash_duo.start_server(app)

    # 2. Wait for the header to show up.
    # We look for the 'Name Tag' (#header) we added earlier.
    # We wait up to 10 seconds just in case the computer is being slow.
    dash_duo.wait_for_element('#header', timeout=10)

    # 3. Check if it's there!
    # 'assert' is like saying "If I don't see this, stop everything and tell me it failed!"
    assert dash_duo.find_element('#header').is_displayed()

def test_visualization_present(dash_duo):
    # 1. Open the app.
    dash_duo.start_server(app)

    # 2. Look for our chart.
    # We wait up to 10 seconds. If it shows up in the 'Building Blueprint' (the DOM), 
    # then our test is happy!
    dash_duo.wait_for_element('#sales-line-chart', timeout=10)

    # 3. Check if it exists!
    # Sometimes charts are 'there' but still invisible for a split second 
    # while they are being drawn. Checking if it's 'present' is more reliable.
    assert dash_duo.find_element('#sales-line-chart') is not None

def test_region_picker_present(dash_duo):
    # 1. Open the app one last time.
    dash_duo.start_server(app)

    # 2. Look for the buttons (the radio items).
    # We gave them the ID 'region-filter'.
    dash_duo.wait_for_element('#region-filter', timeout=10)

    # 3. Check if it's there!
    assert dash_duo.find_element('#region-filter').is_displayed()

# --- HOW TO RUN THESE TESTS ---
# In your terminal, you just type: pytest
# Pytest will find this file (because it starts with 'test_') 
# and run all the functions inside for you!
