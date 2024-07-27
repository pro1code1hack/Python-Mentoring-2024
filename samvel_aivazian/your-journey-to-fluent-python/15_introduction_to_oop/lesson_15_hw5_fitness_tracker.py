import logging
import time
from datetime import datetime

logging.basicConfig(level=logging.INFO, format='%(message)s')


def execution_time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"Execution time of {func.__name__}: {end_time - start_time:.6f} seconds")
        return result

    return wrapper


class Workout:
    def __init__(self, date, exercise, duration, intensity):
        self.date = date
        self.exercise = exercise
        self.duration = duration
        self.intensity = intensity


class User:
    def __init__(self, name):
        self.name = name
        self.workouts = []

    @execution_time_decorator
    def add_workout(self, workout):
        self.workouts.append(workout)

    @execution_time_decorator
    def summarize_activity(self):
        total_duration = sum(workout.duration for workout in self.workouts)
        logging.info(f"Total duration of workouts: {total_duration} minutes")
        for workout in self.workouts:
            logging.info(
                f"{workout.date}: {workout.exercise} for {workout.duration} minutes at {workout.intensity} intensity")

    @execution_time_decorator
    def set_fitness_goals(self, goals):
        self.goals = goals
        logging.info(f"Fitness goals set: {goals}")

    @execution_time_decorator
    def calculate_calories_burned(self):
        calories_burned = 0
        for workout in self.workouts:
            if workout.intensity == "high":
                calories_burned += workout.duration * 10
            elif workout.intensity == "medium":
                calories_burned += workout.duration * 8
            else:
                calories_burned += workout.duration * 5
        logging.info(f"Total calories burned: {calories_burned} calories")


if __name__ == "__main__":
    user = User("Alice")

    workout1 = Workout(datetime.now().strftime("%Y-%m-%d"), "Running", 30, "high")
    workout2 = Workout(datetime.now().strftime("%Y-%m-%d"), "Cycling", 45, "medium")

    user.add_workout(workout1)
    user.add_workout(workout2)

    user.summarize_activity()
    user.set_fitness_goals("Run 100 km in a month")
    user.calculate_calories_burned()
