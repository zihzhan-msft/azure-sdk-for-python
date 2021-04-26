# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import Any, IO, List, Optional

from azure.core.pipeline.transport._base import _format_url_section
from azure.farmbeats.core.rest import HttpRequest
from msrest import Serializer

_SERIALIZER = Serializer()


def build_list_request(
    *,
    ids: Optional[List[str]] = None,
    names: Optional[List[str]] = None,
    property_filters: Optional[List[str]] = None,
    statuses: Optional[List[str]] = None,
    min_created_date_time: Optional[datetime.datetime] = None,
    max_created_date_time: Optional[datetime.datetime] = None,
    min_last_modified_date_time: Optional[datetime.datetime] = None,
    max_last_modified_date_time: Optional[datetime.datetime] = None,
    max_page_size: Optional[int] = 50,
    skip_token: Optional[str] = None,
    **kwargs: Any
) -> HttpRequest:
    """Returns a paginated list of oauthProvider resources.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword ids: Ids of the resource.
    :paramtype ids: list[str]
    :keyword names: Names of the resource.
    :paramtype names: list[str]
    :keyword property_filters: Filters on key-value pairs within the Properties object.
     eg. "{testkey} eq {testvalue}".
    :paramtype property_filters: list[str]
    :keyword statuses: Statuses of the resource.
    :paramtype statuses: list[str]
    :keyword min_created_date_time: Minimum creation date of resource (inclusive).
    :paramtype min_created_date_time: ~datetime.datetime
    :keyword max_created_date_time: Maximum creation date of resource (inclusive).
    :paramtype max_created_date_time: ~datetime.datetime
    :keyword min_last_modified_date_time: Minimum last modified date of resource (inclusive).
    :paramtype min_last_modified_date_time: ~datetime.datetime
    :keyword max_last_modified_date_time: Maximum last modified date of resource (inclusive).
    :paramtype max_last_modified_date_time: ~datetime.datetime
    :keyword max_page_size: Maximum number of items needed (inclusive).
     Minimum = 10, Maximum = 1000, Default value = 50.
    :paramtype max_page_size: int
    :keyword skip_token: Skip token for getting next set of results.
    :paramtype skip_token: str
    :return: Returns an :class:`~azure.farmbeats.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.farmbeats.core.rest.HttpRequest
    """
    api_version = "2021-03-31-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/oauth/providers')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if ids is not None:
        query_parameters['ids'] = [_SERIALIZER.query("ids", q, 'str') if q is not None else '' for q in ids]
    if names is not None:
        query_parameters['names'] = [_SERIALIZER.query("names", q, 'str') if q is not None else '' for q in names]
    if property_filters is not None:
        query_parameters['propertyFilters'] = [_SERIALIZER.query("property_filters", q, 'str') if q is not None else '' for q in property_filters]
    if statuses is not None:
        query_parameters['statuses'] = [_SERIALIZER.query("statuses", q, 'str') if q is not None else '' for q in statuses]
    if min_created_date_time is not None:
        query_parameters['minCreatedDateTime'] = _SERIALIZER.query("min_created_date_time", min_created_date_time, 'iso-8601')
    if max_created_date_time is not None:
        query_parameters['maxCreatedDateTime'] = _SERIALIZER.query("max_created_date_time", max_created_date_time, 'iso-8601')
    if min_last_modified_date_time is not None:
        query_parameters['minLastModifiedDateTime'] = _SERIALIZER.query("min_last_modified_date_time", min_last_modified_date_time, 'iso-8601')
    if max_last_modified_date_time is not None:
        query_parameters['maxLastModifiedDateTime'] = _SERIALIZER.query("max_last_modified_date_time", max_last_modified_date_time, 'iso-8601')
    if max_page_size is not None:
        query_parameters['$maxPageSize'] = _SERIALIZER.query("max_page_size", max_page_size, 'int', maximum=1000, minimum=10)
    if skip_token is not None:
        query_parameters['$skipToken'] = _SERIALIZER.query("skip_token", skip_token, 'str')
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_request(
    oauth_provider_id: str,
    **kwargs: Any
) -> HttpRequest:
    """Get a specified oauthProvider resource.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :param oauth_provider_id: ID of the oauthProvider resource.
    :type oauth_provider_id: str
    :return: Returns an :class:`~azure.farmbeats.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.farmbeats.core.rest.HttpRequest
    """
    api_version = "2021-03-31-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/oauth/providers/{oauthProviderId}')
    path_format_arguments = {
        'oauthProviderId': _SERIALIZER.url("oauth_provider_id", oauth_provider_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="GET",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_create_or_update_request(
    oauth_provider_id: str,
    *,
    content: Optional["_models.OAuthProvider"] = None,
    **kwargs: Any
) -> HttpRequest:
    """Creates or updates an oauthProvider resource.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :param oauth_provider_id: ID of oauthProvider resource.
    :type oauth_provider_id: str
    :keyword content: OauthProvider resource payload to create or update.
    :paramtype content: ~azure.farmbeats.models.OAuthProvider
    :return: Returns an :class:`~azure.farmbeats.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.farmbeats.core.rest.HttpRequest
    """
    content_type = kwargs.pop("content_type", None)
    api_version = "2021-03-31-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/oauth/providers/{oauthProviderId}')
    path_format_arguments = {
        'oauthProviderId': _SERIALIZER.url("oauth_provider_id", oauth_provider_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="PATCH",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        content=content,
        **kwargs
    )


def build_delete_request(
    oauth_provider_id: str,
    **kwargs: Any
) -> HttpRequest:
    """Deletes an specified oauthProvider resource.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :param oauth_provider_id: ID of oauthProvider.
    :type oauth_provider_id: str
    :return: Returns an :class:`~azure.farmbeats.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.farmbeats.core.rest.HttpRequest
    """
    api_version = "2021-03-31-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/oauth/providers/{oauthProviderId}')
    path_format_arguments = {
        'oauthProviderId': _SERIALIZER.url("oauth_provider_id", oauth_provider_id, 'str'),
    }
    url = _format_url_section(url, **path_format_arguments)

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="DELETE",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

