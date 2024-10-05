import re
from playwright.sync_api import sync_playwright
import time
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access environment variables
email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")

orders = ['CINC0023279', 'CINC0020798']

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False, channel='msedge')
    page = browser.new_page()
    page.goto("https://nordexprod.service-now.com/now/nav/ui/classic/params/target/home.do")
    
    # Use email and password from .env file
    page.fill('#i0116', email)
    page.click('#idSIButton9')
    page.fill('#i0118', password)
    page.click('#idSIButton9')

    for order in orders:
        page.goto("https://nordexprod.service-now.com/now/nav/ui/classic/params/target/home.do")
        page.fill('#sncwsgs-typeahead-input', order)  # Fill in the search field with the variable 'order'
        page.press('#sncwsgs-typeahead-input', 'Enter')  # Press 'Enter' to submit the search
        page.click('.sn-list-group li:first-child')  # Click on the first item of the list with class 'sn-list-group'
        page.wait_for_selector('#chg_create_normal_change')  # Wait for the button to be loaded
        time.sleep(1)
        page.click('#chg_create_normal_change')  # Click on the button with the specified ID
        time.sleep(2)
        page.select_option('change_request.u_assessment_committee', 'Steel_Tower_Committee')  # Select the option from the dropdown
        page.click('#change_request.u_impacted_committee_unlock')
        page.wait_for_selector('#choice.change_request.u_impacted_committee')
        page.select_option('choice.change_request.u_impacted_committee', 'Steel_Tower_Committee')
        page.fill('#change_request.u_solution_proposal', 'Update/correct EBOM')  # Write the text in the textarea
        page.fill('#change_request.u_expected_savings_ic', 'avoid errors and extracosts')
        page.select_option('choice.change_request.u_impacted_committee', 'Steel_Tower_Committee')
        page.click('span:text("Source & Scope")')  # Click on the span label with the text "Source & Scope"
        page.select_option('change_request.u_source', 'industrialization')
        page.select_option('change_request.u_drivers', 'Quality')
        page.select_option('change_request.u_root_cause', 'Configuration_delay')
        page.select_option('change_request.scope', '7')
        page.click('#change_request.u_projects_unlock')
        time.sleep(1)
        windfarm = page.input_value('#sys_display.change_request.u_detected_in_detail_windpark')  # Read the value and store it in 'windfarm'
        page.fill('#sys_display.change_request.u_projects', windfarm)  # Fill in the 'windfarm' value in the projects input field
        page.press('#sys_display.change_request.u_projects', 'Enter')  # Press 'Enter' to submit the value
        
        print(page.url)
    
    time.sleep(5)
    print(page.title)
    browser.close()
