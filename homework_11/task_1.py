import json


class Person:
    def __init__(self, name):
        self.name = name


class Address:
    def __init__(self, address):
        self. address = address


class Contact(Address, Person):
    def __init__(self, name, address):
        super().__init__(name)
        self.name = name
        super().__init__(address)
        self.address = address


class Notebook:
    def __init__(self, data):
        self.data = data
        self.contacts_arr = []

    def review_c(self):
        for i in self.data.items():
            a, b = i
            print(f"{a} - {b}")

    def add_c(self):
        name = input("Name: ")
        info = input("Contacts: ")
        with open("contacts.json", "w") as file:
            self.data.update({name: info})
            json.dump(self.data, file)
            print("Mission complete.")

    def edit_c(self):
        Notebook.review_c(self)
        name = input("Name: ")
        new_name = input("Enter new name: ")
        new_address = input("Enter new address: ")
        del self.data[name]
        self.data.update({new_name: new_address})
        with open("contacts.json", "w") as file:
            json.dump(self.data, file)
            print("Mission complete.")

    def read_contacts_from_file(self):
        self.contacts_arr = []
        with open("contacts.json", "r") as file:
            text = json.load(file)
        for i in text:
            new_contact = Contact(i, text[i])
            self.contacts_arr.append(new_contact)


def actions(data):
    go_to_do = Notebook(data)
    doings = {
        "review": go_to_do.review_c,
        "add": go_to_do.add_c,
        "edit": go_to_do.edit_c
    }
    while True:
        action = input(" - ").lower()
        if action != "add" and action != "review" and action != "edit":
            print("Choose from what is")
        else:
            return doings[action]()


def main():
    with open("contacts.json", "r") as contacts:
        data = json.load(contacts)
    print("What do you want?")
    print("View contacts, add a contact, edit a contact (review/add/edit)")
    actions(data)
    x = Notebook(data)
    x.read_contacts_from_file()


if __name__ == '__main__':
    main()
