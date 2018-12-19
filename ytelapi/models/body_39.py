# -*- coding: utf-8 -*-

"""
    ytelapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Body39(object):

    """Implementation of the 'body_39' model.

    TODO: type model description here.

    Attributes:
        page (int): The page count to retrieve from the total results in the
            collection. Page indexing starts at 1.
        pagesize (int): Number of individual resources listed in the response
            per page
        mfrom (string): From Number to Inbound ShortCode
        shortcode (string): Only list messages sent to this Short Code

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "page":'page',
        "pagesize":'pagesize',
        "mfrom":'from',
        "shortcode":'Shortcode'
    }

    def __init__(self,
                 page=None,
                 pagesize=None,
                 mfrom=None,
                 shortcode=None):
        """Constructor for the Body39 class"""

        # Initialize members of the class
        self.page = page
        self.pagesize = pagesize
        self.mfrom = mfrom
        self.shortcode = shortcode


    @classmethod
    def from_dictionary(cls,
                        dictionary):
        """Creates an instance of this model from a dictionary

        Args:
            dictionary (dictionary): A dictionary representation of the object as
            obtained from the deserialization of the server's response. The keys
            MUST match property names in the API description.

        Returns:
            object: An instance of this structure class.

        """
        if dictionary is None:
            return None

        # Extract variables from the dictionary
        page = dictionary.get('page')
        pagesize = dictionary.get('pagesize')
        mfrom = dictionary.get('from')
        shortcode = dictionary.get('Shortcode')

        # Return an object of this model
        return cls(page,
                   pagesize,
                   mfrom,
                   shortcode)


