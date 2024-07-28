import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        logging.info("Engine started.")

    def stop(self):
        logging.info("Engine stopped.")


class Wheel:
    def __init__(self, size):
        self.size = size

    def inflate(self):
        logging.info("Wheel inflated.")

    def deflate(self):
        logging.info("Wheel deflated.")


class Body:
    def __init__(self, color):
        self.color = color

    def paint(self, new_color):
        self.color = new_color
        logging.info(f"Body painted {new_color}.")


class Car:
    def __init__(self, engine, wheels, body):
        self.engine = engine
        self.wheels = wheels
        self.body = body

    def start_engine(self):
        self.engine.start()

    def stop_engine(self):
        self.engine.stop()

    def inflate_tires(self):
        for wheel in self.wheels:
            wheel.inflate()

    def paint_body(self, new_color):
        self.body.paint(new_color)


if __name__ == "__main__":
    engine = Engine(horsepower=300)
    wheels = [Wheel(size=18) for _ in range(4)]
    body = Body(color="red")

    car = Car(engine=engine, wheels=wheels, body=body)

    car.start_engine()
    car.inflate_tires()
    car.paint_body("blue")
    car.stop_engine()
