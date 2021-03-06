# coding: utf-8

"""
    Gluster Management API

    Gluster Management APIs  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: you@your-company.com
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six


class Option(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'name': 'str',
        'value': 'str',
        'default_value': 'str',
        'configurable': 'bool',
        'modified': 'bool'
    }

    attribute_map = {
        'name': 'name',
        'value': 'value',
        'default_value': 'default_value',
        'configurable': 'configurable',
        'modified': 'modified'
    }

    def __init__(self, name=None, value=None, default_value=None, configurable=None, modified=None):  # noqa: E501
        """Option - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._value = None
        self._default_value = None
        self._configurable = None
        self._modified = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if value is not None:
            self.value = value
        if default_value is not None:
            self.default_value = default_value
        if configurable is not None:
            self.configurable = configurable
        if modified is not None:
            self.modified = modified

    @property
    def name(self):
        """Gets the name of this Option.  # noqa: E501


        :return: The name of this Option.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Option.


        :param name: The name of this Option.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def value(self):
        """Gets the value of this Option.  # noqa: E501


        :return: The value of this Option.  # noqa: E501
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this Option.


        :param value: The value of this Option.  # noqa: E501
        :type: str
        """

        self._value = value

    @property
    def default_value(self):
        """Gets the default_value of this Option.  # noqa: E501


        :return: The default_value of this Option.  # noqa: E501
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """Sets the default_value of this Option.


        :param default_value: The default_value of this Option.  # noqa: E501
        :type: str
        """

        self._default_value = default_value

    @property
    def configurable(self):
        """Gets the configurable of this Option.  # noqa: E501


        :return: The configurable of this Option.  # noqa: E501
        :rtype: bool
        """
        return self._configurable

    @configurable.setter
    def configurable(self, configurable):
        """Sets the configurable of this Option.


        :param configurable: The configurable of this Option.  # noqa: E501
        :type: bool
        """

        self._configurable = configurable

    @property
    def modified(self):
        """Gets the modified of this Option.  # noqa: E501


        :return: The modified of this Option.  # noqa: E501
        :rtype: bool
        """
        return self._modified

    @modified.setter
    def modified(self, modified):
        """Sets the modified of this Option.


        :param modified: The modified of this Option.  # noqa: E501
        :type: bool
        """

        self._modified = modified

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.openapi_types):
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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Option):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
