# coding: utf-8

"""
    Gluster Management API

    Gluster Management APIs  # noqa: E501

    OpenAPI spec version: 1.0.0
    Contact: you@your-company.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient


class DefaultApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def peers_get(self, **kwargs):  # noqa: E501
        """peers_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.peers_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Peer]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.peers_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.peers_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def peers_get_with_http_info(self, **kwargs):  # noqa: E501
        """peers_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.peers_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Peer]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method peers_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/peers', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Peer]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def peers_peerid_delete(self, peerid, **kwargs):  # noqa: E501
        """peers_peerid_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.peers_peerid_delete(peerid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str peerid: Peer ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.peers_peerid_delete_with_http_info(peerid, **kwargs)  # noqa: E501
        else:
            (data) = self.peers_peerid_delete_with_http_info(peerid, **kwargs)  # noqa: E501
            return data

    def peers_peerid_delete_with_http_info(self, peerid, **kwargs):  # noqa: E501
        """peers_peerid_delete  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.peers_peerid_delete_with_http_info(peerid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str peerid: Peer ID (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['peerid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method peers_peerid_delete" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'peerid' is set
        if ('peerid' not in local_var_params or
                local_var_params['peerid'] is None):
            raise ValueError("Missing the required parameter `peerid` when calling `peers_peerid_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'peerid' in local_var_params:
            path_params['peerid'] = local_var_params['peerid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/peers/{peerid}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def peers_peerid_get(self, peerid, **kwargs):  # noqa: E501
        """peers_peerid_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.peers_peerid_get(peerid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str peerid: Peer ID (required)
        :return: Peer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.peers_peerid_get_with_http_info(peerid, **kwargs)  # noqa: E501
        else:
            (data) = self.peers_peerid_get_with_http_info(peerid, **kwargs)  # noqa: E501
            return data

    def peers_peerid_get_with_http_info(self, peerid, **kwargs):  # noqa: E501
        """peers_peerid_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.peers_peerid_get_with_http_info(peerid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str peerid: Peer ID (required)
        :return: Peer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['peerid']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method peers_peerid_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'peerid' is set
        if ('peerid' not in local_var_params or
                local_var_params['peerid'] is None):
            raise ValueError("Missing the required parameter `peerid` when calling `peers_peerid_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'peerid' in local_var_params:
            path_params['peerid'] = local_var_params['peerid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/peers/{peerid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Peer',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def peers_peerid_post(self, peerid, **kwargs):  # noqa: E501
        """peers_peerid_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.peers_peerid_post(peerid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str peerid: Peer ID (required)
        :param Add add:
        :return: Peer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.peers_peerid_post_with_http_info(peerid, **kwargs)  # noqa: E501
        else:
            (data) = self.peers_peerid_post_with_http_info(peerid, **kwargs)  # noqa: E501
            return data

    def peers_peerid_post_with_http_info(self, peerid, **kwargs):  # noqa: E501
        """peers_peerid_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.peers_peerid_post_with_http_info(peerid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str peerid: Peer ID (required)
        :param Add add:
        :return: Peer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['peerid', 'add']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method peers_peerid_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'peerid' is set
        if ('peerid' not in local_var_params or
                local_var_params['peerid'] is None):
            raise ValueError("Missing the required parameter `peerid` when calling `peers_peerid_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'peerid' in local_var_params:
            path_params['peerid'] = local_var_params['peerid']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'add' in local_var_params:
            body_params = local_var_params['add']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/peers/{peerid}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Peer',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def peers_post(self, **kwargs):  # noqa: E501
        """peers_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.peers_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Add add:
        :return: Peer
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.peers_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.peers_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def peers_post_with_http_info(self, **kwargs):  # noqa: E501
        """peers_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.peers_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Add add:
        :return: Peer
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['add']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method peers_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'add' in local_var_params:
            body_params = local_var_params['add']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/peers', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Peer',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def volumes_get(self, **kwargs):  # noqa: E501
        """volumes_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.volumes_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Volume]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.volumes_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.volumes_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def volumes_get_with_http_info(self, **kwargs):  # noqa: E501
        """volumes_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.volumes_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[Volume]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method volumes_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/volumes', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Volume]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def volumes_post(self, **kwargs):  # noqa: E501
        """volumes_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.volumes_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Add add:
        :return: Volume
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.volumes_post_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.volumes_post_with_http_info(**kwargs)  # noqa: E501
            return data

    def volumes_post_with_http_info(self, **kwargs):  # noqa: E501
        """volumes_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.volumes_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param Add add:
        :return: Volume
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['add']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method volumes_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'add' in local_var_params:
            body_params = local_var_params['add']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/volumes', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Volume',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def volumes_volname_start_post(self, volname, **kwargs):  # noqa: E501
        """volumes_volname_start_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.volumes_volname_start_post(volname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str volname: Volume Name (required)
        :return: Volume
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.volumes_volname_start_post_with_http_info(volname, **kwargs)  # noqa: E501
        else:
            (data) = self.volumes_volname_start_post_with_http_info(volname, **kwargs)  # noqa: E501
            return data

    def volumes_volname_start_post_with_http_info(self, volname, **kwargs):  # noqa: E501
        """volumes_volname_start_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.volumes_volname_start_post_with_http_info(volname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str volname: Volume Name (required)
        :return: Volume
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['volname']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method volumes_volname_start_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'volname' is set
        if ('volname' not in local_var_params or
                local_var_params['volname'] is None):
            raise ValueError("Missing the required parameter `volname` when calling `volumes_volname_start_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'volname' in local_var_params:
            path_params['volname'] = local_var_params['volname']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/volumes/{volname}/start', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Volume',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def volumes_volname_stop_post(self, volname, **kwargs):  # noqa: E501
        """volumes_volname_stop_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.volumes_volname_stop_post(volname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str volname: Volume Name (required)
        :return: Volume
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.volumes_volname_stop_post_with_http_info(volname, **kwargs)  # noqa: E501
        else:
            (data) = self.volumes_volname_stop_post_with_http_info(volname, **kwargs)  # noqa: E501
            return data

    def volumes_volname_stop_post_with_http_info(self, volname, **kwargs):  # noqa: E501
        """volumes_volname_stop_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.volumes_volname_stop_post_with_http_info(volname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str volname: Volume Name (required)
        :return: Volume
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['volname']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method volumes_volname_stop_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'volname' is set
        if ('volname' not in local_var_params or
                local_var_params['volname'] is None):
            raise ValueError("Missing the required parameter `volname` when calling `volumes_volname_stop_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'volname' in local_var_params:
            path_params['volname'] = local_var_params['volname']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/volumes/{volname}/stop', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Volume',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)