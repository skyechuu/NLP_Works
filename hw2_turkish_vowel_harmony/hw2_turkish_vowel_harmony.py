import re

def has_turkish_vowel_harmony(word,return_output):
    dotted_vowels = ['E', 'İ', 'Ö', 'Ü', 'e', 'i', 'ö', 'ü']
    undotted_vowels = ['A', 'I', 'O', 'U', 'a', 'ı', 'o', 'u']
    vowels = dotted_vowels + undotted_vowels

    must_dotted = None

    for letter in word:
        if must_dotted == None: # decide type of harmony by looking first vowel in the word
            if dotted_vowels.__contains__(letter):
                must_dotted = True
            elif undotted_vowels.__contains__(letter):
                must_dotted = False
        if vowels.__contains__(letter) and must_dotted is not None: # if type is decided check only vowel letters for harmony
            if must_dotted:
                if not dotted_vowels.__contains__(letter):
                    if(return_output):
                        print("Word",{word},"has not vowel harmony :(",file=output_words_file)
                    return False # if not match with decided harmony, return false immediately
            else:
                if not undotted_vowels.__contains__(letter):
                    if (return_output):
                        print("Word",{word},"has not vowel harmony :(",file=output_words_file)
                    return False # if not match with decided harmony, return false immediately
    if must_dotted == None:
        if (return_output):
            print("Word",{word},"doesn't contain any vowel :S",file=output_words_file)
        return False
    else:
        if (return_output):
            print("Word",{word},"has","E-Dotted" if must_dotted else "A-Undotted","harmony!",file=output_words_file)
        return True


input_file = open('train.txt', mode='r', encoding='UTF-8')
output_file = open('output.txt', mode='w', encoding='UTF-8')
output_words_file = open('output_words.txt', mode='w', encoding='UTF-8')

lines = []
words = []

harmony_word_count = 0
not_harmony_word_count = 0



with input_file:
    for line in input_file:
        lines.append(line)

regex = "\\b[A-Za-zÜĞÇŞİÖüçöşiğı\']+(?=[^>])\\b"
#filtering words
for line in lines:
    seperated_lines = re.findall(regex, line)
    if(seperated_lines != []):
        for word in seperated_lines:
            words.append(word)

'''
#EXAMPLES FOR DEFINION TEST
w = "cseskodma"
w2 = "araba"
w3 = "pencere"
w4 = "akrilik"
w5 = "shdfghdfgfgh"
print(has_turkish_vowel_harmony(w))
print(has_turkish_vowel_harmony(w2))
print(has_turkish_vowel_harmony(w3))
print(has_turkish_vowel_harmony(w4))
print(has_turkish_vowel_harmony(w5))
'''

#change this variable to see word list and their statuses
create_output_word_list = True

for word in words:
    if(has_turkish_vowel_harmony(word,create_output_word_list)):
        harmony_word_count += 1
    else:
        not_harmony_word_count += 1

print("\nWords that has Turkish Vowel Harmony count:",harmony_word_count)
print("Words that has not Turkish Vowel Harmony count:",not_harmony_word_count)
print("\nNote: You can find word list with information about their harmony status on the file \'output_words.txt\'\nbut you need to change \'create_output_word_list\' parameter of the definition as True first!")
print("\nWords that has Turkish Vowel Harmony count:",harmony_word_count,file=output_file)
print("Words that has not Turkish Vowel Harmony count:",not_harmony_word_count,file=output_file)
print("\nNote: You can find word list with information about their harmony status on the file \'output_words.txt\'\nbut you need to change \'create_output_word_list\' parameter of the definition as True first!",file=output_file)








