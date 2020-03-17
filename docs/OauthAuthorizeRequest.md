# OauthAuthorizeRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**response_type** | **str** | One of code, password, refresh_token, client_credentials | 
**client_id** | **str** |  | [optional] 
**redirect_uri** | **str** | A uri to redirect steward after authorization | [optional] 
**username** | **str** | stewardname of user | [optional] 
**scopes** | **list[str]** | A comma separated list of scopes. If not provided, scope defaults to an empty list of scopes for stewards that don’t have a valid token for the app. For stewards who do already have a valid token for the app, the steward won’t be shown the OAuth authorization page with the list of scopes. Instead, this step of the flow will automatically complete with the same scopes that were used last time the steward completed the flow. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


