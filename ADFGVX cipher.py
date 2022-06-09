import random as rd

def ADFGVX_cipher(exchange_key='BETA',cipher_alpha="ADFGVX",alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789',plain_text=''):
    if len(alpha)>len(cipher_alpha)**2:
        print('Not all alphas will be crypted.Lengthen your cipher alpha.')
    elif len(exchange_key)=={i for i in exchange_key}:
        print("Please choose an exchange key with no same alphas.")
    else:
        if len(alpha)<len(cipher_alpha)**2:
            print('This is a poor cipher!Conclude unused cipher alpha couple.')
            print('As a result,it\'s a waste of resource.')

        table={}
        k=0
        exchange_key=exchange_key.upper()
        cipher_alpha=cipher_alpha.upper()
        alpha=alpha.upper()
        plain_text=plain_text.upper()

        unarranged_alpha=[i for i in alpha]
        rd.shuffle(unarranged_alpha)
        for i in cipher_alpha:
            for j in cipher_alpha:
                table[unarranged_alpha[k]]=i+j
                k+=1
        raw_cipher_text=''
        for i in plain_text:
            raw_cipher_text+=table[i]
        if len(raw_cipher_text)%len(exchange_key)!=0:
            for j in range(len(raw_cipher_text) % len(exchange_key),len(exchange_key)):
                raw_cipher_text+=(cipher_alpha[rd.randint(0,len(cipher_alpha)-1)])                
        column=[[] for i in range(len(exchange_key))]
        i=0
        for i in range(len(raw_cipher_text)):
            column[i%len(exchange_key)].append(raw_cipher_text[i])
        dic={}
        for i in range(len(exchange_key)):
            dic[ord(exchange_key[i])]=column[i]
        cipher_text=''
        pre_exchange=sorted([ord(i) for i in exchange_key])
        for i in range(len(raw_cipher_text)):
            cipher_text+=dic[pre_exchange[i%len(exchange_key)]][i//len(exchange_key)]
        print(cipher_text)
        return table,exchange_key,cipher_text


def decrypt_ADFGVX_cipher(cipher_table={},exchange_key='BETA',cipher_text=''):
    #给密码本即可，密码本即代表了所有的可用字符，不需要alphabeta
    cipher_table={v:k for k,v in cipher_table.items()}
    print(cipher_table)
    column=[[] for i in range(len(exchange_key))]
    for i in range(len(cipher_text)):
        column[i%len(exchange_key)].append(cipher_text[i])

    dic={}
    for i,k in zip(sorted([ord(j) for j in exchange_key]),column):
        dic[i]=k
    column=[dic[ord(i)] for i in exchange_key]
    raw_cipher_text=''
    plain_text=''
    for i in range(len(cipher_text)):
        raw_cipher_text+=column[i%len(exchange_key)][i//len(exchange_key)]

    for i in range(0,len(raw_cipher_text),2):
        plain_text+=cipher_table[raw_cipher_text[i:i+2]]
        #包含为了补全column而随机生成的乱码的解编码，解编码后会保留在句末
    print(plain_text)
