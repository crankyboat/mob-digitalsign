import hashlib

DEFAULT_SECRET = "holamobivitysd"

def createSignature(message):
    return hashlib.sha1(message.encode()+DEFAULT_SECRET.encode()).hexdigest()

def verifySignature(message, digest):
    return hashlib.sha1(message.encode()+DEFAULT_SECRET.encode()).hexdigest() == digest
