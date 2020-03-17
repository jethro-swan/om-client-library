# coding: utf-8

"""
    Openmoney API

    Openmoney API  # noqa: E501

    OpenAPI spec version: 2.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class NamespacesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def spaces_delete(self, stewardname, namespace, **kwargs):  # noqa: E501
        """spaces_delete  # noqa: E501

        Delete a namespace  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.spaces_delete(stewardname, namespace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param str namespace: namespace name (required)
        :param str authorization: Authorization Token
        :return: DeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.spaces_delete_with_http_info(stewardname, namespace, **kwargs)  # noqa: E501
        else:
            (data) = self.spaces_delete_with_http_info(stewardname, namespace, **kwargs)  # noqa: E501
            return data

    def spaces_delete_with_http_info(self, stewardname, namespace, **kwargs):  # noqa: E501
        """spaces_delete  # noqa: E501

        Delete a namespace  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.spaces_delete_with_http_info(stewardname, namespace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param str namespace: namespace name (required)
        :param str authorization: Authorization Token
        :return: DeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stewardname', 'namespace', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method spaces_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stewardname' is set
        if ('stewardname' not in params or
                params['stewardname'] is None):
            raise ValueError("Missing the required parameter `stewardname` when calling `spaces_delete`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `spaces_delete`")  # noqa: E501

        if 'stewardname' in params and not re.search(r'^[A-Za-z0-9_.-]+$', params['stewardname']):  # noqa: E501
            raise ValueError("Invalid value for parameter `stewardname` when calling `spaces_delete`, must conform to the pattern `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501
        if ('namespace' in params and
                len(params['namespace']) > 1048):
            raise ValueError("Invalid value for parameter `namespace` when calling `spaces_delete`, length must be less than or equal to `1048`")  # noqa: E501
        if 'namespace' in params and not re.search(r'^[A-Za-z0-9_.-]+$', params['namespace']):  # noqa: E501
            raise ValueError("Invalid value for parameter `namespace` when calling `spaces_delete`, must conform to the pattern `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501
        if 'authorization' in params and not re.search(r'^Bearer [A-Za-z0-9=\/+]+$', params['authorization']):  # noqa: E501
            raise ValueError("Invalid value for parameter `authorization` when calling `spaces_delete`, must conform to the pattern `/^Bearer [A-Za-z0-9=\/+]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'stewardname' in params:
            path_params['stewardname'] = params['stewardname']  # noqa: E501
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeySecurity', 'basicAuthenticationSecurity', 'oauth2AccessCodeSecurity', 'oauth2ApplicationSecurity', 'oauth2ImplicitSecurity', 'oauth2PasswordSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/stewards/{stewardname}/namespaces/{namespace}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeleteResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def spaces_get(self, stewardname, namespace, **kwargs):  # noqa: E501
        """Get a namespace by it's name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.spaces_get(stewardname, namespace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param str namespace: space name (required)
        :param str authorization: Authorization Token
        :return: NamespacesGet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.spaces_get_with_http_info(stewardname, namespace, **kwargs)  # noqa: E501
        else:
            (data) = self.spaces_get_with_http_info(stewardname, namespace, **kwargs)  # noqa: E501
            return data

    def spaces_get_with_http_info(self, stewardname, namespace, **kwargs):  # noqa: E501
        """Get a namespace by it's name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.spaces_get_with_http_info(stewardname, namespace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param str namespace: space name (required)
        :param str authorization: Authorization Token
        :return: NamespacesGet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stewardname', 'namespace', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method spaces_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stewardname' is set
        if ('stewardname' not in params or
                params['stewardname'] is None):
            raise ValueError("Missing the required parameter `stewardname` when calling `spaces_get`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `spaces_get`")  # noqa: E501

        if 'stewardname' in params and not re.search(r'^[A-Za-z0-9_.-]+$', params['stewardname']):  # noqa: E501
            raise ValueError("Invalid value for parameter `stewardname` when calling `spaces_get`, must conform to the pattern `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501
        if ('namespace' in params and
                len(params['namespace']) > 255):
            raise ValueError("Invalid value for parameter `namespace` when calling `spaces_get`, length must be less than or equal to `255`")  # noqa: E501
        if 'namespace' in params and not re.search(r'^[A-Za-z0-9_.-]+$', params['namespace']):  # noqa: E501
            raise ValueError("Invalid value for parameter `namespace` when calling `spaces_get`, must conform to the pattern `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501
        if 'authorization' in params and not re.search(r'^Bearer [A-Za-z0-9=\/+]+$', params['authorization']):  # noqa: E501
            raise ValueError("Invalid value for parameter `authorization` when calling `spaces_get`, must conform to the pattern `/^Bearer [A-Za-z0-9=\/+]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'stewardname' in params:
            path_params['stewardname'] = params['stewardname']  # noqa: E501
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeySecurity', 'basicAuthenticationSecurity', 'oauth2AccessCodeSecurity', 'oauth2ApplicationSecurity', 'oauth2ImplicitSecurity', 'oauth2PasswordSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/stewards/{stewardname}/namespaces/{namespace}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NamespacesGet',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def spaces_list(self, stewardname, **kwargs):  # noqa: E501
        """Get a Listing of namespaces known by steward.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.spaces_list(stewardname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param str authorization: Authorization Token
        :param str parent_namespace:
        :return: NamespacesList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.spaces_list_with_http_info(stewardname, **kwargs)  # noqa: E501
        else:
            (data) = self.spaces_list_with_http_info(stewardname, **kwargs)  # noqa: E501
            return data

    def spaces_list_with_http_info(self, stewardname, **kwargs):  # noqa: E501
        """Get a Listing of namespaces known by steward.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.spaces_list_with_http_info(stewardname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param str authorization: Authorization Token
        :param str parent_namespace:
        :return: NamespacesList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stewardname', 'authorization', 'parent_namespace']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method spaces_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stewardname' is set
        if ('stewardname' not in params or
                params['stewardname'] is None):
            raise ValueError("Missing the required parameter `stewardname` when calling `spaces_list`")  # noqa: E501

        if 'stewardname' in params and not re.search(r'^[A-Za-z0-9_.-]+$', params['stewardname']):  # noqa: E501
            raise ValueError("Invalid value for parameter `stewardname` when calling `spaces_list`, must conform to the pattern `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501
        if 'authorization' in params and not re.search(r'^Bearer [A-Za-z0-9=\/+]+$', params['authorization']):  # noqa: E501
            raise ValueError("Invalid value for parameter `authorization` when calling `spaces_list`, must conform to the pattern `/^Bearer [A-Za-z0-9=\/+]+$/`")  # noqa: E501
        if ('parent_namespace' in params and
                len(params['parent_namespace']) > 255):
            raise ValueError("Invalid value for parameter `parent_namespace` when calling `spaces_list`, length must be less than or equal to `255`")  # noqa: E501
        if 'parent_namespace' in params and not re.search(r'^[A-Za-z0-9_.-]+$', params['parent_namespace']):  # noqa: E501
            raise ValueError("Invalid value for parameter `parent_namespace` when calling `spaces_list`, must conform to the pattern `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'stewardname' in params:
            path_params['stewardname'] = params['stewardname']  # noqa: E501

        query_params = []
        if 'parent_namespace' in params:
            query_params.append(('parent_namespace', params['parent_namespace']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeySecurity', 'basicAuthenticationSecurity', 'oauth2AccessCodeSecurity', 'oauth2ApplicationSecurity', 'oauth2ImplicitSecurity', 'oauth2PasswordSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/stewards/{stewardname}/namespaces', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='NamespacesList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def spaces_post(self, stewardname, space, **kwargs):  # noqa: E501
        """Create a namespace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.spaces_post(stewardname, space, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param NamespacesRequest space: (required)
        :param str authorization: Authorization Token
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.spaces_post_with_http_info(stewardname, space, **kwargs)  # noqa: E501
        else:
            (data) = self.spaces_post_with_http_info(stewardname, space, **kwargs)  # noqa: E501
            return data

    def spaces_post_with_http_info(self, stewardname, space, **kwargs):  # noqa: E501
        """Create a namespace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.spaces_post_with_http_info(stewardname, space, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param NamespacesRequest space: (required)
        :param str authorization: Authorization Token
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stewardname', 'space', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method spaces_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stewardname' is set
        if ('stewardname' not in params or
                params['stewardname'] is None):
            raise ValueError("Missing the required parameter `stewardname` when calling `spaces_post`")  # noqa: E501
        # verify the required parameter 'space' is set
        if ('space' not in params or
                params['space'] is None):
            raise ValueError("Missing the required parameter `space` when calling `spaces_post`")  # noqa: E501

        if 'stewardname' in params and not re.search(r'^[A-Za-z0-9_.-]+$', params['stewardname']):  # noqa: E501
            raise ValueError("Invalid value for parameter `stewardname` when calling `spaces_post`, must conform to the pattern `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501
        if 'authorization' in params and not re.search(r'^Bearer [A-Za-z0-9=\/+]+$', params['authorization']):  # noqa: E501
            raise ValueError("Invalid value for parameter `authorization` when calling `spaces_post`, must conform to the pattern `/^Bearer [A-Za-z0-9=\/+]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'stewardname' in params:
            path_params['stewardname'] = params['stewardname']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'space' in params:
            body_params = params['space']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeySecurity', 'basicAuthenticationSecurity', 'oauth2AccessCodeSecurity', 'oauth2ApplicationSecurity', 'oauth2ImplicitSecurity', 'oauth2PasswordSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/stewards/{stewardname}/namespaces', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def spaces_put(self, stewardname, namespace, **kwargs):  # noqa: E501
        """Update a namespace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.spaces_put(stewardname, namespace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param str namespace: space name (required)
        :param str authorization: Authorization Token
        :param NamespacesRequest space:
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.spaces_put_with_http_info(stewardname, namespace, **kwargs)  # noqa: E501
        else:
            (data) = self.spaces_put_with_http_info(stewardname, namespace, **kwargs)  # noqa: E501
            return data

    def spaces_put_with_http_info(self, stewardname, namespace, **kwargs):  # noqa: E501
        """Update a namespace  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.spaces_put_with_http_info(stewardname, namespace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param str namespace: space name (required)
        :param str authorization: Authorization Token
        :param NamespacesRequest space:
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stewardname', 'namespace', 'authorization', 'space']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method spaces_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stewardname' is set
        if ('stewardname' not in params or
                params['stewardname'] is None):
            raise ValueError("Missing the required parameter `stewardname` when calling `spaces_put`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `spaces_put`")  # noqa: E501

        if 'stewardname' in params and not re.search(r'^[A-Za-z0-9_.-]+$', params['stewardname']):  # noqa: E501
            raise ValueError("Invalid value for parameter `stewardname` when calling `spaces_put`, must conform to the pattern `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501
        if ('namespace' in params and
                len(params['namespace']) > 512):
            raise ValueError("Invalid value for parameter `namespace` when calling `spaces_put`, length must be less than or equal to `512`")  # noqa: E501
        if 'namespace' in params and not re.search(r'^[A-Za-z0-9_.-]+$', params['namespace']):  # noqa: E501
            raise ValueError("Invalid value for parameter `namespace` when calling `spaces_put`, must conform to the pattern `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501
        if 'authorization' in params and not re.search(r'^Bearer [A-Za-z0-9=\/+]+$', params['authorization']):  # noqa: E501
            raise ValueError("Invalid value for parameter `authorization` when calling `spaces_put`, must conform to the pattern `/^Bearer [A-Za-z0-9=\/+]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'stewardname' in params:
            path_params['stewardname'] = params['stewardname']  # noqa: E501
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'space' in params:
            body_params = params['space']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeySecurity', 'basicAuthenticationSecurity', 'oauth2AccessCodeSecurity', 'oauth2ApplicationSecurity', 'oauth2ImplicitSecurity', 'oauth2PasswordSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/stewards/{stewardname}/namespaces/{namespace}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
