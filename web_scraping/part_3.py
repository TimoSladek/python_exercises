import requests

movie = input('What movie would you like to search? ')
actor = input('What actor/actress would you like to search for? ')

r = requests.get(f"http://www.omdbapi.com/?t={movie}&apikey=8cfff058")

if actor.lower() in r.json()['Actors'].lower():
    print(f"Yes, {actor} was in {movie}.")
else:
    print(f"No, {actor} is not in {movie}.")

bonus = input("Do you want to know who is the director and writer of this movie? Y/n ")

if bonus == 'Y':
    print("Director: ", r.json()["Director"])
    print("Writer: ", r.json()["Writer"])
