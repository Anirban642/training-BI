def get_extension_count(files):
    extension_count = {}
    for file in files:
        if "." not in file:
            continue
        extension = file.split(".")[-1]
        if extension in extension_count:
            extension_count[extension] += 1
        else:
            extension_count[extension] = 1
    return extension_count

files = [
    "resume.pdf",
    "photo.jpg",
    "report.pdf",
    "data.csv",
    "image.png",
    "notes.txt",
    "file",
    "README",
    "archive.tar.gz"
]

print(get_extension_count(files))