# -*- coding: utf-8 -*-

"""
    ytelapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Body36(object):

    """Implementation of the 'body_36' model.

    TODO: type model description here.

    Attributes:
        date (string): Filter account information based on date.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "date":'Date'
    }

    def __init__(self,
                 date=None):
        """Constructor for the Body36 class"""

        # Initialize members of the class
        self.date = date


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
        date = dictionary.get('Date')

        # Return an object of this model
        return cls(date)

