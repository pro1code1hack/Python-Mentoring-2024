import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def favourite_football_team():
    logging.info("Enter the name of your favourite soccer team: ")
    team_name = input().strip()
    team_cheer = (f"{team_name} is a champion!",)
    logging.info(team_cheer[0])


if __name__ == "__main__":
    favourite_football_team()
