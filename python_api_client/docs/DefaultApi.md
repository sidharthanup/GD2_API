# openapi_client.DefaultApi

All URIs are relative to *https://virtserver.swaggerhub.com/Red-Hat93/GD2-Py/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**peers_get**](DefaultApi.md#peers_get) | **GET** /peers | Get a Peer information
[**peers_peerid_delete**](DefaultApi.md#peers_peerid_delete) | **DELETE** /peers/{peerid} | 
[**peers_peerid_get**](DefaultApi.md#peers_peerid_get) | **GET** /peers/{peerid} | Get a Peer information
[**peers_peerid_post**](DefaultApi.md#peers_peerid_post) | **POST** /peers/{peerid} | 
[**peers_post**](DefaultApi.md#peers_post) | **POST** /peers | Add Peer
[**volumes_get**](DefaultApi.md#volumes_get) | **GET** /volumes | 
[**volumes_post**](DefaultApi.md#volumes_post) | **POST** /volumes | Volume Create
[**volumes_volname_start_post**](DefaultApi.md#volumes_volname_start_post) | **POST** /volumes/{volname}/start | 
[**volumes_volname_stop_post**](DefaultApi.md#volumes_volname_stop_post) | **POST** /volumes/{volname}/stop | 


# **peers_get**
> list[Peer] peers_get(peerid)

Get a Peer information

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
peerid = 4f196836-0d9d-475a-aae2-642bb0eac685 # str | Peer ID

try:
    # Get a Peer information
    api_response = api_instance.peers_get(peerid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->peers_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **peerid** | **str**| Peer ID | 

### Return type

[**list[Peer]**](Peer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **peers_peerid_delete**
> peers_peerid_delete(peerid)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
peerid = 4f196836-0d9d-475a-aae2-642bb0eac685 # str | Peer ID

try:
    api_instance.peers_peerid_delete(peerid)
except ApiException as e:
    print("Exception when calling DefaultApi->peers_peerid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **peerid** | **str**| Peer ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **peers_peerid_get**
> list[Peer] peers_peerid_get(peerid)

Get a Peer information

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
peerid = 4f196836-0d9d-475a-aae2-642bb0eac685 # str | Peer ID

try:
    # Get a Peer information
    api_response = api_instance.peers_peerid_get(peerid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->peers_peerid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **peerid** | **str**| Peer ID | 

### Return type

[**list[Peer]**](Peer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **peers_peerid_post**
> list[Peer] peers_peerid_post(peerid, edit=edit)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
peerid = 4f196836-0d9d-475a-aae2-642bb0eac685 # str | Peer ID
edit = openapi_client.Edit() # Edit |  (optional)

try:
    api_response = api_instance.peers_peerid_post(peerid, edit=edit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->peers_peerid_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **peerid** | **str**| Peer ID | 
 **edit** | [**Edit**](Edit.md)|  | [optional] 

### Return type

[**list[Peer]**](Peer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **peers_post**
> Peer peers_post(body=body)

Add Peer

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
body = openapi_client.Add() # Add |  (optional)

try:
    # Add Peer
    api_response = api_instance.peers_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->peers_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **Add**|  | [optional] 

### Return type

[**Peer**](Peer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volumes_get**
> list[Volume] volumes_get()



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
    api_response = api_instance.volumes_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->volumes_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Volume]**](Volume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volumes_post**
> Volume volumes_post(volcreate=volcreate)

Volume Create

### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
volcreate = openapi_client.Volcreate() # Volcreate |  (optional)

try:
    # Volume Create
    api_response = api_instance.volumes_post(volcreate=volcreate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->volumes_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volcreate** | [**Volcreate**](Volcreate.md)|  | [optional] 

### Return type

[**Volume**](Volume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volumes_volname_start_post**
> list[Volume] volumes_volname_start_post(volname)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
volname = gv1 # str | Volume Name

try:
    api_response = api_instance.volumes_volname_start_post(volname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->volumes_volname_start_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volname** | **str**| Volume Name | 

### Return type

[**list[Volume]**](Volume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volumes_volname_stop_post**
> list[Volume] volumes_volname_stop_post(volname)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
volname = gv1 # str | Volume Name

try:
    api_response = api_instance.volumes_volname_stop_post(volname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->volumes_volname_stop_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volname** | **str**| Volume Name | 

### Return type

[**list[Volume]**](Volume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

