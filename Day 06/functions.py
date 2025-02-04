print("Hello")
print(len("Hello"))

def my_function() -> None: #defining de function
    print("Hello")
    print("Bye")

def bye() -> str:
    return "Bye"

my_function() #calling the function

print(f"Hello {bye()}")

my_function()

if 1 > 0:
    print("Yes")
