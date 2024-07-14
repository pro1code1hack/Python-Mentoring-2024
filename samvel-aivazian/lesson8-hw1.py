from typing import List


class Engine:
    def __init__(self, horsepower: int) -> None:
        self.horsepower: int = horsepower
        self.is_running: bool = False

    def start(self) -> None:
        self.is_running = True
        print("Engine started.")

    def stop(self) -> None:
        self.is_running = False
        print("Engine stopped.")

    def __str__(self) -> str:
        return f"Engine with {self.horsepower} HP"


class Wheel:
    def __init__(self, size: int) -> None:
        self.size: int = size
        self.pressure: int = 32  # Default tire pressure in PSI

    def inflate(self, pressure: int) -> None:
        self.pressure = pressure
        print(f"Wheel inflated to {self.pressure} PSI.")

    def __str__(self) -> str:
        return f"Wheel of size {self.size} inches"


class Body:
    def __init__(self, color: str, type: str) -> None:
        self.color: str = color
        self.type: str = type

    def __str__(self) -> str:
        return f"{self.color} {self.type} body"


class Car:
    def __init__(self, engine: Engine, wheels: List[Wheel], body: Body) -> None:
        self.engine: Engine = engine
        self.wheels: List[Wheel] = wheels
        self.body: Body = body

    def start_engine(self) -> None:
        self.engine.start()

    def stop_engine(self) -> None:
        self.engine.stop()

    def inflate_tires(self, pressure: int) -> None:
        for wheel in self.wheels:
            wheel.inflate(pressure)

    def display_parts(self) -> None:
        print(f"Car with {self.engine}")
        for i, wheel in enumerate(self.wheels, 1):
            print(f"  {i}: {wheel}")
        print(f"  {self.body}")


def main() -> None:
    engine = Engine(horsepower=300)
    wheels = [Wheel(size=18) for _ in range(4)]
    body = Body(color="Red", type="Sedan")

    car = Car(engine=engine, wheels=wheels, body=body)

    car.display_parts()

    car.start_engine()

    car.inflate_tires(35)

    car.stop_engine()


if __name__ == "__main__":
    main()
