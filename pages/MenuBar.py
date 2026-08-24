class MenuBar:

    def __init__(self,page):
        self.page = page

    def clickEventButton(self):
        self.page.locator("#nav-events").click()



