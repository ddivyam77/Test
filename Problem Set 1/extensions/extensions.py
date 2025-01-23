x = input("File name: ").strip()

mime_types = {
    "png": "image/png",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "gif": "image/gif",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip"
}

file_extension = x.split(".")[-1].lower()

if file_extension in mime_types:
    print(mime_types[file_extension])
else:
    print('application/octet-stream')
