# Text Pro Demo App
# Description: very basic demo app covering the Python syntax: functions, loops, statements

# Author: Valeriy B.
# Language: Python


# Question words
def question_words(msg):
    questions_list = ["what", "where", "when", "which", "who", "whom", "whose", "why", "how", "is", "are", "will"]
    hello_list = ["hello", "hi", "howdy"]
    if msg == "hello":
        return hello_list
    elif msg == "questions":
        return questions_list


# App logic
def textpro(msg):
    
    # Result list
    result_list = []
    
    # Looping while message not equals '!end'
    while msg != ("!end"):

        # Typing messages
        msg = input("Type something: ")
        
        # Verifying if first typed word is not in question words list
        if msg.split()[0] in question_words("questions"):
            result_list.append(msg.capitalize() + "?")
        elif msg.split()[0] in question_words("hello"):
            result_list.append(msg.capitalize() + "!")
        else:
            result_list.append(msg.capitalize() + ".")
    
    # Printing the the list converted into string without the last element
    print(" ".join(result_list[:-1]))


textpro("")