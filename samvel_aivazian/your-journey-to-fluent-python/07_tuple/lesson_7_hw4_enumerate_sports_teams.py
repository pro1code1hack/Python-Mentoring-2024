import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')


def enumerate_sports_teams():
    logging.info("Enter teams (separated by commas): ")
    teams = input().split(',')
    teams = [team.strip() for team in teams]

    logging.info("Team Rankings:")
    for index, team in enumerate(teams, start=1):
        logging.info(f"{index}. {team}")


if __name__ == "__main__":
    enumerate_sports_teams()
