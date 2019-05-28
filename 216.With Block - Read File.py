# 216.With Block - Read File.py

# f.read
# f.close

# with block
# context manager


with open(r"F:\Ustaad\audio files\video files\document files\textfile.txt") as f:
    data = f.read()
    print(data)

print(f.closed)