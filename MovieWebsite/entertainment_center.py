import media
    # importing contents of the file "media.py" in the same folder
    # importing the module named media (media.py file without the .py extention)

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

print(toy_story.storyline)
    # toy_story.storyline is an instance variable

avatar = media.Movie("Avatar",
                    "A marine on an alien planet.",
                    "https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                    "https://www.youtube.com/watch?v=d1_JBMrrYw8",)

print(avatar.storyline)
print(avatar)
    # example output: <media.Movie instance at 0x7fafe22844d0>

