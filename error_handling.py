try:
    with open("file.txt","r") as f:
        content = f.read()
        print(content)
except FileNotFoundError:
    print("File not Found")
finally:
    print("closing file if opened")
    f.close() if 'file' in locals() else None