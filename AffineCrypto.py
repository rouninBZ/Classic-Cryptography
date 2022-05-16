def isCoprime(a,b):
    lger=max(a,b)
    lser=min(a,b)
    c=lger%lser
    if a==1 or b==1:
        return True
    while c not in (0,1):
        lger,lser=lser,lger%lser
        c=lger%lser
    if c==0:
        return False
    elif c==1:
        return True

def affine_cipher(a,b,cipher_list='ABCDEFGHIJKLMNOPQRSTUVWXYZ',plain_text=''):
    #Need GCD(a,n)=1,or it fails.
    cipher_list=cipher_list.upper().replace(' ','')
    plain_text=plain_text.upper().replace(' ','')
    n=len(cipher_list)
    if not isCoprime(a,n):
        print("Your a&n are not coprime.This will lead to multiple decryption.Please change your a&n.")
    elif len(cipher_list)!=len({i for i in cipher_list}):
        print("No same letters in cipher_list.")
    else:
        #Default LETTERS only.
        cipher_text=''
        try:
            for letter in plain_text:
                #!
                cipher_text+=cipher_list[((cipher_list.index(letter))*a+b)%n]
            print(cipher_text)
        except:
            print("Check if all letters in your plain_message is in cipher_list!")

def decrypt_affine_cipher(a,b,cipher_list='ABCDEFGHIJKLMNOPQRSTUVWXYZ',cipher_text=''):
    plain_text=''
    cipher_list.upper().replace(' ','')
    n=len(cipher_list)
    if not isCoprime(a,n):
        print("Your a&n are not coprime.This will lead to multiple decryption.Please change your a&n.")
    elif len(cipher_list)!=len({i for i in cipher_list}):
        print("No same letters in cipher_list.")
    else:
        for letter in cipher_text:
            y=cipher_list.index(letter)
            for i in range(n):
                x=(y+n*i-b)/a
                if x==int(x):
                    break
            plain_text+=cipher_list[int(x)]
    print(plain_text)

affine_cipher(3,1,plain_text='ABC')
decrypt_affine_cipher(3,1,cipher_text='BEH')
