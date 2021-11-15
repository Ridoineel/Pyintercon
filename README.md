# A simple python Server and Client for interconnect your application

All package that use in this is built-in packages (refer in requirements.txt)

The server is activate on server host, and the client in all application clients (interconnecedt).

Client send request to Server and the Server answered.
The traitement function of server can be edit by developper.

## Samples:

### Server:
```python
    >>> from server import Server

    >>> # initialize the server
    >>> sv = Server(nb_client = 1)

    >>> # run the server on $host address and $port
    >>> sv.actiavte("localhost", 8080)
    """Server is activated on localhost:8080...
    Tap CTRL + C to quit !!!!!"""
```

### Client
```python
    >>> from client import Client

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
    >>> # use disconnected method to disconnect server
    >>> cl.disconnect()

    >>> """ server output:
        ('127.0.0.1', 44042) is disconnected ...
    """
```
