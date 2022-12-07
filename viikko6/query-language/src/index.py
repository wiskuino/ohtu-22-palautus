from stats import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

   #matcher = And(
   #   HasAtLeast(5, "goals"),
   #   HasAtLeast(5, "assists"),
   #   PlaysIn("PHI"))
   #   
   #for player in stats.matches(matcher):
   #   print(player)

    matcher2 = All( "name")

    for player in stats.matches(matcher2):
       print(player)


if __name__ == "__main__":
    main()
