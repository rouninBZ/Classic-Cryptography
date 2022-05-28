def Playfair_cipher(plain_text='',cipher_key='JAMES',alphabeta='ABCDEFGHIKLMNOPQRSTUVWXYZ',append_letter='X',search_column=True,ignored='J',employed='I'):
    #Default alphabeta doesn't include J,replaced by I.
    #Maybe Japanese kana is fitter for Playfair?
    change_set=[ignored,employed]
    plain_text=plain_text.upper().replace(change_set[0],change_set[1]).replace(' ','')
    cipher_key=cipher_key.upper().replace(change_set[0],change_set[1]).replace(' ','')
    cipher_table={}
    ls=[i for i in cipher_key+alphabeta]
    arranged_letters=list(set(ls))
    arranged_letters.sort(key=(cipher_key+alphabeta).index)
    for i in range(len(arranged_letters)):
        cipher_table[arranged_letters[i]]=(i//5,i%5)
    #print(cipher_table)
    raw_text=[]
    if len(plain_text)%2!=0:
        plain_text+=append_letter
    for i in range(0,len(plain_text),2):
        if plain_text[i]!=plain_text[i+1]:
            raw_text.append(plain_text[i:i+2])
        else:
            raw_text.append(plain_text[i]+append_letter)
            raw_text.append(plain_text[i+1]+append_letter)
    anti_table=dict([k,v] for v,k in cipher_table.items())
    cipher_text=[]
    for couple in raw_text:
        first=cipher_table[couple[0]]
        second=cipher_table[couple[1]]
        if first[0]==second[0]:
            cipher_text.append(anti_table[(first[0],(first[1]+1)%5)]+anti_table[(second[0],(second[1]+1)%5)])
        elif first[1]==second[1]:
            cipher_text.append(anti_table[((first[0]+1)%5,first[1])]+anti_table[((second[0]+1)%5,second[1])])
        else:
            if search_column:
                cipher_text.append(anti_table[(first[0],second[1])]+anti_table[(second[0]),first[1]])
                #Default search for the same column
            else:
                cipher_text.append(anti_table[(second[0],first[1])]+anti_table[(first[0]),second[1]])
    cipher_text=''.join(cipher_text)
    print(cipher_text)


def decrypt_Playfair_cipher(cipher_text='',cipher_key='JAMES',alphabeta='ABCDEFGHIKLMNOPQRSTUVWXYZ',append_letter='X',ignored='J',employed='I',search_column=True):
    change_set=[ignored,employed]
    cipher_key=cipher_key.upper().replace(change_set[0],change_set[1]).replace(' ','')
    cipher_table={}
    ls=[i for i in cipher_key+alphabeta]
    arranged_letters=list(set(ls))
    arranged_letters.sort(key=(cipher_key+alphabeta).index)
    for i in range(len(arranged_letters)):
        cipher_table[arranged_letters[i]]=(i//5,i%5)
    anti_table=dict([k,v] for v,k in cipher_table.items())
    plain_text=[]
    raw_text=[]
    for i in range(0,len(cipher_text),2):
        raw_text.append(cipher_text[i:i+2])
    for couple in raw_text:
        first=cipher_table[couple[0]]
        second=cipher_table[couple[1]]
        if first[0]==second[0]:
            plain_text.append(anti_table[(first[0],(first[1]-1)%5)]+anti_table[(second[0],(second[1]-1)%5)])
        elif first[1]==second[1]:
            plain_text.append(anti_table[((first[0]-1)%5,first[1])]+anti_table[((second[0]-1)%5,second[1])])
        else:
            if search_column:
                plain_text.append(anti_table[(first[0],second[1])]+anti_table[(second[0]),first[1]])
                #Default search for the same column
            else:
                plain_text.append(anti_table[(second[0],first[1])]+anti_table[(first[0]),second[1]])
    plain_text=''.join(plain_text)
    print(plain_text)