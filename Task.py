import re

class Field:
    pass

class Name(Field):
    def __init__(self, name):
        self.name = name

class Phone(Field):
    def __init__(self, number):
        if not re.match(r'^\d{10}$', number):
            raise ValueError("Invalid phone number format")
        self.number = number

class Record:
    def __init__(self, name):
        self.name = Name(name)
        self.phones = []

    def add_phone(self, number):
        try:
            phone = Phone(number)
            self.phones.append(phone)
        except ValueError as e:
            print(e)

    def remove_phone(self, number):
        for phone in self.phones:
            if phone.number == number:
                self.phones.remove(phone)
                print("Phone number removed:", number)
                return
        print("Phone number not found.")

    def edit_phone(self, old_number, new_number):
        for phone in self.phones:
            if phone.number == old_number:
                try:
                    phone.number = new_number
                    print("Phone number edited successfully.")
                    return
                except ValueError as e:
                    print(e)
        print("Phone number not found.")

    def search_phone(self, number):
        for phone in self.phones:
            if phone.number == number:
                return phone
        return None

class AddressBook:
    def __init__(self):
        self.records = []

    def add_record(self, record):
        self.records.append(record)

    def find(self, name):
        for record in self.records:
            if record.name.name == name:
                return record
        return None

    def delete(self, name):
        for record in self.records:
            if record.name.name == name:
                self.records.remove(record)
                print("Record removed:", name)
                return
        print("Record not found.")
