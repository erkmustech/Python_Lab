print("this is lab 110");
print("Python has three numeric types: int, float, and complex");

myValue=1;
print(myValue);
print(type(myValue));

myValue=3.14;
print(type(myValue));

print(str(myValue) + " is of the data type " + str(type(myValue)));

myValue =False;
print(myValue);
print(type(myValue));

myString = "This is a string."
print(myString);
print(type(myString));

print(myString + " is of the data type " + str(type(myString)))


firstString = "water"
secondString = "fall"
thirdString = firstString + secondString
print(thirdString);

# input
name = input("What is your name? ");
color = input("What is your favorite color?  ")
animal = input("What is your favorite animal?  ")
print("your name is "+ (name)+", your favorite color is "+(color)+" and your favorite animal is "+(animal));


# format
print("{}, you like a {} {}!".format(name,color,animal))