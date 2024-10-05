# Playwright Automation for ServiceNow Orders

Automates the process of updating ServiceNow orders using Playwright.

## Description

This script uses Playwright to automate the process of logging into the ServiceNow platform and updating specific orders based on predefined criteria.

## Prerequisites

1. Python 3.x
2. Playwright
3. Python-dotenv

## Installation

1. Clone the repository:
   ```bash
   git clone <repo-url>
   cd <repo-directory>
   ```

2. Install required packages:
   ```bash
   pip install playwright python-dotenv
   ```

3. Set up Playwright:
   ```bash
   playwright install
   ```

4. Create a `.env` file in the root directory with the following content:
   ```bash
   EMAIL="your-email@example.com"
   PASSWORD="your-password"
   ```

## Usage

1. Update the `orders` list in the script with the relevant order numbers.
2. Run the script:
   ```bash
   python script.py
   ```

## Notes

- Make sure your `.env` file is not tracked by Git (add it to `.gitignore`).
- The script currently runs in non-headless mode for debugging purposes (`headless=False`).

