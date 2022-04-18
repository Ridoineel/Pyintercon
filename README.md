# Pyintercon is a python module to connect a server and clients allowing them to exchange information


When an instance of Client sends a request to an instance of Server, the value returned by the `request handler` function is the response sent to the client. <br />
See below for how to set a request handler function and how it works


## Installation

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
        # the default host address is "localhost"
    >>> sv.activate("", 8080)
    """Server is activated on localhost:8080...
    Tap CTRL + C to quit !!!!!"""
```

### Client

```python
    >>> from pyintercon import Client

    >>> # initialize the client
    >>> cl = Client()

    >>> # connect client to server by calling the connect method with $hostname and $port used as for server.activate
    >>> cl.connect("localhost", 8080)


    # you will get on server side a message like this
    >>> """ server output:
            ('127.0.0.1', 44042) is connected ...
        """

    >>> # You are ready to go with pyintercon
    >>> # You can send a request to server by calling the send method of the client instance
    >>> response = cl.send({ message: "Hello World !" })

    >>> print(response)
    {'status': 1, 'message': 'default'}
    >>> # use disconnect method to disconnect from the server
    >>> cl.disconnect()

    # you will get on server side a message like this
    >>> """ server output:
            ('127.0.0.1', 44042) is disconnected ...
        """
```

</br>

> #### The server manage the request by executing the request handler function and sends its returned value as response
>
> This function takes the request data (dict object) and returns the a value which will be used as response.
> The default handler returns _{"status": 1, "message": "default"}_ for everything. </br>
> This can be edited by setting a custom handler using setRequestHandler method

> ```python
>    >>> sv = Server()
>    >>> server.setRequestHandler(your_handler_function)
> ```
>
> See example below

## Example:

### Server

```python
from pyintercon import Server

def response_loader(request):
    """ Just reverse the message content.
        It takes dict object and returns dict object

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

> ## Features:

* Add more events, possibility to emit events. <br/>
    ```python
    client.emit("event_name", callback_function)
    ```
    at the moment sending the request is considered as the only event
