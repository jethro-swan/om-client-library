# swagger_client.AccountsApi

All URIs are relative to *https://om-api-dev.lrc.org.uk/V2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts_delete**](AccountsApi.md#accounts_delete) | **DELETE** /stewards/{stewardname}/namespaces/{namespace}/accounts/{account} | Delete an account
[**accounts_discovery**](AccountsApi.md#accounts_discovery) | **GET** /stewards/{stewardname}/accounts/lookup | Lookup an account by it&#39;s public key
[**accounts_get**](AccountsApi.md#accounts_get) | **GET** /stewards/{stewardname}/namespaces/{namespace}/accounts/{account} | Get an account by account name
[**accounts_list**](AccountsApi.md#accounts_list) | **GET** /stewards/{stewardname}/accounts | Get a Listing of accounts in a namespace
[**accounts_post**](AccountsApi.md#accounts_post) | **POST** /stewards/{stewardname}/namespaces/{namespace}/accounts | create an account in a namespace
[**accounts_put**](AccountsApi.md#accounts_put) | **PUT** /stewards/{stewardname}/namespaces/{namespace}/accounts/{account} | Update an account


# **accounts_delete**
> DeleteResponse accounts_delete(stewardname, namespace, account, authorization=authorization)

Delete an account

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
stewardname = 'stewardname_example' # str | 
namespace = 'namespace_example' # str | 
account = 'account_example' # str | 
authorization = 'authorization_example' # str | Authorization Token (optional)

try:
    # Delete an account
    api_response = api_instance.accounts_delete(stewardname, namespace, account, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 
 **namespace** | **str**|  | 
 **account** | **str**|  | 
 **authorization** | **str**| Authorization Token | [optional] 

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [basicAuthenticationSecurity](../README.md#basicAuthenticationSecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity), [oauth2ImplicitSecurity](../README.md#oauth2ImplicitSecurity), [oauth2PasswordSecurity](../README.md#oauth2PasswordSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_discovery**
> AccountsResponse accounts_discovery(stewardname, authorization=authorization, public_key=public_key)

Lookup an account by it's public key

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
stewardname = 'stewardname_example' # str | 
authorization = 'authorization_example' # str | Authorization Token (optional)
public_key = 'public_key_example' # str | Accounts public Key (optional)

try:
    # Lookup an account by it's public key
    api_response = api_instance.accounts_discovery(stewardname, authorization=authorization, public_key=public_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_discovery: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 
 **authorization** | **str**| Authorization Token | [optional] 
 **public_key** | **str**| Accounts public Key | [optional] 

### Return type

[**AccountsResponse**](AccountsResponse.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [basicAuthenticationSecurity](../README.md#basicAuthenticationSecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity), [oauth2ImplicitSecurity](../README.md#oauth2ImplicitSecurity), [oauth2PasswordSecurity](../README.md#oauth2PasswordSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_get**
> AccountsGet accounts_get(stewardname, namespace, account, currency, currency_namespace, authorization=authorization)

Get an account by account name

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
stewardname = 'stewardname_example' # str | 
namespace = 'namespace_example' # str | 
account = 'account_example' # str | 
currency = 'currency_example' # str | 
currency_namespace = 'currency_namespace_example' # str | 
authorization = 'authorization_example' # str | Authorization Token (optional)

try:
    # Get an account by account name
    api_response = api_instance.accounts_get(stewardname, namespace, account, currency, currency_namespace, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 
 **namespace** | **str**|  | 
 **account** | **str**|  | 
 **currency** | **str**|  | 
 **currency_namespace** | **str**|  | 
 **authorization** | **str**| Authorization Token | [optional] 

### Return type

[**AccountsGet**](AccountsGet.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [basicAuthenticationSecurity](../README.md#basicAuthenticationSecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity), [oauth2ImplicitSecurity](../README.md#oauth2ImplicitSecurity), [oauth2PasswordSecurity](../README.md#oauth2PasswordSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_list**
> AccountsList accounts_list(stewardname, authorization=authorization, namespace=namespace, currency=currency, currency_namespace=currency_namespace)

Get a Listing of accounts in a namespace

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
stewardname = 'stewardname_example' # str | 
authorization = 'authorization_example' # str | Authorization Token (optional)
namespace = 'namespace_example' # str |  (optional)
currency = 'currency_example' # str |  (optional)
currency_namespace = 'currency_namespace_example' # str |  (optional)

try:
    # Get a Listing of accounts in a namespace
    api_response = api_instance.accounts_list(stewardname, authorization=authorization, namespace=namespace, currency=currency, currency_namespace=currency_namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 
 **authorization** | **str**| Authorization Token | [optional] 
 **namespace** | **str**|  | [optional] 
 **currency** | **str**|  | [optional] 
 **currency_namespace** | **str**|  | [optional] 

### Return type

[**AccountsList**](AccountsList.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [basicAuthenticationSecurity](../README.md#basicAuthenticationSecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity), [oauth2ImplicitSecurity](../README.md#oauth2ImplicitSecurity), [oauth2PasswordSecurity](../README.md#oauth2PasswordSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_post**
> DeleteResponse accounts_post(stewardname, namespace, authorization=authorization, account=account)

create an account in a namespace

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
stewardname = 'stewardname_example' # str | 
namespace = 'namespace_example' # str | 
authorization = 'authorization_example' # str | Authorization Token (optional)
account = swagger_client.AccountsRequest() # AccountsRequest |  (optional)

try:
    # create an account in a namespace
    api_response = api_instance.accounts_post(stewardname, namespace, authorization=authorization, account=account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 
 **namespace** | **str**|  | 
 **authorization** | **str**| Authorization Token | [optional] 
 **account** | [**AccountsRequest**](AccountsRequest.md)|  | [optional] 

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [basicAuthenticationSecurity](../README.md#basicAuthenticationSecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity), [oauth2ImplicitSecurity](../README.md#oauth2ImplicitSecurity), [oauth2PasswordSecurity](../README.md#oauth2PasswordSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_put**
> CreateResponse accounts_put(stewardname, namespace, account, authorization=authorization, accounts=accounts)

Update an account

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
api_instance = swagger_client.AccountsApi(swagger_client.ApiClient(configuration))
stewardname = 'stewardname_example' # str | 
namespace = 'namespace_example' # str | 
account = 'account_example' # str | Account Name
authorization = 'authorization_example' # str | Authorization Token (optional)
accounts = swagger_client.AccountsRequest() # AccountsRequest |  (optional)

try:
    # Update an account
    api_response = api_instance.accounts_put(stewardname, namespace, account, authorization=authorization, accounts=accounts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 
 **namespace** | **str**|  | 
 **account** | **str**| Account Name | 
 **authorization** | **str**| Authorization Token | [optional] 
 **accounts** | [**AccountsRequest**](AccountsRequest.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [basicAuthenticationSecurity](../README.md#basicAuthenticationSecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity), [oauth2ImplicitSecurity](../README.md#oauth2ImplicitSecurity), [oauth2PasswordSecurity](../README.md#oauth2PasswordSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

