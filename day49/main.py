from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import NoSuchElementException
import time
import os

ACCOUNT_EMAIL = os.getenv('LINKED_IN_EMAIL')
ACCOUNT_PASSWORD = os.getenv('LINKED_IN_PASSWORD')
PHONE = '3852512971'

# Optional - Keep the browser open (helps diagnose issues if the script crashes)
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/jobs/search/?currentJobId=4172373925&f_WT=2%2C3&geoId=103752383&keywords=technical%20support%20engineer&origin=JOB_SEARCH_PAGE_SEARCH_BUTTON&refresh=true")


def main():
    # print(f"email: {ACCOUNT_EMAIL}\npassword: {ACCOUNT_PASSWORD}")


    # Click Reject Cookies Button
    # time.sleep(2)
    # reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
    # reject_button.click()

    # Click Sign in Button
    time.sleep(2)
    sign_in_button = driver.find_element(by=By.CSS_SELECTOR, value='button[data-modal="base-sign-in-modal"]')
    # print(f"found sign in button: {sign_in_button}\n\n")
    sign_in_button.click()
    # print('sign in button clicked\n\n')

    # Sign in
    time.sleep(1)
    email_field = driver.find_element(by=By.ID, value="base-sign-in-modal_session_key")
    email_field.send_keys(ACCOUNT_EMAIL)
    time.sleep(1)
    password_field = driver.find_element(by=By.ID, value="base-sign-in-modal_session_password")
    password_field.send_keys(ACCOUNT_PASSWORD)
    time.sleep(1)
    password_field.send_keys(Keys.ENTER)
    print('\n\nlogged in\n\n')
    time.sleep(10)


    # Get Listings
    time.sleep(5)
    all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

    # Apply for Jobs
    for listing in all_listings:
        print("Opening Listing")
        listing.click()
        time.sleep(2)
        try:
            # Click Apply Button
            apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
            apply_button.click()

            # Insert Phone Number
            # Find an <input> element where the id contains phoneNumber
            time.sleep(5)
            phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
            if phone.text == "":
                phone.send_keys(PHONE)

            # Check the Submit Button
            submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
            if submit_button.get_attribute("data-control-name") == "continue_unify":
                abort_application()
                print("Complex application, skipped.")
                continue
            else:
                # Click Submit Button
                print("Submitting job application")
                submit_button.click()

            time.sleep(2)
            # Click Close Button
            close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
            close_button.click()

        except NoSuchElementException:
            abort_application()
            print("No application button, skipped.")
            continue

    time.sleep(5)
    driver.quit()


def abort_application():
    # Click Close Button
    close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
    close_button.click()

    time.sleep(2)
    # Click Discard Button
    discard_button = driver.find_elements(by=By.CLASS_NAME, value="artdeco-modal__confirm-dialog-btn")[1]
    discard_button.click()


if __name__ == "__main__":
    main()
    # test_explicit()