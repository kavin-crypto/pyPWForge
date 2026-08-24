from playwright.sync_api import expect


class EventPage:

    def __init__(self,page):
        self.page = page
        self.eventCard = self.page.locator('[data-testid="event-card"]')


    def clickAddNewEventButton(self):
        self.page.get_by_role("button", name="Add New Event").click()

    def eventCard(self):
        self.page.locator('[data-testid="event-card"]')

    def verifyCreatedNewEventIsVisible(self,event_name):
        expect(
            self.eventCard.filter(has_text=event_name)
        ).to_be_visible()
