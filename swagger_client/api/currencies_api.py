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


class CurrenciesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def currencies_delete(self, stewardname, currency, **kwargs):  # noqa: E501
        """Delete a currency  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.currencies_delete(stewardname, currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param str currency: Currency name (required)
        :param str authorization: Authorization Token
        :return: DeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.currencies_delete_with_http_info(stewardname, currency, **kwargs)  # noqa: E501
        else:
            (data) = self.currencies_delete_with_http_info(stewardname, currency, **kwargs)  # noqa: E501
            return data

    def currencies_delete_with_http_info(self, stewardname, currency, **kwargs):  # noqa: E501
        """Delete a currency  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.currencies_delete_with_http_info(stewardname, currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param str currency: Currency name (required)
        :param str authorization: Authorization Token
        :return: DeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stewardname', 'currency', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method currencies_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stewardname' is set
        if ('stewardname' not in params or
                params['stewardname'] is None):
            raise ValueError("Missing the required parameter `stewardname` when calling `currencies_delete`")  # noqa: E501
        # verify the required parameter 'currency' is set
        if ('currency' not in params or
                params['currency'] is None):
            raise ValueError("Missing the required parameter `currency` when calling `currencies_delete`")  # noqa: E501

        if 'stewardname' in params and not re.search(r'^[A-Za-z0-9_.-]+$', params['stewardname']):  # noqa: E501
            raise ValueError("Invalid value for parameter `stewardname` when calling `currencies_delete`, must conform to the pattern `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501
        if ('currency' in params and
                len(params['currency']) > 512):
            raise ValueError("Invalid value for parameter `currency` when calling `currencies_delete`, length must be less than or equal to `512`")  # noqa: E501
        if 'currency' in params and not re.search(r'^[A-Za-z0-9_.-]+$', params['currency']):  # noqa: E501
            raise ValueError("Invalid value for parameter `currency` when calling `currencies_delete`, must conform to the pattern `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501
        if 'authorization' in params and not re.search(r'^Bearer [A-Za-z0-9=\/+]+$', params['authorization']):  # noqa: E501
            raise ValueError("Invalid value for parameter `authorization` when calling `currencies_delete`, must conform to the pattern `/^Bearer [A-Za-z0-9=\/+]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'stewardname' in params:
            path_params['stewardname'] = params['stewardname']  # noqa: E501
        if 'currency' in params:
            path_params['currency'] = params['currency']  # noqa: E501

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
            '/stewards/{stewardname}/currencies/{currency}', 'DELETE',
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

    def currencies_get(self, stewardname, currency, **kwargs):  # noqa: E501
        """Get a currency by its name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.currencies_get(stewardname, currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param str currency: Name of a currency (required)
        :param str authorization: Authorization Token
        :return: CurrenciesGet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.currencies_get_with_http_info(stewardname, currency, **kwargs)  # noqa: E501
        else:
            (data) = self.currencies_get_with_http_info(stewardname, currency, **kwargs)  # noqa: E501
            return data

    def currencies_get_with_http_info(self, stewardname, currency, **kwargs):  # noqa: E501
        """Get a currency by its name  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.currencies_get_with_http_info(stewardname, currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param str currency: Name of a currency (required)
        :param str authorization: Authorization Token
        :return: CurrenciesGet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stewardname', 'currency', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method currencies_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stewardname' is set
        if ('stewardname' not in params or
                params['stewardname'] is None):
            raise ValueError("Missing the required parameter `stewardname` when calling `currencies_get`")  # noqa: E501
        # verify the required parameter 'currency' is set
        if ('currency' not in params or
                params['currency'] is None):
            raise ValueError("Missing the required parameter `currency` when calling `currencies_get`")  # noqa: E501

        if 'stewardname' in params and not re.search(r'^[A-Za-z0-9_.-]+$', params['stewardname']):  # noqa: E501
            raise ValueError("Invalid value for parameter `stewardname` when calling `currencies_get`, must conform to the pattern `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501
        if ('currency' in params and
                len(params['currency']) > 512):
            raise ValueError("Invalid value for parameter `currency` when calling `currencies_get`, length must be less than or equal to `512`")  # noqa: E501
        if 'currency' in params and not re.search(r'^[A-Za-z0-9_.-]+$', params['currency']):  # noqa: E501
            raise ValueError("Invalid value for parameter `currency` when calling `currencies_get`, must conform to the pattern `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501
        if 'authorization' in params and not re.search(r'^Bearer [A-Za-z0-9=\/+]+$', params['authorization']):  # noqa: E501
            raise ValueError("Invalid value for parameter `authorization` when calling `currencies_get`, must conform to the pattern `/^Bearer [A-Za-z0-9=\/+]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'stewardname' in params:
            path_params['stewardname'] = params['stewardname']  # noqa: E501
        if 'currency' in params:
            path_params['currency'] = params['currency']  # noqa: E501

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
            '/stewards/{stewardname}/currencies/{currency}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CurrenciesGet',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def currencies_list(self, stewardname, **kwargs):  # noqa: E501
        """Get a Listing currencies known by steward.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.currencies_list(stewardname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param str authorization: Authorization Token
        :param str namespace:
        :return: CurrenciesList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.currencies_list_with_http_info(stewardname, **kwargs)  # noqa: E501
        else:
            (data) = self.currencies_list_with_http_info(stewardname, **kwargs)  # noqa: E501
            return data

    def currencies_list_with_http_info(self, stewardname, **kwargs):  # noqa: E501
        """Get a Listing currencies known by steward.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.currencies_list_with_http_info(stewardname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param str authorization: Authorization Token
        :param str namespace:
        :return: CurrenciesList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stewardname', 'authorization', 'namespace']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method currencies_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stewardname' is set
        if ('stewardname' not in params or
                params['stewardname'] is None):
            raise ValueError("Missing the required parameter `stewardname` when calling `currencies_list`")  # noqa: E501

        if 'stewardname' in params and not re.search(r'^[A-Za-z0-9_.-]+$', params['stewardname']):  # noqa: E501
            raise ValueError("Invalid value for parameter `stewardname` when calling `currencies_list`, must conform to the pattern `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501
        if 'authorization' in params and not re.search(r'^Bearer [A-Za-z0-9=\/+]+$', params['authorization']):  # noqa: E501
            raise ValueError("Invalid value for parameter `authorization` when calling `currencies_list`, must conform to the pattern `/^Bearer [A-Za-z0-9=\/+]+$/`")  # noqa: E501
        if ('namespace' in params and
                len(params['namespace']) > 255):
            raise ValueError("Invalid value for parameter `namespace` when calling `currencies_list`, length must be less than or equal to `255`")  # noqa: E501
        if 'namespace' in params and not re.search(r'^[A-Za-z0-9_.-]+$', params['namespace']):  # noqa: E501
            raise ValueError("Invalid value for parameter `namespace` when calling `currencies_list`, must conform to the pattern `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'stewardname' in params:
            path_params['stewardname'] = params['stewardname']  # noqa: E501

        query_params = []
        if 'namespace' in params:
            query_params.append(('namespace', params['namespace']))  # noqa: E501

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
            '/stewards/{stewardname}/currencies', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CurrenciesList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def currencies_post(self, stewardname, **kwargs):  # noqa: E501
        """Create a currency  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.currencies_post(stewardname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param str authorization: Authorization Token
        :param CurrenciesRequest currency:
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.currencies_post_with_http_info(stewardname, **kwargs)  # noqa: E501
        else:
            (data) = self.currencies_post_with_http_info(stewardname, **kwargs)  # noqa: E501
            return data

    def currencies_post_with_http_info(self, stewardname, **kwargs):  # noqa: E501
        """Create a currency  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.currencies_post_with_http_info(stewardname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param str authorization: Authorization Token
        :param CurrenciesRequest currency:
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stewardname', 'authorization', 'currency']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method currencies_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stewardname' is set
        if ('stewardname' not in params or
                params['stewardname'] is None):
            raise ValueError("Missing the required parameter `stewardname` when calling `currencies_post`")  # noqa: E501

        if 'stewardname' in params and not re.search(r'^[A-Za-z0-9_.-]+$', params['stewardname']):  # noqa: E501
            raise ValueError("Invalid value for parameter `stewardname` when calling `currencies_post`, must conform to the pattern `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501
        if 'authorization' in params and not re.search(r'^Bearer [A-Za-z0-9=\/+]+$', params['authorization']):  # noqa: E501
            raise ValueError("Invalid value for parameter `authorization` when calling `currencies_post`, must conform to the pattern `/^Bearer [A-Za-z0-9=\/+]+$/`")  # noqa: E501
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
        if 'currency' in params:
            body_params = params['currency']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeySecurity', 'basicAuthenticationSecurity', 'oauth2AccessCodeSecurity', 'oauth2ApplicationSecurity', 'oauth2ImplicitSecurity', 'oauth2PasswordSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/stewards/{stewardname}/currencies', 'POST',
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

    def currencies_put(self, stewardname, currency, **kwargs):  # noqa: E501
        """Update a Currency  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.currencies_put(stewardname, currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param str currency: Name of a currency (required)
        :param str authorization: Authorization Token
        :param CurrenciesRequest currencies:
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.currencies_put_with_http_info(stewardname, currency, **kwargs)  # noqa: E501
        else:
            (data) = self.currencies_put_with_http_info(stewardname, currency, **kwargs)  # noqa: E501
            return data

    def currencies_put_with_http_info(self, stewardname, currency, **kwargs):  # noqa: E501
        """Update a Currency  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.currencies_put_with_http_info(stewardname, currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param str currency: Name of a currency (required)
        :param str authorization: Authorization Token
        :param CurrenciesRequest currencies:
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stewardname', 'currency', 'authorization', 'currencies']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method currencies_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stewardname' is set
        if ('stewardname' not in params or
                params['stewardname'] is None):
            raise ValueError("Missing the required parameter `stewardname` when calling `currencies_put`")  # noqa: E501
        # verify the required parameter 'currency' is set
        if ('currency' not in params or
                params['currency'] is None):
            raise ValueError("Missing the required parameter `currency` when calling `currencies_put`")  # noqa: E501

        if 'stewardname' in params and not re.search(r'^[A-Za-z0-9_.-]+$', params['stewardname']):  # noqa: E501
            raise ValueError("Invalid value for parameter `stewardname` when calling `currencies_put`, must conform to the pattern `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501
        if ('currency' in params and
                len(params['currency']) > 512):
            raise ValueError("Invalid value for parameter `currency` when calling `currencies_put`, length must be less than or equal to `512`")  # noqa: E501
        if 'currency' in params and not re.search(r'^[A-Za-z0-9_.-]+$', params['currency']):  # noqa: E501
            raise ValueError("Invalid value for parameter `currency` when calling `currencies_put`, must conform to the pattern `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501
        if 'authorization' in params and not re.search(r'^Bearer [A-Za-z0-9=\/+]+$', params['authorization']):  # noqa: E501
            raise ValueError("Invalid value for parameter `authorization` when calling `currencies_put`, must conform to the pattern `/^Bearer [A-Za-z0-9=\/+]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'stewardname' in params:
            path_params['stewardname'] = params['stewardname']  # noqa: E501
        if 'currency' in params:
            path_params['currency'] = params['currency']  # noqa: E501

        query_params = []

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'currencies' in params:
            body_params = params['currencies']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeySecurity', 'basicAuthenticationSecurity', 'oauth2AccessCodeSecurity', 'oauth2ApplicationSecurity', 'oauth2ImplicitSecurity', 'oauth2PasswordSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/stewards/{stewardname}/currencies/{currency}', 'PUT',
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
