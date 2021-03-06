# -*- coding: utf-8 -*-

"""
    ytelapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Body49(object):

    """Implementation of the 'body_49' model.

    TODO: type model description here.

    Attributes:
        product_code (ProductCodeEnum): Filter usage results by product type.
        start_date (string): Filter usage objects by start date.
        end_date (string): Filter usage objects by end date.
        include_sub_accounts (string): Will include all subaccount usage data

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "product_code":'ProductCode',
        "start_date":'startDate',
        "end_date":'endDate',
        "include_sub_accounts":'IncludeSubAccounts'
    }

    def __init__(self,
                 product_code=None,
                 start_date=None,
                 end_date=None,
                 include_sub_accounts=None):
        """Constructor for the Body49 class"""

        # Initialize members of the class
        self.product_code = product_code
        self.start_date = start_date
        self.end_date = end_date
        self.include_sub_accounts = include_sub_accounts


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
        product_code = dictionary.get('ProductCode')
        start_date = dictionary.get('startDate')
        end_date = dictionary.get('endDate')
        include_sub_accounts = dictionary.get('IncludeSubAccounts')

        # Return an object of this model
        return cls(product_code,
                   start_date,
                   end_date,
                   include_sub_accounts)


