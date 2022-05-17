def virginia_cipher(given_list="ABCDEFGHIJKLMNOPQRSTUVWXYZ",cipher_key="",plain_text=""):
    #You can give your own alpha list to make cipher_table.
    #Default alpha list is based on English alphabeta.
    given_list=given_list.upper().replace(' ','')
    cipher_key=cipher_key.upper().replace(' ','')
    plain_text=plain_text.upper().replace(' ','')

    if len(cipher_key)!=len({i for i in cipher_key}):
        print("No same letters in cipher_key.")
    elif len(given_list)!=len({i for i in given_list}):
        print("No same letters in given_list.")
    else:
        ls=[given_list.index(i) for i in cipher_key]
        table=[]
        cipher_text=''
        for index in ls:
            table.append(given_list[index:]+given_list[:index])
        for index in range(len(plain_text)):
            cipher_text+=table[index%len(table)][given_list.index(plain_text[index])]
    print(cipher_text)

def decrypt_virginia_cipher(given_list="ABCDEFGHIJKLMNOPQRSTUVWXYZ",cipher_key="",cipher_text=""):
    given_list=given_list.upper().replace(' ','')
    cipher_key=cipher_key.upper().replace(' ','')
    cipher_text=cipher_text.upper().replace(' ','')

    if len(cipher_key)!=len({i for i in cipher_key}):
        print("No same letters in cipher_key.")
    elif len(given_list)!=len({i for i in given_list}):
        print("No same letters in given_list.")
    else:
        ls=[given_list.index(i) for i in cipher_key]
        table=[]
        plain_text=''
        for index in ls:
            table.append(given_list[index:]+given_list[:index])
        for index in range(len(cipher_text)):
            mod_index=index%len(table)
            plain_text+=given_list[table[mod_index].index(cipher_text[index])]
        print(plain_text)

virginia_cipher(cipher_key='MONDAY',plain_text="iffuguidontxiangwang")
decrypt_virginia_cipher(cipher_key='MONDAY',cipher_text='UTSXGSURBQTVUOAJWYZU')