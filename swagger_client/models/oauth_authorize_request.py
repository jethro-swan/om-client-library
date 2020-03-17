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


class OauthAuthorizeRequest(object):
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
        'response_type': 'str',
        'client_id': 'str',
        'redirect_uri': 'str',
        'username': 'str',
        'scopes': 'list[str]'
    }

    attribute_map = {
        'response_type': 'response_type',
        'client_id': 'client_id',
        'redirect_uri': 'redirect_uri',
        'username': 'username',
        'scopes': 'scopes'
    }

    def __init__(self, response_type=None, client_id=None, redirect_uri=None, username=None, scopes=None):  # noqa: E501
        """OauthAuthorizeRequest - a model defined in Swagger"""  # noqa: E501

        self._response_type = None
        self._client_id = None
        self._redirect_uri = None
        self._username = None
        self._scopes = None
        self.discriminator = None

        self.response_type = response_type
        if client_id is not None:
            self.client_id = client_id
        if redirect_uri is not None:
            self.redirect_uri = redirect_uri
        if username is not None:
            self.username = username
        if scopes is not None:
            self.scopes = scopes

    @property
    def response_type(self):
        """Gets the response_type of this OauthAuthorizeRequest.  # noqa: E501

        One of code, password, refresh_token, client_credentials  # noqa: E501

        :return: The response_type of this OauthAuthorizeRequest.  # noqa: E501
        :rtype: str
        """
        return self._response_type

    @response_type.setter
    def response_type(self, response_type):
        """Sets the response_type of this OauthAuthorizeRequest.

        One of code, password, refresh_token, client_credentials  # noqa: E501

        :param response_type: The response_type of this OauthAuthorizeRequest.  # noqa: E501
        :type: str
        """
        if response_type is None:
            raise ValueError("Invalid value for `response_type`, must not be `None`")  # noqa: E501
        if response_type is not None and len(response_type) > 20:
            raise ValueError("Invalid value for `response_type`, length must be less than or equal to `20`")  # noqa: E501
        if response_type is not None and not re.search(r'^[A-Za-z_]+$', response_type):  # noqa: E501
            raise ValueError(r"Invalid value for `response_type`, must be a follow pattern or equal to `/^[A-Za-z_]+$/`")  # noqa: E501

        self._response_type = response_type

    @property
    def client_id(self):
        """Gets the client_id of this OauthAuthorizeRequest.  # noqa: E501


        :return: The client_id of this OauthAuthorizeRequest.  # noqa: E501
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """Sets the client_id of this OauthAuthorizeRequest.


        :param client_id: The client_id of this OauthAuthorizeRequest.  # noqa: E501
        :type: str
        """
        if client_id is not None and len(client_id) > 800:
            raise ValueError("Invalid value for `client_id`, length must be less than or equal to `800`")  # noqa: E501
        if client_id is not None and len(client_id) < 266:
            raise ValueError("Invalid value for `client_id`, length must be greater than or equal to `266`")  # noqa: E501
        if client_id is not None and not re.search(r'^-----BEGIN PUBLIC KEY-----[A-Za-z0-9\\\\\\s\/=+]+-----END PUBLIC KEY-----$', client_id):  # noqa: E501
            raise ValueError(r"Invalid value for `client_id`, must be a follow pattern or equal to `/^-----BEGIN PUBLIC KEY-----[A-Za-z0-9\\\\\\s\/=+]+-----END PUBLIC KEY-----$/`")  # noqa: E501

        self._client_id = client_id

    @property
    def redirect_uri(self):
        """Gets the redirect_uri of this OauthAuthorizeRequest.  # noqa: E501

        A uri to redirect steward after authorization  # noqa: E501

        :return: The redirect_uri of this OauthAuthorizeRequest.  # noqa: E501
        :rtype: str
        """
        return self._redirect_uri

    @redirect_uri.setter
    def redirect_uri(self, redirect_uri):
        """Sets the redirect_uri of this OauthAuthorizeRequest.

        A uri to redirect steward after authorization  # noqa: E501

        :param redirect_uri: The redirect_uri of this OauthAuthorizeRequest.  # noqa: E501
        :type: str
        """
        if redirect_uri is not None and len(redirect_uri) > 512:
            raise ValueError("Invalid value for `redirect_uri`, length must be less than or equal to `512`")  # noqa: E501

        self._redirect_uri = redirect_uri

    @property
    def username(self):
        """Gets the username of this OauthAuthorizeRequest.  # noqa: E501

        stewardname of user  # noqa: E501

        :return: The username of this OauthAuthorizeRequest.  # noqa: E501
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """Sets the username of this OauthAuthorizeRequest.

        stewardname of user  # noqa: E501

        :param username: The username of this OauthAuthorizeRequest.  # noqa: E501
        :type: str
        """
        if username is not None and not re.search(r'^[A-Za-z_]+$', username):  # noqa: E501
            raise ValueError(r"Invalid value for `username`, must be a follow pattern or equal to `/^[A-Za-z_]+$/`")  # noqa: E501

        self._username = username

    @property
    def scopes(self):
        """Gets the scopes of this OauthAuthorizeRequest.  # noqa: E501

        A comma separated list of scopes. If not provided, scope defaults to an empty list of scopes for stewards that don’t have a valid token for the app. For stewards who do already have a valid token for the app, the steward won’t be shown the OAuth authorization page with the list of scopes. Instead, this step of the flow will automatically complete with the same scopes that were used last time the steward completed the flow.  # noqa: E501

        :return: The scopes of this OauthAuthorizeRequest.  # noqa: E501
        :rtype: list[str]
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """Sets the scopes of this OauthAuthorizeRequest.

        A comma separated list of scopes. If not provided, scope defaults to an empty list of scopes for stewards that don’t have a valid token for the app. For stewards who do already have a valid token for the app, the steward won’t be shown the OAuth authorization page with the list of scopes. Instead, this step of the flow will automatically complete with the same scopes that were used last time the steward completed the flow.  # noqa: E501

        :param scopes: The scopes of this OauthAuthorizeRequest.  # noqa: E501
        :type: list[str]
        """

        self._scopes = scopes

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
        if issubclass(OauthAuthorizeRequest, dict):
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
        if not isinstance(other, OauthAuthorizeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
