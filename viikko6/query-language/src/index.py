from stats import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or
from query_builder import QueryBuilder

def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)
    query = QueryBuilder()

    matcher2 = (
    query
    .hasAtLeast(10, "goals")
    .hasFewerThan(20, "goals")
    .playsIn("NYR").build())
    
    
    for player in stats.matches(matcher2):
        print(player)
    
    
    print("")
    print("")
    
    matcher = (query
    .oneOf(
        query.playsIn("PHI")
          .hasAtLeast(10, "assists")
          .hasFewerThan(5, "goals")
          .build(),
        query.playsIn("EDM")
          .hasAtLeast(50, "points")
          .build()
    )
    .build())

    for player in stats.matches(matcher):
        print(player)

   
   

    
    #

   #matcher = And(
   #HasFewerThan(1, "goals"),
   #PlaysIn("NYR"))

    matcher = And(
    HasAtLeast(70, "points"),
    Or(
        PlaysIn("NYR"),
        PlaysIn("FLA"),
        PlaysIn("BOS")))

   #for player in stats.matches(matcher):
   #    print(player)
   #print("välirivi")
   #
   #for player in stats.matches(matcher3):
   #    print(player)
    
    




if __name__ == "__main__":
    main()
