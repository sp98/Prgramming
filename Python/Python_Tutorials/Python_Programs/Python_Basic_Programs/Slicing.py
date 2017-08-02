#Slicing can be applied to both Strings and Lists.

myList = [1, 2, 3, 4, 5]
print(myList[1:3])

myList2 = [5, 4, 3, 2, 1]
myList3 = myList[:]  #creates a copy of the myList
myList3.sort()
print (myList2);
print (myList3)

#slicing limited things.
myList4 = list(range(0, 11));
print(myList4);
print(myList4[::2])   #leave a gap of 2
print(myList4[2::2])  #start from 2nd index and give a gap of 2
print(myList4[::-1])  # print List in a reversed order.
print(myList4[-1])
print(myList4[-2])


def myTest (text):
    return text[0: int(len(text)/2)].lower() + text[int(len(text)/2):].upper()

print(myTest("Santosh"))


def word_count(sentence):
    word_dict= {}
    for words in sentence.lower().split(" "):
        if not words in word_dict:
           word_dict[words] = 1
        else:
            word_dict[words] =  word_dict[words] + 1


    return word_dict


print(word_count("An else statement can be combined with an if statement. An else statement contains the block of code that executes if the conditional expression in the if statement resolves to 0 or a FALSE value. "

"The else statement is an optional statement and there could be at most only one else statement following if ."))



