# Inheritance: super class and sub classs, parent class and child class base class and derived class


class Vehicle:
    brand = None
    model = None
    color = None

    def get_info(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color


# todo:
# create animal class,attributes: eye, ears,legs
# methods: get info, show info
# create dog class, attributes: name method:move , sound()
# create bird class attributes: name methods move(),sound()


class Animal:
    eyes = None
    ears = None
    color = None

    def get_info(self, eyes, ears, color):
        self.eyes = eyes
        self.ears = ears
        self.color = color

    def show_info(self):
        print(f""""
            Eyes={self.eyes}
            Ears={self.ears}
            Color={self.color}
            """)
