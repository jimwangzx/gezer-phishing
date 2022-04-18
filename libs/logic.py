import requests
import random
import pathlib


class Logic:

    def __init__(self):
        self.users = []

    def render_courses(self, username, password, identity):
        session_id = self.get_session_id(username, password, identity)

        headers = {
            "Referer": "https://gezer1.bgu.ac.il/meser/main.php",
            "Cookie": f"PHPSESSID={session_id}"
        }

        res = requests.post("https://gezer1.bgu.ac.il/meser/crslist.php", headers=headers).content
        res = res.decode("windows-1255").replace("<link href=\"n3style.css\" rel=\"Stylesheet\" type=\"text/css\">", "<link rel= \"stylesheet\" "
                                                                                                                     "type= \"text/css\" href= \"{{"
                                                                                                                     " url_for('static',"
                                                                                                                     "filename='styles/n3style.css"
                                                                                                                     "') }}\"> ")

        r = random.randint(0, 1000)
        with open(f"website/templates/courses{r}.html", "w+") as f:
            f.write(res)
        return f"courses{r}.html"

    def get_session_id(self, username, password, identity):
        session = requests.Session()
        res = session.post("https://gezer1.bgu.ac.il/meser/main.php", data={"username": username, "pass": password, "id": identity})
        return session.cookies.get_dict()["PHPSESSID"]

    def save(self, username, password, identity):
        self.users.append({"username": username, "password": password, "id": identity})
        print(self.users)

    def save_to_file(self, username, password, identity):
        pass
        # with open('users.txt', 'w') as f:
        #     f.write(f'username: {username}\npassword: {password}\nid: {identity}\n')
