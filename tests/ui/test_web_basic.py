import time
import allure
import pytest

from pages.CreateNewEventPage import CreateNewEventPage
from pages.EventPage import EventPage
from pages.LoginPage import LoginPage
from pages.MenuBar import MenuBar
from utils.test_data import get_user_credentials

"""
Test Scenario:
 - Login with user credentials
 - Navigate to Events and open the Create New Event form
 - Fill in event details
 - Create the event
 -Verify the newly created event is visible
"""
@allure.feature("Event Management")
@allure.story("Create Event")
@allure.title("Create and verify a new event")
@pytest.mark.parametrize("UserCredentials", get_user_credentials())
def test_new_event(UserCredentials, browser_invoke):
    #data
    userEmail = UserCredentials["userEmailId"]
    userPassword = UserCredentials["Password"]
    event_name = "TestEvent" + str(int(time.time() * 1000))

    #page
    loginPage = LoginPage(browser_invoke)
    menuBar = MenuBar(browser_invoke)
    eventPage = EventPage(browser_invoke)
    createNewEventPage = CreateNewEventPage(browser_invoke)

    #test
    loginPage.login(userEmail,userPassword)
    menuBar.clickEventButton()
    eventPage.clickAddNewEventButton()
    createNewEventPage.fillEventName(event_name)
    createNewEventPage.fillEventDescription()
    createNewEventPage.selectEventCategory()
    createNewEventPage.fillCity()
    createNewEventPage.fillEventVenue()
    createNewEventPage.fillEventDateAndTime()
    createNewEventPage.fillEventPrice()
    createNewEventPage.fillTotalSeats()
    createNewEventPage.clickAddEventButton()
    menuBar.clickEventButton()
    eventPage.verifyCreatedNewEventIsVisible(event_name)
