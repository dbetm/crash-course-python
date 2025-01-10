from temperature import Temperature

class Calorie:
    """Represent amount of calories calculated with
    BMR = 10*weight + 6.25*height - 5*age + 5 - 10*temperature"""

    def __init__(self, weight: int, height: int, age: int, temperature: Temperature):
        self.temperature = temperature
        self.weight = weight
        self.height = height
        self.age = age

    def calculate(self) -> float:
        return 10*self.weight + 6.5*self.height + 5 - self.temperature*10


    def __str__(self):
        return (
            f"Temp: {self.temperature}, Weight: {self.weight}, Height: {self.height}, Age: {self.age}"
        )



if __name__ == "__main__":
    temperature = Temperature(country="Mexico", city="Zacatecas").get()

    calorie = Calorie(weight=65, height=175, age=27, temperature=temperature)

    print(calorie.calculate())