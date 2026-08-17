# ============== READING AND WRITING FILES ==============

def main():
    with open('alice.txt', 'r') as f:
        contents = f.readlines() # to read lines in a file .txt

    chapter1 = contents[52:272]
    with open('chapter1,txt', 'w') as f:
        f.writelines(chapter1) # to write lines in a file .txt

main()