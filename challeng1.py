# count vowels and consenants in a string
# count the number of capital / upper case letters
# remove spaces from string without string methods

sentence = "Lorem ipsum dolor sit amet consectetur adipisicing elit. Fugit iure tempore iusto id maiores. Quidem quos eius tenetur quisquam, laudantium ea ex deleniti earum alias inventore tempore? Dolores, dicta sit?"

num_vowels = 0
num_consonants = 0
num_upper_case = 0

for character in sentence: 
    if character.isupper():
        num_upper_case += 1

    if character in ' !"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~':
        continue 

    if character.lower() in 'aeiou':
        num_vowels += 1
    else:
        num_consonants += 1 # this would include punctuation and numbers also

print(f"Number of vowels: {num_vowels}")
print(f"Number of Consonants: {num_consonants}")
print(f"Number of upper case letters: {num_upper_case}")


sentence_without_space = ""

for character in sentence:
        if character != " ":
            sentence_without_space += character

print (sentence_without_space)