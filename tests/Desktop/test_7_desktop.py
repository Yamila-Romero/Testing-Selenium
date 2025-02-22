from selenium.webdriver.common.by import By
from utils.test_data_loader import load_test_data
from utils.custom_assertion import assert_resolution
from utils.product_interactions import wait_for_element, click_element
from page.home import configHome
from dotenv import load_dotenv

from page.home_page import HomePage

load_dotenv()

REGISTRATION_DATA = load_test_data("test_data.json")["registration"]
DEVICE = load_test_data("test_data.json")["device"]
APP_URL = "APP_URL"
WAIT_TIME = 20
CONTACT_US_ID = "contact-link"
EMAIL_BOX_NAME = "email"
SUSCRIBE_BUTTON_XPATH = "//*[@id='blockEmailSubscription_displayFooterBefore']/div/div/form/div/div[1]/input[1]"
SUSCRIBE_BUTTON_NAME= "submitNewsletter"
MESSAGE_XPATH = "//*[@id='blockEmailSubscription_displayFooterBefore']/div/div/form/div/div[2]/p[2]"

def test_sign_up_newsletter(driver):

    home_page = HomePage(driver)
    #configHome(driver,url=APP_URL, device = DEVICE["desktop"])
    home_page.config_home(url=APP_URL, device=DEVICE["desktop"])
    
    # Arrange
    wait_for_element(driver, By.ID, CONTACT_US_ID)
    home_page.sign_up_newsletter(REGISTRATION_DATA["email"])
    # contactUs = driver.find_element(By.ID, CONTACT_US_ID)
    # contactUs.click()

    # # Act
    # wait_for_element(driver, By.NAME, EMAIL_BOX_NAME, WAIT_TIME)
    # emailbox = driver.find_element(By.NAME, EMAIL_BOX_NAME)
    # emailbox.send_keys(REGISTRATION_DATA["email"])
    # click_element(driver, By.NAME, SUSCRIBE_BUTTON_NAME)

    # Assert  
    wait_for_element(driver, By.XPATH, MESSAGE_XPATH)
    success_message = driver.find_element(By.XPATH, MESSAGE_XPATH)
    assert success_message.text == "You have successfully subscribed to this newsletter.", \
        f"Expected success message not displayed. Actual message: {success_message.text}"
    
    expectedResolution = 'desktop'
    assert_resolution(driver,expectedResolution)

