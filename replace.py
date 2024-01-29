#Save the designated sentence under a variable
#Replace all the !'s in the sentence so it reads well
#Print this sentence
#Turn that whole sentence into uppercase
#Print the new uppercase sentence
#Reverse the sentence and print again

sentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."
print(sentence) #proof it has been stored properly

sentence = sentence.replace('!',' ')
print(sentence)

sentence = sentence.upper()
print(sentence)

sentence = sentence[::-1]
print(sentence)