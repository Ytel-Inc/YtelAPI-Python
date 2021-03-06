# -*- coding: utf-8 -*-

"""
    ytelapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Body67(object):

    """Implementation of the 'body_67' model.

    TODO: type model description here.

    Attributes:
        shortcode (string): List of valid Dedicated Short Code to your Ytel
            account

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "shortcode":'Shortcode'
    }

    def __init__(self,
                 shortcode=None):
        """Constructor for the Body67 class"""

        # Initialize members of the class
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
        shortcode = dictionary.get('Shortcode')

        # Return an object of this model
        return cls(shortcode)


