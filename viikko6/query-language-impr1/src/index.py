from stats import Statistics
from player_reader import PlayerReader
from matchers import And, HasAtLeast, PlaysIn, All, Not, HasFewerThan, Or
from query_builder import QueryBuilder


def main():
    url = "https://studies.cs.helsinki.fi/nhlstats/2021-22/players.txt"
    reader = PlayerReader(url)
    stats = Statistics(reader)

    query = QueryBuilder()

    print("välirivi")

    matcher2 = (
        query
        .hasAtLeast(10, "goals")
        .hasFewerThan(20, "goals")
        .playsIn("NYR").build())

    for player in stats.matches(matcher2):
        print(player)

    m1 = (
      query
        .playsIn("PHI")
        .hasAtLeast(10, "assists")
        .hasFewerThan(5, "goals")
        .build()
    )

    print("välirivi")

    m2 = (
      query
        .playsIn("EDM")
        .hasAtLeast(50, "points")
        .build()
    )

    matcher = query.oneOf(m1, m2).build()

    for player in stats.matches(matcher):
        print(player)




if __name__ == "__main__":
    main()
