import re

input_file = open('train.txt', mode='r', encoding='UTF-8')
output_file = open('output.txt', mode='w', encoding='UTF-8')

lines = []
plural_words = []
proper_plural_words = []

word_count = 0
total_letters = 0
avg_word_length = 0

with input_file:
    for line in input_file:
        lines.append(line)

#search for plural words
for line in lines:
    matches = re.findall('\\b([^ \n]*?l[ae]r)\\b',line)
    for x in matches:
        if(x != None):
            if(x not in plural_words):
                plural_words.append(x)

#print("Plural Words ({}):\n {}\n".format(len(plural_words),plural_words),"\n")
#print("Plural Words ({}):\n {}\n".format(len(plural_words),plural_words),"\n", file=output_file)


#search for proper plural words
for line in lines:
    matches = re.findall('(([A-ZŞÇÜÖİ][\wşçüöı]*(\s[A-ZŞÇÜÖİ][\wşçüöı]*)+)|(?<= )([A-ZŞÇÜÖİ][^ \n]*))l[ea]r',line)
    for x in matches:
        if(x != None):
            if(x not in proper_plural_words):
                proper_plural_words.append(x)

#print("Proper Plural Words ({}):\n {}\n".format(len(proper_plural_words),proper_plural_words),"\n")
#print("Proper Plural Words ({}):\n {}\n".format(len(proper_plural_words),proper_plural_words),"\n", file=output_file)


#find average word length \b[^\d+][a-zA-ZöçşığÖÇŞİĞüÜ']*?
for line in lines:
    matches = re.findall('\\b[^\d+\.\s][a-zA-ZöçşığÖÇŞİĞüÜ\']*? ',line)
    for x in matches:
        if(x != None):
            total_letters += len(x) - 1 #because white space at last character of string
            word_count += 1

if word_count>0:
    avg_word_length = total_letters / word_count
else:
    avg_word_length = 0

print ("Total word count:", word_count)
print ("Total word count:", word_count, file=output_file)
print ("Total letter count:", total_letters)
print ("Total letter count:", total_letters, file=output_file)
print ("Average word length:",round(avg_word_length,2))
print ("Average word length:",round(avg_word_length,2), file=output_file)




