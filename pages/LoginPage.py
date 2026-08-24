class LoginPage:

    def __init__(self,page):
        self.page = page

    def login(self,username,password):
        self.page.get_by_placeholder("you@email.com").fill(username)
        self.page.get_by_label("password").fill(password)
        self.page.locator("#login-btn").click()



