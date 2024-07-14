from typing import List


class Engine:
    """
    A class to represent a car engine.

    Attributes:
    horsepower (int): The horsepower of the engine.
    is_running (bool): The state of the engine (running or not).
    """

    def __init__(self, horsepower: int) -> None:
        self.horsepower: int = horsepower
        self.is_running: bool = False

    def start(self) -> None:
        """
        Start the engine.
        """
        self.is_running = True
        print("Engine started.")

    def stop(self) -> None:
        """
        Stop the engine.
        """
        self.is_running = False
        print("Engine stopped.")

    def __str__(self) -> str:
        return f"Engine with {self.horsepower} HP"


class Wheel:
    """
    A class to represent a car wheel.

    Attributes:
    size (int): The size of the wheel in inches.
    pressure (int): The pressure of the tire in PSI.
    """

    def __init__(self, size: int) -> None:
        self.size: int = size
        self.pressure: int = 32  # Default tire pressure in PSI

    def inflate(self, pressure: int) -> None:
        """
        Inflate the tire to the given pressure.

        Args:
        pressure (int): The desired tire pressure in PSI.
        """
        self.pressure = pressure
        print(f"Wheel inflated to {self.pressure} PSI.")

    def __str__(self) -> str:
        return f"Wheel of size {self.size} inches"


class Body:
    """
    A class to represent a car body.

    Attributes:
    color (str): The color of the car body.
    type (str): The type of the car body (e.g., sedan, SUV).
    """

    def __init__(self, color: str, type: str) -> None:
        self.color: str = color
        self.type: str = type

    def __str__(self) -> str:
        return f"{self.color} {self.type} body"


class Car:
    """
    A class to represent a car, composed of an engine, wheels, and a body.

    Attributes:
    engine (Engine): The car's engine.
    wheels (List[Wheel]): The car's wheels.
    body (Body): The car's body.
    """

    def __init__(self, engine: Engine, wheels: List[Wheel], body: Body) -> None:
        self.engine: Engine = engine
        self.wheels: List[Wheel] = wheels
        self.body: Body = body

    def start_engine(self) -> None:
        """
        Start the car's engine.
        """
        self.engine.start()

    def stop_engine(self) -> None:
        """
        Stop the car's engine.
        """
        self.engine.stop()

    def inflate_tires(self, pressure: int) -> None:
        """
        Inflate all the car's tires to the given pressure.

        Args:
        pressure (int): The desired tire pressure in PSI.
        """
        for wheel in self.wheels:
            wheel.inflate(pressure)

    def display_parts(self) -> None:
        """
        Display the details of the car's parts.
        """
        print(f"Car with {self.engine}")
        for i, wheel in enumerate(self.wheels, 1):
            print(f"  {i}: {wheel}")
        print(f"  {self.body}")


def main() -> None:
    """
    Main function to create a car object and demonstrate its functionality.
    """
    # Create car components
    engine = Engine(horsepower=300)
    wheels = [Wheel(size=18) for _ in range(4)]
    body = Body(color="Red", type="Sedan")

    # Create a car with the above components
    car = Car(engine=engine, wheels=wheels, body=body)

    # Display car parts
    car.display_parts()

    # Start the engine
    car.start_engine()

    # Inflate tires
    car.inflate_tires(35)

    # Stop the engine
    car.stop_engine()


if __name__ == "__main__":
    main()
