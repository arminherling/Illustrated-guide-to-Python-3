# Exercise: Create a class that could represent a tweet. If you aren’t familiar with Twitter,
# Wikipedia describes it as:
#    [...] an online news and social networking service where users post and
#    interact with messages, ”tweets”, restricted to 140 characters.


class Tweet:
    max_lenght = 140

    def __init__(self, sender, message):
        self._sender = sender
        self._message = message
        self._id = self._unique_id()
        self._timestamp = "now"


    def _unique_id(self):
        # return a new unique id
        return 42


    def message(self):
        # returns the message
        return self._message


    def sender(self):
        # returns the sender
        return self._sender


    def timestamp(self):
        # returns the creation time
        return self._timestamp
