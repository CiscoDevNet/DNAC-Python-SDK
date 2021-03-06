# coding: utf-8

"""
    Swagger

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from python_client.models.path_response_result_response_egress_physical_interface_acl_analysis import PathResponseResultResponseEgressPhysicalInterfaceAclAnalysis  # noqa: F401,E501
from python_client.models.path_response_result_response_egress_physical_interface_interface_statistics import PathResponseResultResponseEgressPhysicalInterfaceInterfaceStatistics  # noqa: F401,E501
from python_client.models.path_response_result_response_egress_physical_interface_path_overlay_info import PathResponseResultResponseEgressPhysicalInterfacePathOverlayInfo  # noqa: F401,E501
from python_client.models.path_response_result_response_egress_physical_interface_qos_statistics import PathResponseResultResponseEgressPhysicalInterfaceQosStatistics  # noqa: F401,E501


class PathResponseResultResponseEgressPhysicalInterface(object):
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
        'acl_analysis': 'PathResponseResultResponseEgressPhysicalInterfaceAclAnalysis',
        'id': 'str',
        'interface_statistics': 'PathResponseResultResponseEgressPhysicalInterfaceInterfaceStatistics',
        'interface_stats_collection': 'str',
        'interface_stats_collection_failure_reason': 'str',
        'name': 'str',
        'path_overlay_info': 'list[PathResponseResultResponseEgressPhysicalInterfacePathOverlayInfo]',
        'qos_statistics': 'list[PathResponseResultResponseEgressPhysicalInterfaceQosStatistics]',
        'qos_stats_collection': 'str',
        'qos_stats_collection_failure_reason': 'str',
        'used_vlan': 'str',
        'vrf_name': 'str'
    }

    attribute_map = {
        'acl_analysis': 'aclAnalysis',
        'id': 'id',
        'interface_statistics': 'interfaceStatistics',
        'interface_stats_collection': 'interfaceStatsCollection',
        'interface_stats_collection_failure_reason': 'interfaceStatsCollectionFailureReason',
        'name': 'name',
        'path_overlay_info': 'pathOverlayInfo',
        'qos_statistics': 'qosStatistics',
        'qos_stats_collection': 'qosStatsCollection',
        'qos_stats_collection_failure_reason': 'qosStatsCollectionFailureReason',
        'used_vlan': 'usedVlan',
        'vrf_name': 'vrfName'
    }

    def __init__(self, acl_analysis=None, id=None, interface_statistics=None, interface_stats_collection=None, interface_stats_collection_failure_reason=None, name=None, path_overlay_info=None, qos_statistics=None, qos_stats_collection=None, qos_stats_collection_failure_reason=None, used_vlan=None, vrf_name=None):  # noqa: E501
        """PathResponseResultResponseEgressPhysicalInterface - a model defined in Swagger"""  # noqa: E501

        self._acl_analysis = None
        self._id = None
        self._interface_statistics = None
        self._interface_stats_collection = None
        self._interface_stats_collection_failure_reason = None
        self._name = None
        self._path_overlay_info = None
        self._qos_statistics = None
        self._qos_stats_collection = None
        self._qos_stats_collection_failure_reason = None
        self._used_vlan = None
        self._vrf_name = None
        self.discriminator = None

        if acl_analysis is not None:
            self.acl_analysis = acl_analysis
        if id is not None:
            self.id = id
        if interface_statistics is not None:
            self.interface_statistics = interface_statistics
        if interface_stats_collection is not None:
            self.interface_stats_collection = interface_stats_collection
        if interface_stats_collection_failure_reason is not None:
            self.interface_stats_collection_failure_reason = interface_stats_collection_failure_reason
        if name is not None:
            self.name = name
        if path_overlay_info is not None:
            self.path_overlay_info = path_overlay_info
        if qos_statistics is not None:
            self.qos_statistics = qos_statistics
        if qos_stats_collection is not None:
            self.qos_stats_collection = qos_stats_collection
        if qos_stats_collection_failure_reason is not None:
            self.qos_stats_collection_failure_reason = qos_stats_collection_failure_reason
        if used_vlan is not None:
            self.used_vlan = used_vlan
        if vrf_name is not None:
            self.vrf_name = vrf_name

    @property
    def acl_analysis(self):
        """Gets the acl_analysis of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501


        :return: The acl_analysis of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501
        :rtype: PathResponseResultResponseEgressPhysicalInterfaceAclAnalysis
        """
        return self._acl_analysis

    @acl_analysis.setter
    def acl_analysis(self, acl_analysis):
        """Sets the acl_analysis of this PathResponseResultResponseEgressPhysicalInterface.


        :param acl_analysis: The acl_analysis of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501
        :type: PathResponseResultResponseEgressPhysicalInterfaceAclAnalysis
        """

        self._acl_analysis = acl_analysis

    @property
    def id(self):
        """Gets the id of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501


        :return: The id of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PathResponseResultResponseEgressPhysicalInterface.


        :param id: The id of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def interface_statistics(self):
        """Gets the interface_statistics of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501


        :return: The interface_statistics of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501
        :rtype: PathResponseResultResponseEgressPhysicalInterfaceInterfaceStatistics
        """
        return self._interface_statistics

    @interface_statistics.setter
    def interface_statistics(self, interface_statistics):
        """Sets the interface_statistics of this PathResponseResultResponseEgressPhysicalInterface.


        :param interface_statistics: The interface_statistics of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501
        :type: PathResponseResultResponseEgressPhysicalInterfaceInterfaceStatistics
        """

        self._interface_statistics = interface_statistics

    @property
    def interface_stats_collection(self):
        """Gets the interface_stats_collection of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501


        :return: The interface_stats_collection of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501
        :rtype: str
        """
        return self._interface_stats_collection

    @interface_stats_collection.setter
    def interface_stats_collection(self, interface_stats_collection):
        """Sets the interface_stats_collection of this PathResponseResultResponseEgressPhysicalInterface.


        :param interface_stats_collection: The interface_stats_collection of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501
        :type: str
        """

        self._interface_stats_collection = interface_stats_collection

    @property
    def interface_stats_collection_failure_reason(self):
        """Gets the interface_stats_collection_failure_reason of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501


        :return: The interface_stats_collection_failure_reason of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501
        :rtype: str
        """
        return self._interface_stats_collection_failure_reason

    @interface_stats_collection_failure_reason.setter
    def interface_stats_collection_failure_reason(self, interface_stats_collection_failure_reason):
        """Sets the interface_stats_collection_failure_reason of this PathResponseResultResponseEgressPhysicalInterface.


        :param interface_stats_collection_failure_reason: The interface_stats_collection_failure_reason of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501
        :type: str
        """

        self._interface_stats_collection_failure_reason = interface_stats_collection_failure_reason

    @property
    def name(self):
        """Gets the name of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501


        :return: The name of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PathResponseResultResponseEgressPhysicalInterface.


        :param name: The name of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def path_overlay_info(self):
        """Gets the path_overlay_info of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501


        :return: The path_overlay_info of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501
        :rtype: list[PathResponseResultResponseEgressPhysicalInterfacePathOverlayInfo]
        """
        return self._path_overlay_info

    @path_overlay_info.setter
    def path_overlay_info(self, path_overlay_info):
        """Sets the path_overlay_info of this PathResponseResultResponseEgressPhysicalInterface.


        :param path_overlay_info: The path_overlay_info of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501
        :type: list[PathResponseResultResponseEgressPhysicalInterfacePathOverlayInfo]
        """

        self._path_overlay_info = path_overlay_info

    @property
    def qos_statistics(self):
        """Gets the qos_statistics of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501


        :return: The qos_statistics of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501
        :rtype: list[PathResponseResultResponseEgressPhysicalInterfaceQosStatistics]
        """
        return self._qos_statistics

    @qos_statistics.setter
    def qos_statistics(self, qos_statistics):
        """Sets the qos_statistics of this PathResponseResultResponseEgressPhysicalInterface.


        :param qos_statistics: The qos_statistics of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501
        :type: list[PathResponseResultResponseEgressPhysicalInterfaceQosStatistics]
        """

        self._qos_statistics = qos_statistics

    @property
    def qos_stats_collection(self):
        """Gets the qos_stats_collection of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501


        :return: The qos_stats_collection of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501
        :rtype: str
        """
        return self._qos_stats_collection

    @qos_stats_collection.setter
    def qos_stats_collection(self, qos_stats_collection):
        """Sets the qos_stats_collection of this PathResponseResultResponseEgressPhysicalInterface.


        :param qos_stats_collection: The qos_stats_collection of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501
        :type: str
        """

        self._qos_stats_collection = qos_stats_collection

    @property
    def qos_stats_collection_failure_reason(self):
        """Gets the qos_stats_collection_failure_reason of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501


        :return: The qos_stats_collection_failure_reason of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501
        :rtype: str
        """
        return self._qos_stats_collection_failure_reason

    @qos_stats_collection_failure_reason.setter
    def qos_stats_collection_failure_reason(self, qos_stats_collection_failure_reason):
        """Sets the qos_stats_collection_failure_reason of this PathResponseResultResponseEgressPhysicalInterface.


        :param qos_stats_collection_failure_reason: The qos_stats_collection_failure_reason of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501
        :type: str
        """

        self._qos_stats_collection_failure_reason = qos_stats_collection_failure_reason

    @property
    def used_vlan(self):
        """Gets the used_vlan of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501


        :return: The used_vlan of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501
        :rtype: str
        """
        return self._used_vlan

    @used_vlan.setter
    def used_vlan(self, used_vlan):
        """Sets the used_vlan of this PathResponseResultResponseEgressPhysicalInterface.


        :param used_vlan: The used_vlan of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501
        :type: str
        """

        self._used_vlan = used_vlan

    @property
    def vrf_name(self):
        """Gets the vrf_name of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501


        :return: The vrf_name of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501
        :rtype: str
        """
        return self._vrf_name

    @vrf_name.setter
    def vrf_name(self, vrf_name):
        """Sets the vrf_name of this PathResponseResultResponseEgressPhysicalInterface.


        :param vrf_name: The vrf_name of this PathResponseResultResponseEgressPhysicalInterface.  # noqa: E501
        :type: str
        """

        self._vrf_name = vrf_name

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, PathResponseResultResponseEgressPhysicalInterface):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
