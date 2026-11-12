class User:
    def __init__(self, first_name: str, last_name: str):
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self):
        print(self.first_name)

    def print_surname(self):
        print(self.last_name)

    def print_name_surname(self):
        print(self.first_name, self.last_name)