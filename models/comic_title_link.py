class ComicTitleLink:
    """
    Represents a comic title, i.e Amazing X-Men (1995).
    
    Attributes:
    - title (str): The title of the comic.
    - first_issue (str): The first issue of the series.
    - last_issue (str): The last issue of the series.
    - date (str): The date the series began OR range it ran for.
    - publisher (str): The publisher who published the comic.

    Functions:
    - is_tpb
    - is_oneshot

    """
    
    def __init__(self, title, link):
        """ Initializes a comic title with its attributes."""

        self.title = title
        self.link = link
    

    def __repr__(self):
        """ String representation of the object. """

        return f'{{"title":"{self.title}","link": "{self.link}"}}'
    

    def is_tpb(self):
        """
        Checks if a comic series is the trade paper back (TPB).

        Example: 
            title = Wicked and the Divine (2014) - This is not a TPB
            title = Wicked and the Divine Funnies (2018 Image) - This is not a TBP. Likely a one-shot.
            title = Wicked and the Divine TPB (2014-2019 Image) - This is a TPB

        Parameters:
            Self is the only parameter. This function will check the comcic title of the object. 

        Returns:
            bool: True if the comic series is the trade paper back (TPB).
        """

        if 'TPB' in self.title:
            return True
        else:
            return False

