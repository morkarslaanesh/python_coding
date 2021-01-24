# Function that is filling up cut strings to the longest matching string in the set

def scanList(equipment):
    dict_tmp = {}
    if (equipment != None) and (equipment != ''):
        for word in data_germany_note_10['equipment1']:
            if (equipment != word) and (word != None) and (word != '') and equipment == word[:len(equipment)]:
                dict_tmp[word] = levenshtein(equipment,word)
            else:
                equipment_r = equipment
        try:
            if (len(equipment) < len(min(dict_tmp,key=dict_tmp.get)) and equipment == min(dict_tmp,key=dict_tmp.get)[:len(equipment)] ):
                equipment_r = min(dict_tmp,key=dict_tmp.get)
            else:
                equipment_r = equipment
        except:
            equipment_r = equipment
    else:
        equipment_r = None
    return equipment_r
