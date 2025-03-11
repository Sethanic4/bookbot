def get_num_words(strbook):
    i = 0
    words = strbook.split()
    for word in strbook.split():
        i += 1
    print(f"Found {i} total words")
def letter_count(strbook):
    cntletters = {}
    for word in strbook.split():
        word = word.lower()
        for letter in word:
            if letter.isalpha():
                chk = letter in cntletters
                if chk == False:
                    cntletters[letter] = 1
                else:
                    cntletters[letter] += 1
    return cntletters
def clean_print(dictlettercount):
    newdict = []
    for item in dictlettercount:
        newdict.append({"name":item,"num":dictlettercount[item]})
    newdict.sort(reverse=True,key=lambda x: x["num"])
    return newdict