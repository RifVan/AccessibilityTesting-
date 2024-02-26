import time

from selenium import webdriver
from axe_selenium_python import Axe
import os


# Initialize Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://prestamarinedetailing.com/")

driver.maximize_window()
# Initialize Axe
axe = Axe(driver)

# Inject Axe JavaScript library into the webpage
axe.inject()

# Analyze accessibility
results = axe.run()

# Check for violations
if len(results["violations"]) > 0:
    print("Accessibility violations found:")
    for violation in results["violations"]:
        print("- Description:", violation["description"])
        print("- Help:", violation["help"])
        print("- Tags:", violation["tags"])
        print("- Impact:", violation["impact"])
        print("- Nodes:", violation["nodes"])
        print()

    # Save screenshot for reference
    driver.save_screenshot("accessibility_violation.png")
    print("Screenshot saved as 'accessibility_violation.png'.")
else:
    print("No accessibility violations found.")

print("Current working directory:", os.getcwd())
time.sleep(10)
# Quit the WebDriver
driver.quit()
