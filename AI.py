# Nikolei Advani, 1/27/17
# This program allows the user to converse with an AI
import random
# The following lines of code open and analyze a list of responses
g = open('Responses.txt', 'r')
readg = g.readlines()
g.close()
# The following lines of code open and analyze a list of questions
f = open('Questions.txt', 'r')
readf = f.readlines()
f.close()
# This while loop operates the conversation
while True:
# The following lines of code assigns the data in each list to a set
    setg = set(readg)
    setf = set(readf)
# The following lines of code prompts the user for conversation and gives a command to terminate
    start = input("> ")
    if start in ["end", "END", "End"]:
        break
# The following lines of code registers the user input as a question and pulls a response
# It then appends the input to the set of questions (f)
    elif "?" in start:
        print("> ", random.choice(readg))
        readf.append(start + "\n")
# If the input is registered as a statement, the input is appended to set g
# A question or response is pulled and delivered to the user
    else:
        readg.append(start + "\n")
        chance = random.randint(1, 2)
        if chance == 1:
            print(random.choice(readf))
        else:
            print(random.choice(readg))


# The following lines of code takes all the data collected in each set and allocates it to its appropriate text file
# The lists are then closed
g = open('Responses.txt', 'w')
f = open('Questions.txt', 'w')
for x in setg:
    g.write(x)

for x in setf:
    f.write(x)

g.close()
f.close()