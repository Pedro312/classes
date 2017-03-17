#Class 1
class Item(object):
    def __init__(self, name, value):
        self.name = name
        self.value = value
    def sell(self):
        print "You sell the %s for %d gold." % (self.name, self.value)

#Class 2
class Weapon(Item):
    def __init__(self, name, value, damage):
        super(Weapon, self).__init__(name, value)
        self.damage = damage
    def attack(self, target):
        print "You attack %s for %d damage." % (target.name, self.damage)
        
#Class 3 
class Bomb(Weapon):
    def __init__(self, name, value, damage):
        super(Weapon, self).__init__(name, value)
        self.damage = damage
    def blow_up(self, target):
        print "You have bombed %s and done %d damage." % (target.name, self.damage)
        target.take_damage(self.damage)
        
#Class 4
class Vehicle(Item):
    def __init__ (self, name, motor, material, vtype):
        self.motor = motor
        self.material = material
        self.name = name
        self.vtype = vtype

#Class 5        
class Car(Vehicle):
    def __init__(self, name, motor, material):
        super(Car, self). __init__(name, motor, material, "Car")
        self.engine_status = False
    def move(self):
        if self.engine_status:
           print "You move forward"
        else:
            print "The car is off."
    def engine_on(self):
        self.engine_status =True
        print "You turn the key and the engine turns on."
        
#Class 6 
class Character(Item):
    def __init__(self, name, hp, damage, attack_speed, armor):
        self.name = name
        self.damage = damage
        self.health = hp
        self.attack_speed = attack_speed
        self.bag = []
        self.armor = armor
        
    def pick_up(self, item):
        self.bag.append(item)
        print "You put the %s in your bag." % item
        
    def attack(self, target):
        if target.health == 0:
            print "%s is already dead." % target.name
        else:
            target.take_damage(self.damage)
            print "You attacked %s for %d damage." % (target.name , self.damage)
        
    def take_damage(self, damage):
        if self.armor > 0:
            self.armor -= damage
        elif self.armor == 0:
            if self.health > 0:
                self.health -= damage
        else:
            print "%s is already dead" % self.name
    def eat(self, food):
        if self.health < 100:
            self.health += food.health
            print "You have eaten %s and gained %d health." %(food.name, food.health)
        else:
            print "You can not eat anymore, or you may explode."
    def good(self):
        print "Good"

#Class 7
class Food(Item):
    def __init__(self, name, value, health):
        self.name = name
        self. value = value
        self.health = health
#Class 8 
        
bobby = Bomb("Bobby's Bomb", 2, 20)
cookie = Food("Cookie", 15, 20)
bobe = Car("Bobby's Car", "V8", "Carbon Fiber")
rob = Character('Roberto Moreno', 100, 100, 2, 200)
bob = Character('Bobby Vixathep', 100, 20, 2, 0)
