players_count=1
team_rating=4.8
team_name="sahara india"
has_won_world_cup =True

print(players_count)
print(team_rating)
print(team_name)
print(has_won_world_cup)

print(__name__)
print("-"*40)

a, b, c = 10, 20, "hello"
print(a, b, c, sep=", ")

a = b = c = 150
print (a, b, c, sep=" : ")
print("-"*40)

firstname = "Sachin"
lastname = "Tendulkar"

print ("My name is " + firstname + " and I am also called as " + lastname)

# interpolation - format string or fstring

print(f"My name is {firstname} and I am also called as {lastname}")

frt1 = 'Ooty Apple'
frt2 = 'Kanpur Orange'
print(f"We sell {frt1} and {frt2} to the customers")
print(f"We made a sales of {10 * 50 + 20 * 80} by selling {frt1} and {frt2}")

print(f"example {'hello' + ' world'}")
print("-"*40)

team_name = "Sahara India"
print(team_name)
team_name = "Sahara 'India'"
print(team_name)
team_name = 'Sahara India'
print(team_name)
team_name = 'Sahara "India"'
print(team_name)
team_name = '"\'Sahara \'India\'\'"'
print(team_name)
