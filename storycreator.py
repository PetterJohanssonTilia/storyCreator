#Open the story.txt in read mode
with open("story.txt", "r") as storytxt:
    story = storytxt.read()

print(story)