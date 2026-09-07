class FileExtensionAnalyzer:
    def __init__(self, files):
        self.files = files

    def get_extension_count(self):
        extension_count = {}
        for file in self.files:
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

analyzer = FileExtensionAnalyzer(files)
print(analyzer.get_extension_count())