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


class JournalsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def journals_list(self, stewardname, **kwargs):  # noqa: E501
        """List Journal Entries for this accountname  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.journals_list(stewardname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param str authorization: Authorization Token
        :param str namespace:
        :param str account:
        :param str currency:
        :param str currency_namespace:
        :param int offset:
        :param int range:
        :return: JournalsList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.journals_list_with_http_info(stewardname, **kwargs)  # noqa: E501
        else:
            (data) = self.journals_list_with_http_info(stewardname, **kwargs)  # noqa: E501
            return data

    def journals_list_with_http_info(self, stewardname, **kwargs):  # noqa: E501
        """List Journal Entries for this accountname  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.journals_list_with_http_info(stewardname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param str authorization: Authorization Token
        :param str namespace:
        :param str account:
        :param str currency:
        :param str currency_namespace:
        :param int offset:
        :param int range:
        :return: JournalsList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stewardname', 'authorization', 'namespace', 'account', 'currency', 'currency_namespace', 'offset', 'range']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method journals_list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stewardname' is set
        if ('stewardname' not in params or
                params['stewardname'] is None):
            raise ValueError("Missing the required parameter `stewardname` when calling `journals_list`")  # noqa: E501

        if 'stewardname' in params and not re.search(r'^[A-Za-z0-9_.-]+$', params['stewardname']):  # noqa: E501
            raise ValueError("Invalid value for parameter `stewardname` when calling `journals_list`, must conform to the pattern `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501
        if 'authorization' in params and not re.search(r'^Bearer [A-Za-z0-9=\/+]+$', params['authorization']):  # noqa: E501
            raise ValueError("Invalid value for parameter `authorization` when calling `journals_list`, must conform to the pattern `/^Bearer [A-Za-z0-9=\/+]+$/`")  # noqa: E501
        if ('namespace' in params and
                len(params['namespace']) > 255):
            raise ValueError("Invalid value for parameter `namespace` when calling `journals_list`, length must be less than or equal to `255`")  # noqa: E501
        if 'namespace' in params and not re.search(r'^[A-Za-z0-9_.-]+$', params['namespace']):  # noqa: E501
            raise ValueError("Invalid value for parameter `namespace` when calling `journals_list`, must conform to the pattern `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501
        if ('account' in params and
                len(params['account']) > 255):
            raise ValueError("Invalid value for parameter `account` when calling `journals_list`, length must be less than or equal to `255`")  # noqa: E501
        if 'account' in params and not re.search(r'^[A-Za-z0-9_-]+$', params['account']):  # noqa: E501
            raise ValueError("Invalid value for parameter `account` when calling `journals_list`, must conform to the pattern `/^[A-Za-z0-9_-]+$/`")  # noqa: E501
        if ('currency' in params and
                len(params['currency']) > 255):
            raise ValueError("Invalid value for parameter `currency` when calling `journals_list`, length must be less than or equal to `255`")  # noqa: E501
        if 'currency' in params and not re.search(r'^[A-Za-z0-9_-]+$', params['currency']):  # noqa: E501
            raise ValueError("Invalid value for parameter `currency` when calling `journals_list`, must conform to the pattern `/^[A-Za-z0-9_-]+$/`")  # noqa: E501
        if ('currency_namespace' in params and
                len(params['currency_namespace']) > 255):
            raise ValueError("Invalid value for parameter `currency_namespace` when calling `journals_list`, length must be less than or equal to `255`")  # noqa: E501
        if 'currency_namespace' in params and not re.search(r'^[A-Za-z0-9_.-]*$', params['currency_namespace']):  # noqa: E501
            raise ValueError("Invalid value for parameter `currency_namespace` when calling `journals_list`, must conform to the pattern `/^[A-Za-z0-9_.-]*$/`")  # noqa: E501
        if 'offset' in params and params['offset'] < 0:  # noqa: E501
            raise ValueError("Invalid value for parameter `offset` when calling `journals_list`, must be a value greater than or equal to `0`")  # noqa: E501
        if 'range' in params and params['range'] < 5:  # noqa: E501
            raise ValueError("Invalid value for parameter `range` when calling `journals_list`, must be a value greater than or equal to `5`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'stewardname' in params:
            path_params['stewardname'] = params['stewardname']  # noqa: E501

        query_params = []
        if 'namespace' in params:
            query_params.append(('namespace', params['namespace']))  # noqa: E501
        if 'account' in params:
            query_params.append(('account', params['account']))  # noqa: E501
        if 'currency' in params:
            query_params.append(('currency', params['currency']))  # noqa: E501
        if 'currency_namespace' in params:
            query_params.append(('currency_namespace', params['currency_namespace']))  # noqa: E501
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501
        if 'range' in params:
            query_params.append(('range', params['range']))  # noqa: E501

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
            '/stewards/{stewardname}/journals', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='JournalsList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def journals_post(self, stewardname, namespace, account, currency, **kwargs):  # noqa: E501
        """Create a journal entry for this account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.journals_post(stewardname, namespace, account, currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param str namespace: (required)
        :param str account: (required)
        :param str currency: (required)
        :param str authorization: Authorization Token
        :param str currency_namespace:
        :param JournalsRequest journal:
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.journals_post_with_http_info(stewardname, namespace, account, currency, **kwargs)  # noqa: E501
        else:
            (data) = self.journals_post_with_http_info(stewardname, namespace, account, currency, **kwargs)  # noqa: E501
            return data

    def journals_post_with_http_info(self, stewardname, namespace, account, currency, **kwargs):  # noqa: E501
        """Create a journal entry for this account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.journals_post_with_http_info(stewardname, namespace, account, currency, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param str namespace: (required)
        :param str account: (required)
        :param str currency: (required)
        :param str authorization: Authorization Token
        :param str currency_namespace:
        :param JournalsRequest journal:
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stewardname', 'namespace', 'account', 'currency', 'authorization', 'currency_namespace', 'journal']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method journals_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stewardname' is set
        if ('stewardname' not in params or
                params['stewardname'] is None):
            raise ValueError("Missing the required parameter `stewardname` when calling `journals_post`")  # noqa: E501
        # verify the required parameter 'namespace' is set
        if ('namespace' not in params or
                params['namespace'] is None):
            raise ValueError("Missing the required parameter `namespace` when calling `journals_post`")  # noqa: E501
        # verify the required parameter 'account' is set
        if ('account' not in params or
                params['account'] is None):
            raise ValueError("Missing the required parameter `account` when calling `journals_post`")  # noqa: E501
        # verify the required parameter 'currency' is set
        if ('currency' not in params or
                params['currency'] is None):
            raise ValueError("Missing the required parameter `currency` when calling `journals_post`")  # noqa: E501

        if 'stewardname' in params and not re.search(r'^[A-Za-z0-9_.-]+$', params['stewardname']):  # noqa: E501
            raise ValueError("Invalid value for parameter `stewardname` when calling `journals_post`, must conform to the pattern `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501
        if ('namespace' in params and
                len(params['namespace']) > 255):
            raise ValueError("Invalid value for parameter `namespace` when calling `journals_post`, length must be less than or equal to `255`")  # noqa: E501
        if 'namespace' in params and not re.search(r'^[A-Za-z0-9_.-]+$', params['namespace']):  # noqa: E501
            raise ValueError("Invalid value for parameter `namespace` when calling `journals_post`, must conform to the pattern `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501
        if ('account' in params and
                len(params['account']) > 255):
            raise ValueError("Invalid value for parameter `account` when calling `journals_post`, length must be less than or equal to `255`")  # noqa: E501
        if 'account' in params and not re.search(r'^[A-Za-z0-9_.-]+$', params['account']):  # noqa: E501
            raise ValueError("Invalid value for parameter `account` when calling `journals_post`, must conform to the pattern `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501
        if ('currency' in params and
                len(params['currency']) > 255):
            raise ValueError("Invalid value for parameter `currency` when calling `journals_post`, length must be less than or equal to `255`")  # noqa: E501
        if 'currency' in params and not re.search(r'^[A-Za-z0-9_-]+$', params['currency']):  # noqa: E501
            raise ValueError("Invalid value for parameter `currency` when calling `journals_post`, must conform to the pattern `/^[A-Za-z0-9_-]+$/`")  # noqa: E501
        if 'authorization' in params and not re.search(r'^Bearer [A-Za-z0-9=\/+]+$', params['authorization']):  # noqa: E501
            raise ValueError("Invalid value for parameter `authorization` when calling `journals_post`, must conform to the pattern `/^Bearer [A-Za-z0-9=\/+]+$/`")  # noqa: E501
        if ('currency_namespace' in params and
                len(params['currency_namespace']) > 255):
            raise ValueError("Invalid value for parameter `currency_namespace` when calling `journals_post`, length must be less than or equal to `255`")  # noqa: E501
        if 'currency_namespace' in params and not re.search(r'^[A-Za-z0-9_.-]*$', params['currency_namespace']):  # noqa: E501
            raise ValueError("Invalid value for parameter `currency_namespace` when calling `journals_post`, must conform to the pattern `/^[A-Za-z0-9_.-]*$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'stewardname' in params:
            path_params['stewardname'] = params['stewardname']  # noqa: E501
        if 'namespace' in params:
            path_params['namespace'] = params['namespace']  # noqa: E501
        if 'account' in params:
            path_params['account'] = params['account']  # noqa: E501
        if 'currency' in params:
            path_params['currency'] = params['currency']  # noqa: E501

        query_params = []
        if 'currency_namespace' in params:
            query_params.append(('currency_namespace', params['currency_namespace']))  # noqa: E501

        header_params = {}
        if 'authorization' in params:
            header_params['Authorization'] = params['authorization']  # noqa: E501

        form_params = []
        local_var_files = {}

        body_params = None
        if 'journal' in params:
            body_params = params['journal']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeySecurity', 'basicAuthenticationSecurity', 'oauth2AccessCodeSecurity', 'oauth2ApplicationSecurity', 'oauth2ImplicitSecurity', 'oauth2PasswordSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/stewards/{stewardname}/namespaces/{namespace}/accounts/{account}/journals/{currency}', 'POST',
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