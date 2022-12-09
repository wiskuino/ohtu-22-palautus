from stats import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or
from query_builder import QueryBuilder


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()
    matcher= query.playsIn("NYR").build()

    for player in stats.matches(matcher):
        print(player)




   #matcher = And(
   #   HasAtLeast(5, "goals"),
   #   HasAtLeast(5, "assists"),
   #   PlaysIn("PHI"))
   #   
   #for player in stats.matches(matcher):
   #   print(player)

    #matcher2 = All( "name")
#
    #for player in stats.matches(matcher2):
    #   print(player)

    #matcher3 = Not(HasAtLeast(1,"goals"))    
    #matcher3 = And(
    #    Not(HasAtLeast(1, "goals")),
    #    PlaysIn("NYR"))   
    
   #matcher3 = Or(
   #HasAtLeast(45, "goals"),
   #HasAtLeast(70, "assists"))
   #
   #
   #

   #
   ##

   #matcher = And(
   #HasFewerThan(1, "goals"),
   #PlaysIn("NYR"))

    #matcher = And(
    #HasAtLeast(70, "points"),
    #Or(
    #    PlaysIn("NYR"),
    #    PlaysIn("FLA"),
    #    PlaysIn("BOS")))
#
    #for player in stats.matches(matcher):
    #    print(player)
    #print("välirivi")
    #
    #for player in stats.matches(matcher3):
    #   print(player)
    
    




if __name__ == "__main__":
    main()
