import fresh_tomatoes  # importing the fresh_tomatoes.py file
import media  # importing the media.py file


# specific data for each movie
rough_one = media.Movie("Rogue One",
                        "Craving the attention of her busy father, a 7-year"
                        "-old Star Wars fan disobeys him and starts a "
                        "rebellion with his Star Wars toy collection that "
                        "would have surprising consequences",
                        "https://image.tmdb.org/t/p/original/qjiskwlV1qQzRCjpV0cL9pEMF9a.jpg",  # NOQA
                        "https://www.youtube.com/watch?v=frdj1zb9sMY")


blade_runner = media.Movie("Blade Runner",
                           "In the smog-choked dystopian Los Angeles of 2019, "
                           "blade runner Rick Deckard is called out of "
                           "retirement to terminate a quartet of replicants "
                           "who have escaped to Earth seeking their creator "
                           "for a way to extend their short life spans.",
                           "https://image.tmdb.org/t/p/original/od70sq3crCZGQo463O5Juu3KlFE.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=eogpIG53Cis")

alien = media.Movie("Alien",
                    "During its return to the earth, commercial spaceship "
                    "Nostromo intercepts a distress signal from a distant "
                    "planet. When a three-member team of the crew discovers a "
                    "chamber containing thousands of eggs on the planet, a "
                    "creature inside one of the eggs attacks an explorer. The "
                    "entire crew is unaware of the impending nightmare set to "
                    "descend upon them when the alien parasite planted inside"
                    " its unfortunate host is birthed.",
                    "https://image.tmdb.org/t/p/original/mNS1Eg07JEA34eOEyqYB32L42VB.jpg",  # NOQA
                    "https://www.youtube.com/watch?v=LjLamj-b0I8")

trainspotting = media.Movie("Trainspotting",
                   "Renton, deeply immersed in the Edinburgh drug scene,"
                   " tries to clean up and get out, despite the allure of"
                   " the drugs and influence of friends.",
                   "https://image.tmdb.org/t/p/original/7Ag7U6Jgah0G13DEPy8eHcsoUk.jpg",  # NOQA
                   "https://www.youtube.com/watch?v=8LuxOYIpu-I")

hateful_eight = media.Movie("Hateful Eight",
                   "Bounty hunters seek shelter from a raging blizzard and"
                   " get caught up in a plot of betrayal and deception.",
                   "https://image.tmdb.org/t/p/original/701INmeeILYKGGIFH6f7t0Wf9YV.jpg",  # NOQA
                   "https://www.youtube.com/watch?v=gnRbXn4-Yis")

legends_of_the_fall = media.Movie("Legends of the Fall",
                   "An epic tale of three brothers and their father living"
                   " in the remote wilderness of 1900s USA and how their "
                   "lives are affected by nature, history, war, and love.",
                   "https://image.tmdb.org/t/p/original/5jjnaCfsC0B0KFPbxV2RMTQYBm.jpg",   # NOQA
                   "https://www.youtube.com/watch?v=ocAeBZdSDWg")

# list of movies in variable movies
movies = [rough_one, blade_runner, alien, trainspotting, hateful_eight,
          legends_of_the_fall]

# generate and open the webpage
fresh_tomatoes.open_movies_page(movies)
