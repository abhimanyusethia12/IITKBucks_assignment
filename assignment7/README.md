# Mining Server

The server has two endpoints:

## `/start`

* will start the worker to mine a string
* target value will be `0000000f00000000000000000000000000000000000000000000000000000000` 
* receives a `POST` request with a string
* returns status `200` immediately
* This will accept a POST request with the following JSON data:
```
{
    "data" : "meowmeow"
}
```

## `/result`

* receives a `GET` request
* returns JSON response in format: 
```
{
    "result": "found", // Either "found" or "searching"
    "nonce": 123 // This field should be -1 if still searching, or the nonce value if it has been found.
}
```

## Threading

The important part here is the worker. It should run separate from the main thread (or the main thread will be blocked and you'll not be able to receive any requests)
