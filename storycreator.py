#Open the story.txt in read mode
with open("story.txt", "r") as storytxt:
    story = storytxt.read()

#store the words
words = set()
start_of_word = -1
target_start = "<"
target_end = ">"

#Finds the place and element of the words
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i #Stores the index of start_of_word

    if char == target_end and start_of_word != -1: #Only targets words with -1 value
        word = story[start_of_word: i + 1] # adds the value of +1 to the word
        words.add(word) #adds the word to the list
        start_of_word = -1 #resets start_of_word to -1 to find the next word

answers = {} #stores the answers in a list

for word in words:
    answer = input("Enter a word for" + word + ": ") #loops through each word, the player inputs the answers
    answers[word] = answer     #the current word is now the player input answer


for word in words:
    story = story.replace(word, answers[word]) #replaces the words set with the words from the answers dictionary

print(story)
