#!/bin/bash

# Step 1: Install the required Python packages
echo "Installing required Python packages..."
pip install -r requirements.txt

# Step 2: Open Chrome in remote debugging mode and navigate to the Stake.com Limbo game
echo "Opening Chrome in remote debugging mode and navigating to the game..."
/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 "https://stake.com/casino/games/limbo" &

# Step 3: Wait a few seconds to ensure Chrome starts properly and the page loads
sleep 5

# Step 4: Run the Python script with arguments from the terminal
echo "Running the Python script..."
python3 app.py "$@"
