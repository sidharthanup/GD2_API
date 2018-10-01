# openapi_client.DefaultApi

All URIs are relative to *https://virtserver.swaggerhub.com/Red-Hat93/GD2-Py/1.0.0*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bitrot_disable**](DefaultApi.md#bitrot_disable) | **POST** /volumes/{volname}/bitrot/disable | 
[**bitrot_enable**](DefaultApi.md#bitrot_enable) | **POST** /volumes/{volname}/bitrot/enable | 
[**bitrot_scrub_ondemand**](DefaultApi.md#bitrot_scrub_ondemand) | **POST** /volumes/{volname}/bitrot/scrubondemand | 
[**bitrot_scrub_status**](DefaultApi.md#bitrot_scrub_status) | **GET** /volumes/{volname}/bitrot/scrubstatus | 
[**self_heal**](DefaultApi.md#self_heal) | **POST** /volumes/{volname}/heal | 
[**self_heal_info**](DefaultApi.md#self_heal_info) | **GET** /volumes/{volname}/{opts}/heal-info | 
[**self_heal_info2**](DefaultApi.md#self_heal_info2) | **GET** /volumes/{volname}/heal-info | 


# **bitrot_disable**
> bitrot_disable(volname)



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
    api_instance.bitrot_disable(volname)
except ApiException as e:
    print("Exception when calling DefaultApi->bitrot_disable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volname** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bitrot_enable**
> bitrot_enable(volname)



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
    api_instance.bitrot_enable(volname)
except ApiException as e:
    print("Exception when calling DefaultApi->bitrot_enable: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volname** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bitrot_scrub_ondemand**
> bitrot_scrub_ondemand(volname)



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
    api_instance.bitrot_scrub_ondemand(volname)
except ApiException as e:
    print("Exception when calling DefaultApi->bitrot_scrub_ondemand: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volname** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **bitrot_scrub_status**
> bitrot_scrub_status(volname)



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
    api_instance.bitrot_scrub_status(volname)
except ApiException as e:
    print("Exception when calling DefaultApi->bitrot_scrub_status: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volname** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **self_heal**
> self_heal(volname)



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
    api_instance.self_heal(volname)
except ApiException as e:
    print("Exception when calling DefaultApi->self_heal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volname** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **self_heal_info**
> BrickHeal self_heal_info(volname, opts)



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
opts = 'opts_example' # str | 

try:
    api_response = api_instance.self_heal_info(volname, opts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->self_heal_info: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volname** | **str**|  | 
 **opts** | **str**|  | 

### Return type

[**BrickHeal**](BrickHeal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **self_heal_info2**
> BrickHeal self_heal_info2(volname)



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
    api_response = api_instance.self_heal_info2(volname)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->self_heal_info2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **volname** | **str**|  | 

### Return type

[**BrickHeal**](BrickHeal.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

