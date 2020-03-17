# coding: utf-8

"""
    Openmoney API

    Openmoney API  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class CurrenciesGet(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'currency': 'str',
        'currency_namespace': 'str',
        'created': 'int',
        'created_by': 'str',
        'modifications': 'list[Modification]',
        'stewards': 'list[str]'
    }

    attribute_map = {
        'currency': 'currency',
        'currency_namespace': 'currency_namespace',
        'created': 'created',
        'created_by': 'created_by',
        'modifications': 'modifications',
        'stewards': 'stewards'
    }

    def __init__(self, currency=None, currency_namespace=None, created=None, created_by=None, modifications=None, stewards=None):  # noqa: E501
        """CurrenciesGet - a model defined in Swagger"""  # noqa: E501

        self._currency = None
        self._currency_namespace = None
        self._created = None
        self._created_by = None
        self._modifications = None
        self._stewards = None
        self.discriminator = None

        self.currency = currency
        self.currency_namespace = currency_namespace
        if created is not None:
            self.created = created
        if created_by is not None:
            self.created_by = created_by
        if modifications is not None:
            self.modifications = modifications
        self.stewards = stewards

    @property
    def currency(self):
        """Gets the currency of this CurrenciesGet.  # noqa: E501


        :return: The currency of this CurrenciesGet.  # noqa: E501
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this CurrenciesGet.


        :param currency: The currency of this CurrenciesGet.  # noqa: E501
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")  # noqa: E501
        if currency is not None and len(currency) > 255:
            raise ValueError("Invalid value for `currency`, length must be less than or equal to `255`")  # noqa: E501
        if currency is not None and not re.search(r'^[A-Za-z0-9_-]+$', currency):  # noqa: E501
            raise ValueError(r"Invalid value for `currency`, must be a follow pattern or equal to `/^[A-Za-z0-9_-]+$/`")  # noqa: E501

        self._currency = currency

    @property
    def currency_namespace(self):
        """Gets the currency_namespace of this CurrenciesGet.  # noqa: E501


        :return: The currency_namespace of this CurrenciesGet.  # noqa: E501
        :rtype: str
        """
        return self._currency_namespace

    @currency_namespace.setter
    def currency_namespace(self, currency_namespace):
        """Sets the currency_namespace of this CurrenciesGet.


        :param currency_namespace: The currency_namespace of this CurrenciesGet.  # noqa: E501
        :type: str
        """
        if currency_namespace is None:
            raise ValueError("Invalid value for `currency_namespace`, must not be `None`")  # noqa: E501
        if currency_namespace is not None and len(currency_namespace) > 255:
            raise ValueError("Invalid value for `currency_namespace`, length must be less than or equal to `255`")  # noqa: E501
        if currency_namespace is not None and not re.search(r'^[A-Za-z0-9_.-]*$', currency_namespace):  # noqa: E501
            raise ValueError(r"Invalid value for `currency_namespace`, must be a follow pattern or equal to `/^[A-Za-z0-9_.-]*$/`")  # noqa: E501

        self._currency_namespace = currency_namespace

    @property
    def created(self):
        """Gets the created of this CurrenciesGet.  # noqa: E501

        timestamp in milliseconds since epoch  # noqa: E501

        :return: The created of this CurrenciesGet.  # noqa: E501
        :rtype: int
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this CurrenciesGet.

        timestamp in milliseconds since epoch  # noqa: E501

        :param created: The created of this CurrenciesGet.  # noqa: E501
        :type: int
        """

        self._created = created

    @property
    def created_by(self):
        """Gets the created_by of this CurrenciesGet.  # noqa: E501

        stewardname of steward who made change  # noqa: E501

        :return: The created_by of this CurrenciesGet.  # noqa: E501
        :rtype: str
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this CurrenciesGet.

        stewardname of steward who made change  # noqa: E501

        :param created_by: The created_by of this CurrenciesGet.  # noqa: E501
        :type: str
        """

        self._created_by = created_by

    @property
    def modifications(self):
        """Gets the modifications of this CurrenciesGet.  # noqa: E501


        :return: The modifications of this CurrenciesGet.  # noqa: E501
        :rtype: list[Modification]
        """
        return self._modifications

    @modifications.setter
    def modifications(self, modifications):
        """Sets the modifications of this CurrenciesGet.


        :param modifications: The modifications of this CurrenciesGet.  # noqa: E501
        :type: list[Modification]
        """

        self._modifications = modifications

    @property
    def stewards(self):
        """Gets the stewards of this CurrenciesGet.  # noqa: E501


        :return: The stewards of this CurrenciesGet.  # noqa: E501
        :rtype: list[str]
        """
        return self._stewards

    @stewards.setter
    def stewards(self, stewards):
        """Sets the stewards of this CurrenciesGet.


        :param stewards: The stewards of this CurrenciesGet.  # noqa: E501
        :type: list[str]
        """
        if stewards is None:
            raise ValueError("Invalid value for `stewards`, must not be `None`")  # noqa: E501

        self._stewards = stewards

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(CurrenciesGet, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, CurrenciesGet):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
