"""Use the enumerate() function to list sports teams and their ranking based on 
user input."""

# Input: Enter teams (separated by commas): Lakers, Bulls, Celtics
# Output: Team Rankings:
#  1. Lakers
#  2. Bulls
#  3. Celtics

teams = input("Enter teams (separated by commas): ")
teams_tuple = tuple(teams.split(", "))
print("Team Rankings:")
for index, team in enumerate(teams_tuple):
    print(f"{index + 1}. {team}")
