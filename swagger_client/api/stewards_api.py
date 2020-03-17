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


class StewardsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def stewards_delete(self, stewardname, **kwargs):  # noqa: E501
        """Delete a steward account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stewards_delete(stewardname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param str authorization:
        :return: DeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stewards_delete_with_http_info(stewardname, **kwargs)  # noqa: E501
        else:
            (data) = self.stewards_delete_with_http_info(stewardname, **kwargs)  # noqa: E501
            return data

    def stewards_delete_with_http_info(self, stewardname, **kwargs):  # noqa: E501
        """Delete a steward account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stewards_delete_with_http_info(stewardname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param str authorization:
        :return: DeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stewardname', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stewards_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stewardname' is set
        if ('stewardname' not in params or
                params['stewardname'] is None):
            raise ValueError("Missing the required parameter `stewardname` when calling `stewards_delete`")  # noqa: E501

        if ('stewardname' in params and
                len(params['stewardname']) > 1024):
            raise ValueError("Invalid value for parameter `stewardname` when calling `stewards_delete`, length must be less than or equal to `1024`")  # noqa: E501
        if 'stewardname' in params and not re.search(r'^[A-Za-z0-9_.-]+$', params['stewardname']):  # noqa: E501
            raise ValueError("Invalid value for parameter `stewardname` when calling `stewards_delete`, must conform to the pattern `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501
        if 'authorization' in params and not re.search(r'^Bearer [A-Za-z0-9=\/+]+$', params['authorization']):  # noqa: E501
            raise ValueError("Invalid value for parameter `authorization` when calling `stewards_delete`, must conform to the pattern `/^Bearer [A-Za-z0-9=\/+]+$/`")  # noqa: E501
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeySecurity', 'basicAuthenticationSecurity', 'oauth2AccessCodeSecurity', 'oauth2ApplicationSecurity', 'oauth2ImplicitSecurity', 'oauth2PasswordSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/stewards/{stewardname}', 'DELETE',
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

    def stewards_forgot_post(self, forgot_request, **kwargs):  # noqa: E501
        """Forgot password or stewardname request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stewards_forgot_post(forgot_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ForgotRequest forgot_request: Forgot Password Request (required)
        :return: ForgotResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stewards_forgot_post_with_http_info(forgot_request, **kwargs)  # noqa: E501
        else:
            (data) = self.stewards_forgot_post_with_http_info(forgot_request, **kwargs)  # noqa: E501
            return data

    def stewards_forgot_post_with_http_info(self, forgot_request, **kwargs):  # noqa: E501
        """Forgot password or stewardname request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stewards_forgot_post_with_http_info(forgot_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ForgotRequest forgot_request: Forgot Password Request (required)
        :return: ForgotResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['forgot_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stewards_forgot_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'forgot_request' is set
        if ('forgot_request' not in params or
                params['forgot_request'] is None):
            raise ValueError("Missing the required parameter `forgot_request` when calling `stewards_forgot_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'forgot_request' in params:
            body_params = params['forgot_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/stewards/forgot', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ForgotResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def stewards_get(self, stewardname, **kwargs):  # noqa: E501
        """Get a single steward  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stewards_get(stewardname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param str authorization:
        :return: StewardsGet
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stewards_get_with_http_info(stewardname, **kwargs)  # noqa: E501
        else:
            (data) = self.stewards_get_with_http_info(stewardname, **kwargs)  # noqa: E501
            return data

    def stewards_get_with_http_info(self, stewardname, **kwargs):  # noqa: E501
        """Get a single steward  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stewards_get_with_http_info(stewardname, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param str authorization:
        :return: StewardsGet
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stewardname', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stewards_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stewardname' is set
        if ('stewardname' not in params or
                params['stewardname'] is None):
            raise ValueError("Missing the required parameter `stewardname` when calling `stewards_get`")  # noqa: E501

        if ('stewardname' in params and
                len(params['stewardname']) > 255):
            raise ValueError("Invalid value for parameter `stewardname` when calling `stewards_get`, length must be less than or equal to `255`")  # noqa: E501
        if 'stewardname' in params and not re.search(r'^[A-Za-z0-9_.-]+$', params['stewardname']):  # noqa: E501
            raise ValueError("Invalid value for parameter `stewardname` when calling `stewards_get`, must conform to the pattern `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501
        if 'authorization' in params and not re.search(r'^Bearer [A-Za-z0-9=\/+]+$', params['authorization']):  # noqa: E501
            raise ValueError("Invalid value for parameter `authorization` when calling `stewards_get`, must conform to the pattern `/^Bearer [A-Za-z0-9=\/+]+$/`")  # noqa: E501
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeySecurity', 'basicAuthenticationSecurity', 'oauth2AccessCodeSecurity', 'oauth2ApplicationSecurity', 'oauth2ImplicitSecurity', 'oauth2PasswordSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/stewards/{stewardname}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StewardsGet',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def stewards_list(self, **kwargs):  # noqa: E501
        """Get a listing of known stewards  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stewards_list(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization:
        :return: StewardsList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stewards_list_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.stewards_list_with_http_info(**kwargs)  # noqa: E501
            return data

    def stewards_list_with_http_info(self, **kwargs):  # noqa: E501
        """Get a listing of known stewards  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stewards_list_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str authorization:
        :return: StewardsList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stewards_list" % key
                )
            params[key] = val
        del params['kwargs']

        if 'authorization' in params and not re.search(r'^Bearer [A-Za-z0-9\/+=.]+$', params['authorization']):  # noqa: E501
            raise ValueError("Invalid value for parameter `authorization` when calling `stewards_list`, must conform to the pattern `/^Bearer [A-Za-z0-9\/+=.]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}

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
            '/stewards', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StewardsList',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def stewards_post(self, register_request, **kwargs):  # noqa: E501
        """Register a steward on the system  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stewards_post(register_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RegisterRequest register_request: Registration Request (required)
        :return: RegisterResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stewards_post_with_http_info(register_request, **kwargs)  # noqa: E501
        else:
            (data) = self.stewards_post_with_http_info(register_request, **kwargs)  # noqa: E501
            return data

    def stewards_post_with_http_info(self, register_request, **kwargs):  # noqa: E501
        """Register a steward on the system  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stewards_post_with_http_info(register_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RegisterRequest register_request: Registration Request (required)
        :return: RegisterResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['register_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stewards_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'register_request' is set
        if ('register_request' not in params or
                params['register_request'] is None):
            raise ValueError("Missing the required parameter `register_request` when calling `stewards_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'register_request' in params:
            body_params = params['register_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/stewards', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RegisterResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def stewards_put(self, stewardname, steward, **kwargs):  # noqa: E501
        """Update a steward account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stewards_put(stewardname, steward, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param StewardsRequest steward: Steward Document (required)
        :param str authorization:
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stewards_put_with_http_info(stewardname, steward, **kwargs)  # noqa: E501
        else:
            (data) = self.stewards_put_with_http_info(stewardname, steward, **kwargs)  # noqa: E501
            return data

    def stewards_put_with_http_info(self, stewardname, steward, **kwargs):  # noqa: E501
        """Update a steward account  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stewards_put_with_http_info(stewardname, steward, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param StewardsRequest steward: Steward Document (required)
        :param str authorization:
        :return: CreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stewardname', 'steward', 'authorization']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stewards_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stewardname' is set
        if ('stewardname' not in params or
                params['stewardname'] is None):
            raise ValueError("Missing the required parameter `stewardname` when calling `stewards_put`")  # noqa: E501
        # verify the required parameter 'steward' is set
        if ('steward' not in params or
                params['steward'] is None):
            raise ValueError("Missing the required parameter `steward` when calling `stewards_put`")  # noqa: E501

        if ('stewardname' in params and
                len(params['stewardname']) > 255):
            raise ValueError("Invalid value for parameter `stewardname` when calling `stewards_put`, length must be less than or equal to `255`")  # noqa: E501
        if 'stewardname' in params and not re.search(r'^[A-Za-z0-9_.-]+$', params['stewardname']):  # noqa: E501
            raise ValueError("Invalid value for parameter `stewardname` when calling `stewards_put`, must conform to the pattern `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501
        if 'authorization' in params and not re.search(r'^Bearer [A-Za-z0-9=\/+]+$', params['authorization']):  # noqa: E501
            raise ValueError("Invalid value for parameter `authorization` when calling `stewards_put`, must conform to the pattern `/^Bearer [A-Za-z0-9=\/+]+$/`")  # noqa: E501
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
        if 'steward' in params:
            body_params = params['steward']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['apiKeySecurity', 'basicAuthenticationSecurity', 'oauth2AccessCodeSecurity', 'oauth2ApplicationSecurity', 'oauth2ImplicitSecurity', 'oauth2PasswordSecurity']  # noqa: E501

        return self.api_client.call_api(
            '/stewards/{stewardname}', 'PUT',
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

    def stewards_reset_post(self, stewardname, reset_request, **kwargs):  # noqa: E501
        """Reset password request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stewards_reset_post(stewardname, reset_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param ResetRequest reset_request: Reset Password Request (required)
        :return: ResetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.stewards_reset_post_with_http_info(stewardname, reset_request, **kwargs)  # noqa: E501
        else:
            (data) = self.stewards_reset_post_with_http_info(stewardname, reset_request, **kwargs)  # noqa: E501
            return data

    def stewards_reset_post_with_http_info(self, stewardname, reset_request, **kwargs):  # noqa: E501
        """Reset password request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.stewards_reset_post_with_http_info(stewardname, reset_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str stewardname: (required)
        :param ResetRequest reset_request: Reset Password Request (required)
        :return: ResetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['stewardname', 'reset_request']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method stewards_reset_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'stewardname' is set
        if ('stewardname' not in params or
                params['stewardname'] is None):
            raise ValueError("Missing the required parameter `stewardname` when calling `stewards_reset_post`")  # noqa: E501
        # verify the required parameter 'reset_request' is set
        if ('reset_request' not in params or
                params['reset_request'] is None):
            raise ValueError("Missing the required parameter `reset_request` when calling `stewards_reset_post`")  # noqa: E501

        if ('stewardname' in params and
                len(params['stewardname']) > 255):
            raise ValueError("Invalid value for parameter `stewardname` when calling `stewards_reset_post`, length must be less than or equal to `255`")  # noqa: E501
        if 'stewardname' in params and not re.search(r'^[A-Za-z0-9_.-]+$', params['stewardname']):  # noqa: E501
            raise ValueError("Invalid value for parameter `stewardname` when calling `stewards_reset_post`, must conform to the pattern `/^[A-Za-z0-9_.-]+$/`")  # noqa: E501
        collection_formats = {}

        path_params = {}
        if 'stewardname' in params:
            path_params['stewardname'] = params['stewardname']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'reset_request' in params:
            body_params = params['reset_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/html'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/stewards/{stewardname}/reset', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ResetResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
