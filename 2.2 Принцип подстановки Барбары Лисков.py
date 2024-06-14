# class Bird():
#     def __init__(self, name):
#         self.name = name
#     def fly(self):
#         print(self.name + " Она летит")
#
# class Ping(Bird):
#     def fly(self):
#         print(self.name + " Она летит")
#         super().fly()

class Bird():
   def fly(self):
       print("Эта птица летает")

class Duck(Bird):
   def fly(self):
       print("Эта утка летает быстро")

def fly_in_the_sky(animal):
    animal.fly()

b = Bird()
d = Duck()
fly_in_the_sky(b)
fly_in_the_sky(d)