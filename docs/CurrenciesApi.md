# swagger_client.CurrenciesApi

All URIs are relative to *https://om-12.lrc.org.uk/V2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**currencies_delete**](CurrenciesApi.md#currencies_delete) | **DELETE** /stewards/{stewardname}/currencies/{currency} | Delete a currency
[**currencies_get**](CurrenciesApi.md#currencies_get) | **GET** /stewards/{stewardname}/currencies/{currency} | Get a currency by its name
[**currencies_list**](CurrenciesApi.md#currencies_list) | **GET** /stewards/{stewardname}/currencies | Get a Listing currencies known by steward.
[**currencies_post**](CurrenciesApi.md#currencies_post) | **POST** /stewards/{stewardname}/currencies | Create a currency
[**currencies_put**](CurrenciesApi.md#currencies_put) | **PUT** /stewards/{stewardname}/currencies/{currency} | Update a Currency


# **currencies_delete**
> DeleteResponse currencies_delete(stewardname, currency, authorization=authorization)

Delete a currency

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
api_instance = swagger_client.CurrenciesApi(swagger_client.ApiClient(configuration))
stewardname = 'stewardname_example' # str | 
currency = 'currency_example' # str | Currency name
authorization = 'authorization_example' # str | Authorization Token (optional)

try:
    # Delete a currency
    api_response = api_instance.currencies_delete(stewardname, currency, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrenciesApi->currencies_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 
 **currency** | **str**| Currency name | 
 **authorization** | **str**| Authorization Token | [optional] 

### Return type

[**DeleteResponse**](DeleteResponse.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [basicAuthenticationSecurity](../README.md#basicAuthenticationSecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity), [oauth2ImplicitSecurity](../README.md#oauth2ImplicitSecurity), [oauth2PasswordSecurity](../README.md#oauth2PasswordSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currencies_get**
> CurrenciesGet currencies_get(stewardname, currency, authorization=authorization)

Get a currency by its name

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
api_instance = swagger_client.CurrenciesApi(swagger_client.ApiClient(configuration))
stewardname = 'stewardname_example' # str | 
currency = 'currency_example' # str | Name of a currency
authorization = 'authorization_example' # str | Authorization Token (optional)

try:
    # Get a currency by its name
    api_response = api_instance.currencies_get(stewardname, currency, authorization=authorization)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrenciesApi->currencies_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 
 **currency** | **str**| Name of a currency | 
 **authorization** | **str**| Authorization Token | [optional] 

### Return type

[**CurrenciesGet**](CurrenciesGet.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [basicAuthenticationSecurity](../README.md#basicAuthenticationSecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity), [oauth2ImplicitSecurity](../README.md#oauth2ImplicitSecurity), [oauth2PasswordSecurity](../README.md#oauth2PasswordSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currencies_list**
> CurrenciesList currencies_list(stewardname, authorization=authorization, namespace=namespace)

Get a Listing currencies known by steward.

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
api_instance = swagger_client.CurrenciesApi(swagger_client.ApiClient(configuration))
stewardname = 'stewardname_example' # str | 
authorization = 'authorization_example' # str | Authorization Token (optional)
namespace = 'namespace_example' # str |  (optional)

try:
    # Get a Listing currencies known by steward.
    api_response = api_instance.currencies_list(stewardname, authorization=authorization, namespace=namespace)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrenciesApi->currencies_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 
 **authorization** | **str**| Authorization Token | [optional] 
 **namespace** | **str**|  | [optional] 

### Return type

[**CurrenciesList**](CurrenciesList.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [basicAuthenticationSecurity](../README.md#basicAuthenticationSecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity), [oauth2ImplicitSecurity](../README.md#oauth2ImplicitSecurity), [oauth2PasswordSecurity](../README.md#oauth2PasswordSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currencies_post**
> CreateResponse currencies_post(stewardname, authorization=authorization, currency=currency)

Create a currency

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
api_instance = swagger_client.CurrenciesApi(swagger_client.ApiClient(configuration))
stewardname = 'stewardname_example' # str | 
authorization = 'authorization_example' # str | Authorization Token (optional)
currency = swagger_client.CurrenciesRequest() # CurrenciesRequest |  (optional)

try:
    # Create a currency
    api_response = api_instance.currencies_post(stewardname, authorization=authorization, currency=currency)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrenciesApi->currencies_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 
 **authorization** | **str**| Authorization Token | [optional] 
 **currency** | [**CurrenciesRequest**](CurrenciesRequest.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [basicAuthenticationSecurity](../README.md#basicAuthenticationSecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity), [oauth2ImplicitSecurity](../README.md#oauth2ImplicitSecurity), [oauth2PasswordSecurity](../README.md#oauth2PasswordSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **currencies_put**
> CreateResponse currencies_put(stewardname, currency, authorization=authorization, currencies=currencies)

Update a Currency

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
api_instance = swagger_client.CurrenciesApi(swagger_client.ApiClient(configuration))
stewardname = 'stewardname_example' # str | 
currency = 'currency_example' # str | Name of a currency
authorization = 'authorization_example' # str | Authorization Token (optional)
currencies = swagger_client.CurrenciesRequest() # CurrenciesRequest |  (optional)

try:
    # Update a Currency
    api_response = api_instance.currencies_put(stewardname, currency, authorization=authorization, currencies=currencies)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CurrenciesApi->currencies_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 
 **currency** | **str**| Name of a currency | 
 **authorization** | **str**| Authorization Token | [optional] 
 **currencies** | [**CurrenciesRequest**](CurrenciesRequest.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [basicAuthenticationSecurity](../README.md#basicAuthenticationSecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity), [oauth2ImplicitSecurity](../README.md#oauth2ImplicitSecurity), [oauth2PasswordSecurity](../README.md#oauth2PasswordSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

