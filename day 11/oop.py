class Person:
    name = None
    age = None
    address = None
    gender = None

    def get_intro(self, name, age, address, gender):

        self.name = name
        self.age = age
        self.address = address
        self.gender = gender

    def intro(self):
        print(f"""
            Name: {self.name}
            Age: {self.age}
            Address: {self.address}
            Gender: {self.gender}
            """)


sita = Person()

sita.name = "Sita"
sita.age = "30"
sita.address = "BKT"
sita.gender = "female"

sita.intro()


ram = Person()

ram.get_intro("Ram", "25", "KTM", "Male")

ram.intro()

