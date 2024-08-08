import tkinter as tk

def wordcounter(): # word counter function - opens, reads, counts the words, closes the file
    file_path = input("Enter the file pathway: ")
    target_file = open(file_path, "r")
    file_content = target_file.read()
    words = file_content.split()
    word_count = len(words)
    print(f"There are {word_count} words in the file.")
    target_file.close()

root = tk.Tk() #creates the main window (blank)
root.geometry('500x350') #sets the size of the main window
root.title("Word Counter") #adds a title to the main window
label = tk.Label(root, text="Enter the file path:") #creates a label that can have designated parameters and text
entry = tk.Entry(root, width=50) #creates an entry field to collect text from the user
word_count_button = tk.Button(root, text="Count Words",command=wordcounter) #creates a clickable button that can be customised
exit_button = tk.Button(root, text="Quit Program", command=root.destroy)

label.pack()
entry.pack()
word_count_button.pack()
exit_button.pack()

root.mainloop()