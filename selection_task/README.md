# Hash Web Server
The program `task.py` creates a simple web server in Python, using Flask. The server listens on port `8787`.

There is one endpoint `/hash` which accepts a POST request that contains JSON encoded data in the following format:
```
{
    "data": "<a string>"
}
```
and the endpoint calculates the SHA-256 hash of the given string, converts it to hexadecimal representation, and returns it in the following format as JSON encoded data:
```
{
    "hash": "hexadecimal representation of the SHA-256 hash of the given string"
}
```
