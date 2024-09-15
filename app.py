import time
import argparse
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json
import requests

# Argument parsing 
parser = argparse.ArgumentParser(description='Automate betting on stake.com')
parser.add_argument('bet_amount', type=float, help='The amount to bet (e.g. 0.01)')
parser.add_argument('multiplier', type=float, help='The multiplier to set (e.g. 1.01)')
parser.add_argument('delay', type=float, help='The delay between button clicks in seconds (e.g. 0.5)')
parser.add_argument('clicks', type=int, help='The number of times to click the button')
args = parser.parse_args()

# Chrome options to connect to the existing session
chrome_options = Options()
chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")

service = Service('/opt/homebrew/bin/chromedriver')  # Ensure this path is correct

# Create a WebDriver instance
driver = webdriver.Chrome(service=service, options=chrome_options)

# Fetch list of open tabs from DevTools
def get_tabs():
    try:
        response = requests.get('http://localhost:9222/json')
        response.raise_for_status()  # Raise an exception for HTTP errors
        tabs = json.loads(response.text)
        return tabs
    except requests.RequestException as e:
        print(f"Failed to fetch tabs: {e}")
        return []

# Locate the stake.com tab
def find_stake_tab(tabs):
    for tab in tabs:
        if "stake.com" in tab["url"]:
            return tab
    return None

try:
    # Fetch and find the correct tab
    tabs = get_tabs()
    stake_tab = find_stake_tab(tabs)
    if not stake_tab:
        print("Unable to find the stake.com tab.")
        exit()

    # Switch to the stake.com tab
    driver.get(stake_tab["url"])

    # Initialize WebDriverWait
    wait = WebDriverWait(driver, 10)  # Adjust timeout as needed

    # Wait for 10 seconds before starting interactions
    time.sleep(10)

    # Set the multiplier value with user-like interaction
    try:
        # Locate the multiplier input field
        multiplier_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#main-content > div > div.content.svelte-aj9tu > div.game-content.svelte-1ku0r3 > div > div.footer.svelte-17aq4sd > label:nth-child(1) > div > div > input')))
        
        # Scroll the input field into view
        driver.execute_script("arguments[0].scrollIntoView();", multiplier_input)

        # Focus the input field and clear existing value
        multiplier_input.click()
        multiplier_input.clear()

        # Set the multiplier
        multiplier_input.send_keys(str(args.multiplier))

        # Trigger the necessary events
        driver.execute_script("""
            var input = arguments[0];
            var event = new Event('input', { bubbles: true });
            input.dispatchEvent(event);
            var changeEvent = new Event('change', { bubbles: true });
            input.dispatchEvent(changeEvent);
        """, multiplier_input)

        print(f"Multiplier set to {args.multiplier} and events triggered.")
    except Exception as e:
        print(f"Error setting multiplier: {e}")
        exit()

    # Set the bet amount with user-like interaction
    try:
        # Locate the bet input field
        bet_input = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#main-content > div > div.content.svelte-aj9tu > div.game-sidebar.svelte-2ftx9j > label > div > div.input-content.svelte-1u979cd > input')))
        
        # Scroll the input field into view
        driver.execute_script("arguments[0].scrollIntoView();", bet_input)

        # Focus the input field and clear existing value
        bet_input.click()
        bet_input.clear()

        # Set the bet amount 
        bet_input.send_keys(str(args.bet_amount))

        # Trigger the necessary events
        driver.execute_script("""
            var input = arguments[0];
            var event = new Event('input', { bubbles: true });
            input.dispatchEvent(event);
            var changeEvent = new Event('change', { bubbles: true });
            input.dispatchEvent(changeEvent);
        """, bet_input)

        print(f"Bet amount set to {args.bet_amount} and events triggered.")
    except Exception as e:
        print(f"Error setting bet amount: {e}")
        exit()

    # Initialize click counter
    click_count = 0
    max_clicks = args.clicks  # Set the max clicks

    # Loop to press the button
    while click_count < max_clicks:
        # Print current URL and title for debugging
        print("Current URL:", driver.current_url)
        print("Current Title:", driver.title)
        
        try:
            # Wait for the button to be clickable
            button = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#main-content > div > div.content.svelte-aj9tu > div.game-sidebar.svelte-2ftx9j > button')))
            button.click()
            click_count += 1
            print(f"Button clicked! Total clicks: {click_count}")
        
        except Exception as e:
            print(f"Error finding or interacting with the button: {e}")

        # Wait for the delay 
        time.sleep(args.delay)

    print(f"Reached {max_clicks} clicks. Stopping.")

except Exception as e:
    print(f"An error occurred: {e}")

# Optionally close the browser after interacting
# driver.quit()
