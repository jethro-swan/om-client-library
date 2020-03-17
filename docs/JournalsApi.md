# swagger_client.JournalsApi

All URIs are relative to *https://om-12.lrc.org.uk/V2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**journals_list**](JournalsApi.md#journals_list) | **GET** /stewards/{stewardname}/journals | List Journal Entries for this accountname
[**journals_post**](JournalsApi.md#journals_post) | **POST** /stewards/{stewardname}/namespaces/{namespace}/accounts/{account}/journals/{currency} | Create a journal entry for this account


# **journals_list**
> JournalsList journals_list(stewardname, authorization=authorization, namespace=namespace, account=account, currency=currency, currency_namespace=currency_namespace, offset=offset, range=range)

List Journal Entries for this accountname

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
api_instance = swagger_client.JournalsApi(swagger_client.ApiClient(configuration))
stewardname = 'stewardname_example' # str | 
authorization = 'authorization_example' # str | Authorization Token (optional)
namespace = 'namespace_example' # str |  (optional)
account = 'account_example' # str |  (optional)
currency = 'currency_example' # str |  (optional)
currency_namespace = 'currency_namespace_example' # str |  (optional)
offset = 56 # int |  (optional)
range = 56 # int |  (optional)

try:
    # List Journal Entries for this accountname
    api_response = api_instance.journals_list(stewardname, authorization=authorization, namespace=namespace, account=account, currency=currency, currency_namespace=currency_namespace, offset=offset, range=range)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalsApi->journals_list: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 
 **authorization** | **str**| Authorization Token | [optional] 
 **namespace** | **str**|  | [optional] 
 **account** | **str**|  | [optional] 
 **currency** | **str**|  | [optional] 
 **currency_namespace** | **str**|  | [optional] 
 **offset** | **int**|  | [optional] 
 **range** | **int**|  | [optional] 

### Return type

[**JournalsList**](JournalsList.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [basicAuthenticationSecurity](../README.md#basicAuthenticationSecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity), [oauth2ImplicitSecurity](../README.md#oauth2ImplicitSecurity), [oauth2PasswordSecurity](../README.md#oauth2PasswordSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **journals_post**
> CreateResponse journals_post(stewardname, namespace, account, currency, authorization=authorization, currency_namespace=currency_namespace, journal=journal)

Create a journal entry for this account

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
api_instance = swagger_client.JournalsApi(swagger_client.ApiClient(configuration))
stewardname = 'stewardname_example' # str | 
namespace = 'namespace_example' # str | 
account = 'account_example' # str | 
currency = 'currency_example' # str | 
authorization = 'authorization_example' # str | Authorization Token (optional)
currency_namespace = 'currency_namespace_example' # str |  (optional)
journal = swagger_client.JournalsRequest() # JournalsRequest |  (optional)

try:
    # Create a journal entry for this account
    api_response = api_instance.journals_post(stewardname, namespace, account, currency, authorization=authorization, currency_namespace=currency_namespace, journal=journal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling JournalsApi->journals_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stewardname** | **str**|  | 
 **namespace** | **str**|  | 
 **account** | **str**|  | 
 **currency** | **str**|  | 
 **authorization** | **str**| Authorization Token | [optional] 
 **currency_namespace** | **str**|  | [optional] 
 **journal** | [**JournalsRequest**](JournalsRequest.md)|  | [optional] 

### Return type

[**CreateResponse**](CreateResponse.md)

### Authorization

[apiKeySecurity](../README.md#apiKeySecurity), [basicAuthenticationSecurity](../README.md#basicAuthenticationSecurity), [oauth2AccessCodeSecurity](../README.md#oauth2AccessCodeSecurity), [oauth2ApplicationSecurity](../README.md#oauth2ApplicationSecurity), [oauth2ImplicitSecurity](../README.md#oauth2ImplicitSecurity), [oauth2PasswordSecurity](../README.md#oauth2PasswordSecurity)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, text/html

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

