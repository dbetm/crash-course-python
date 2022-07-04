import random
import string

# Low cohesion: A function of method has a lot of responsabilities.
# High coupling: Change a part of the code requires to change other parts of the code.

class VehicleInfo:
    brand: str
    catalogue_price: int
    is_electric: bool

    def __init__(self, brand: str, catalogue_price: int, is_electric: bool):
        self.brand = brand
        self.catalogue_price = catalogue_price
        self.is_electric = is_electric

    def compute_tax(self) -> float:
        tax_percentage = 0.05

        if self.is_electric:
            tax_percentage = 0.02

        return self.catalogue_price * tax_percentage

    def print(self):
        print(f"Brand: {self.brand}")
        print(f"Payable tax: {self.compute_tax()}")


class Vehicle:
    id: str
    license_plate: str
    info: VehicleInfo

    def __init__(self, id: str, license_plate: str, info: VehicleInfo):
        self.id = id
        self.license_plate = license_plate
        self.info = info
    
    def print(self):
        print(f"ID: {self.id}")
        print(f"License plate: {self.license_plate}")
        self.info.print()


class VehicleRegistry:
    vehicle_info = {}

    def __init__(self):
        self.add_vehicle_info("Tesla Model 3", True, 60000)
        self.add_vehicle_info("Volkswagen ID3", True, 3500)
        self.add_vehicle_info("BMW 5", False, 45000)
        # it's quite easy to add a new vehicle without change the code
        # this info could come from a database in a real life scenario

    def add_vehicle_info(self, brand: str, is_electric: bool, catalogue_price: int):
        self.vehicle_info[brand] = VehicleInfo(brand, catalogue_price, is_electric)

    def generate_vehicle_id(self, length: int) -> str:
        return "".join(random.choices(string.ascii_uppercase, k=length))

    def generate_vehicle_license(self, id: str) -> str:
        prefix = id[:2]
        suffix = "".join(random.choices(string.ascii_uppercase, k=2))
        return f"{prefix}-{''.join(random.choices(string.digits, k=2))}-{suffix}"

    def create_vehicle(self, brand: str) -> Vehicle:
        vehicle_id = self.generate_vehicle_id(length=12)
        license_plate = self.generate_vehicle_license(id=vehicle_id)

        return Vehicle(
            id=vehicle_id, license_plate=license_plate, info=self.vehicle_info[brand]
        )


class Application:
    def register_vehicle(self, brand: str):
        registry = VehicleRegistry()

        return registry.create_vehicle(brand)


app = Application()
vehicle = app.register_vehicle("Tesla Model 3")
vehicle.print()

