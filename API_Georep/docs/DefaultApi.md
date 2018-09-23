# openapi_client.DefaultApi

All URIs are relative to *https://virtserver.swaggerhub.com/Red-Hat93/GD2-Py/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**geo_replication_config_get**](DefaultApi.md#geo_replication_config_get) | **GET** /geo-replication/{mastervolid}/{remotevolid}/config | 
[**geo_replication_config_reset**](DefaultApi.md#geo_replication_config_reset) | **DELETE** /geo-replication/{mastervolid}/{remotevolid}/config | 
[**geo_replication_config_set**](DefaultApi.md#geo_replication_config_set) | **POST** /geo-replication/{mastervolid}/{remotevolid}/config | 
[**geo_replication_create**](DefaultApi.md#geo_replication_create) | **POST** /geo-replication/{mastervolid}/{remotevolid} | 
[**geo_replication_delete**](DefaultApi.md#geo_replication_delete) | **DELETE** /geo-replication/{mastervolid}/{remotevolid} | 
[**geo_replication_pause**](DefaultApi.md#geo_replication_pause) | **POST** /geo-replication/{mastervolid}/{remotevolid}/pause | 
[**geo_replication_resume**](DefaultApi.md#geo_replication_resume) | **POST** /geo-replication/{mastervolid}/{remotevolid}/resume | 
[**geo_replication_ssh_key_generate**](DefaultApi.md#geo_replication_ssh_key_generate) | **POST** /ssh-key/{volname}/generate | 
[**geo_replication_ssh_key_get**](DefaultApi.md#geo_replication_ssh_key_get) | **GET** /ssh-key/{volname} | 
[**geo_replication_ssh_key_push**](DefaultApi.md#geo_replication_ssh_key_push) | **POST** /ssh-key/{volname}/push | 
[**geo_replication_start**](DefaultApi.md#geo_replication_start) | **POST** /geo-replication/{mastervolid}/{remotevolid}/start | 
[**geo_replication_status**](DefaultApi.md#geo_replication_status) | **GET** /geo-replication/{mastervolid}/{remotevolid} | 
[**geo_replication_status_list**](DefaultApi.md#geo_replication_status_list) | **GET** /geo-replication | 
[**geo_replication_stop**](DefaultApi.md#geo_replication_stop) | **POST** /geo-replication/{mastervolid}/{remotevolid}/stop | 


# **geo_replication_config_get**
> Option geo_replication_config_get(mastervolid, remotevolid)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
mastervolid = 'mastervolid_example' # str | 
remotevolid = 'remotevolid_example' # str | 

try:
    api_response = api_instance.geo_replication_config_get(mastervolid, remotevolid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->geo_replication_config_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mastervolid** | **str**|  | 
 **remotevolid** | **str**|  | 

### Return type

[**Option**](Option.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geo_replication_config_reset**
> geo_replication_config_reset(mastervolid, remotevolid)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
mastervolid = 'mastervolid_example' # str | 
remotevolid = 'remotevolid_example' # str | 

try:
    api_instance.geo_replication_config_reset(mastervolid, remotevolid)
except ApiException as e:
    print("Exception when calling DefaultApi->geo_replication_config_reset: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mastervolid** | **str**|  | 
 **remotevolid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geo_replication_config_set**
> Option geo_replication_config_set(mastervolid, remotevolid, option2=option2)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
mastervolid = 'mastervolid_example' # str | 
remotevolid = 'remotevolid_example' # str | 
option2 = openapi_client.Option2() # Option2 |  (optional)

try:
    api_response = api_instance.geo_replication_config_set(mastervolid, remotevolid, option2=option2)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->geo_replication_config_set: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mastervolid** | **str**|  | 
 **remotevolid** | **str**|  | 
 **option2** | [**Option2**](Option2.md)|  | [optional] 

### Return type

[**Option**](Option.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geo_replication_create**
> Session geo_replication_create(mastervolid, remotevolid, create=create)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
mastervolid = 'mastervolid_example' # str | 
remotevolid = 'remotevolid_example' # str | 
create = openapi_client.Create() # Create |  (optional)

try:
    api_response = api_instance.geo_replication_create(mastervolid, remotevolid, create=create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->geo_replication_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mastervolid** | **str**|  | 
 **remotevolid** | **str**|  | 
 **create** | [**Create**](Create.md)|  | [optional] 

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geo_replication_delete**
> geo_replication_delete(mastervolid, remotevolid)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
mastervolid = 'mastervolid_example' # str | 
remotevolid = 'remotevolid_example' # str | 

try:
    api_instance.geo_replication_delete(mastervolid, remotevolid)
except ApiException as e:
    print("Exception when calling DefaultApi->geo_replication_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mastervolid** | **str**|  | 
 **remotevolid** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geo_replication_pause**
> Session geo_replication_pause(mastervolid, remotevolid, start_stop=start_stop)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
mastervolid = 'mastervolid_example' # str | 
remotevolid = 'remotevolid_example' # str | 
start_stop = openapi_client.StartStop() # StartStop |  (optional)

try:
    api_response = api_instance.geo_replication_pause(mastervolid, remotevolid, start_stop=start_stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->geo_replication_pause: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mastervolid** | **str**|  | 
 **remotevolid** | **str**|  | 
 **start_stop** | [**StartStop**](StartStop.md)|  | [optional] 

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geo_replication_resume**
> Session geo_replication_resume(mastervolid, remotevolid, start_stop=start_stop)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
mastervolid = 'mastervolid_example' # str | 
remotevolid = 'remotevolid_example' # str | 
start_stop = openapi_client.StartStop() # StartStop |  (optional)

try:
    api_response = api_instance.geo_replication_resume(mastervolid, remotevolid, start_stop=start_stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->geo_replication_resume: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mastervolid** | **str**|  | 
 **remotevolid** | **str**|  | 
 **start_stop** | [**StartStop**](StartStop.md)|  | [optional] 

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geo_replication_ssh_key_generate**
> SshPublicKey geo_replication_ssh_key_generate(volname)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
volname = 'volname_example' # str | 

try:
    api_response = api_instance.geo_replication_ssh_key_generate(volname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->geo_replication_ssh_key_generate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volname** | **str**|  | 

### Return type

[**SshPublicKey**](SshPublicKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geo_replication_ssh_key_get**
> SshPublicKey geo_replication_ssh_key_get(volname)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
volname = 'volname_example' # str | 

try:
    api_response = api_instance.geo_replication_ssh_key_get(volname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->geo_replication_ssh_key_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volname** | **str**|  | 

### Return type

[**SshPublicKey**](SshPublicKey.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geo_replication_ssh_key_push**
> geo_replication_ssh_key_push(volname, ssh_public_key2=ssh_public_key2)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
volname = 'volname_example' # str | 
ssh_public_key2 = openapi_client.SshPublicKey2() # SshPublicKey2 |  (optional)

try:
    api_instance.geo_replication_ssh_key_push(volname, ssh_public_key2=ssh_public_key2)
except ApiException as e:
    print("Exception when calling DefaultApi->geo_replication_ssh_key_push: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volname** | **str**|  | 
 **ssh_public_key2** | [**SshPublicKey2**](SshPublicKey2.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geo_replication_start**
> Session geo_replication_start(mastervolid, remotevolid, start_stop=start_stop)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
mastervolid = 'mastervolid_example' # str | 
remotevolid = 'remotevolid_example' # str | 
start_stop = openapi_client.StartStop() # StartStop |  (optional)

try:
    api_response = api_instance.geo_replication_start(mastervolid, remotevolid, start_stop=start_stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->geo_replication_start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mastervolid** | **str**|  | 
 **remotevolid** | **str**|  | 
 **start_stop** | [**StartStop**](StartStop.md)|  | [optional] 

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geo_replication_status**
> Session geo_replication_status(mastervolid, remotevolid)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
mastervolid = 'mastervolid_example' # str | 
remotevolid = 'remotevolid_example' # str | 

try:
    api_response = api_instance.geo_replication_status(mastervolid, remotevolid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->geo_replication_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mastervolid** | **str**|  | 
 **remotevolid** | **str**|  | 

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geo_replication_status_list**
> Session geo_replication_status_list()



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()

try:
    api_response = api_instance.geo_replication_status_list()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->geo_replication_status_list: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **geo_replication_stop**
> Session geo_replication_stop(mastervolid, remotevolid, start_stop=start_stop)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
mastervolid = 'mastervolid_example' # str | 
remotevolid = 'remotevolid_example' # str | 
start_stop = openapi_client.StartStop() # StartStop |  (optional)

try:
    api_response = api_instance.geo_replication_stop(mastervolid, remotevolid, start_stop=start_stop)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->geo_replication_stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mastervolid** | **str**|  | 
 **remotevolid** | **str**|  | 
 **start_stop** | [**StartStop**](StartStop.md)|  | [optional] 

### Return type

[**Session**](Session.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

