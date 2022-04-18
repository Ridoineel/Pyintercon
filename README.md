# Pyintercon is a python module to connect your server and your clients and exchange information with  them

```
The class Server of pyintercon is used on server host, <br />
and the class  Client on all your application's clients.

Client send request to Server and the Server answered.
The server's request handler function would be defined.
```


## Install pyintercon

```bash
    pip install pyintercon
```


## Example:

### Server:
```python
    >>> from pyintercon import Server

    >>> # initialize the server
    >>> sv = Server()

    >>> # run the server using host address and port
    >>> sv.actiavte("", 8080)
    """Server is activated on localhost:8080...
    Tap CTRL + C to quit !!!!!"""
```

### Client
```python
    >>> from pyintercon import Client

    >>> # initialize the client
    >>> cl = Client()

    >>> """ server output:
        ('127.0.0.1', 44042) is connected ...
    """

    >>> # connect client to server on $host address and $port
    >>> cl.connect("localhost", 8080)

    >>> # Now send request to server and get response
    >>> response = cl.send({ message: "Hello World !" })

    >>> print(response)
    {'status': 1, 'message': 'default'}
    >>> # use disconnect method to disconnect server
    >>> cl.disconnect()

    >>> """ server output:
        ('127.0.0.1', 44042) is disconnected ...
    """
```
</br>

> #### The server manage the response by the request handler function.
> This function take the request data (dict object) and return by default _{"status": 1, "message": "default"}_. </br>
> Can be edited by server.setRequestHandler(your_handler_function)

> ```python
>    >>> sv = Server()
>    >>> server.setRequestHandler(your_handler_function)
> ```
> See example below

## Example:

### Server

```python
from pyintercon import Server

def response_loader(request):
    """ Just reverse the message content.
        He take dict object and return dict object

    """

    res = {"message": request["message"][::-1]}

    return res

def main():
    sv = Server()

    # set the request handler function
    sv.setRequestHandler(response_loader)

    sv.activate("localhost", 8080)

if __name__ == "__main__":
    main()
```

### Client

```python
    >>> from pyintercon import Client
    >>> cl = Client()
    >>> cl.connect("localhost", 8080)
    >>> res = cl.send({"message": "Hello World !"})
    >>>
    >>> print(res)
    {"message": "! dlroW olleH"}
```

</br>

> ## Futures:
* Add more events, possibility to emit events.
