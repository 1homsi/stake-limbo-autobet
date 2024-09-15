# Stake.com Betting Automation Script

## Overview

This Python script automates betting interactions on stake.com using Selenium because the auto bet functionality on the website stops after a certain time randomly.

## Prerequisites

1. **Python 3.x** installed on your system.
2. **Selenium** installed. If not, install it via:

```
   pip install selenium

   ## or let run.sh install it for you
```

3. **ChromeDriver** for Google Chrome installed.
   ChromeDriver installed and accessible on your system. You can download it here.

4. **Chrome** debugging session running on port 9222. Alternatively, the run.sh script provided automates this step.

Clone or download the repository to your local machine.

## Make run.sh executable by running:

```bash
sudo chmod +x run.sh
```

Execute the script with the required parameters:

```
./run.sh <bet_amount> <multiplier> <delay> <clicks>
```

bet_amount : The amount to bet (e.g., 0.01).
multiplier: The multiplier value to set (e.g., 1.01).
delay: Delay between button clicks in seconds (e.g., 0.5).
clicks: Number of times to click the button (e.g., 2000000).

Example:

```bash
./run.sh 0.01 1.01 0.5 2000000
```

alternatively, you can run the script with the following command:

```
python app.py <bet_amount> <multiplier> <delay> <clicks>
```

## Notes

1. Ensure your Chrome is already logged in to stake.com.
2. The script interacts with the Chrome debugging session, so Chrome must remain open during the execution.
3. If you need any addition features, please let me know.

## Troubleshooting

1. If you encounter issues with ChromeDriver, ensure it's correctly installed and the path is correctly set in the script.
2. The Chrome window should not be minimized while the script is running to ensure proper element interaction.
