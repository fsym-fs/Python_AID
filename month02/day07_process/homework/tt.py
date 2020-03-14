import os

n = os.path.getsize("dict.txt")
with open("dict.txt", "r", 1) as f:
    with open("tt.txt", "w") as f1:
        while True:
            data = f.read(1024)
            if data:
                if f.tell() <= n // 2:
                    f1.write(data)
            else:
                break