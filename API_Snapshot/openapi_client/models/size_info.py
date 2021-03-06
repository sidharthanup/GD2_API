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


class SizeInfo(object):
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
        'capacity': 'str',
        'used': 'str',
        'free': 'str'
    }

    attribute_map = {
        'capacity': 'capacity',
        'used': 'used',
        'free': 'free'
    }

    def __init__(self, capacity=None, used=None, free=None):  # noqa: E501
        """SizeInfo - a model defined in OpenAPI"""  # noqa: E501

        self._capacity = None
        self._used = None
        self._free = None
        self.discriminator = None

        if capacity is not None:
            self.capacity = capacity
        if used is not None:
            self.used = used
        if free is not None:
            self.free = free

    @property
    def capacity(self):
        """Gets the capacity of this SizeInfo.  # noqa: E501


        :return: The capacity of this SizeInfo.  # noqa: E501
        :rtype: str
        """
        return self._capacity

    @capacity.setter
    def capacity(self, capacity):
        """Sets the capacity of this SizeInfo.


        :param capacity: The capacity of this SizeInfo.  # noqa: E501
        :type: str
        """

        self._capacity = capacity

    @property
    def used(self):
        """Gets the used of this SizeInfo.  # noqa: E501


        :return: The used of this SizeInfo.  # noqa: E501
        :rtype: str
        """
        return self._used

    @used.setter
    def used(self, used):
        """Sets the used of this SizeInfo.


        :param used: The used of this SizeInfo.  # noqa: E501
        :type: str
        """

        self._used = used

    @property
    def free(self):
        """Gets the free of this SizeInfo.  # noqa: E501


        :return: The free of this SizeInfo.  # noqa: E501
        :rtype: str
        """
        return self._free

    @free.setter
    def free(self, free):
        """Sets the free of this SizeInfo.


        :param free: The free of this SizeInfo.  # noqa: E501
        :type: str
        """

        self._free = free

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
        if not isinstance(other, SizeInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
