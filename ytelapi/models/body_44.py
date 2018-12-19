# -*- coding: utf-8 -*-

"""
    ytelapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Body44(object):

    """Implementation of the 'body_44' model.

    TODO: type model description here.

    Attributes:
        email (string): A valid email address that is to be remove from the
            invalid email list.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "email":'Email'
    }

    def __init__(self,
                 email=None):
        """Constructor for the Body44 class"""

        # Initialize members of the class
        self.email = email


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
        email = dictionary.get('Email')

        # Return an object of this model
        return cls(email)


