# Use the if statement
# Use the else statement
# Use the elif statement

userReply = input("Do you need to ship a package? (Enter yes or no) ")
if userReply == "yes":
    print("We can help you ship that package!")
elif userReply == "no":
    print("take your rubbish away");
else:
    print("hallo, are you there? Say 'yes or no'")
    userReply = input();
    if userReply == "yes":
        print("please select destiny")