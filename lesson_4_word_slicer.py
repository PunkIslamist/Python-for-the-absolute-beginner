word = input("Guess what?\n")

start = None

while start != "":
    start = int(input("Start value?\n"))
    end = int(input("End value?\n"))
    print(word[start:end])
    
