import base64
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import datetime as d


    
def encrypt(data,password):

    
    #print("==========Password generated========",password)
    
    try:
        password=bytes(password,'utf-8')   #Encoded Password
        data=bytes(data,'utf-8') #DATA
    except:
        pass
    
    
    dt=bytes(str(d.datetime.timestamp(d.datetime.now())),'utf-8')         #TIMESTAMP BEING USED AS SALT
    #print(dt)
    
    
    kdf = PBKDF2HMAC(                          #OBJECT MAKING
        algorithm=hashes.SHA256(),
        length=32,
        salt=dt,
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    
    
    
    f = Fernet(key)
    token = f.encrypt(data)  #ENCRYPTION

    #TIMESTAMP ADDED AT THE END OF ENCRYPTED DATA.
    token=token+dt
    
    #print(token)
    return token
    #print(f.extract_timestamp(token))


def decrypt(data,password):
    print(data)
    try:
        password=bytes(password,'utf-8')           #DECRYPT
        #print(password)    
        #INPUT ENCRYPTED DATA
        data=bytes(data,'utf-8')
        #print(data)
    except:
        pass
    
    
    
    #TAKING TIMESTAMP FROM THE END OF ENCRYTPED DATA
    dt=data[-17:]
    
    #REMOVING TIMESTAMP FROM THE END OF ENCRYTPED DATA
    data=data[:-17]
    
    
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=dt,
        iterations=480000,
    )
    key = base64.urlsafe_b64encode(kdf.derive(password))
    
    
    #DECRYPTION
    f=Fernet(key)
    value=f.decrypt(data)
    return value


