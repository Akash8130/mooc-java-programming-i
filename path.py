import os

out = "path.txt"
for i in range(1, len(os.listdir("mooc-java-programming-i"))):
    with open("path.txt", "a", encoding="utf-8") as f:
        f.write(os.listdir("mooc-java-programming-i")[i] + "\n")
