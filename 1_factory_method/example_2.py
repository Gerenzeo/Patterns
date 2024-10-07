from abc import ABC, abstractmethod

class TripCreator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def start_trip(self) -> str:
        trip: Trip = self.factory_method()
        return trip.trip()

# Trip methods
class TaxiTripCreator(TripCreator):
    def factory_method(self):
        return TaxiTrip()

class CarTripCreator(TripCreator):
    def factory_method(self):
        return CarTrip()

class MetroTripCreator(TripCreator):
    def factory_method(self):
        return MetroTrip()


class Trip(ABC):

    @abstractmethod
    def trip(self) -> str:
        pass

class TaxiTrip(Trip):
    def trip(self):
        return "Our trip will be made by taxy."

class CarTrip(Trip):
    def trip(self) -> str:
        return "Our trip will by made our car."

class MetroTrip(Trip):
    def trip(self) -> str:
        return "Our trip will by metro."


def client_code(trip_creator: TripCreator):
    print(trip_creator.start_trip())


if __name__ == "__main__":
    print("Start trip by taxi")
    client_code(TaxiTripCreator())

    print("\nStart trip by car")
    client_code(CarTripCreator())

    print("\nStart trip by metro")
    client_code(MetroTripCreator())