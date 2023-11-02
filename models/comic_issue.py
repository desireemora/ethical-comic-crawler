class ComicIssue:
    """
    Represents a comic issue, i.e Amazing X-Men (1995) #1.
    
    Attributes:
    - title (str): The title of the comic.
    - issue_num (str): The issue number.
    - date (str): The date the issue was puiblished.
    - publisher (str): The publisher who published the comic.

    Functions:
    - isVariant

    """
    
    def __init__(self, title, issue_num, date, publisher):
        """ Initializes an Issue with its attributes."""

        self.title = title
        self.issue_num = issue_num
        self.date = date
        self.publisher = publisher
    

    def __repr__(self):
        """ String representation of the object. """

        return f'{{"title":"{self.title}","issueNumber":"{self.issue_num}", "date":"{self.date}", "publisher":"{self.publisher}"}}'
    

    def isVariant(self):
        """
        Checks if a comic is a variant cover.
        A variant cover is any cover that i not the original first print of the issue.
        Often notated in the issue number along with a letter to notate if it isa variant.
        Example: 
            issue_num = 16A - This is not a variant.
            issue_num = 16C - This is a vairant.
            issue_num = 13 - This is not a variant.

        Parameters:
            Self is the only parameter. This function will check the issue number of the object. 

        Returns:
            bool: True if the issue is a variant and False if it is not.
        """

        if 'A' in self.issue_num or self.issue_num.isnumeric():
            return False
        else:
            return True

