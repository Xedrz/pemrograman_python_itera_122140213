from abc import ABC, abstractmethod

# Abstract class: Vehicle
class Vehicle(ABC):
    def __init__(self, vehicle_id, name, price_per_day):
        self.__vehicle_id = vehicle_id
        self._name = name
        self._price_per_day = price_per_day

    @abstractmethod
    def display_info(self):
        pass

    @property
    def vehicle_id(self):
        return self.__vehicle_id

    @property
    def name(self):
        return self._name

# Subclass: Car
class Car(Vehicle):
    def __init__(self, vehicle_id, name, price_per_day, num_doors):
        super().__init__(vehicle_id, name, price_per_day)
        self.__num_doors = num_doors

    def display_info(self):
        print(f"[Car] ID: {self.vehicle_id}, Name: {self.name}, Doors: {self.__num_doors}, Price/Day: ${self._price_per_day}")

# Subclass: Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, vehicle_id, name, price_per_day, has_gear):
        super().__init__(vehicle_id, name, price_per_day)
        self.__has_gear = has_gear

    def display_info(self):
        gear_info = "Yes" if self.__has_gear else "No"
        print(f"[Motorcycle] ID: {self.vehicle_id}, Name: {self.name}, Gear: {gear_info}, Price/Day: ${self._price_per_day}")

# Class: VehicleRental
class VehicleRental:
    def __init__(self):
        self.__vehicles = []

    def add_vehicle(self, vehicle):
        self.__vehicles.append(vehicle)

    def show_all_vehicles(self):
        if not self.__vehicles:
            print("No vehicles available.")
        for v in self.__vehicles:
            v.display_info()

    def search_vehicle(self, keyword):
        found = False
        for v in self.__vehicles:
            if keyword.lower() in v.name.lower() or keyword.lower() == v.vehicle_id.lower():
                v.display_info()
                found = True
        if not found:
            print(f"No vehicle found with keyword: {keyword}")

# Menu interaktif
def main():
    rental = VehicleRental()

    while True:
        print("\n=== Vehicle Rental System ===")
        print("1. Add Car")
        print("2. Add Motorcycle")
        print("3. Show All Vehicles")
        print("4. Search Vehicle")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            vid = input("Enter Car ID: ")
            name = input("Enter Car Name: ")
            price = float(input("Enter Price per Day: "))
            doors = int(input("Enter Number of Doors: "))
            car = Car(vid, name, price, doors)
            rental.add_vehicle(car)
            print("Car added successfully!")

        elif choice == "2":
            vid = input("Enter Motorcycle ID: ")
            name = input("Enter Motorcycle Name: ")
            price = float(input("Enter Price per Day: "))
            gear = input("Has Gear (yes/no): ").strip().lower() == "yes"
            bike = Motorcycle(vid, name, price, gear)
            rental.add_vehicle(bike)
            print("Motorcycle added successfully!")

        elif choice == "3":
            print("\n--- All Vehicles ---")
            rental.show_all_vehicles()

        elif choice == "4":
            keyword = input("Enter vehicle ID or name to search: ")
            rental.search_vehicle(keyword)

        elif choice == "5":
            print("Exiting program. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
