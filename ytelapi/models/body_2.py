# -*- coding: utf-8 -*-

"""
    ytelapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Body2(object):

    """Implementation of the 'body_2' model.

    TODO: type model description here.

    Attributes:
        template_id (uuid|string): The unique identifier for a template
            object

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "template_id":'TemplateId'
    }

    def __init__(self,
                 template_id=None):
        """Constructor for the Body2 class"""

        # Initialize members of the class
        self.template_id = template_id


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
        template_id = dictionary.get('TemplateId')

        # Return an object of this model
        return cls(template_id)


