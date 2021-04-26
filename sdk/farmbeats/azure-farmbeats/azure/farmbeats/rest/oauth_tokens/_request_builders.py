# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
import datetime
from typing import TYPE_CHECKING

from azure.core.pipeline.transport._base import _format_url_section
from azure.farmbeats.core.rest import HttpRequest
from msrest import Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, IO, List, Optional

_SERIALIZER = Serializer()


def build_list_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Returns a list of OAuthToken documents.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword auth_provider_ids: Name of AuthProvider.
    :paramtype auth_provider_ids: list[str]
    :keyword farmer_ids: List of farmers.
    :paramtype farmer_ids: list[str]
    :keyword is_valid: If the token object is valid.
    :paramtype is_valid: bool
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
    auth_provider_ids = kwargs.pop('auth_provider_ids', None)  # type: Optional[List[str]]
    farmer_ids = kwargs.pop('farmer_ids', None)  # type: Optional[List[str]]
    is_valid = kwargs.pop('is_valid', None)  # type: Optional[bool]
    min_created_date_time = kwargs.pop('min_created_date_time', None)  # type: Optional[datetime.datetime]
    max_created_date_time = kwargs.pop('max_created_date_time', None)  # type: Optional[datetime.datetime]
    min_last_modified_date_time = kwargs.pop('min_last_modified_date_time', None)  # type: Optional[datetime.datetime]
    max_last_modified_date_time = kwargs.pop('max_last_modified_date_time', None)  # type: Optional[datetime.datetime]
    max_page_size = kwargs.pop('max_page_size', 50)  # type: Optional[int]
    skip_token = kwargs.pop('skip_token', None)  # type: Optional[str]
    api_version = "2021-03-31-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/oauth/tokens')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    if auth_provider_ids is not None:
        query_parameters['authProviderIds'] = [_SERIALIZER.query("auth_provider_ids", q, 'str') if q is not None else '' for q in auth_provider_ids]
    if farmer_ids is not None:
        query_parameters['farmerIds'] = [_SERIALIZER.query("farmer_ids", q, 'str') if q is not None else '' for q in farmer_ids]
    if is_valid is not None:
        query_parameters['isValid'] = _SERIALIZER.query("is_valid", is_valid, 'bool')
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


def build_delete_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Deletes OAuth Token for given oauth provider Id and farmer Id.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword farmer_id: Id of the associated farmer.
    :paramtype farmer_id: str
    :keyword oauth_provider_id: Id of the associated oauth provider.
    :paramtype oauth_provider_id: str
    :return: Returns an :class:`~azure.farmbeats.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.farmbeats.core.rest.HttpRequest
    """
    farmer_id = kwargs.pop('farmer_id')  # type: str
    oauth_provider_id = kwargs.pop('oauth_provider_id')  # type: str
    api_version = "2021-03-31-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/oauth/tokens/:remove')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['farmerId'] = _SERIALIZER.query("farmer_id", farmer_id, 'str')
    query_parameters['oauthProviderId'] = _SERIALIZER.query("oauth_provider_id", oauth_provider_id, 'str')
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )


def build_get_o_auth_connection_link_request(
    **kwargs  # type: Any
):
    # type: (...) -> HttpRequest
    """Returns Connection link needed in the OAuth flow.

    See https://aka.ms/azsdk/python/llcwiki for how to incorporate this request builder into your code flow.

    :keyword json: OAuth Connect Request.
    :paramtype json: Any
    :keyword content: OAuth Connect Request.
    :paramtype content: Any
    :return: Returns an :class:`~azure.farmbeats.core.rest.HttpRequest` that you will pass to the client's `send_request` method.
     See https://aka.ms/azsdk/python/llcwiki for how to incorporate this response into your code flow.
    :rtype: ~azure.farmbeats.core.rest.HttpRequest

    Example:
        .. code-block:: python

            # JSON input template you can fill out and use as your `json` input.
            json = {
                "farmerId": "str",
                "oAuthProviderId": "str",
                "userRedirectLink": "str",
                "userRedirectState": "str (optional)"
            }
    """
    content_type = kwargs.pop("content_type", None)
    api_version = "2021-03-31-preview"
    accept = "application/json"

    # Construct URL
    url = kwargs.pop("template_url", '/oauth/tokens/:connect')

    # Construct parameters
    query_parameters = kwargs.pop("params", {})  # type: Dict[str, Any]
    query_parameters['api-version'] = _SERIALIZER.query("api_version", api_version, 'str')

    # Construct headers
    header_parameters = kwargs.pop("headers", {})  # type: Dict[str, Any]
    if content_type is not None:
        header_parameters['Content-Type'] = _SERIALIZER.header("content_type", content_type, 'str')
    header_parameters['Accept'] = _SERIALIZER.header("accept", accept, 'str')

    return HttpRequest(
        method="POST",
        url=url,
        params=query_parameters,
        headers=header_parameters,
        **kwargs
    )

