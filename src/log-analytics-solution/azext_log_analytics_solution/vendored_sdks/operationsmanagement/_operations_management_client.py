# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer

from ._configuration import OperationsManagementClientConfiguration
from .operations import SolutionsOperations
from .operations import ManagementAssociationsOperations
from .operations import ManagementConfigurationsOperations
from .operations import Operations
from . import models


class OperationsManagementClient(SDKClient):
    """Operations Management Client

    :ivar config: Configuration for client.
    :vartype config: OperationsManagementClientConfiguration

    :ivar solutions: Solutions operations
    :vartype solutions: azure.mgmt.operationsmanagement.operations.SolutionsOperations
    :ivar management_associations: ManagementAssociations operations
    :vartype management_associations: azure.mgmt.operationsmanagement.operations.ManagementAssociationsOperations
    :ivar management_configurations: ManagementConfigurations operations
    :vartype management_configurations: azure.mgmt.operationsmanagement.operations.ManagementConfigurationsOperations
    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.operationsmanagement.operations.Operations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param subscription_id: Gets subscription credentials which uniquely
     identify Microsoft Azure subscription. The subscription ID forms part of
     the URI for every service call.
    :type subscription_id: str
    :param provider_name: Provider name for the parent resource.
    :type provider_name: str
    :param resource_type: Resource type for the parent resource
    :type resource_type: str
    :param resource_name: Parent resource name.
    :type resource_name: str
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, subscription_id, provider_name, resource_type, resource_name, base_url=None):

        self.config = OperationsManagementClientConfiguration(credentials, subscription_id, provider_name, resource_type, resource_name, base_url)
        super(OperationsManagementClient, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2015-11-01-preview'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.solutions = SolutionsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.management_associations = ManagementAssociationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.management_configurations = ManagementConfigurationsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.operations = Operations(
            self._client, self.config, self._serialize, self._deserialize)
