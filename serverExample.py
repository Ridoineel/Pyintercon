from server import Server

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
