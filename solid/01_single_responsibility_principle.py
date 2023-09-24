# Single Responsibility principle states that a
# class should have only one primary responsibility


class Journal:
    """This class primary functionality is to manage entries in entries"""

    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text):
        self.count = self.count + 1
        self.entries.append(f"{self.count}: {text}")

    def remove_entry(self, pos):
        del self.entries[pos]

    def __str__(self):
        return "\n".join(self.entries)


class PersistenceManager:
    """
    This class primary responsibility is to
    save entries in some persistence storage
    """

    @staticmethod
    def save_to_file(journal, filename):
        file_obj = open(filename, 'w')
        file_obj.write(str(journal))
        file_obj.close()


if __name__ == "__main__":
    j = Journal()
    j.add_entry("Hello World!!")
    j.add_entry("Hello Python!!")
    print(j)

    file_name = "sro.txt"
    PersistenceManager.save_to_file(j, file_name)

    with open(file_name, "r") as f:
        print(f.read())
