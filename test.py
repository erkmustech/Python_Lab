# print("inter your age")
# age = ""
# b = "adult"
# c = "tenegeer"
# print(age > 10 ? b: c)

#Ternary operator in python

def my_function(real_name, optional_display_name=None):
    optional_display_name = optional_display_name or real_name
    print(optional_display_name)


my_function("John")
my_function("Mike", "anonymous123")


# 1.2. Usage of **kwargs
def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))


greet_me(name="furkan")
