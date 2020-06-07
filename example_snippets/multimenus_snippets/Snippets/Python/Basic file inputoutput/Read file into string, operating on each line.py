file_contents = ""
with open("some/file.txt", "r") as file_handle:
    for line in file_handle.readlines():
        file_contents += line.replace("-", "_")