class Contact:
    def __init__(self, name="", phones="", emails="", address="", note="", tags=""):
        self.name = name
        self.phones = phones
        self.emails = emails
        self.address = address
        self.note = note
        self.tags = tags

    def revise_individual(self):
        return input()

    def revise_list(self):
        new_data = []
        while True:
            result = input()
            if result == "":
                break
            else:
                new_data.append(result)
        return new_data