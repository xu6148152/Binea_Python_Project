import socket
import requests

def public_ip():
    return requests.get('http://ipecho.net/plain').content

def local_ip():
    # return socket.gethostbyname(socket.gethostname())
    return ""
    
if __name__=="__main__":
    print("Getting public and local ip")
    print("Public IP: {}\nLocal IP: {}".format(public_ip(), local_ip()))