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


class CreateResp(object):
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
        'snapinfo': 'Volume',
        'parentname': 'str',
        'description': 'str',
        'created_at': 'str'
    }

    attribute_map = {
        'snapinfo': 'snapinfo',
        'parentname': 'parentname',
        'description': 'description',
        'created_at': 'created-at'
    }

    def __init__(self, snapinfo=None, parentname=None, description=None, created_at=None):  # noqa: E501
        """CreateResp - a model defined in OpenAPI"""  # noqa: E501

        self._snapinfo = None
        self._parentname = None
        self._description = None
        self._created_at = None
        self.discriminator = None

        if snapinfo is not None:
            self.snapinfo = snapinfo
        if parentname is not None:
            self.parentname = parentname
        if description is not None:
            self.description = description
        if created_at is not None:
            self.created_at = created_at

    @property
    def snapinfo(self):
        """Gets the snapinfo of this CreateResp.  # noqa: E501


        :return: The snapinfo of this CreateResp.  # noqa: E501
        :rtype: Volume
        """
        return self._snapinfo

    @snapinfo.setter
    def snapinfo(self, snapinfo):
        """Sets the snapinfo of this CreateResp.


        :param snapinfo: The snapinfo of this CreateResp.  # noqa: E501
        :type: Volume
        """

        self._snapinfo = snapinfo

    @property
    def parentname(self):
        """Gets the parentname of this CreateResp.  # noqa: E501


        :return: The parentname of this CreateResp.  # noqa: E501
        :rtype: str
        """
        return self._parentname

    @parentname.setter
    def parentname(self, parentname):
        """Sets the parentname of this CreateResp.


        :param parentname: The parentname of this CreateResp.  # noqa: E501
        :type: str
        """

        self._parentname = parentname

    @property
    def description(self):
        """Gets the description of this CreateResp.  # noqa: E501


        :return: The description of this CreateResp.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CreateResp.


        :param description: The description of this CreateResp.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def created_at(self):
        """Gets the created_at of this CreateResp.  # noqa: E501


        :return: The created_at of this CreateResp.  # noqa: E501
        :rtype: str
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this CreateResp.


        :param created_at: The created_at of this CreateResp.  # noqa: E501
        :type: str
        """

        self._created_at = created_at

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
        if not isinstance(other, CreateResp):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other