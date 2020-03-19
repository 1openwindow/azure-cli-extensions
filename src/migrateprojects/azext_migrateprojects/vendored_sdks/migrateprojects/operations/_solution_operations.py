# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse

from .. import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]

class SolutionOperations(object):
    """SolutionOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~azure_migrate_hub.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def get_solution(
        self,
        resource_group_name,  # type: str
        migrate_project_name,  # type: str
        solution_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Solution"
        """Gets a solution in the migrate project.

        Gets a solution in the migrate project.

        :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
        :type resource_group_name: str
        :param migrate_project_name: Name of the Azure Migrate project.
        :type migrate_project_name: str
        :param solution_name: Unique name of a migration solution within a migrate project.
        :type solution_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Solution or the result of cls(response)
        :rtype: ~azure_migrate_hub.models.Solution
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Solution"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2018-09-01-preview"

        # Construct URL
        url = self.get_solution.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'migrateProjectName': self._serialize.url("migrate_project_name", migrate_project_name, 'str'),
            'solutionName': self._serialize.url("solution_name", solution_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('Solution', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_solution.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/solutions/{solutionName}'}

    def put_solution(
        self,
        resource_group_name,  # type: str
        migrate_project_name,  # type: str
        solution_name,  # type: str
        etag=None,  # type: Optional[str]
        properties=None,  # type: Optional["models.SolutionProperties"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Solution"
        """Creates a solution in the migrate project.

        Creates a solution in the migrate project.

        :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
        :type resource_group_name: str
        :param migrate_project_name: Name of the Azure Migrate project.
        :type migrate_project_name: str
        :param solution_name: Unique name of a migration solution within a migrate project.
        :type solution_name: str
        :param etag: Gets or sets the ETAG for optimistic concurrency control.
        :type etag: str
        :param properties: Gets or sets the properties of the solution.
        :type properties: ~azure_migrate_hub.models.SolutionProperties
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Solution or the result of cls(response)
        :rtype: ~azure_migrate_hub.models.Solution or ~azure_migrate_hub.models.Solution
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Solution"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

        _solution_input = models.Solution(etag=etag, properties=properties)
        api_version = "2018-09-01-preview"

        # Construct URL
        url = self.put_solution.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'migrateProjectName': self._serialize.url("migrate_project_name", migrate_project_name, 'str'),
            'solutionName': self._serialize.url("solution_name", solution_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = kwargs.pop('content_type', 'application/json')

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_solution_input, 'Solution')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Solution', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('Solution', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    put_solution.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/solutions/{solutionName}'}

    def patch_solution(
        self,
        resource_group_name,  # type: str
        migrate_project_name,  # type: str
        solution_name,  # type: str
        etag=None,  # type: Optional[str]
        properties=None,  # type: Optional["models.SolutionProperties"]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Solution"
        """Update a solution with specified name. Supports partial updates, for example only tags can be provided.

        Update solution.

        :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
        :type resource_group_name: str
        :param migrate_project_name: Name of the Azure Migrate project.
        :type migrate_project_name: str
        :param solution_name: Unique name of a migration solution within a migrate project.
        :type solution_name: str
        :param etag: Gets or sets the ETAG for optimistic concurrency control.
        :type etag: str
        :param properties: Gets or sets the properties of the solution.
        :type properties: ~azure_migrate_hub.models.SolutionProperties
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Solution or the result of cls(response)
        :rtype: ~azure_migrate_hub.models.Solution
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Solution"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

        _solution_input = models.Solution(etag=etag, properties=properties)
        api_version = "2018-09-01-preview"

        # Construct URL
        url = self.patch_solution.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'migrateProjectName': self._serialize.url("migrate_project_name", migrate_project_name, 'str'),
            'solutionName': self._serialize.url("solution_name", solution_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = kwargs.pop('content_type', 'application/json')

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_solution_input, 'Solution')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('Solution', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    patch_solution.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/solutions/{solutionName}'}

    def delete_solution(
        self,
        resource_group_name,  # type: str
        migrate_project_name,  # type: str
        solution_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Delete the solution. Deleting non-existent project is a no-operation.

        Delete the solution.

        :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
        :type resource_group_name: str
        :param migrate_project_name: Name of the Azure Migrate project.
        :type migrate_project_name: str
        :param solution_name: Unique name of a migration solution within a migrate project.
        :type solution_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2018-09-01-preview"

        # Construct URL
        url = self.delete_solution.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'migrateProjectName': self._serialize.url("migrate_project_name", migrate_project_name, 'str'),
            'solutionName': self._serialize.url("solution_name", solution_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        if self._config.accept_language is not None:
            header_parameters['Accept-Language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
          return cls(pipeline_response, None, {})

    delete_solution.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/solutions/{solutionName}'}

    def enumerate_solution(
        self,
        resource_group_name,  # type: str
        migrate_project_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SolutionsCollection"
        """Gets the list of solutions in the migrate project.

        Gets the list of solutions in the migrate project.

        :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
        :type resource_group_name: str
        :param migrate_project_name: Name of the Azure Migrate project.
        :type migrate_project_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SolutionsCollection or the result of cls(response)
        :rtype: ~azure_migrate_hub.models.SolutionsCollection
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SolutionsCollection"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2018-09-01-preview"

        # Construct URL
        url = self.enumerate_solution.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'migrateProjectName': self._serialize.url("migrate_project_name", migrate_project_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('SolutionsCollection', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    enumerate_solution.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/solutions'}

    def get_config(
        self,
        resource_group_name,  # type: str
        migrate_project_name,  # type: str
        solution_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.SolutionConfig"
        """Gets the config for the solution in the migrate project.

        Gets the config for the solution in the migrate project.

        :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
        :type resource_group_name: str
        :param migrate_project_name: Name of the Azure Migrate project.
        :type migrate_project_name: str
        :param solution_name: Unique name of a migration solution within a migrate project.
        :type solution_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SolutionConfig or the result of cls(response)
        :rtype: ~azure_migrate_hub.models.SolutionConfig
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.SolutionConfig"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2018-09-01-preview"

        # Construct URL
        url = self.get_config.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'migrateProjectName': self._serialize.url("migrate_project_name", migrate_project_name, 'str'),
            'solutionName': self._serialize.url("solution_name", solution_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('SolutionConfig', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_config.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/solutions/{solutionName}/getConfig'}

    def cleanup_solution_data(
        self,
        resource_group_name,  # type: str
        migrate_project_name,  # type: str
        solution_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Cleanup the solution data in the migrate project.

        Cleanup the solution data in the migrate project.

        :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
        :type resource_group_name: str
        :param migrate_project_name: Name of the Azure Migrate project.
        :type migrate_project_name: str
        :param solution_name: Unique name of a migration solution within a migrate project.
        :type solution_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2018-09-01-preview"

        # Construct URL
        url = self.cleanup_solution_data.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'migrateProjectName': self._serialize.url("migrate_project_name", migrate_project_name, 'str'),
            'solutionName': self._serialize.url("solution_name", solution_name, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query("api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]

        # Construct and send request
        request = self._client.post(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
          return cls(pipeline_response, None, {})

    cleanup_solution_data.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/solutions/{solutionName}/cleanupData'}
