class PasswordChecker:
    def __init__(self, password):
        self.password = password

    def length_check(self):
        return len(self.password) >= 8

    def has_digit(self):
        for ch in self.password:
            if ch.isdigit():
                return True
        return False

    def has_upper(self):
        for ch in self.password:
            if ch.isupper():
                return True
        return False

    def has_lower(self):
        for ch in self.password:
            if ch.islower():
                return True
        return False

    def is_strong(self):
        if (self.length_check() and
            self.has_digit() and
            self.has_upper() and
            self.has_lower()):
            return True
        return False

    def show_result(self):
        if self.is_strong():
            print("Parol kuchli")
        else:
            print("Parol kuchsiz")


def main():
    p1 = PasswordChecker("Python123")
    p2 = PasswordChecker("abc")

    p1.show_result()
    p2.show_result()


main()
