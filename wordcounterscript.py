print("Enter the file pathway: ")

try:
    file_path = input()
    target_file = open(file_path, "r")
    file_content = target_file.read()
    words = file_content.split()
    word_count = len(words)
    print(word_count)
    target_file.close()
except ValueError:
    print("The file does not exist. Please enter the correct file pathway.")
    file_path = input()
    target_file = open(file_path, "r")
    file_content = target_file.read()
    words = file_content.split()
    word_count = len(words)
    print(word_count)
    target_file.close()
