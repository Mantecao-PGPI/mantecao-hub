import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

from core.environment.host import get_host_for_selenium_testing
from core.selenium.common import close_driver, initialize_driver_firefox


def test_login_and_check_element():

    driver = initialize_driver_firefox()

    try:
        host = get_host_for_selenium_testing()

        # Open the login page
        driver.get(f'{host}/login')

        # Wait a little while to make sure the page has loaded completely
        time.sleep(4)

        # Find the username and password field and enter the values
        email_field = driver.find_element(By.NAME, 'email')
        password_field = driver.find_element(By.NAME, 'password')

        email_field.send_keys('user1@example.com')
        password_field.send_keys('1234')

        # Send the form
        password_field.send_keys(Keys.RETURN)

        # Wait a little while to ensure that the action has been completed
        time.sleep(4)

        try:

            driver.find_element(By.XPATH, "//h1[contains(@class, 'h2 mb-3') and contains(., 'Latest datasets')]")
            print('Test passed!')

        except NoSuchElementException:
            raise AssertionError('Test failed!')

    finally:

        # Close the browser
        close_driver(driver)


def test_login_and_remember_me_true():
    driver = initialize_driver_firefox()

    try:
        host = get_host_for_selenium_testing()

        # Open the login page
        driver.get(f'{host}/login')

        # Wait a little while to make sure the page has loaded completely
        time.sleep(4)

        # Find the username and password field and enter the values
        email_field = driver.find_element(By.NAME, 'email')
        password_field = driver.find_element(By.NAME, 'password')
        password_field = driver.find_element(By.NAME, 'password')
        driver.find_element(By.NAME, "remember_me").click()
        email_field.send_keys('user1@example.com')
        password_field.send_keys('1234')

        # Send the form
        password_field.send_keys(Keys.RETURN)

        # Wait a little while to ensure that the action has been completed
        time.sleep(4)

        driver.delete_cookie('session')

        driver.get(f'{host}/profile/summary')
        try:

            driver.find_element(By.XPATH, "//h1[contains(@class, 'h3 mb-3') and contains(., 'User profile')]")
            print('Test passed!')

        except NoSuchElementException:
            raise AssertionError('Test failed!')

    finally:

        # Close the browser
        close_driver(driver)


def test_login_and_remember_me_false():

    driver = initialize_driver_firefox()

    try:
        host = get_host_for_selenium_testing()

        # Open the login page
        driver.get(f'{host}/login')

        # Wait a little while to make sure the page has loaded completely
        time.sleep(4)

        # Find the username and password field and enter the values
        email_field = driver.find_element(By.NAME, 'email')
        password_field = driver.find_element(By.NAME, 'password')
        email_field.send_keys('user1@example.com')
        password_field.send_keys('1234')

        # Send the form
        password_field.send_keys(Keys.RETURN)

        # Wait a little while to ensure that the action has been completed
        time.sleep(4)

        driver.delete_cookie('session')

        driver.get(f'{host}/profile/summary')
        try:

            driver.find_element(By.XPATH, "//h1[contains(@class, 'h2 mb-3') and contains(., 'Login')]")
            print('Test passed!')

        except NoSuchElementException:
            raise AssertionError('Test failed!')

    finally:

        # Close the browser
        close_driver(driver)


def test_signup_developer_and_check_element():

    driver = initialize_driver_firefox()

    try:
        host = get_host_for_selenium_testing()

        # Open the login page
        driver.get(f'{host}/signup')

        # Wait a little while to make sure the page has loaded completely
        time.sleep(4)

        # Find the username and password field and enter the values
        name_field = driver.find_element(By.NAME, 'name')
        surname_field = driver.find_element(By.NAME, 'surname')
        email_field = driver.find_element(By.NAME, 'email')
        password_field = driver.find_element(By.NAME, 'password')
        is_developer_field = driver.find_element(By.NAME, 'is_developer')

        name_field.send_keys('Footer')
        surname_field.send_keys('Looter')
        email_field.send_keys('user3@example.com')
        password_field.send_keys('1234')
        is_developer_field.click()

        # Send the form
        password_field.send_keys(Keys.RETURN)

        # Wait a little while to ensure that the action has been completed
        time.sleep(4)

        try:

            driver.find_element(By.XPATH,
                                "//div[contains(@class, 'col-xl-4 col-lg-12 col-md-12 col-sm-12')"
                                + " and contains(., 'You are in Developer Mode')]")
            print('Test passed!')

        except NoSuchElementException:
            raise AssertionError('Test failed!')

    finally:
        # Close the browser
        close_driver(driver)


# Call the test function

test_login_and_remember_me_true()
test_login_and_remember_me_false()

test_login_and_check_element()
test_signup_developer_and_check_element()
