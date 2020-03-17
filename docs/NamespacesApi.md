# swagger_client.NamespacesApi

All URIs are relative to *https://om-api-dev.lrc.org.uk/V2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**spaces_delete**](NamespacesApi.md#spaces_delete) | **DELETE** /stewards/{stewardname}/namespaces/{namespace} | 
[**spaces_get**](NamespacesApi.md#spaces_get) | **GET** /stewards/{stewardname}/namespaces/{namespace} | Get a namespace by it&#39;s name
[**spaces_list**](NamespacesApi.md#spaces_list) | **GET** /stewards/{stewardname}/namespaces | Get a Listing of namespaces known by steward.
[**spaces_post**](NamespacesApi.md#spaces_post) | **POST** /stewards/{stewardname}/namespaces | Create a namespace
[**spaces_put**](NamespacesApi.md#spaces_put) | **PUT** /stewards/{stewardname}/namespaces/{namespace} | Update a namespace


# **spaces_delete**
> DeleteResponse spaces_delete(stewardname, namespace, authorization=authorization)



Delete a namespace

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
api_instance = swagger_client.NamespacesApi(swagger_client.ApiClient(configuration))
stewardname = 'stewardname_example' # str | 
namespace = 'namespace_example' # str | namespace name
authorization = 'authorization_example' # str | Authorization Token (optional)

try:
    api_response = api_instance.spaces_delete(stewardname, namespace, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespacesApi->spaces_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 
 **namespace** | **str**| namespace name | 
 **authorization** | **str**| Authorization Token | [optional] 

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [basicAuthenticationSecurity](../README.md#basicAuthenticationSecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity), [oauth2ImplicitSecurity](../README.md#oauth2ImplicitSecurity), [oauth2PasswordSecurity](../README.md#oauth2PasswordSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spaces_get**
> NamespacesGet spaces_get(stewardname, namespace, authorization=authorization)

Get a namespace by it's name

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
api_instance = swagger_client.NamespacesApi(swagger_client.ApiClient(configuration))
stewardname = 'stewardname_example' # str | 
namespace = 'namespace_example' # str | space name
authorization = 'authorization_example' # str | Authorization Token (optional)

try:
    # Get a namespace by it's name
    api_response = api_instance.spaces_get(stewardname, namespace, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespacesApi->spaces_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 
 **namespace** | **str**| space name | 
 **authorization** | **str**| Authorization Token | [optional] 

### Return type

[**NamespacesGet**](NamespacesGet.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [basicAuthenticationSecurity](../README.md#basicAuthenticationSecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity), [oauth2ImplicitSecurity](../README.md#oauth2ImplicitSecurity), [oauth2PasswordSecurity](../README.md#oauth2PasswordSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spaces_list**
> NamespacesList spaces_list(stewardname, authorization=authorization, parent_namespace=parent_namespace)

Get a Listing of namespaces known by steward.

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
api_instance = swagger_client.NamespacesApi(swagger_client.ApiClient(configuration))
stewardname = 'stewardname_example' # str | 
authorization = 'authorization_example' # str | Authorization Token (optional)
parent_namespace = 'parent_namespace_example' # str |  (optional)

try:
    # Get a Listing of namespaces known by steward.
    api_response = api_instance.spaces_list(stewardname, authorization=authorization, parent_namespace=parent_namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespacesApi->spaces_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 
 **authorization** | **str**| Authorization Token | [optional] 
 **parent_namespace** | **str**|  | [optional] 

### Return type

[**NamespacesList**](NamespacesList.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [basicAuthenticationSecurity](../README.md#basicAuthenticationSecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity), [oauth2ImplicitSecurity](../README.md#oauth2ImplicitSecurity), [oauth2PasswordSecurity](../README.md#oauth2PasswordSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spaces_post**
> CreateResponse spaces_post(stewardname, space, authorization=authorization)

Create a namespace

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
api_instance = swagger_client.NamespacesApi(swagger_client.ApiClient(configuration))
stewardname = 'stewardname_example' # str | 
space = swagger_client.NamespacesRequest() # NamespacesRequest | 
authorization = 'authorization_example' # str | Authorization Token (optional)

try:
    # Create a namespace
    api_response = api_instance.spaces_post(stewardname, space, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespacesApi->spaces_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 
 **space** | [**NamespacesRequest**](NamespacesRequest.md)|  | 
 **authorization** | **str**| Authorization Token | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [basicAuthenticationSecurity](../README.md#basicAuthenticationSecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity), [oauth2ImplicitSecurity](../README.md#oauth2ImplicitSecurity), [oauth2PasswordSecurity](../README.md#oauth2PasswordSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **spaces_put**
> CreateResponse spaces_put(stewardname, namespace, authorization=authorization, space=space)

Update a namespace

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
api_instance = swagger_client.NamespacesApi(swagger_client.ApiClient(configuration))
stewardname = 'stewardname_example' # str | 
namespace = 'namespace_example' # str | space name
authorization = 'authorization_example' # str | Authorization Token (optional)
space = swagger_client.NamespacesRequest() # NamespacesRequest |  (optional)

try:
    # Update a namespace
    api_response = api_instance.spaces_put(stewardname, namespace, authorization=authorization, space=space)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling NamespacesApi->spaces_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 
 **namespace** | **str**| space name | 
 **authorization** | **str**| Authorization Token | [optional] 
 **space** | [**NamespacesRequest**](NamespacesRequest.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [basicAuthenticationSecurity](../README.md#basicAuthenticationSecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity), [oauth2ImplicitSecurity](../README.md#oauth2ImplicitSecurity), [oauth2PasswordSecurity](../README.md#oauth2PasswordSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

