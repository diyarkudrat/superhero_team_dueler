# class Dog:
#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#
#     def bark(self):
#         print("Woof!")
#
#
# from dog import Dog
#
# my_dog = dog.Dog("Rex", "SuperDog")
# my_dog.bark()
#
# my_other_dog = dog.Dog('Annie','Superdog')
# print(my_other_dog)

class Dog:
    def __init__(self, name):
        self.name = name

my_dog = Dog("Rex")
print(my_dog)
print(my_dog.name)
