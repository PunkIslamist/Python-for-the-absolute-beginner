#get message and print it minus vowels

vowels = "aeiouAEIOU"
message = input("Yes, I need your input again:\n")
msg_new = ""

for i in message:
    if i not in vowels:
        msg_new += i
        print(msg_new)
