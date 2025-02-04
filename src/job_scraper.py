# Install necessary packages if they are not already installed:
!pip install --upgrade pip
!pip install -U selenium
# If needed, install undetected-chromedriver:
# !pip install undetected-chromedriver

import time
import random
import pandas as pd
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import undetected_chromedriver as uc

# Initialize an empty list to store job data
job_data = []

# Initialize the browser using undetected-chromedriver
driver = uc.Chrome()

# Open the Indeed website
driver.get("https://au.indeed.com/")
print("Opened Indeed website")
time.sleep(random.uniform(2, 4))  # Wait randomly between 2 to 4 seconds for the page to load

# Enter search criteria
what_box = driver.find_element(By.ID, "text-input-what")   # "What" input box
where_box = driver.find_element(By.ID, "text-input-where")  # "Where" input box

where_box.clear()  # Clear the location input box
what_box.send_keys("Data Analyst")  # Enter the job keyword
time.sleep(random.uniform(2, 4))
where_box.send_keys("Australia")  # Enter the location
time.sleep(random.uniform(2, 4))
where_box.send_keys(Keys.RETURN)  # Simulate pressing the search button
time.sleep(random.uniform(3, 5))

# Define a function to navigate to the next page
def go_to_next_page(driver):
    try:
        next_button = driver.find_element(By.CSS_SELECTOR, "a[data-testid='pagination-page-next']")
        next_button.click()  # Click the next page button
        time.sleep(random.uniform(3, 5))  # Wait for the page to load
        return True
    except Exception as e:
        print("No more next page, the scraping ends.")
        return False

# Scrape data from multiple pages
while True:
    # Retrieve job cards on the current page
    job_cards = driver.find_elements(By.CSS_SELECTOR, "a.jcs-JobTitle")
    print(f"Found {len(job_cards)} jobs.")

    for job in job_cards:
        try:
            title = job.text  # Get the job title
            job_url = job.get_attribute("href")  # Get the job URL
            print(f"Job Title: {title}")
            print(f"Job URL: {job_url}")
            job_data.append({"Job Title": title, "Job URL": job_url})
            time.sleep(random.uniform(2, 4))  # Random delay to mimic human behavior
        except Exception as e:
            print(f"Error fetching job details: {e}")

    print("Finished scraping current page, moving to the next page...")
    print("-" * 50)

    # Navigate to the next page
    if not go_to_next_page(driver):
        break

# Close the browser
driver.quit()
print("Closed Indeed website")

# Convert the job data list to a DataFrame
df = pd.DataFrame(job_data)

# Save the results to a CSV file
df.to_csv("indeed_jobs.csv", index=False)
print("Job data saved to 'indeed_jobs.csv'.")

# Display the data
print(df)
