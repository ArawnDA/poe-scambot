import re

class SearchParameters():
    """Class that contains search parameters."""
    
    def __init__(self, league, maxprice, minprice, currency, sockets, links, frame_type, corrupted, crafted, regex):
        """Initializes the object with search parameters."""
        self.league = league
        self.maxprice = maxprice
        self.minprice = minprice
        self.sockets = max(sockets, links)
        self.links = links
        self.frame_type = frame_type
        self.corrupted = corrupted
        self.crafted = crafted
        self.price_regex = re.compile('~(b/o|price) ([0-9]+) (' + currency + ')')
        self.regex = re.compile(regex, re.IGNORECASE)