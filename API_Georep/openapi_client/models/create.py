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
        'mastervol': 'str',
        'remoteuser': 'str',
        'remotehosts': 'list[object]',
        'remotevol': 'str',
        'force': 'Bool'
    }

    attribute_map = {
        'mastervol': 'mastervol',
        'remoteuser': 'remoteuser',
        'remotehosts': 'remotehosts',
        'remotevol': 'remotevol',
        'force': 'force'
    }

    def __init__(self, mastervol=None, remoteuser=None, remotehosts=None, remotevol=None, force=None):  # noqa: E501
        """Create - a model defined in OpenAPI"""  # noqa: E501

        self._mastervol = None
        self._remoteuser = None
        self._remotehosts = None
        self._remotevol = None
        self._force = None
        self.discriminator = None

        if mastervol is not None:
            self.mastervol = mastervol
        if remoteuser is not None:
            self.remoteuser = remoteuser
        if remotehosts is not None:
            self.remotehosts = remotehosts
        if remotevol is not None:
            self.remotevol = remotevol
        if force is not None:
            self.force = force

    @property
    def mastervol(self):
        """Gets the mastervol of this Create.  # noqa: E501


        :return: The mastervol of this Create.  # noqa: E501
        :rtype: str
        """
        return self._mastervol

    @mastervol.setter
    def mastervol(self, mastervol):
        """Sets the mastervol of this Create.


        :param mastervol: The mastervol of this Create.  # noqa: E501
        :type: str
        """

        self._mastervol = mastervol

    @property
    def remoteuser(self):
        """Gets the remoteuser of this Create.  # noqa: E501


        :return: The remoteuser of this Create.  # noqa: E501
        :rtype: str
        """
        return self._remoteuser

    @remoteuser.setter
    def remoteuser(self, remoteuser):
        """Sets the remoteuser of this Create.


        :param remoteuser: The remoteuser of this Create.  # noqa: E501
        :type: str
        """

        self._remoteuser = remoteuser

    @property
    def remotehosts(self):
        """Gets the remotehosts of this Create.  # noqa: E501


        :return: The remotehosts of this Create.  # noqa: E501
        :rtype: list[object]
        """
        return self._remotehosts

    @remotehosts.setter
    def remotehosts(self, remotehosts):
        """Sets the remotehosts of this Create.


        :param remotehosts: The remotehosts of this Create.  # noqa: E501
        :type: list[object]
        """

        self._remotehosts = remotehosts

    @property
    def remotevol(self):
        """Gets the remotevol of this Create.  # noqa: E501


        :return: The remotevol of this Create.  # noqa: E501
        :rtype: str
        """
        return self._remotevol

    @remotevol.setter
    def remotevol(self, remotevol):
        """Sets the remotevol of this Create.


        :param remotevol: The remotevol of this Create.  # noqa: E501
        :type: str
        """

        self._remotevol = remotevol

    @property
    def force(self):
        """Gets the force of this Create.  # noqa: E501


        :return: The force of this Create.  # noqa: E501
        :rtype: Bool
        """
        return self._force

    @force.setter
    def force(self, force):
        """Sets the force of this Create.


        :param force: The force of this Create.  # noqa: E501
        :type: Bool
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