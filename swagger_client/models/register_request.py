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


class RegisterRequest(object):
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
        'stewardname': 'str',
        'password': 'str',
        'public_key': 'str',
        'email': 'str',
        'email_notifications': 'bool'
    }

    attribute_map = {
        'stewardname': 'stewardname',
        'password': 'password',
        'public_key': 'publicKey',
        'email': 'email',
        'email_notifications': 'email_notifications'
    }

    def __init__(self, stewardname=None, password=None, public_key=None, email=None, email_notifications=None):  # noqa: E501
        """RegisterRequest - a model defined in Swagger"""  # noqa: E501

        self._stewardname = None
        self._password = None
        self._public_key = None
        self._email = None
        self._email_notifications = None
        self.discriminator = None

        self.stewardname = stewardname
        self.password = password
        if public_key is not None:
            self.public_key = public_key
        if email is not None:
            self.email = email
        if email_notifications is not None:
            self.email_notifications = email_notifications

    @property
    def stewardname(self):
        """Gets the stewardname of this RegisterRequest.  # noqa: E501

        Stewards name  # noqa: E501

        :return: The stewardname of this RegisterRequest.  # noqa: E501
        :rtype: str
        """
        return self._stewardname

    @stewardname.setter
    def stewardname(self, stewardname):
        """Sets the stewardname of this RegisterRequest.

        Stewards name  # noqa: E501

        :param stewardname: The stewardname of this RegisterRequest.  # noqa: E501
        :type: str
        """
        if stewardname is None:
            raise ValueError("Invalid value for `stewardname`, must not be `None`")  # noqa: E501
        if stewardname is not None and len(stewardname) > 255:
            raise ValueError("Invalid value for `stewardname`, length must be less than or equal to `255`")  # noqa: E501
        if stewardname is not None and not re.search(r'^[A-Za-z0-9_.-]+$', stewardname):  # noqa: E501
            raise ValueError(r"Invalid value for `stewardname`, must be a follow pattern or equal to `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501

        self._stewardname = stewardname

    @property
    def password(self):
        """Gets the password of this RegisterRequest.  # noqa: E501

        Stewards password  # noqa: E501

        :return: The password of this RegisterRequest.  # noqa: E501
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """Sets the password of this RegisterRequest.

        Stewards password  # noqa: E501

        :param password: The password of this RegisterRequest.  # noqa: E501
        :type: str
        """
        if password is None:
            raise ValueError("Invalid value for `password`, must not be `None`")  # noqa: E501
        if password is not None and len(password) > 1024:
            raise ValueError("Invalid value for `password`, length must be less than or equal to `1024`")  # noqa: E501
        if password is not None and len(password) < 4:
            raise ValueError("Invalid value for `password`, length must be greater than or equal to `4`")  # noqa: E501

        self._password = password

    @property
    def public_key(self):
        """Gets the public_key of this RegisterRequest.  # noqa: E501

        Stewards 1024bit - 4096bit RSA public key. command: openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:4096 ,openssl rsa -pubout -in private_key.pem -out public_key.pem , you can deterministically generate an RSA key from a passphrase http://crypto.stackexchange.com/questions/24514/deterministically-generate-a-rsa-public-private-key-pair-from-a-passphrase-with you can also use this service to generate a key online: http://travistidwell.com/blog/2013/09/06/an-online-rsa-public-and-private-key-generator/  # noqa: E501

        :return: The public_key of this RegisterRequest.  # noqa: E501
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this RegisterRequest.

        Stewards 1024bit - 4096bit RSA public key. command: openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:4096 ,openssl rsa -pubout -in private_key.pem -out public_key.pem , you can deterministically generate an RSA key from a passphrase http://crypto.stackexchange.com/questions/24514/deterministically-generate-a-rsa-public-private-key-pair-from-a-passphrase-with you can also use this service to generate a key online: http://travistidwell.com/blog/2013/09/06/an-online-rsa-public-and-private-key-generator/  # noqa: E501

        :param public_key: The public_key of this RegisterRequest.  # noqa: E501
        :type: str
        """
        if public_key is not None and len(public_key) > 800:
            raise ValueError("Invalid value for `public_key`, length must be less than or equal to `800`")  # noqa: E501
        if public_key is not None and len(public_key) < 266:
            raise ValueError("Invalid value for `public_key`, length must be greater than or equal to `266`")  # noqa: E501
        if public_key is not None and not re.search(r'^-----BEGIN PUBLIC KEY-----[A-Za-z0-9\\\\\\s\/=+]+-----END PUBLIC KEY-----$', public_key):  # noqa: E501
            raise ValueError(r"Invalid value for `public_key`, must be a follow pattern or equal to `/^-----BEGIN PUBLIC KEY-----[A-Za-z0-9\\\\\\s\/=+]+-----END PUBLIC KEY-----$/`")  # noqa: E501

        self._public_key = public_key

    @property
    def email(self):
        """Gets the email of this RegisterRequest.  # noqa: E501

        Stewards email address  # noqa: E501

        :return: The email of this RegisterRequest.  # noqa: E501
        :rtype: str
        """
        return self._email

    @email.setter
    def email(self, email):
        """Sets the email of this RegisterRequest.

        Stewards email address  # noqa: E501

        :param email: The email of this RegisterRequest.  # noqa: E501
        :type: str
        """
        if email is not None and len(email) > 255:
            raise ValueError("Invalid value for `email`, length must be less than or equal to `255`")  # noqa: E501
        if email is not None and not re.search(r'^([\\w-]+(?:[\\.\\+][\\w-]+)*)@((?:[\\w-]+\\.)*\\w[\\w-]{0,66})\\.([a-z]{2,6}(?:\\.[a-z]{2})?)$', email):  # noqa: E501
            raise ValueError(r"Invalid value for `email`, must be a follow pattern or equal to `/^([\\w-]+(?:[\\.\\+][\\w-]+)*)@((?:[\\w-]+\\.)*\\w[\\w-]{0,66})\\.([a-z]{2,6}(?:\\.[a-z]{2})?)$/`")  # noqa: E501

        self._email = email

    @property
    def email_notifications(self):
        """Gets the email_notifications of this RegisterRequest.  # noqa: E501

        Does steward wish to receive email notifications  # noqa: E501

        :return: The email_notifications of this RegisterRequest.  # noqa: E501
        :rtype: bool
        """
        return self._email_notifications

    @email_notifications.setter
    def email_notifications(self, email_notifications):
        """Sets the email_notifications of this RegisterRequest.

        Does steward wish to receive email notifications  # noqa: E501

        :param email_notifications: The email_notifications of this RegisterRequest.  # noqa: E501
        :type: bool
        """

        self._email_notifications = email_notifications

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
        if issubclass(RegisterRequest, dict):
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
        if not isinstance(other, RegisterRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other