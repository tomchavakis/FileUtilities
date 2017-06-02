import os
import magic

scanDirectory = "./Files"

fw = open("./images", 'w')

for root, dirs, files in os.walk(scanDirectory, topdown=False):
    for name in files:
        try:
            filepath = root + "/" + name
            filetype = magic.from_file(filepath)
            if "PNG" in filetype:
                print(filepath)
                fw.write(filepath)
        except Exception:
            pass
fw.close()
