# -*- coding: utf-8 -*-

"""
    ytelapi

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

import jsonpickle
import dateutil.parser
from .controller_test_base import ControllerTestBase
from ..test_helper import TestHelper
from ytelapi.api_helper import APIHelper


class UsageControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(UsageControllerTests, cls).setUpClass()
        cls.controller = cls.api_client.usage

    # Retrieve usage metrics regarding your Ytel account. The results includes inbound/outbound voice calls and inbound/outbound SMS messages as well as carrier lookup requests.
    def test_test_list_usage(self):
        # Parameters for the API call
        product_code = None
        start_date = None
        end_date = None
        include_sub_accounts = None

        # Perform the API call through the SDK function
        result = self.controller.create_list_usage(product_code, start_date, end_date, include_sub_accounts)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


