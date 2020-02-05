from mathy import *
print("***********NAMASKARA*********")
print(responses[0])
print(responses[1])
while True:
    print()
    text = input("WHAT OPERATIONS YOU WANT ME TO PERFORM???")
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:

                l=extract_num_from_string(text)
                print(operations[word.upper()](l[0],l[1]))


            except:
                    print("SOMETHING WENT WRONG , PLEASE RETRY!!!")
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
    else:
        sorry()