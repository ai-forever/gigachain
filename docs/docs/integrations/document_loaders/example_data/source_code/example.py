class MyClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
<<<<<<< HEAD
        print(f"Hello, {self.name}!")  # noqa: T201
=======
        print(f"Hello, {self.name}!")
>>>>>>> langchan/master


def main():
    name = input("Enter your name: ")
    obj = MyClass(name)
    obj.greet()


if __name__ == "__main__":
    main()
