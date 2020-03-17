# RegisterRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stewardname** | **str** | Stewards name | 
**password** | **str** | Stewards password | 
**public_key** | **str** | Stewards 1024bit - 4096bit RSA public key. command: openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:4096 ,openssl rsa -pubout -in private_key.pem -out public_key.pem , you can deterministically generate an RSA key from a passphrase http://crypto.stackexchange.com/questions/24514/deterministically-generate-a-rsa-public-private-key-pair-from-a-passphrase-with you can also use this service to generate a key online: http://travistidwell.com/blog/2013/09/06/an-online-rsa-public-and-private-key-generator/ | [optional] 
**email** | **str** | Stewards email address | [optional] 
**email_notifications** | **bool** | Does steward wish to receive email notifications | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


