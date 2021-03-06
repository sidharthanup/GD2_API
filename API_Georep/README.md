# openapi-client
Gluster Management APIs

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: 1.0.0
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = openapi_client.DefaultApi(openapi_client.ApiClient(configuration))
mastervolid = 'mastervolid_example' # str | 
remotevolid = 'remotevolid_example' # str | 

try:
    api_response = api_instance.geo_replication_config_get(mastervolid, remotevolid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->geo_replication_config_get: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *https://virtserver.swaggerhub.com/Red-Hat93/GD2-Py/1.0.0*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*DefaultApi* | [**geo_replication_config_get**](docs/DefaultApi.md#geo_replication_config_get) | **GET** /geo-replication/{mastervolid}/{remotevolid}/config | 
*DefaultApi* | [**geo_replication_config_reset**](docs/DefaultApi.md#geo_replication_config_reset) | **DELETE** /geo-replication/{mastervolid}/{remotevolid}/config | 
*DefaultApi* | [**geo_replication_config_set**](docs/DefaultApi.md#geo_replication_config_set) | **POST** /geo-replication/{mastervolid}/{remotevolid}/config | 
*DefaultApi* | [**geo_replication_create**](docs/DefaultApi.md#geo_replication_create) | **POST** /geo-replication/{mastervolid}/{remotevolid} | 
*DefaultApi* | [**geo_replication_delete**](docs/DefaultApi.md#geo_replication_delete) | **DELETE** /geo-replication/{mastervolid}/{remotevolid} | 
*DefaultApi* | [**geo_replication_pause**](docs/DefaultApi.md#geo_replication_pause) | **POST** /geo-replication/{mastervolid}/{remotevolid}/pause | 
*DefaultApi* | [**geo_replication_resume**](docs/DefaultApi.md#geo_replication_resume) | **POST** /geo-replication/{mastervolid}/{remotevolid}/resume | 
*DefaultApi* | [**geo_replication_ssh_key_generate**](docs/DefaultApi.md#geo_replication_ssh_key_generate) | **POST** /ssh-key/{volname}/generate | 
*DefaultApi* | [**geo_replication_ssh_key_get**](docs/DefaultApi.md#geo_replication_ssh_key_get) | **GET** /ssh-key/{volname} | 
*DefaultApi* | [**geo_replication_ssh_key_push**](docs/DefaultApi.md#geo_replication_ssh_key_push) | **POST** /ssh-key/{volname}/push | 
*DefaultApi* | [**geo_replication_start**](docs/DefaultApi.md#geo_replication_start) | **POST** /geo-replication/{mastervolid}/{remotevolid}/start | 
*DefaultApi* | [**geo_replication_status**](docs/DefaultApi.md#geo_replication_status) | **GET** /geo-replication/{mastervolid}/{remotevolid} | 
*DefaultApi* | [**geo_replication_status_list**](docs/DefaultApi.md#geo_replication_status_list) | **GET** /geo-replication | 
*DefaultApi* | [**geo_replication_stop**](docs/DefaultApi.md#geo_replication_stop) | **POST** /geo-replication/{mastervolid}/{remotevolid}/stop | 


## Documentation For Models

 - [Create](docs/Create.md)
 - [Option](docs/Option.md)
 - [OptionResp](docs/OptionResp.md)
 - [Pause](docs/Pause.md)
 - [Remotehost](docs/Remotehost.md)
 - [Remotehost2](docs/Remotehost2.md)
 - [Resume](docs/Resume.md)
 - [Session](docs/Session.md)
 - [SshPublicKey](docs/SshPublicKey.md)
 - [SshPublicKey2](docs/SshPublicKey2.md)
 - [Start](docs/Start.md)
 - [Stop](docs/Stop.md)
 - [Worker](docs/Worker.md)


## Documentation For Authorization

 All endpoints do not require authorization.


## Author

you@your-company.com


