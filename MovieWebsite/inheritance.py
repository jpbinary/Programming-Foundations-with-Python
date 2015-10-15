class Parent():
    def __init__(self, last_name, eye_color):
        print ("Parent Constructor Called.")
        self.last_name = last_name
        self.eye_color = eye_color


class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called.")
        # reuse the Parents __init__ method
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys



daddy = Parent("Dad", "grey")
little_boy = Child("Dad", "grey", 4)

print(daddy.last_name)
print(little_boy.last_name)
print(little_boy.number_of_toys)