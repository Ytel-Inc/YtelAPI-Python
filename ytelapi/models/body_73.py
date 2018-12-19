# -*- coding: utf-8 -*-

"""
    ytelapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Body73(object):

    """Implementation of the 'body_73' model.

    TODO: type model description here.

    Attributes:
        number_type (NumberType2Enum): The capability the number supports.
        area_code (string): Specifies the area code for the returned list of
            available numbers. Only available for North American numbers.
        quantity (string): A positive integer that tells how many number you
            want to buy at a time.
        leftover (string): If desired quantity is unavailable purchase what is
            available .

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "number_type":'NumberType',
        "area_code":'AreaCode',
        "quantity":'Quantity',
        "leftover":'Leftover'
    }

    def __init__(self,
                 number_type=None,
                 area_code=None,
                 quantity=None,
                 leftover=None):
        """Constructor for the Body73 class"""

        # Initialize members of the class
        self.number_type = number_type
        self.area_code = area_code
        self.quantity = quantity
        self.leftover = leftover


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
        number_type = dictionary.get('NumberType')
        area_code = dictionary.get('AreaCode')
        quantity = dictionary.get('Quantity')
        leftover = dictionary.get('Leftover')

        # Return an object of this model
        return cls(number_type,
                   area_code,
                   quantity,
                   leftover)


