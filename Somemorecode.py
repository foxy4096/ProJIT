from cryptography.fernet import Fernet


import simplejson

data = simplejson.dumps({"key": Fernet.generate_key()})

print(data)