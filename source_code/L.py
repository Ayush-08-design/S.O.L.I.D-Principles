# The Liskov substitution principle , states that objects of a subclass should be 
# replaceable with objects of their superclass without affecting the correctness of 
# the program In simple terms : if class B inherits from class A , 
# we should be able to use B wherever A is expected , without breaking the system


class Bird:
    def make_sound(self):
        print(f'Some generic bird sound')
        
    def fly(self):
        print('this bird is flying')
        
class Sparrow(Bird):
    def make_sound(self):
        print('Chirp Chirp')

# Violates LSP    
class Penguin(Bird):
    def make_sound(self):
        print('Honk Honk')
        
    def fly(self):
        print('Error : Penguins cannot fly')
        
def make_bird_fly(bird : Bird):
    bird.fly()
    
s = Sparrow()

p = Penguin()

make_bird_fly(s)
make_bird_fly(p)