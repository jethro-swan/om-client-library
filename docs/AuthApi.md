# swagger_client.AuthApi

All URIs are relative to *https://om-api-dev.lrc.org.uk/V2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**account_get**](AuthApi.md#account_get) | **GET** /stewards/{stewardname}/account | Get Steward account information
[**login_get**](AuthApi.md#login_get) | **GET** /stewards/{stewardname}/login | Login Page for the steward
[**login_post**](AuthApi.md#login_post) | **POST** /stewards/{stewardname}/login | Login steward
[**logout_post**](AuthApi.md#logout_post) | **GET** /stewards/{stewardname}/logout | Logout steward
[**oauth_access_token_post**](AuthApi.md#oauth_access_token_post) | **POST** /stewards/{stewardname}/oauth/token | Exchanges the user or client credentials for an access token used to access resources.
[**oauth_application_post**](AuthApi.md#oauth_application_post) | **POST** /stewards/{stewardname}/oauth/application | Create an application for a client_id and client_secret for oauth token authorization.
[**oauth_dialoge_get**](AuthApi.md#oauth_dialoge_get) | **GET** /stewards/{stewardname}/dialog/authorize | Implicit authorization dialog presented to steward to authorize client_id to access API resources on their behalf.
[**oauth_dialoge_post**](AuthApi.md#oauth_dialoge_post) | **POST** /stewards/{stewardname}/dialog/authorize/decision | Authorizes a steward on the openmoney network


# **account_get**
> str account_get(stewardname)

Get Steward account information

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
stewardname = 'stewardname_example' # str | 

try:
    # Get Steward account information
    api_response = api_instance.account_get(stewardname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->account_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_get**
> str login_get(stewardname)

Login Page for the steward

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
stewardname = 'stewardname_example' # str | 

try:
    # Login Page for the steward
    api_response = api_instance.login_get(stewardname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->login_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_post**
> login_post(stewardname, authorization=authorization)

Login steward

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
stewardname = 'stewardname_example' # str | 
authorization = 'authorization_example' # str |  (optional)

try:
    # Login steward
    api_instance.login_post(stewardname, authorization=authorization)
except ApiException as e:
    print("Exception when calling AuthApi->login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: text/plain

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **logout_post**
> logout_post(stewardname)

Logout steward

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
stewardname = 'stewardname_example' # str | 

try:
    # Logout steward
    api_instance.logout_post(stewardname)
except ApiException as e:
    print("Exception when calling AuthApi->logout_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_access_token_post**
> TokenResponse oauth_access_token_post(stewardname, access_token_request, authorization=authorization)

Exchanges the user or client credentials for an access token used to access resources.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuthenticationSecurity
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure API key authorization: oauth2Refresh
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
stewardname = 'stewardname_example' # str | 
access_token_request = swagger_client.AccessTokenRequest() # AccessTokenRequest | Access Token Request Object
authorization = 'authorization_example' # str |  (optional)

try:
    # Exchanges the user or client credentials for an access token used to access resources.
    api_response = api_instance.oauth_access_token_post(stewardname, access_token_request, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->oauth_access_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 
 **access_token_request** | [**AccessTokenRequest**](AccessTokenRequest.md)| Access Token Request Object | 
 **authorization** | **str**|  | [optional] 

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

[basicAuthenticationSecurity](../README.md#basicAuthenticationSecurity), [oauth2Refresh](../README.md#oauth2Refresh)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_application_post**
> ApplicationResponse oauth_application_post(stewardname, application, authorization=authorization)

Create an application for a client_id and client_secret for oauth token authorization.

Existing steward Registers an application with the openmoney network.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure HTTP basic authorization: basicAuthenticationSecurity
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.AuthApi(swagger_client.ApiClient(configuration))
stewardname = 'stewardname_example' # str | 
application = swagger_client.ApplicationRequest() # ApplicationRequest | Application Object
authorization = 'authorization_example' # str |  (optional)

try:
    # Create an application for a client_id and client_secret for oauth token authorization.
    api_response = api_instance.oauth_application_post(stewardname, application, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->oauth_application_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 
 **application** | [**ApplicationRequest**](ApplicationRequest.md)| Application Object | 
 **authorization** | **str**|  | [optional] 

### Return type

[**ApplicationResponse**](ApplicationResponse.md)

### Authorization

[basicAuthenticationSecurity](../README.md#basicAuthenticationSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_dialoge_get**
> ErrorModel oauth_dialoge_get(stewardname, client_id, redirect_uri=redirect_uri, scopes=scopes)

Implicit authorization dialog presented to steward to authorize client_id to access API resources on their behalf.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
stewardname = 'stewardname_example' # str | 
client_id = 'client_id_example' # str | Client ID received during registration
redirect_uri = 'redirect_uri_example' # str | A uri to redirect steward after authorization (optional)
scopes = ['scopes_example'] # list[str] | A comma separated list of scopes. If not provided, scope defaults to an empty list of scopes for stewards that don’t have a valid token for the app. For stewards who do already have a valid token for the app, the steward won’t be shown the OAuth authorization page with the list of scopes. Instead, this step of the flow will automatically complete with the same scopes that were used last time the steward completed the flow. (optional)

try:
    # Implicit authorization dialog presented to steward to authorize client_id to access API resources on their behalf.
    api_response = api_instance.oauth_dialoge_get(stewardname, client_id, redirect_uri=redirect_uri, scopes=scopes)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->oauth_dialoge_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 
 **client_id** | **str**| Client ID received during registration | 
 **redirect_uri** | **str**| A uri to redirect steward after authorization | [optional] 
 **scopes** | [**list[str]**](str.md)| A comma separated list of scopes. If not provided, scope defaults to an empty list of scopes for stewards that don’t have a valid token for the app. For stewards who do already have a valid token for the app, the steward won’t be shown the OAuth authorization page with the list of scopes. Instead, this step of the flow will automatically complete with the same scopes that were used last time the steward completed the flow. | [optional] 

### Return type

[**ErrorModel**](ErrorModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_dialoge_post**
> ErrorModel oauth_dialoge_post(stewardname, oauth_authorize_request)

Authorizes a steward on the openmoney network

Authorization dialoge decision with allowed scopes.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AuthApi()
stewardname = 'stewardname_example' # str | 
oauth_authorize_request = swagger_client.OauthAuthorizeRequest() # OauthAuthorizeRequest | 

try:
    # Authorizes a steward on the openmoney network
    api_response = api_instance.oauth_dialoge_post(stewardname, oauth_authorize_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthApi->oauth_dialoge_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 
 **oauth_authorize_request** | [**OauthAuthorizeRequest**](OauthAuthorizeRequest.md)|  | 

### Return type

[**ErrorModel**](ErrorModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

