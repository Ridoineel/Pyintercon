# Pyintercon is a simple python server and client to interconnect the hosts of your application.

> All package that use in this is built-in packages (refer in requirements.txt)

The server is activate on server host, and the client in all application clients (interconnected).

Client send request to Server and the Server answered.
The traitement function of server can be edit by developper.


## Example:

### Server:
```python
    >>> from pyintercon import Server

    >>> # initialize the server
    >>> sv = Server(nb_client = 1)

    >>> # run the server on $host address and $port
    >>> sv.actiavte("localhost", 8080)
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
    >>> # use disconnected method to disconnect server
    >>> cl.disconnect()

    >>> """ server output:
        ('127.0.0.1', 44042) is disconnected ...
    """
```
</br>

> #### The server manage the response loader by the treatment function.
> This function take the request data (dict object) and return by default _{"status": 1, "message": "default"}_. </br>
> He can edit it by set server.treatment = your_treatment_function

> ```python
>    >>> sv = Server() # One client by default
>    >>> sv.treatment = your_treatment_function
> ```

## Last's example:

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

    # set the treatment function
    sv.treatment = response_loader

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
* Use threading for get client simultaneously with manage request response.
* Add more events, possibility to emit events.
