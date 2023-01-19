from signal import SIGTERM # or SIGKILL
import socket
import hashlib

            
# Takes key string, uses SHA-1 hashing and returns a 10-bit (1024) compressed integer
def getHash(key, max_nodes):
    result = hashlib.sha1(key.encode())
    return int(result.hexdigest(), 16) % max_nodes

# Get local IP
def getSelfIP():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip = s.getsockname()[0]
    s.close()
    return ip
