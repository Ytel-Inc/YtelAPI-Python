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


class SMSControllerTests(ControllerTestBase):

    @classmethod
    def setUpClass(cls):
        super(SMSControllerTests, cls).setUpClass()
        cls.controller = cls.api_client.sms

    # Retrieve a list of Outbound SMS message objects.
    def test_test_list_sms(self):
        # Parameters for the API call
        page = None
        page_size = None
        mfrom = None
        to = None
        date_sent = None

        # Perform the API call through the SDK function
        result = self.controller.create_list_sms(page, page_size, mfrom, to, date_sent)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


    # Retrieve a list of Inbound SMS message objects.
    def test_test_list_inbound_sms(self):
        # Parameters for the API call
        page = None
        page_size = None
        mfrom = None
        to = None
        date_sent = None

        # Perform the API call through the SDK function
        result = self.controller.create_list_inbound_sms(page, page_size, mfrom, to, date_sent)

        # Test response code
        self.assertEquals(self.response_catcher.response.status_code, 200)

        # Test headers
        expected_headers = {}
        expected_headers['content-type'] = 'application/json'

        self.assertTrue(TestHelper.match_headers(expected_headers, self.response_catcher.response.headers))


