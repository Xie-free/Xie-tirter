import os
with open(r"C:\Users\Administrator\Pictures\Screenshots\ars.png", "rb") as r_stream:
    date = r_stream.read()
    file = r_stream.name
    print(file)
    file_name = file[file.rfind("\\") + 1]
    path = os.path.dirname(__file__)
    file_name = os.path.join(path, file_name)
    with open(file_name, "wb") as w_stream:
        w_stream.write(date)
