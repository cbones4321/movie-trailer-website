import webbrowser

#Movie Structure
class Movie():
    """ This class provides a way to store movie related information"""

    
    #This is the constructor
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube, director = "", actors = "", year = ""):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.director = director
        self.actors = actors
        self.year = year

    #Method that plays the trailer
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
