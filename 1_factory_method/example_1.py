from abc import ABC, abstractmethod

class DeliveryCreator(ABC):

    @abstractmethod
    def factory_method(self):
        pass

    def process_delivery(self) -> str:
        delivery: Delivery = self.factory_method()
        return f"Delivery processed with {delivery.deliver()}"
    

class CourierDeliveryCreator(DeliveryCreator):
    def factory_method(self):
        return CourierDelivery()

class PostDeliveryCreator(DeliveryCreator):
    def factory_method(self):
        return PostDelivery()

class Delivery(ABC):
    @abstractmethod
    def deliver(self) -> str:
        pass

class CourierDelivery(Delivery):
    def deliver(self):
        return "Courier delivery: Your package will be delivered by a courier."

class PostDelivery(Delivery):
    def deliver(self):
        return "Post delivery: Your package will be delivered through the postal service."


def client_code(creator: DeliveryCreator) -> None:
    print(creator.process_delivery())

if __name__ == "__main__":
    print("Client: Order with courier delivery.")
    client_code(CourierDeliveryCreator())

    print("\nClient: Order with post delivery.")
    client_code(PostDeliveryCreator())