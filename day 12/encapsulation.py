# Encapsulation: properties are bind into a single unit, data hiding


class Login:
    __username = None
    __password = None

    def get_info(self, username, password):
        self.__username = username
        self.__password = password

    def __show(self):
        print(f"""Username: {self.__username}
Password:{self.__password}""")

    def calls(self):
        self.__show()


p1 = Login()
p1.get_info("ram", "ram123")
p1.calls()
