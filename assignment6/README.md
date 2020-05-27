# Distributed Server System

The program `assignment6.py` has been written using Flask framework in Python to initiate a server with the following features. 

The program `assignment6.py` maintains a map (where the keys are integers, and values are strings). 

## Endpoints

The program `assignment6.py` initiates a web server at port `8787` with two endpoints:

### /add

/add : This endpoint will accept POST requests containing JSON encoded data in the following format:
```
{
    'key': <an integer>,
    'value': <a string>
}
```
When the server receives a POST request on this endpoint, it adds the key:value pair in the map. However, if the key is already set, it ignores this request.
Also, whenever a new key is added to the map, the program sends POST requests to all the peers (a hardcoded list of urls) (so that they may add this value too).

### /list
/list : When this endpoint receives a GET request, it returns all the entries in the map as json data in the following format:
```
{
    key1: value1,
    key2: value2,
    key3: value3,
    ...
}
```

