from main import *

writeToFile("greet.txt", "Hello!\n")
appendTofile("greet.txt", "Goodbye!\n")
assert readFromFile("greet.txt") == "Hello!\nGoodbye!\n"