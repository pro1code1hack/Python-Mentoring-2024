import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


class TravelItineraryPlanner:
    def __init__(self):
        self.cities = []

    def capture_itinerary(self):
        for i in range(3):
            logging.info(f"Enter city {i + 1}: ")
            city = input().strip()
            self.cities.append(city)

    def show_itinerary(self):
        itinerary = " -> ".join(self.cities)
        logging.info(f"Your travel itinerary: {itinerary}")


def main():
    planner = TravelItineraryPlanner()
    planner.capture_itinerary()
    planner.show_itinerary()


if __name__ == "__main__":
    main()
