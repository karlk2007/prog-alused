#1. Sõna-tüüpi muutujate deklareerimine
first_name = "James"
last_name = "Bond"

#2. Sõnede kujundamine - names
full_name = first_name + " " + last_name
self_description_sentence = f"My name is {last_name}, {first_name} {last_name}."

#3 Sõnede kujundamine - cake string 
cake = "vahukoormarjadtäidispõhi"
print(cake.replace("täidis", "täidis\n").replace("põhi", "põhi").replace("marjad", "marjad\n").replace("vahukoor", "vahukoor\n"))

#Sõnede tükeldamine
original_string = "Programming is fun!"
backwards = original_string[::-1]
every_other = original_string[::2]
first_word_reversed = original_string.split()[0][::-1]

#Printimine
"""
print("1. Sõna-tüüpi muutjad:")
print(f"first_name:  {first_name}")
print(f"last_name: {last_name}\n")

print("2. Sõnede kujundamine - names:")
print(f"full_name: {full_name}")
print(f"self_description_sentence: {self_description_sentence}\n")

print("3. Sõnede kujundamine - cake string:")
print(cake.replace("täidis", "täidis\n"). replace ("põhi", "põhi"). replace("marjad", "marjad\n").replace("vahukoor", "vahukoor\n"))

print("\n4. Sõnede tükeldamine:")
print(f"original_string: ) {original_string}")
print(f"backwards: {backwards}")
print(f"every_other: {every_other}")
print(f"first_word_reversed: {first_word_reversed}")
"""