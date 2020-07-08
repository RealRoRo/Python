'''
translater ronak language
vowel -> la

------------------------------------
find -> fland
eat -> lalat
'''


def lang_to_ronak(word):
    translator = ""
    for i in word:
        if i in "aeiouAEIOU":
            translator = translator + "la"
        else:
            translator = translator + i
    return translator


print(lang_to_ronak(input("ENter a phrase: ")))