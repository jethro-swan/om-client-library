# coding: utf-8

"""
    Openmoney API

    Openmoney API  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.currencies_api import CurrenciesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestCurrenciesApi(unittest.TestCase):
    """CurrenciesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.currencies_api.CurrenciesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_currencies_delete(self):
        """Test case for currencies_delete

        Delete a currency  # noqa: E501
        """
        pass

    def test_currencies_get(self):
        """Test case for currencies_get

        Get a currency by its name  # noqa: E501
        """
        pass

    def test_currencies_list(self):
        """Test case for currencies_list

        Get a Listing currencies known by steward.  # noqa: E501
        """
        pass

    def test_currencies_post(self):
        """Test case for currencies_post

        Create a currency  # noqa: E501
        """
        pass

    def test_currencies_put(self):
        """Test case for currencies_put

        Update a Currency  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
