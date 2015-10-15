class Parent():
    def __init__(self, last_name, eye_color):
        print ("Parent Constructor Called.")
        self.last_name = last_name
        self.eye_color = eye_color

    def show_info(self):
        print("Last Name - " + self.last_name)
        print("Eye Color - " + self.eye_color)


class Child(Parent):
    def __init__(self, last_name, eye_color, number_of_toys):
        print("Child Constructor Called.")
        # reuse the Parents __init__ method
        Parent.__init__(self, last_name, eye_color)
        self.number_of_toys = number_of_toys

    def show_info(self):
        print(self.last_name)
        print(self.eye_color)
        print(self.number_of_toys)

daddy = Parent("Dad", "grey")
little_boy = Child("Dad", "blue", 4)

print(daddy.last_name)
daddy.show_info()
#print(little_boy.last_name)
#print(little_boy.number_of_toys)
little_boy.show_info()
    # can call show_info() in Parent class, since inherited
    # but if create show_info() in Child class, then it will use the Child's show_info()
        # this is known as method overriding