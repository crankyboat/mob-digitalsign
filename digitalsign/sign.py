import hashlib

DEFAULT_SECRET = "mobivitysd"

def createSignature(message):
    return hashlib.sha1(message+DEFAULT_SECRET).hexdigest()

def verifySignature(message, digest):
    return hashlib.sha1(message+DEFAULT_SECRET).hexdigest() == digest
