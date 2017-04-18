# get message from user and print it backwards
#[x] get message
#[x] create message_backwards
#[x] print message_backwards

msg = input("msg?\n")
msg_back = ""
letter = ""

while msg:
    msg_back += msg[len(msg) -1]
    msg = msg[:len(msg) -1]
    print("\nYe olde word:", msg)
    print("THIS IS THE NEW SHIT:", msg_back)
