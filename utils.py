from signal import SIGTERM # or SIGKILL
import socket
import hashlib
import random
import logging
import os


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

def createDummyFile(repeat): # default is 50 MB
    print("createDummyFile")
    filename = 'file_' + str(random.randint(1,2000)) + ".txt"
    f = open(filename,"w")
    repeat = 1024*1024*repeat or 1024*1024*random.randint(60,100)+random.randint(20,100)
    print(repeat)
    for i in range(repeat):
        if (i % (1024*1024*10) == 0): print(i)
        f.write("bobo\n")
    
    
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('repeat', type=int, nargs='+', default=1)
    args = parser.parse_args()    
    _ = list(map(createDummyFile, args.repeat))
    