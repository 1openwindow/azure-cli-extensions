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
from azure.core.pipeline.transport import AsyncHttpResponse, HttpRequest

from ... import models

T = TypeVar('T')
ClsType = Optional[Callable[[PipelineResponse[HttpRequest, AsyncHttpResponse], T, Dict[str, Any]], Any]]

class MigrateProjectOperations:
    """MigrateProjectOperations async operations.

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

    def __init__(self, client, config, serializer, deserializer) -> None:
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    async def get_migrate_project(
        self,
        resource_group_name: str,
        migrate_project_name: str,
        **kwargs
    ) -> "models.MigrateProject":
        """Method to get a migrate project.

        Method to get a migrate project.

        :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
        :type resource_group_name: str
        :param migrate_project_name: Name of the Azure Migrate project.
        :type migrate_project_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MigrateProject or the result of cls(response)
        :rtype: ~azure_migrate_hub.models.MigrateProject
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MigrateProject"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2018-09-01-preview"

        # Construct URL
        url = self.get_migrate_project.metadata['url']
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
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('MigrateProject', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    get_migrate_project.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}'}

    async def put_migrate_project(
        self,
        resource_group_name: str,
        migrate_project_name: str,
        e_tag: Optional[str] = None,
        location: Optional[str] = None,
        properties: Optional["models.MigrateProjectProperties"] = None,
        tags: Optional["models.MigrateProjectTags"] = None,
        **kwargs
    ) -> "models.MigrateProject":
        """Method to create or update a migrate project.

        Method to create or update a migrate project.

        :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
        :type resource_group_name: str
        :param migrate_project_name: Name of the Azure Migrate project.
        :type migrate_project_name: str
        :param e_tag: Gets or sets the eTag for concurrency control.
        :type e_tag: str
        :param location: Gets or sets the Azure location in which migrate project is created.
        :type location: str
        :param properties: Gets or sets the nested properties.
        :type properties: ~azure_migrate_hub.models.MigrateProjectProperties
        :param tags: Gets or sets the tags.
        :type tags: ~azure_migrate_hub.models.MigrateProjectTags
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MigrateProject or the result of cls(response)
        :rtype: ~azure_migrate_hub.models.MigrateProject or ~azure_migrate_hub.models.MigrateProject
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MigrateProject"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

        _body = models.MigrateProject(e_tag=e_tag, location=location, properties=properties, tags=tags)
        api_version = "2018-09-01-preview"

        # Construct URL
        url = self.put_migrate_project.metadata['url']
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
        if self._config.accept_language is not None:
            header_parameters['Accept-Language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = kwargs.pop('content_type', 'application/json')

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MigrateProject')
        body_content_kwargs['content'] = body_content
        request = self._client.put(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('MigrateProject', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('MigrateProject', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    put_migrate_project.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}'}

    async def patch_migrate_project(
        self,
        resource_group_name: str,
        migrate_project_name: str,
        e_tag: Optional[str] = None,
        location: Optional[str] = None,
        properties: Optional["models.MigrateProjectProperties"] = None,
        tags: Optional["models.MigrateProjectTags"] = None,
        **kwargs
    ) -> "models.MigrateProject":
        """Update a migrate project with specified name. Supports partial updates, for example only tags can be provided.

        Update migrate project.

        :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
        :type resource_group_name: str
        :param migrate_project_name: Name of the Azure Migrate project.
        :type migrate_project_name: str
        :param e_tag: Gets or sets the eTag for concurrency control.
        :type e_tag: str
        :param location: Gets or sets the Azure location in which migrate project is created.
        :type location: str
        :param properties: Gets or sets the nested properties.
        :type properties: ~azure_migrate_hub.models.MigrateProjectProperties
        :param tags: Gets or sets the tags.
        :type tags: ~azure_migrate_hub.models.MigrateProjectTags
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MigrateProject or the result of cls(response)
        :rtype: ~azure_migrate_hub.models.MigrateProject
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.MigrateProject"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

        _body = models.MigrateProject(e_tag=e_tag, location=location, properties=properties, tags=tags)
        api_version = "2018-09-01-preview"

        # Construct URL
        url = self.patch_migrate_project.metadata['url']
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
        if self._config.accept_language is not None:
            header_parameters['Accept-Language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = kwargs.pop('content_type', 'application/json')

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_body, 'MigrateProject')
        body_content_kwargs['content'] = body_content
        request = self._client.patch(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('MigrateProject', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    patch_migrate_project.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}'}

    async def delete_migrate_project(
        self,
        resource_group_name: str,
        migrate_project_name: str,
        **kwargs
    ) -> None:
        """Delete the migrate project. Deleting non-existent project is a no-operation.

        Delete the migrate project.

        :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
        :type resource_group_name: str
        :param migrate_project_name: Name of the Azure Migrate project.
        :type migrate_project_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})
        api_version = "2018-09-01-preview"

        # Construct URL
        url = self.delete_migrate_project.metadata['url']
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
        if self._config.accept_language is not None:
            header_parameters['Accept-Language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        if cls:
          return cls(pipeline_response, None, {})

    delete_migrate_project.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}'}

    async def register_tool(
        self,
        resource_group_name: str,
        migrate_project_name: str,
        tool: Optional[Union[str, "models.RegisterToolInputTool"]] = None,
        **kwargs
    ) -> "models.RegistrationResult":
        """Registers a tool with the migrate project.

        Registers a tool with the migrate project.

        :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
        :type resource_group_name: str
        :param migrate_project_name: Name of the Azure Migrate project.
        :type migrate_project_name: str
        :param tool: Gets or sets the tool to be registered.
        :type tool: str or ~azure_migrate_hub.models.RegisterToolInputTool
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RegistrationResult or the result of cls(response)
        :rtype: ~azure_migrate_hub.models.RegistrationResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.RegistrationResult"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

        _input = models.RegisterToolInput(tool=tool)
        api_version = "2018-09-01-preview"

        # Construct URL
        url = self.register_tool.metadata['url']
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
        if self._config.accept_language is not None:
            header_parameters['Accept-Language'] = self._serialize.header("self._config.accept_language", self._config.accept_language, 'str')
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = kwargs.pop('content_type', 'application/json')

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_input, 'RegisterToolInput')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('RegistrationResult', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    register_tool.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/registerTool'}

    async def refresh_migrate_project_summary(
        self,
        resource_group_name: str,
        migrate_project_name: str,
        goal: Optional[Union[str, "models.RefreshSummaryInputGoal"]] = None,
        **kwargs
    ) -> "models.RefreshSummaryResult":
        """Refresh the summary of the migrate project.

        Refresh the summary of the migrate project.

        :param resource_group_name: Name of the Azure Resource Group that migrate project is part of.
        :type resource_group_name: str
        :param migrate_project_name: Name of the Azure Migrate project.
        :type migrate_project_name: str
        :param goal: Gets or sets the goal for which summary needs to be refreshed.
        :type goal: str or ~azure_migrate_hub.models.RefreshSummaryInputGoal
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: RefreshSummaryResult or the result of cls(response)
        :rtype: ~azure_migrate_hub.models.RefreshSummaryResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.RefreshSummaryResult"]
        error_map = kwargs.pop('error_map', {404: ResourceNotFoundError, 409: ResourceExistsError})

        _input = models.RefreshSummaryInput(goal=goal)
        api_version = "2018-09-01-preview"

        # Construct URL
        url = self.refresh_migrate_project_summary.metadata['url']
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
        header_parameters['Content-Type'] = kwargs.pop('content_type', 'application/json')

        # Construct and send request
        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(_input, 'RefreshSummaryInput')
        body_content_kwargs['content'] = body_content
        request = self._client.post(url, query_parameters, header_parameters, **body_content_kwargs)

        pipeline_response = await self._client._pipeline.run(request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code, response=response, error_map=error_map)
            raise HttpResponseError(response=response)

        deserialized = self._deserialize('RefreshSummaryResult', pipeline_response)

        if cls:
          return cls(pipeline_response, deserialized, {})

        return deserialized
    refresh_migrate_project_summary.metadata = {'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Migrate/migrateProjects/{migrateProjectName}/refreshSummary'}
