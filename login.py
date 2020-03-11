from pip._vendor.distlib.compat import raw_input
import stdiomask


class Login:

    def __init__(self, id, password):
        self.id = id
        self.password = password
        self.error = "Enter a valid username and password"

    def check(self):
        if (self.id == log_id and self.password == log_pass):
            print("Login successful")


log = Login("admin", "admin")
log_id = input("Enter your user ID: ")
log_pass = stdiomask.getpass("Enter password: ")
log.check()
