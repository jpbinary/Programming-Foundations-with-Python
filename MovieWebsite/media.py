class Movie():
    # best practice to keep class definition in one file and call class from main file
    # __init__ is also known as a constructor, since it constructs space in memory for the new object
    def __init__(self, movie_title,
                 movie_storyline,
                 movie_poster_image_url,
                 movie_trailer_on_youtube):
        # __init__ is a reserved word in python
        # self refers to the instance being created
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = movie_poster_image_url
        self.trailer_youtube_url = movie_trailer_on_youtube
    
