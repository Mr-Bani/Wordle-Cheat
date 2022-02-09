with open("Words.txt","r",encoding="utf-8") as file:
    words = file.read()
words = list(set(list(words.lower().replace("\u200c","").split())))
print("Welcome to Wordle-Cheat cheat. This is just for fun")
print("What should it have ?")
inc = list(set(list(input().lower().replace(" ",""))))
print("What should it not have ?")
exc = list(set(list(input().lower().replace(" ",""))))
print("Enter right letters in right places. Enter 0 for empty places.")
right = list(input().lower())
print("Enter right letters in wrong places. Enter 0 for empty places.")
wrong = list(input().lower())


def includes(word,inc):
    for char in inc:
        if char not in word:
            return False
    return True
def excludes(word,exc):
    for char in exc:
        if char in word:
            return False
    return True
def word_check(word,places):
    for i in range(len(places)):
        if places[i]!="0":
            if word[i]!=places[i]:
                return False
    return True
def wrong_place(word,places):
    for i in range(len(places)):
        if places[i]!="0":
            if word[i]==places[i]:
                return False
    return True




res = [word for word in words if (len(word)==5 and includes(word,inc) and excludes(word,exc) and word_check(word,right) and wrong_place(word,wrong))]

print("These words can be the answer: \n")
print(*[i+"\n" for i in res])




