"""Practice writing a class. (object oriented thingy)."""

# create class
class Profile:
    # create attributes
    username: str
    private: bool

    # create contructor
    def __init__(self, username_input: str):
        """Create new profile object."""
        self.username = username_input
        self.private = True

    # new method: function that belongs to a class
    def tweet(self, msg: str) -> None:
        """If profile is public, print msg."""
        if not self.private:
            print(msg)


# Instantiation
user1: Profile = Profile("110_rulez") #calls __init__(), sets username to "110_rulez"
user1.private = False #sets private attribute to False 
msg: str = "OOP is cool!" #define msg

user1.tweet(msg) #calls tweet method 
