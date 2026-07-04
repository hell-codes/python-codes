#Program to perform set operations on two sets of students playing different sports.
basketball_team = {"Alice", "Bob", "Charlie", "David"}
baseball_team = {"Charlie", "Edward", "Frank", "Alice"}

both_sports = basketball_team.intersection(baseball_team)
print("Students who play both sports:", both_sports)

either_sport = basketball_team.union(baseball_team)
print("Students who play either sport:", either_sport)

only_basketball = basketball_team - baseball_team
print("Students who only play basketball:", only_basketball)

only_baseball = baseball_team - basketball_team
print("Students who only play baseball:", only_baseball)

sports_not_both = basketball_team.symmetric_difference(baseball_team)
print("Students who play sports but not both:", sports_not_both)
