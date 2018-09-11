# glusterapi.Client

All URIs are relative to *https://virtserver.swaggerhub.com/Red-Hat93/GD2-Py/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**add_peer**](Client.md#add_peer) | **POST** /peers | 
[**delete_peer**](Client.md#delete_peer) | **DELETE** /peers/{peerid} | 
[**edit_peer**](Client.md#edit_peer) | **POST** /peers/{peerid} | 
[**get_peer**](Client.md#get_peer) | **GET** /peers/{peerid} | 
[**get_peers**](Client.md#get_peers) | **GET** /peers | 
[**volume_create**](Client.md#volume_create) | **POST** /volumes | 
[**volume_info**](Client.md#volume_info) | **GET** /volumes | 
[**volume_start**](Client.md#volume_start) | **POST** /volumes/{volname}/start | 
[**volume_stop**](Client.md#volume_stop) | **POST** /volumes/{volname}/stop | 


# **add_peer**
> Peer add_peer(add=add)



### Example
```python
from __future__ import print_function
import time
import glusterapi
from glusterapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = glusterapi.Client()
add = {$ref=./req_peer_example.json#/add} # Add | Add Peer (optional)

try:
    api_response = api_instance.add_peer(add=add)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Client->add_peer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **add** | [**Add**](Add.md)| Add Peer | [optional] 

### Return type

[**Peer**](Peer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_peer**
> delete_peer(peerid)



### Example
```python
from __future__ import print_function
import time
import glusterapi
from glusterapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = glusterapi.Client()
peerid = 4f196836-0d9d-475a-aae2-642bb0eac685 # str | Peer ID

try:
    api_instance.delete_peer(peerid)
except ApiException as e:
    print("Exception when calling Client->delete_peer: %s\n" % e)
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

# **edit_peer**
> Peer edit_peer(peerid, edit=edit)



### Example
```python
from __future__ import print_function
import time
import glusterapi
from glusterapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = glusterapi.Client()
peerid = 4f196836-0d9d-475a-aae2-642bb0eac685 # str | Peer ID
edit = {$ref=./req_peer_example.json#/edit} # Edit |  (optional)

try:
    api_response = api_instance.edit_peer(peerid, edit=edit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Client->edit_peer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **peerid** | **str**| Peer ID | 
 **edit** | [**Edit**](Edit.md)|  | [optional] 

### Return type

[**Peer**](Peer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_peer**
> Peer get_peer(peerid)



### Example
```python
from __future__ import print_function
import time
import glusterapi
from glusterapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = glusterapi.Client()
peerid = 4f196836-0d9d-475a-aae2-642bb0eac685 # str | Peer ID

try:
    api_response = api_instance.get_peer(peerid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Client->get_peer: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **peerid** | **str**| Peer ID | 

### Return type

[**Peer**](Peer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_peers**
> list[Peer] get_peers()



### Example
```python
from __future__ import print_function
import time
import glusterapi
from glusterapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = glusterapi.Client()

try:
    api_response = api_instance.get_peers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Client->get_peers: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Peer]**](Peer.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_create**
> Volume volume_create(body)



### Example
```python
from __future__ import print_function
import time
import glusterapi
from glusterapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = glusterapi.Client()
body = glusterapi.UNKNOWN_BASE_TYPE() # UNKNOWN_BASE_TYPE | Volume Create

try:
    api_response = api_instance.volume_create(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Client->volume_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UNKNOWN_BASE_TYPE**](UNKNOWN_BASE_TYPE.md)| Volume Create | 

### Return type

[**Volume**](Volume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_info**
> list[Volume] volume_info()



### Example
```python
from __future__ import print_function
import time
import glusterapi
from glusterapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = glusterapi.Client()

try:
    api_response = api_instance.volume_info()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Client->volume_info: %s\n" % e)
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

# **volume_start**
> Volume volume_start(volname)



### Example
```python
from __future__ import print_function
import time
import glusterapi
from glusterapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = glusterapi.Client()
volname = gv1 # str | Volume Name

try:
    api_response = api_instance.volume_start(volname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Client->volume_start: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volname** | **str**| Volume Name | 

### Return type

[**Volume**](Volume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **volume_stop**
> Volume volume_stop(volname)



### Example
```python
from __future__ import print_function
import time
import glusterapi
from glusterapi.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = glusterapi.Client()
volname = gv1 # str | Volume Name

try:
    api_response = api_instance.volume_stop(volname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling Client->volume_stop: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volname** | **str**| Volume Name | 

### Return type

[**Volume**](Volume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

