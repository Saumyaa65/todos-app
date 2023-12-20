import zipfile
def extract_archive(path, des):
    with zipfile.ZipFile(path, 'r') as file:
        file.extractall(des)

if __name__=="__main__":
    extract_archive("D:\Python\Bonus\compressed.zip",
                    "E:\Saumya")