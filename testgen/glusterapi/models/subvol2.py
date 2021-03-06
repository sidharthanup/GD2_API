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


class Subvol2(object):
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
        'type': 'str',
        'replica_count': 'int',
        'arbiter_count': 'int',
        'bricks': 'list[object]'
    }

    attribute_map = {
        'name': 'name',
        'type': 'type',
        'replica_count': 'replica-count',
        'arbiter_count': 'arbiter-count',
        'bricks': 'bricks'
    }

    def __init__(self, name=None, type=None, replica_count=None, arbiter_count=None, bricks=None):  # noqa: E501
        """Subvol2 - a model defined in OpenAPI"""  # noqa: E501

        self._name = None
        self._type = None
        self._replica_count = None
        self._arbiter_count = None
        self._bricks = None
        self.discriminator = None

        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if replica_count is not None:
            self.replica_count = replica_count
        if arbiter_count is not None:
            self.arbiter_count = arbiter_count
        if bricks is not None:
            self.bricks = bricks

    @property
    def name(self):
        """Gets the name of this Subvol2.  # noqa: E501


        :return: The name of this Subvol2.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Subvol2.


        :param name: The name of this Subvol2.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this Subvol2.  # noqa: E501


        :return: The type of this Subvol2.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Subvol2.


        :param type: The type of this Subvol2.  # noqa: E501
        :type: str
        """

        self._type = type

    @property
    def replica_count(self):
        """Gets the replica_count of this Subvol2.  # noqa: E501


        :return: The replica_count of this Subvol2.  # noqa: E501
        :rtype: int
        """
        return self._replica_count

    @replica_count.setter
    def replica_count(self, replica_count):
        """Sets the replica_count of this Subvol2.


        :param replica_count: The replica_count of this Subvol2.  # noqa: E501
        :type: int
        """

        self._replica_count = replica_count

    @property
    def arbiter_count(self):
        """Gets the arbiter_count of this Subvol2.  # noqa: E501


        :return: The arbiter_count of this Subvol2.  # noqa: E501
        :rtype: int
        """
        return self._arbiter_count

    @arbiter_count.setter
    def arbiter_count(self, arbiter_count):
        """Sets the arbiter_count of this Subvol2.


        :param arbiter_count: The arbiter_count of this Subvol2.  # noqa: E501
        :type: int
        """

        self._arbiter_count = arbiter_count

    @property
    def bricks(self):
        """Gets the bricks of this Subvol2.  # noqa: E501


        :return: The bricks of this Subvol2.  # noqa: E501
        :rtype: list[object]
        """
        return self._bricks

    @bricks.setter
    def bricks(self, bricks):
        """Sets the bricks of this Subvol2.


        :param bricks: The bricks of this Subvol2.  # noqa: E501
        :type: list[object]
        """

        self._bricks = bricks

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
        if not isinstance(other, Subvol2):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
