class CreateNewEventPage:

    def __init__(self,page):
        self.page = page


    def fillEventName(self,event_name):
        self.page.locator("#event-title-input").fill(event_name)

    def fillEventDescription(self):
        (self. page.locator("#admin-event-form textarea")
         .fill("This is a test event created by Playwright."))

    def selectEventCategory(self):
        self.page.get_by_label("category").select_option("Festival")

    def fillCity(self):
        self.page.get_by_label("city").fill("Bangalore")

    def fillEventVenue(self):
        self.page.get_by_label("venue").fill("Test Venue")

    def fillEventDateAndTime(self):
        self.page.locator('[type="datetime-local"]').fill("2027-02-07T02:10")

    def fillEventPrice(self):
        self.page.locator("[id='price-($)']").fill("500")

    def fillTotalSeats(self):
        self.page.locator("#total-seats").fill("100")

    def clickAddEventButton(self):
        self.page.get_by_role("button", name="+ Add Event").click()
