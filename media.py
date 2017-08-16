import webbrowser  # importing the webbrowser library


'''Movie class to specify instance variables and methods for movies'''


class Movie():

    """ Constructor method for movie instances, creates instance variables """
    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    '''instance method for youtube movie trailers'''
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
