import os

out = "path.txt"
for i in range(len(os.listdir("mooc-java-programming-i"))):
    print(os.listdir("mooc-java-programming-i")[i])
    with open("path.txt", "a", encoding="utf-8") as f:
        f.write(os.listdir("mooc-java-programming-i")[i] + "\n")
