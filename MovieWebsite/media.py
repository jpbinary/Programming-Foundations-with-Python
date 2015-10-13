import webbrowser

class Movie():
    # best practice is to keep class definition in one file and call class from main file
    # __init__ is also known as a constructor, since it constructs space in memory for the new object
    # __init__ is a reserved word in python
    # self refers to the instance being created
    # self is not a python keyword, it is just a convention, and any other word will also work, such as this_instance
    def __init__(self, movie_title,
                 movie_storyline,
                 movie_poster_image_url,
                 movie_trailer_on_youtube):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image_url
        self.trailer_youtube_url = movie_trailer_on_youtube

    # a function that is defined inside a class is referred to as an 'instance method'
    # the first argument for each instance method should be 'self' 
    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
        
