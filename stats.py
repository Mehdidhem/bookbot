

def get_num_words(text):
    l = text.split()
    result = len(l)
    return result

def get_num_char(text):
    dico_char = {}
    for c in text:
        char_low = c.lower()
        if char_low in dico_char:
            dico_char[char_low] += 1
        else:
            dico_char[char_low] = 1
    return dico_char

def sort_on(items):
    return items["num"]

def sort_dic(dic):
    sorted_list_dic = []
    for key,value in dic.items():
        new_dic = {}
        new_dic["char"] = key
        new_dic["num"] = value
        sorted_list_dic.append(new_dic) 
    sorted_list_dic.sort(reverse=True,key=sort_on)
    return sorted_list_dic

