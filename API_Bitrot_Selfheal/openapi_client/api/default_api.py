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

    def bitrot_disable(self, volname, **kwargs):  # noqa: E501
        """bitrot_disable  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bitrot_disable(volname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str volname: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.bitrot_disable_with_http_info(volname, **kwargs)  # noqa: E501
        else:
            (data) = self.bitrot_disable_with_http_info(volname, **kwargs)  # noqa: E501
            return data

    def bitrot_disable_with_http_info(self, volname, **kwargs):  # noqa: E501
        """bitrot_disable  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bitrot_disable_with_http_info(volname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str volname: (required)
        :return: None
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
                    " to method bitrot_disable" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'volname' is set
        if ('volname' not in local_var_params or
                local_var_params['volname'] is None):
            raise ValueError("Missing the required parameter `volname` when calling `bitrot_disable`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'volname' in local_var_params:
            path_params['volname'] = local_var_params['volname']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/volumes/{volname}/bitrot/disable', 'POST',
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

    def bitrot_enable(self, volname, **kwargs):  # noqa: E501
        """bitrot_enable  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bitrot_enable(volname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str volname: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.bitrot_enable_with_http_info(volname, **kwargs)  # noqa: E501
        else:
            (data) = self.bitrot_enable_with_http_info(volname, **kwargs)  # noqa: E501
            return data

    def bitrot_enable_with_http_info(self, volname, **kwargs):  # noqa: E501
        """bitrot_enable  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bitrot_enable_with_http_info(volname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str volname: (required)
        :return: None
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
                    " to method bitrot_enable" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'volname' is set
        if ('volname' not in local_var_params or
                local_var_params['volname'] is None):
            raise ValueError("Missing the required parameter `volname` when calling `bitrot_enable`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'volname' in local_var_params:
            path_params['volname'] = local_var_params['volname']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/volumes/{volname}/bitrot/enable', 'POST',
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

    def bitrot_scrub_ondemand(self, volname, **kwargs):  # noqa: E501
        """bitrot_scrub_ondemand  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bitrot_scrub_ondemand(volname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str volname: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.bitrot_scrub_ondemand_with_http_info(volname, **kwargs)  # noqa: E501
        else:
            (data) = self.bitrot_scrub_ondemand_with_http_info(volname, **kwargs)  # noqa: E501
            return data

    def bitrot_scrub_ondemand_with_http_info(self, volname, **kwargs):  # noqa: E501
        """bitrot_scrub_ondemand  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bitrot_scrub_ondemand_with_http_info(volname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str volname: (required)
        :return: None
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
                    " to method bitrot_scrub_ondemand" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'volname' is set
        if ('volname' not in local_var_params or
                local_var_params['volname'] is None):
            raise ValueError("Missing the required parameter `volname` when calling `bitrot_scrub_ondemand`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'volname' in local_var_params:
            path_params['volname'] = local_var_params['volname']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/volumes/{volname}/bitrot/scrubondemand', 'POST',
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

    def bitrot_scrub_status(self, volname, **kwargs):  # noqa: E501
        """bitrot_scrub_status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bitrot_scrub_status(volname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str volname: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.bitrot_scrub_status_with_http_info(volname, **kwargs)  # noqa: E501
        else:
            (data) = self.bitrot_scrub_status_with_http_info(volname, **kwargs)  # noqa: E501
            return data

    def bitrot_scrub_status_with_http_info(self, volname, **kwargs):  # noqa: E501
        """bitrot_scrub_status  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bitrot_scrub_status_with_http_info(volname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str volname: (required)
        :return: None
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
                    " to method bitrot_scrub_status" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'volname' is set
        if ('volname' not in local_var_params or
                local_var_params['volname'] is None):
            raise ValueError("Missing the required parameter `volname` when calling `bitrot_scrub_status`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'volname' in local_var_params:
            path_params['volname'] = local_var_params['volname']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/volumes/{volname}/bitrot/scrubstatus', 'GET',
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

    def self_heal(self, volname, **kwargs):  # noqa: E501
        """self_heal  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.self_heal(volname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str volname: (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.self_heal_with_http_info(volname, **kwargs)  # noqa: E501
        else:
            (data) = self.self_heal_with_http_info(volname, **kwargs)  # noqa: E501
            return data

    def self_heal_with_http_info(self, volname, **kwargs):  # noqa: E501
        """self_heal  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.self_heal_with_http_info(volname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str volname: (required)
        :return: None
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
                    " to method self_heal" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'volname' is set
        if ('volname' not in local_var_params or
                local_var_params['volname'] is None):
            raise ValueError("Missing the required parameter `volname` when calling `self_heal`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'volname' in local_var_params:
            path_params['volname'] = local_var_params['volname']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/volumes/{volname}/heal', 'POST',
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

    def self_heal_info(self, volname, opts, **kwargs):  # noqa: E501
        """self_heal_info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.self_heal_info(volname, opts, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str volname: (required)
        :param str opts: (required)
        :return: BrickHeal
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.self_heal_info_with_http_info(volname, opts, **kwargs)  # noqa: E501
        else:
            (data) = self.self_heal_info_with_http_info(volname, opts, **kwargs)  # noqa: E501
            return data

    def self_heal_info_with_http_info(self, volname, opts, **kwargs):  # noqa: E501
        """self_heal_info  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.self_heal_info_with_http_info(volname, opts, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str volname: (required)
        :param str opts: (required)
        :return: BrickHeal
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['volname', 'opts']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method self_heal_info" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'volname' is set
        if ('volname' not in local_var_params or
                local_var_params['volname'] is None):
            raise ValueError("Missing the required parameter `volname` when calling `self_heal_info`")  # noqa: E501
        # verify the required parameter 'opts' is set
        if ('opts' not in local_var_params or
                local_var_params['opts'] is None):
            raise ValueError("Missing the required parameter `opts` when calling `self_heal_info`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'volname' in local_var_params:
            path_params['volname'] = local_var_params['volname']  # noqa: E501
        if 'opts' in local_var_params:
            path_params['opts'] = local_var_params['opts']  # noqa: E501

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
            '/volumes/{volname}/{opts}/heal-info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BrickHeal',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def self_heal_info2(self, volname, **kwargs):  # noqa: E501
        """self_heal_info2  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.self_heal_info2(volname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str volname: (required)
        :return: BrickHeal
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.self_heal_info2_with_http_info(volname, **kwargs)  # noqa: E501
        else:
            (data) = self.self_heal_info2_with_http_info(volname, **kwargs)  # noqa: E501
            return data

    def self_heal_info2_with_http_info(self, volname, **kwargs):  # noqa: E501
        """self_heal_info2  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.self_heal_info2_with_http_info(volname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str volname: (required)
        :return: BrickHeal
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
                    " to method self_heal_info2" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']
        # verify the required parameter 'volname' is set
        if ('volname' not in local_var_params or
                local_var_params['volname'] is None):
            raise ValueError("Missing the required parameter `volname` when calling `self_heal_info2`")  # noqa: E501

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
            '/volumes/{volname}/heal-info', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='BrickHeal',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
