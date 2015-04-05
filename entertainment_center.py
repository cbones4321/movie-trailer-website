'''
Author: Calvin Miller
Date: 4/5/15
About:

This file creates a web page of my favorite movie trailers
'''

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "https://upload.wikimedia.org/wikipedia/en/thumb/1/13/Toy_Story.jpg/220px-Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")

avatar = media.Movie("Avatar",
                     "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/thumb/b/b0/Avatar-Teaser-Poster.jpg/220px-Avatar-Teaser-Poster.jpg",
                     "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

half_baked = media.Movie("Half Baked",
                     "A stoners movie",
                     "http://upload.wikimedia.org/wikipedia/en/thumb/1/10/Half-baked-dvd-cover.jpg/220px-Half-baked-dvd-cover.jpg",
                     "https://www.youtube.com/watch?v=JgkE3xoSHLU")

school_of_rock = media.Movie("School of Rock",
                             "Using rock music to learn",
                             "http://upload.wikimedia.org/wikipedia/en/thumb/1/11/School_of_Rock_Poster.jpg/220px-School_of_Rock_Poster.jpg",
                             "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ratatouille = media.Movie("Ratatouille",
                             "A rat is a chef in Paris",
                             "http://upload.wikimedia.org/wikipedia/en/thumb/5/50/RatatouillePoster.jpg/220px-RatatouillePoster.jpg",
                             "https://www.youtube.com/watch?v=c3sBBRxDAqk")

midnight_in_paris = media.Movie("Midnight in Paris",
                             "Going back in time to meet authors",
                             "http://upload.wikimedia.org/wikipedia/en/thumb/9/9f/Midnight_in_Paris_Poster.jpg/215px-Midnight_in_Paris_Poster.jpg",
                             "https://www.youtube.com/watch?v=FAfR8omt-CY")

hunger_games = media.Movie("Hunger Games",
                             "A really real reality show",
                             "http://upload.wikimedia.org/wikipedia/en/thumb/4/42/HungerGamesPoster.jpg/220px-HungerGamesPoster.jpg",
                             "https://www.youtube.com/watch?v=FovFG3N_RSU")

con_air = media.Movie("Con Air",
                             "A prison escape movie",
                             "http://upload.wikimedia.org/wikipedia/en/thumb/1/1d/Conairinternational.jpg/220px-Conairinternational.jpg",
                             "https://www.youtube.com/watch?v=mzg3ND-ITjU")

bad_boys = media.Movie("Bad Boy's",
                             "A cop movie",
                             "http://upload.wikimedia.org/wikipedia/en/thumb/a/a8/Bad_Boys.jpg/220px-Bad_Boys.jpg",
                             "https://www.youtube.com/watch?v=6GaPkMqAS44")

forty_year_old = media.Movie("40 year old virgin",
                             "Movie about a 40 year old virgin",
                             "http://upload.wikimedia.org/wikipedia/en/thumb/4/43/40-Year-OldVirginMoviePoster.jpg/220px-40-Year-OldVirginMoviePoster.jpg",
                             "https://www.youtube.com/watch?v=YnDeJn-BX5Q")

friday = media.Movie("Friday",
                             "A classic",
                             "http://upload.wikimedia.org/wikipedia/en/thumb/2/27/Fridayposter1995.jpg/215px-Fridayposter1995.jpg",
                             "https://www.youtube.com/watch?v=dxduMVVnrvU")

movies = [toy_story, avatar, half_baked, school_of_rock, ratatouille, midnight_in_paris, hunger_games, con_air, bad_boys, forty_year_old, friday]

fresh_tomatoes.open_movies_page(movies)
