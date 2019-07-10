"""
Design a parking lot

https://github.com/donnemartin/system-design-primer/blob/master/solutions/object_oriented_design/parking_lot/parking_lot.ipynb
What types of vehicles should we support? Motorcycle, Car, Bus

Does each vehicle type take up a different amount of parking spots? Yes
Motorcycle spot -> Motorcycle
Compact spot -> Motorcycle, Car
Large spot -> Motorcycle, Car
Bus can park if we have 5 consecutive "large" spots

Does the parking lot have multiple levels? Yes
"""
from abc import ABCMeta, abstractclassmethod

class VehicleSize:
    MOTORCYCLE = 0
    COMPACT = 1
    LARGE = 2

class Vehicle(metaclass = ABCMeta):
    def __init__(self, vehicle_size, license_plate, spot_size):
        self.vechicle_size = vehicle_size
        self.license_plate = license_plate
        self.spot_size = spot_size  # number of parking spots this vehicle will take
        self.spots_taken = []   # 

    def leave_spot(self, spot):
        spot.remove_vehicle()
        self.spots_taken.remove(spot)
    
    def take_spot(self, spot):
        self.spots_taken.append(spot)
    
    @abstractclassmethod
    def can_fit_spot(self, spot):
        pass

class Motorcycle(Vehicle):
    def __init__(self, license_plate):
        super().__init__(VehicleSize.MOTORCYCLE, license_plate, spot_size = 1)
    
    def can_fit_spot(self, spot):
        return True

class Car(Vehicle):
    def __init__(self, license_plate):
        super().__init__(VehicleSize.COMPACT, license_plate, spot_size = 1)

    def can_fit_spot(self, spot):
        return spot.size == VehicleSize.LARGE or spot.size == VehicleSize.COMPACT

class Bus(Vehicle):
    def __init__(self, license_plate):
        super().__init__(VehicleSize.COMPACT, license_plate, spot_size = 5)

    def can_fit_spot(self, spot):
        return spot.size == VehicleSize.LARGE

class ParkingLot:
    def __init__(self, num_levels):
        self.num_levels = num_levels
        self.levels = []

    def park_vehicle(self, vehicle):
        '''
        return True if vehicle is successfully parked, else False
        '''
        for level in self.levels:
            if level.park_vehicle(vehicle):
                return True
        return False

class Level:
    def __init__(self, floor, total_spots):
        self.floor = floor
        self.num_spots = total_spots
        self.available_spots = 0
        self.parking_rows = []

    def park_vehicle(self, vehicle):
        spots = self._find_available_spots(vehicle)
        if not spots:
            return False
        else:
            for spot in spots:
                spot.park_vehicle(vehicle)
                vehicle.take_spot(spot)
                self.available_spots -= 1
            return True
    
    def _find_available_spots(self, vehicle):
        '''
        return available spots in a list for this vehicle
        '''
        if self.available_spots == 0:
            return []
        spots = []
        for parking_row in self.parking_rows:
            cnt = 0
            for i, parking_spot in enumerate(parking_row):
                if parking_spot.is_available() and vehicle.can_fit_spot(parking_spot):
                    cnt += 1
                    if cnt == vehicle.spot_size:
                        spots.extend(parking_row[i-vehicle.spot_size+1:i+1])
                        return spots
                else:
                    cnt = 0

        return spots

class ParkingSpot:

    def __init__(self, level, row, spot_number, spot_size):
        self.level = level
        self.row = row
        self.spot_number = spot_number
        self.spot_size = spot_size
        self.vehicle = None
    
    def is_available(self):
        return self.vehicle is None

    def park_vehicle(self, vehicle):
        self.vehicle = vehicle
    
    def remove_vehicle(self, vehicle):
        self.vehicle = None
