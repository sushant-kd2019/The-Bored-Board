import re,string

def gen_words(st):
    return list(filter(lambda w: len(w) > 0, re.split('\W+', st)))

def create_hsh_table(st,hashtable):
    tmp = hashtable
    for i in gen_words(st):
        if i in tmp:
            tmp[i] += 1
        else:
            tmp[i] = 1
    return tmp
    

def separate_dict(og):
    tmp1=dict()
    tmp2=dict()
    tmp3=dict()
    tmp4=dict()
    tmp5=dict()
    for i in og:
        if og[i]<6:
           tmp1[i]=og[i]
        elif og[i]<11:
            tmp2[i]=og[i]
        elif og[i]<16:
            tmp3[i]=og[i]
        elif og[i]<21:
            tmp4[i]=og[i]
        else:
            tmp5[i]=og[i]
    print(len(tmp1),len(tmp2),len(tmp3),len(tmp4),len(tmp5))
    return [tmp1,tmp2,tmp3,tmp4,tmp5]

