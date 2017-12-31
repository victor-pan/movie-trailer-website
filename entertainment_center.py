import media
import fresh_tomatoes

# Make a lot of movies
toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",    # NOQA
                        "https://www.youtube.com/watch?v=4KPTXpQehio")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",    # NOQA
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

school_of_rock = media.Movie("School of Rock",
              "Using rock music to learn",
              "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",    # NOQA
              "https://www.youtube.com/watch?v=3PsUJFEBC74")

ratatouille = media.Movie("Ratatouille",
              "A rat chef in Paris",
              "https://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",    # NOQA
              "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
              "Going back in time to meet authors",
              "https://upload.wikimedia.org/wikipedia/en/9/9f/Midnight_in_Paris_Poster.jpg",    # NOQA
              "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games",
              "A really real reality show",
              "https://upload.wikimedia.org/wikipedia/en/4/42/HungerGamesPoster.jpg",    # NOQA
              "https://www.youtube.com/watch?v=4S9a5V9ODuY")

dunkirk = media.Movie("Dunkirk",
                "War story",
                "https://upload.wikimedia.org/wikipedia/en/1/15/Dunkirk_Film_poster.jpg",    # NOQA
                "https://www.youtube.com/watch?v=F-eMt3SrfFU")

good_will_hunting = media.Movie("Good Will Hunting",
              "A young man learns to accept himself",
              "https://upload.wikimedia.org/wikipedia/en/b/b8/Good_Will_Hunting_theatrical_poster.jpg",    # NOQA
              "https://www.youtube.com/watch?v=QSMvyuEeIyw")

the_matrix = media.Movie("The Matrix",
              "Discovering reality",
              "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",    # NOQA
              "https://www.youtube.com/watch?v=m8e-FF8MsqU")

finding_forrester = media.Movie("Finding Forrester",
              "Inspirational movie",
              "https://upload.wikimedia.org/wikipedia/en/1/16/Finding_forrester.jpg",    # NOQA
              "https://www.youtube.com/watch?v=8QGCBH_2Dck")

space_odyssey = media.Movie("2001: A Space Odyssey",
              "The future of mankind",
              "https://upload.wikimedia.org/wikipedia/en/a/a7/2001_A_Space_Odyssey_%281968%29_theatrical_poster_variant.jpg",  # NOQA
              "https://www.youtube.com/watch?v=lfF0vxKZRhc")

# Pass them to our webpage
movies = [toy_story, avatar, school_of_rock, ratatouille, midnight_in_paris,
          hunger_games, dunkirk, good_will_hunting, the_matrix,
          finding_forrester, space_odyssey]

fresh_tomatoes.open_movies_page(movies)
