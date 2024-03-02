
import miniproj1 as m1


while True:

    print("Press:\n1.Encrypt\n2.Decrypt\nEnter value:")
    choice_main=int(input())
    
    inp_type=int(input("Press:\n1.Text\n2.File"))
    
    if choice_main==1:
        if inp_type==1:
            inp_data=input("Enter text:")
            passkey=input("Enter password:")
            cipher=m1.encrypt(inp_data, passkey)
            #The encrypted data is in cipher do any manipulations here.
            print("The encrypted data is:\n",cipher)
        elif inp_type==2:
            address=input("Enter address of file:")
            f=open(address,'rb')
            inp_data=f.read();print(inp_data)
            f.flush()
            f.close()
            passkey=input("Enter Password:")
            cipher=m1.encrypt(inp_data, passkey)    #contains encryped cipher
            f=open(input("Enter address to store file:"),"wb")
            f.write(cipher)
        else:
            print("Invalid choice")

    elif choice_main==2:
        if inp_type==1:
            inp_cipher=input("Enter cipher:")
            passkey=input("Enter password:")
            data=m1.decrypt(inp_cipher, passkey)    #contains decrypted data
            print(data)
            
            # The decrypted values are in data
            
        elif inp_type==2:
            f=open(input("Enter address to read cipher from:"),'rb')
            inp_cipher=f.read()
            f.flush()
            f.close()
            passkey=input("Enter Password:")
            data=m1.decrypt(inp_cipher, passkey)    #contains decrypted data
            f=open(input("Enter address to store decrypted data at:"),'wb')
            f.write(data)
            f.flush()
            f.close()
        else:
            print("Invalid choice")
    else:
        print("Invalid choice")
