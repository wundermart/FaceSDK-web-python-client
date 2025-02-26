# coding: utf-8

"""
    Regula FaceSDK Web API

    Regula FaceSDK Web API  # noqa: E501

    The version of the OpenAPI document: 3.2.0
    Generated by: https://openapi-generator.tech
"""


import pprint
import re  # noqa: F401

import six

from regula.facesdk.webclient.gen.configuration import Configuration


class MatchImageDetection(object):
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
        'faces': 'list[DetectionFace]',
        'image_index': 'int',
        'status': 'FaceSDKResultCode'
    }

    attribute_map = {
        'faces': 'faces',
        'image_index': 'imageIndex',
        'status': 'status'
    }

    def __init__(self, faces=None, image_index=None, status=None, local_vars_configuration=None):  # noqa: E501
        """MatchImageDetection - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration()
        self.local_vars_configuration = local_vars_configuration

        self._faces = None
        self._image_index = None
        self._status = None
        self.discriminator = None

        if faces is not None:
            self.faces = faces
        self.image_index = image_index
        self.status = status

    @property
    def faces(self):
        """Gets the faces of this MatchImageDetection.  # noqa: E501


        :return: The faces of this MatchImageDetection.  # noqa: E501
        :rtype: list[DetectionFace]
        """
        return self._faces

    @faces.setter
    def faces(self, faces):
        """Sets the faces of this MatchImageDetection.


        :param faces: The faces of this MatchImageDetection.  # noqa: E501
        :type faces: list[DetectionFace]
        """

        self._faces = faces

    @property
    def image_index(self):
        """Gets the image_index of this MatchImageDetection.  # noqa: E501

        Image index used to identify input photos between themselves. If not specified, than input list index is used  # noqa: E501

        :return: The image_index of this MatchImageDetection.  # noqa: E501
        :rtype: int
        """
        return self._image_index

    @image_index.setter
    def image_index(self, image_index):
        """Sets the image_index of this MatchImageDetection.

        Image index used to identify input photos between themselves. If not specified, than input list index is used  # noqa: E501

        :param image_index: The image_index of this MatchImageDetection.  # noqa: E501
        :type image_index: int
        """
        if self.local_vars_configuration.client_side_validation and image_index is None:  # noqa: E501
            raise ValueError("Invalid value for `image_index`, must not be `None`")  # noqa: E501

        self._image_index = image_index

    @property
    def status(self):
        """Gets the status of this MatchImageDetection.  # noqa: E501


        :return: The status of this MatchImageDetection.  # noqa: E501
        :rtype: FaceSDKResultCode
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this MatchImageDetection.


        :param status: The status of this MatchImageDetection.  # noqa: E501
        :type status: FaceSDKResultCode
        """
        if self.local_vars_configuration.client_side_validation and status is None:  # noqa: E501
            raise ValueError("Invalid value for `status`, must not be `None`")  # noqa: E501

        self._status = status

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
        if not isinstance(other, MatchImageDetection):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, MatchImageDetection):
            return True

        return self.to_dict() != other.to_dict()
