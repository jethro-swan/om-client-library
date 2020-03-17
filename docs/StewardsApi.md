# swagger_client.StewardsApi

All URIs are relative to *https://om-12.lrc.org.uk/V2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stewards_delete**](StewardsApi.md#stewards_delete) | **DELETE** /stewards/{stewardname} | Delete a steward account
[**stewards_forgot_post**](StewardsApi.md#stewards_forgot_post) | **POST** /stewards/forgot | Forgot password or stewardname request
[**stewards_get**](StewardsApi.md#stewards_get) | **GET** /stewards/{stewardname} | Get a single steward
[**stewards_list**](StewardsApi.md#stewards_list) | **GET** /stewards | Get a listing of known stewards
[**stewards_post**](StewardsApi.md#stewards_post) | **POST** /stewards | Register a steward on the system
[**stewards_put**](StewardsApi.md#stewards_put) | **PUT** /stewards/{stewardname} | Update a steward account
[**stewards_reset_post**](StewardsApi.md#stewards_reset_post) | **POST** /stewards/{stewardname}/reset | Reset password request


# **stewards_delete**
> DeleteResponse stewards_delete(stewardname, authorization=authorization)

Delete a steward account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeySecurity
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: basicAuthenticationSecurity
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: oauth2AccessCodeSecurity
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2ApplicationSecurity
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2ImplicitSecurity
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2PasswordSecurity
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.StewardsApi(swagger_client.ApiClient(configuration))
stewardname = 'stewardname_example' # str | 
authorization = 'authorization_example' # str |  (optional)

try:
    # Delete a steward account
    api_response = api_instance.stewards_delete(stewardname, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StewardsApi->stewards_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [basicAuthenticationSecurity](../README.md#basicAuthenticationSecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity), [oauth2ImplicitSecurity](../README.md#oauth2ImplicitSecurity), [oauth2PasswordSecurity](../README.md#oauth2PasswordSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stewards_forgot_post**
> ForgotResponse stewards_forgot_post(forgot_request)

Forgot password or stewardname request

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StewardsApi()
forgot_request = swagger_client.ForgotRequest() # ForgotRequest | Forgot Password Request

try:
    # Forgot password or stewardname request
    api_response = api_instance.stewards_forgot_post(forgot_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StewardsApi->stewards_forgot_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **forgot_request** | [**ForgotRequest**](ForgotRequest.md)| Forgot Password Request | 

### Return type

[**ForgotResponse**](ForgotResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stewards_get**
> StewardsGet stewards_get(stewardname, authorization=authorization)

Get a single steward

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeySecurity
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: basicAuthenticationSecurity
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: oauth2AccessCodeSecurity
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2ApplicationSecurity
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2ImplicitSecurity
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2PasswordSecurity
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.StewardsApi(swagger_client.ApiClient(configuration))
stewardname = 'stewardname_example' # str | 
authorization = 'authorization_example' # str |  (optional)

try:
    # Get a single steward
    api_response = api_instance.stewards_get(stewardname, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StewardsApi->stewards_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 
 **authorization** | **str**|  | [optional] 

### Return type

[**StewardsGet**](StewardsGet.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [basicAuthenticationSecurity](../README.md#basicAuthenticationSecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity), [oauth2ImplicitSecurity](../README.md#oauth2ImplicitSecurity), [oauth2PasswordSecurity](../README.md#oauth2PasswordSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stewards_list**
> StewardsList stewards_list(authorization=authorization)

Get a listing of known stewards

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeySecurity
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: basicAuthenticationSecurity
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: oauth2AccessCodeSecurity
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2ApplicationSecurity
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2ImplicitSecurity
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2PasswordSecurity
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.StewardsApi(swagger_client.ApiClient(configuration))
authorization = 'authorization_example' # str |  (optional)

try:
    # Get a listing of known stewards
    api_response = api_instance.stewards_list(authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StewardsApi->stewards_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **authorization** | **str**|  | [optional] 

### Return type

[**StewardsList**](StewardsList.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [basicAuthenticationSecurity](../README.md#basicAuthenticationSecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity), [oauth2ImplicitSecurity](../README.md#oauth2ImplicitSecurity), [oauth2PasswordSecurity](../README.md#oauth2PasswordSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stewards_post**
> RegisterResponse stewards_post(register_request)

Register a steward on the system

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StewardsApi()
register_request = swagger_client.RegisterRequest() # RegisterRequest | Registration Request

try:
    # Register a steward on the system
    api_response = api_instance.stewards_post(register_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StewardsApi->stewards_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **register_request** | [**RegisterRequest**](RegisterRequest.md)| Registration Request | 

### Return type

[**RegisterResponse**](RegisterResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stewards_put**
> CreateResponse stewards_put(stewardname, steward, authorization=authorization)

Update a steward account

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKeySecurity
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: basicAuthenticationSecurity
configuration = swagger_client.Configuration()
configuration.username = 'YOUR_USERNAME'
configuration.password = 'YOUR_PASSWORD'
# Configure OAuth2 access token for authorization: oauth2AccessCodeSecurity
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2ApplicationSecurity
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2ImplicitSecurity
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'
# Configure OAuth2 access token for authorization: oauth2PasswordSecurity
configuration = swagger_client.Configuration()
configuration.access_token = 'YOUR_ACCESS_TOKEN'

# create an instance of the API class
api_instance = swagger_client.StewardsApi(swagger_client.ApiClient(configuration))
stewardname = 'stewardname_example' # str | 
steward = swagger_client.StewardsRequest() # StewardsRequest | Steward Document
authorization = 'authorization_example' # str |  (optional)

try:
    # Update a steward account
    api_response = api_instance.stewards_put(stewardname, steward, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StewardsApi->stewards_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 
 **steward** | [**StewardsRequest**](StewardsRequest.md)| Steward Document | 
 **authorization** | **str**|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [basicAuthenticationSecurity](../README.md#basicAuthenticationSecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity), [oauth2ImplicitSecurity](../README.md#oauth2ImplicitSecurity), [oauth2PasswordSecurity](../README.md#oauth2PasswordSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stewards_reset_post**
> ResetResponse stewards_reset_post(stewardname, reset_request)

Reset password request

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.StewardsApi()
stewardname = 'stewardname_example' # str | 
reset_request = swagger_client.ResetRequest() # ResetRequest | Reset Password Request

try:
    # Reset password request
    api_response = api_instance.stewards_reset_post(stewardname, reset_request)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StewardsApi->stewards_reset_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 
 **reset_request** | [**ResetRequest**](ResetRequest.md)| Reset Password Request | 

### Return type

[**ResetResponse**](ResetResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

