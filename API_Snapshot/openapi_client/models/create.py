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


class Create(object):
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
        'volname': 'str',
        'snapname': 'str',
        'timestamp': 'bool',
        'description': 'str',
        'force': 'bool'
    }

    attribute_map = {
        'volname': 'volname',
        'snapname': 'snapname',
        'timestamp': 'timestamp',
        'description': 'description',
        'force': 'force'
    }

    def __init__(self, volname=None, snapname=None, timestamp=None, description=None, force=None):  # noqa: E501
        """Create - a model defined in OpenAPI"""  # noqa: E501

        self._volname = None
        self._snapname = None
        self._timestamp = None
        self._description = None
        self._force = None
        self.discriminator = None

        if volname is not None:
            self.volname = volname
        if snapname is not None:
            self.snapname = snapname
        if timestamp is not None:
            self.timestamp = timestamp
        if description is not None:
            self.description = description
        if force is not None:
            self.force = force

    @property
    def volname(self):
        """Gets the volname of this Create.  # noqa: E501


        :return: The volname of this Create.  # noqa: E501
        :rtype: str
        """
        return self._volname

    @volname.setter
    def volname(self, volname):
        """Sets the volname of this Create.


        :param volname: The volname of this Create.  # noqa: E501
        :type: str
        """

        self._volname = volname

    @property
    def snapname(self):
        """Gets the snapname of this Create.  # noqa: E501


        :return: The snapname of this Create.  # noqa: E501
        :rtype: str
        """
        return self._snapname

    @snapname.setter
    def snapname(self, snapname):
        """Sets the snapname of this Create.


        :param snapname: The snapname of this Create.  # noqa: E501
        :type: str
        """

        self._snapname = snapname

    @property
    def timestamp(self):
        """Gets the timestamp of this Create.  # noqa: E501


        :return: The timestamp of this Create.  # noqa: E501
        :rtype: bool
        """
        return self._timestamp

    @timestamp.setter
    def timestamp(self, timestamp):
        """Sets the timestamp of this Create.


        :param timestamp: The timestamp of this Create.  # noqa: E501
        :type: bool
        """

        self._timestamp = timestamp

    @property
    def description(self):
        """Gets the description of this Create.  # noqa: E501


        :return: The description of this Create.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Create.


        :param description: The description of this Create.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def force(self):
        """Gets the force of this Create.  # noqa: E501


        :return: The force of this Create.  # noqa: E501
        :rtype: bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this Create.


        :param force: The force of this Create.  # noqa: E501
        :type: bool
        """

        self._force = force

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
        if not isinstance(other, Create):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
