class ComicTitle:
    """
    Represents a comic title, i.e Amazing X-Men (1995).
    
    Attributes:
    - title (str): The title of the comic.
    - first_issue (str): The first issue of the series.
    - last_issue (str): The last issue of the series.
    - date (str): The date the series began OR range it ran for.
    - publisher (str): The publisher who published the comic.

    Functions:
    - isVariant

    """
    
    def __init__(self, title, first_issue, last_issue, date, publisher):
        """ Initializes an Issue with its attributes."""

        self.title = title
        self.first_issue = first_issue
        self.last_issue = last_issue
        self.date = date
        self.publisher = publisher
    

    def __repr__(self):
        """ String representation of the object. """

        return f'{{"title":"{self.title}","first_issue": "{first_issue}", "last_issue":"{self.isslast_issuee_num}", "date":"{self.date}", "publisher":"{self.publisher}"}}'
    

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

def is_oneshot(self):
        """
        Checks if a comic is a oneshot.
        A oneshot is usually a special and contains a slightly different than the running series title and is usually an issue labeled #0 or #1.
        
        Example: 
            title = Wicked and the Divine (2014); first_issue = #1; last_issue= #45 - regular running series.
            title = Wicked and the Divine Funnies (2018 Image); first_issue = #1; last_issue= None - Does not dontain 'TBP' and only has 1 issue. This is a one-shot.
            title = Wicked and the Divine TPB (2014-2019 Image); first_issue = #1; last_issue= #9 - This is a TPB.

        Parameters:
            Self is the only parameter. This function will check the comcic title, and last_issue of the object. 

        Returns:
            bool: True if the comic series is the trade paper back (TPB).
        """

        if 'TPB' in self.title:
            return False
        elif self.last_issue is None:
            return True
        else:
            return False

