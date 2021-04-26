# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import TYPE_CHECKING

from azure.core import PipelineClient
from azure.farmbeats.core.rest import HttpResponse, _StreamContextManager
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Dict

    from azure.core.credentials import TokenCredential
    from azure.farmbeats.core.rest import HttpRequest

from ._configuration import FarmBeatsClientConfiguration


class FarmBeatsClient(object):
    """APIs documentation for Azure AgPlatform DataPlane Service.

    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        base_url = 'None'
        self._config = FarmBeatsClientConfiguration(credential, **kwargs)
        self._client = PipelineClient(base_url=base_url, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._serialize.client_side_validation = False

    def send_request(self, http_request, **kwargs):
        # type: (HttpRequest, Any) -> HttpResponse
        """Runs the network request through the client's chained policies.

        We have helper methods to create requests specific to this service in `azure.farmbeats.rest`.
        Use these helper methods to create the request you pass to this method. See our example below:

        >>> from azure.farmbeats.rest import build_list_by_farmer_id_request
        >>> request = build_list_by_farmer_id_request(farmer_id, min_avg_material, max_avg_material, min_total_material, max_total_material, sources, associated_boundary_ids, operation_boundary_ids, min_operation_start_date_time, max_operation_start_date_time, min_operation_end_date_time, max_operation_end_date_time, min_operation_modified_date_time, max_operation_modified_date_time, min_area, max_area, ids, names, property_filters, statuses, min_created_date_time, max_created_date_time, min_last_modified_date_time, max_last_modified_date_time, max_page_size, skip_token)
        <HttpRequest [GET], url: '/farmers/{farmerId}/application-data'>
        >>> response = client.send_request(request)
        <HttpResponse: 200 OK>

        For more information on this code flow, see https://aka.ms/azsdk/python/llcwiki

        For advanced cases, you can also create your own :class:`~azure.farmbeats.core.rest.HttpRequest`
        and pass it in.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.farmbeats.core.rest.HttpRequest
        :keyword bool stream_response: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.farmbeats.core.rest.HttpResponse
        """
        request_copy = deepcopy(http_request)
        request_copy.url = self._client.format_url(request_copy.url)
        if kwargs.pop("stream_response", False):
            return _StreamContextManager(
                client=self._client._pipeline,
                request=request_copy,
            )
        pipeline_response = self._client._pipeline.run(request_copy._internal_request, **kwargs)
        response = HttpResponse(
            status_code=pipeline_response.http_response.status_code,
            request=request_copy,
            _internal_response=pipeline_response.http_response
        )
        response.read()
        return response

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> FarmBeatsClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
