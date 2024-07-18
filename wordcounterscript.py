def wordcounter(): # word counter function - opens, reads, counts the words, closes the file
    file_path = input("Enter the file pathway: ")
    target_file = open(file_path, "r")
    file_content = target_file.read()
    words = file_content.split()
    word_count = len(words)
    print(f"There are {word_count} words in the file.")
    target_file.close()

try: # basic error handling - can't handle quotation marks yet as it will throw a traceback, but will work on this for v3
    wordcounter()
except ValueError:
    print("The file does not exist. Please enter the correct file pathway.")
    wordcounter()
