import media
    # importing contents of the file "media.py" in the same folder
    # importing the module named media (media.py file without the .py extention)
import fresh_tomatoes

toy_story = media.Movie("Toy Story",
                        "A story about a boy and his toys that come to life.",
                        "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc")
    # media is the name of the python file
    # Movie is the name of the class in the media file
    # this calls the __init__ function in the Movie class
        # self = the toy_story object in this case.
    # init creates space in memory for the instance being created
    # this instantiates the object toy_story
    # toy_story is an instance of the class Movie

#print(toy_story.storyline)
    # toy_story.storyline is an instance variable

avatar = media.Movie("Avatar",
                    "A marine on an alien planet.",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=d1_JBMrrYw8")

howard_the_duck = media.Movie("Howard the Duck",
                              "A hero from a duck world lands on earth.",
                              "https://upload.wikimedia.org/wikipedia/en/7/7f/Howard_the_Duck_%281986%29.jpg",
                              "https://www.youtube.com/watch?v=M2RNrmCJLtA")
                              

#print(avatar.storyline)
# print(avatar)
    # example output: <media.Movie instance at 0x7fafe22844d0>

#howard_the_duck.show_trailer()

movies = [toy_story, avatar, howard_the_duck]
fresh_tomatoes.open_movies_page(movies)

