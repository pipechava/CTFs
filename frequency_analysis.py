def char_frequency(str1):
    dict_char = {}
    for n in str1.lower():
        if n.isalpha():
            if n in dict_char:
                dict_char[n] += 1
            else:
                dict_char[n] = 1
    sorted_freq = dict(sorted(dict_char.items(), key=lambda item: item[1], reverse=True))
    return sorted_freq

def map_char_freq_percentage(dict1, dict2):
    total_chars_dict1 = sum(dict1.values())
    total_chars_dict2 = sum(dict2.values())
    perc_freq_dict1 = {k: (v / total_chars_dict1) * 100 for k, v in dict1.items() if k.isalpha()}
    perc_freq_dict2 = {k: (v / total_chars_dict2) * 100 for k, v in dict2.items() if k.isalpha()}
    sorted_perc_freq_dict1 = dict(sorted(perc_freq_dict1.items(), key=lambda item: item[1], reverse=True))
    sorted_perc_freq_dict2 = dict(sorted(perc_freq_dict2.items(), key=lambda item: item[1], reverse=True))
    mapping_percentage = dict(zip(list(sorted_perc_freq_dict1.keys()), list(sorted_perc_freq_dict2.keys())))
    return mapping_percentage

def map_char_freq_common(dict1, dict2):
    sorted_dict2 = dict(sorted(dict2.items(), key=lambda item: item[1], reverse=True))
    mapping_common = dict(zip(list(dict1.keys()), list(sorted_dict2.keys())))
    return mapping_common

text1 = '''The quick brown fox jumps over the lazy dog the quick brown fox jumps over the lazy dog The quick brown fox jumps over the lazy dog the quick brown fox jumps over the lazy dog The quick brown fox jumps over the lazy dog the quick brown fox jumps over the lazy dog The quick brown fox jumps over the lazy dog the quick brown fox jumps over the lazy dog The quick brown fox jumps over the lazy dog the quick brown fox jumps over the lazy dog

'''
text2 = '''PDV KLRBC IOEXQ AEY TLGMF EJVO PDV NSWH ZEU.
PDRF PVYP RF S MSQUOSG, XDRBD GVSQF PDSP RP BEQPSRQF SNN 26 NVPPVOF EA PDV VQUNRFD SNMDSIVP. PDRF GSCVF RP RZVSN AEO AOVKLVQBH SQSNHFRF, SF PDV BOHMPSQSNHFP BSQ BEGMSOV PDV AOVKLVQBH EA NVPPVOF RQ PDV BRMDVOPVYP PE PDV CQEXQ AOVKLVQBH EA NVPPVOF RQ PDV VQUNRFD NSQULSUV.

AEO VYSGMNV, PDV GEFP BEGGEQ NVPPVO RQ PDV VQUNRFD NSQULSUV RF V. RA PDV GEFP BEGGEQ NVPPVO RQ PDV BRMDVOPVYP RF Y, PDVQ PDV BOHMPSQSNHFP BSQ SFFLGV PDSP Y RF NRCVNH PE IV S FLIFPRPLPREQ AEO V.

EPDVO BEGGEQ NVPPVOF RQ PDV VQUNRFD NSQULSUV RQBNLZV P, S, E, R, Q, F, SQZ D. PDV BOHMPSQSNHFP BSQ LFV PDRF RQAEOGSPREQ PE GSCV VZLBSPVZ ULVFFVF SIELP PDV EPDVO FLIFPRPLPREQF RQ PDV BRMDVOPVYP.

ANSU{QEX_RJV_NVSOQVZ_GH_SIBF}
'''

freq1 = char_frequency(text1)
freq2 = char_frequency(text2)

mapping_percentage = map_char_freq_percentage(freq1, freq2)
mapping_common = map_char_freq_common(freq1, freq2)

print("Character mapping based on percentage frequencies: ", mapping_percentage)
print("Character mapping based on common frequencies: ", mapping_common)

print("Character frequencies in first text: ", freq1)
print("Character frequencies in second text: ", freq2)

trans_percentage = str.maketrans(''.join(mapping_percentage.keys()), ''.join(mapping_percentage.values()))
trans_common = str.maketrans(''.join(mapping_common.keys()), ''.join(mapping_common.values()))

text2_replaced_percentage = text2.lower().translate(trans_percentage)
print("Text2 after replacement trans_percentage: ", text2_replaced_percentage)
text2_replaced_common = text2.lower().translate(trans_common)
print("Text2 after replacement trans_common: ", text2_replaced_common)
