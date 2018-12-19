# -*- coding: utf-8 -*-

"""
    ytelapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Body60(object):

    """Implementation of the 'body_60' model.

    TODO: type model description here.

    Attributes:
        page (int): The page count to retrieve from the total results in the
            collection. Page indexing starts at 1.
        pagesize (int): Number of individual resources listed in the response
            per page
        keyword (string): Only list keywords of keyword
        shortcode (int): Only list keywords of shortcode

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "page":'page',
        "pagesize":'pagesize',
        "keyword":'Keyword',
        "shortcode":'Shortcode'
    }

    def __init__(self,
                 page=None,
                 pagesize=None,
                 keyword=None,
                 shortcode=None):
        """Constructor for the Body60 class"""

        # Initialize members of the class
        self.page = page
        self.pagesize = pagesize
        self.keyword = keyword
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
        keyword = dictionary.get('Keyword')
        shortcode = dictionary.get('Shortcode')

        # Return an object of this model
        return cls(page,
                   pagesize,
                   keyword,
                   shortcode)

