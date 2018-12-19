# -*- coding: utf-8 -*-

"""
    ytelapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Body35(object):

    """Implementation of the 'body_35' model.

    TODO: type model description here.

    Attributes:
        sub_account_sid (string): The SubaccountSid to be activated or
            suspended
        activate (ActivateEnum): 0 to suspend or 1 to activate

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "sub_account_sid":'SubAccountSID',
        "activate":'Activate'
    }

    def __init__(self,
                 sub_account_sid=None,
                 activate=None):
        """Constructor for the Body35 class"""

        # Initialize members of the class
        self.sub_account_sid = sub_account_sid
        self.activate = activate


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
        sub_account_sid = dictionary.get('SubAccountSID')
        activate = dictionary.get('Activate')

        # Return an object of this model
        return cls(sub_account_sid,
                   activate)


