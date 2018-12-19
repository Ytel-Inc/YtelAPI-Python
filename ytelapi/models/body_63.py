# -*- coding: utf-8 -*-

"""
    ytelapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""


class Body63(object):

    """Implementation of the 'body_63' model.

    TODO: type model description here.

    Attributes:
        shortcode (string): List of valid shortcode to your Ytel account
        friendly_name (string): User generated name of the shortcode
        callback_url (string): URL that can be requested to receive
            notification when call has ended. A set of default parameters will
            be sent here once the call is finished.
        callback_method (string): Specifies the HTTP method used to request
            the required StatusCallBackUrl once call connects.
        fallback_url (string): URL used if any errors occur during execution
            of InboundXML or at initial request of the required Url provided
            with the POST.
        fallback_url_method (string): Specifies the HTTP method used to
            request the required FallbackUrl once call connects.

    """

    # Create a mapping from Model property names to API property names
    _names = {
        "shortcode":'Shortcode',
        "friendly_name":'FriendlyName',
        "callback_url":'CallbackUrl',
        "callback_method":'CallbackMethod',
        "fallback_url":'FallbackUrl',
        "fallback_url_method":'FallbackUrlMethod'
    }

    def __init__(self,
                 shortcode=None,
                 friendly_name=None,
                 callback_url=None,
                 callback_method=None,
                 fallback_url=None,
                 fallback_url_method=None):
        """Constructor for the Body63 class"""

        # Initialize members of the class
        self.shortcode = shortcode
        self.friendly_name = friendly_name
        self.callback_url = callback_url
        self.callback_method = callback_method
        self.fallback_url = fallback_url
        self.fallback_url_method = fallback_url_method


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
        friendly_name = dictionary.get('FriendlyName')
        callback_url = dictionary.get('CallbackUrl')
        callback_method = dictionary.get('CallbackMethod')
        fallback_url = dictionary.get('FallbackUrl')
        fallback_url_method = dictionary.get('FallbackUrlMethod')

        # Return an object of this model
        return cls(shortcode,
                   friendly_name,
                   callback_url,
                   callback_method,
                   fallback_url,
                   fallback_url_method)

