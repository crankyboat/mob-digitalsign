import hashlib
import uuid

def createSignature(message):
    salt = uuid.uuid4().hex
    return hashlib.sha1(message.encode()+salt.encode()).hexdigest() + ':' + salt

def verifySignature(message, hashedMessage):
    digest, salt = hashedMessage.split(':')
    return hashlib.sha1(message.encode()+salt.encode()).hexdigest() == digest
