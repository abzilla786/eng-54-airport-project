import stdiomask


class login:

    def __init__(self, id, password):
        self.id = id
        self.password = password
        self.error = "Enter a valid username and password"

    def check(self):
        if (self.id == log_id and self.password == log_pass):
            print("Login successful")
        elif (self.id != log_id and self.password != log_pass):
            print(self.error)
            try_again = input('Would you like to try again (Y/N): ')
            if try_again == 'N':
                print('Goodbye')
                loop = False
            else:
                pass


log = login("admin", "admin")
log_id = input("Enter your user ID: ")
log_pass = stdiomask.getpass("Enter password: ")
log.check()
