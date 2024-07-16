# chapter_1_hw4_my_favourite_football_team.py

class FootballCheer:
    """
    A class to represent a cheer for a football team.

    Attributes:
    team_name (str): Name of the soccer team

    Methods:
    cheer(): Prints a cheer message for the soccer team
    """

    def __init__(self, team_name):
        """
        Constructs all the necessary attributes for the FootballCheer object.

        Parameters:
        team_name (str): Name of the soccer team
        """
        self.team_name = team_name

    def cheer(self):
        """
        Returns a cheer message for the soccer team.

        Returns:
        str: Cheer message
        """
        return f"{self.team_name} are the champions!"
