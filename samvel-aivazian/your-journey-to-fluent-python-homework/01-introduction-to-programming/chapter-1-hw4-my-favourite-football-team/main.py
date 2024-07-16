# main.py

import logging

from football_cheer import FootballCheer

# Setting up logging
logging.basicConfig(level=logging.INFO)

if __name__ == "__main__":
    team_name = input("Enter the name of the soccer team: ")
    cheer = FootballCheer(team_name)
    logging.info("Cheering for the team.")
    print(cheer.cheer())
