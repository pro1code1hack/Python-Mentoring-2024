import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


class FootballTeamCheer:
    def __init__(self, team_name):
        self.team_name = team_name

    def cheer(self):
        cheer_message = f"{self.team_name} is a champion!"
        logging.info(cheer_message)


def main():
    logging.info("Enter the name of your favourite soccer team: ")
    team_name = input()
    team_cheer = FootballTeamCheer(team_name)
    team_cheer.cheer()


if __name__ == "__main__":
    main()
