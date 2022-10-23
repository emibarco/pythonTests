class User:

    def __init__(self, name, last_name):
        self.name = name
        self.last_name = last_name

    def display_info(self):
        print(f"User mame {self.name} and user last_name {self.last_name}")