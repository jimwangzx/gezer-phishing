import requests


class Logic:

    def __init__(self):
        self.users = {}

    def render_courses(self, username, password, identity, english=False):
        session_id = self.get_session_id(username, password, identity)
        if session_id == -1:
            return "login_fail.html" if not english else "elogin_fail.html"

        headers = {
            "Referer": "https://gezer1.bgu.ac.il/meser/main.php",
            "Cookie": f"PHPSESSID={session_id}"
        }

        data = {
            "isheb": 0 if english else 1
        }

        res = requests.post("https://gezer1.bgu.ac.il/meser/crslist.php", data=data, headers=headers).content
        res = res.decode("windows-1255").replace("<link href=\"n3style.css\" rel=\"Stylesheet\" type=\"text/css\">", "<link rel= \"stylesheet\" "
                                                                                                                     "type= \"text/css\" href= \"{{"
                                                                                                                     " url_for('static',"
                                                                                                                     "filename='styles/n3style.css"
                                                                                                                     "') }}\"> ")

        res = res.replace("crslist.php?moresemesters=1&isheb=1", f"crslist.php?username={username}")
        self.save(username, password, identity)

        with open(f"website/templates/{username}.html", "w+") as f:
            f.write(res)
        return username

    def save(self, username, password, identity):
        if username not in self.users:
            self.users[username] = {"password": password, "id": identity}
            print(self.users)

    def save_to_file(self, username, password, identity):
        pass
        # with open('users.txt', 'w') as f:
        #     f.write(f'username: {username}\npassword: {password}\nid: {identity}\n')

    @staticmethod
    def get_session_id(username, password, identity):
        session = requests.Session()
        res = session.post("https://gezer1.bgu.ac.il/meser/main.php", data={"username": username, "pass": password, "id": identity}).content.decode(
            "windows-1255")

        if "errorfound" in res:
            return -1

        return session.cookies.get_dict()["PHPSESSID"]
