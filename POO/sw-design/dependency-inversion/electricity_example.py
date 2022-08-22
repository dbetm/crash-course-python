# Elemental idea: decouple two classes through an interface

from abc import ABC, abstractmethod


class Switchable(ABC):
    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


# subclass, it needs to implement the abstract methods of Switchable
class LightBulb(Switchable):
    def turn_on(self):
        print("Lightbulb: turned on...")
    
    def turn_off(self):
        print("Lightbulb: turned off...")


class Fan(Switchable):
    def turn_on(self):
        print("Fan: turned on...")
    
    def turn_off(self):
        print("Fan: turned off...")


# switch that operates an received switchable device
class ElectricPowerSwitch:
    def __init__(self, client: Switchable):
        self.client = client
        self.on = False
    
    def press(self):
        if self.on:
            self.client.turn_off()
        else:
            self.client.turn_on()
        
        self.on = False if self.on else True


l = LightBulb()
f = Fan()
# switch = ElectricPowerSwitch(l)
switch = ElectricPowerSwitch(f)

switch.press()
switch.press()
switch.press()