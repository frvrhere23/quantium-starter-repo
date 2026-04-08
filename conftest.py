import pytest
import os
from webdriver_manager.chrome import ChromeDriverManager

# This is like a 'Setup Assistant' for our tests.
# It makes sure the secret browser (Chromedriver) is ready before the tests start!

@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    # 1. Ask webdriver-manager where the browser driver is hidden.
    driver_path = ChromeDriverManager().install()
    
    # 2. Get the folder name where the driver lives.
    driver_dir = os.path.dirname(driver_path)
    
    # 3. Add that folder to the computer's 'Search List' (PATH).
    # This way, when Dash looks for 'chromedriver', it finds it instantly!
    os.environ["PATH"] += os.pathsep + driver_dir
