with open("data.txt", "r") as file:
    content = file.read()
    print("file content")
    print(content)
    file.close()
