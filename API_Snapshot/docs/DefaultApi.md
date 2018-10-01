# openapi_client.DefaultApi

All URIs are relative to *https://virtserver.swaggerhub.com/Red-Hat93/GD2-Py/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**snapshot_activate**](DefaultApi.md#snapshot_activate) | **POST** /snapshots/{snapname}/activate | 
[**snapshot_clone**](DefaultApi.md#snapshot_clone) | **POST** /snapshots/{snapname}/clone | 
[**snapshot_create**](DefaultApi.md#snapshot_create) | **POST** /snapshots | 
[**snapshot_deactivate**](DefaultApi.md#snapshot_deactivate) | **POST** /snapshots/{snapname}/deactivate | 
[**snapshot_delete**](DefaultApi.md#snapshot_delete) | **DELETE** /snapshots/{snapname} | 
[**snapshot_info**](DefaultApi.md#snapshot_info) | **GET** /snapshots/{snapname} | 
[**snapshot_list_all**](DefaultApi.md#snapshot_list_all) | **GET** /snapshots | 
[**snapshot_restore**](DefaultApi.md#snapshot_restore) | **POST** /snapshots/{snapname}/restore | 
[**snapshot_status**](DefaultApi.md#snapshot_status) | **GET** /snapshots/{snapname}/status | 


# **snapshot_activate**
> CreateResp snapshot_activate(snapname, activate=activate)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
snapname = 'snapname_example' # str | 
activate = openapi_client.Activate() # Activate |  (optional)

try:
    api_response = api_instance.snapshot_activate(snapname, activate=activate)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->snapshot_activate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapname** | **str**|  | 
 **activate** | [**Activate**](Activate.md)|  | [optional] 

### Return type

[**CreateResp**](CreateResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshot_clone**
> Volume snapshot_clone(snapname, clone=clone)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
snapname = 'snapname_example' # str | 
clone = openapi_client.Clone() # Clone |  (optional)

try:
    api_response = api_instance.snapshot_clone(snapname, clone=clone)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->snapshot_clone: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapname** | **str**|  | 
 **clone** | [**Clone**](Clone.md)|  | [optional] 

### Return type

[**Volume**](Volume.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshot_create**
> CreateResp snapshot_create(create=create)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
create = openapi_client.Create() # Create |  (optional)

try:
    api_response = api_instance.snapshot_create(create=create)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->snapshot_create: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create** | [**Create**](Create.md)|  | [optional] 

### Return type

[**CreateResp**](CreateResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshot_deactivate**
> CreateResp snapshot_deactivate(snapname)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
snapname = 'snapname_example' # str | 

try:
    api_response = api_instance.snapshot_deactivate(snapname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->snapshot_deactivate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapname** | **str**|  | 

### Return type

[**CreateResp**](CreateResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshot_delete**
> snapshot_delete(snapname)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
snapname = 'snapname_example' # str | 

try:
    api_instance.snapshot_delete(snapname)
except ApiException as e:
    print("Exception when calling DefaultApi->snapshot_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapname** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshot_info**
> CreateResp snapshot_info(snapname)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
snapname = 'snapname_example' # str | 

try:
    api_response = api_instance.snapshot_info(snapname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->snapshot_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapname** | **str**|  | 

### Return type

[**CreateResp**](CreateResp.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshot_list_all**
> SnapList snapshot_list_all()



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
    api_response = api_instance.snapshot_list_all()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->snapshot_list_all: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SnapList**](SnapList.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshot_restore**
> snapshot_restore(snapname)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
snapname = 'snapname_example' # str | 

try:
    api_instance.snapshot_restore(snapname)
except ApiException as e:
    print("Exception when calling DefaultApi->snapshot_restore: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapname** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **snapshot_status**
> Status snapshot_status(snapname)



### Example
```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi()
snapname = 'snapname_example' # str | 

try:
    api_response = api_instance.snapshot_status(snapname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->snapshot_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **snapname** | **str**|  | 

### Return type

[**Status**](Status.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

