import base64
import os
import binascii
import re
import magic

# If optional argument topdown is True or not specified, directories are scanned from top-down.
# If topdown is set to False, directories are scanned from bottom-up.

# directory
scanDirectory = "."

fw = open("./export", 'w')

# flag {gjgnvnbvnbvbnbvbnvbnvbnvbnvbnvnb}

def isBase64Regex(s):
    return (len(s) % 4 == 0) and re.match('^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=)?$', s)


def isbase64(x):
    result = True
    try:
        base64.decodestring(x)
    except binascii.Error:
        result = False
    return result


def is_ascii(s):
    return all(ord(c) < 128 for c in s)


def includes_curlibraces(s):
    return re.match('^\{.*.\}$', s)


def containsflag(s, baseFolder):
    try:
        result = base64.b64decode(s)
        if is_ascii(result) or includes_curlibraces(result):
            if len(result) > 0:
                print(result + "," + baseFolder)
                fw.write(result + "," + baseFolder + "\n")
    except binascii.Error:
        print("Error")


for root, dirs, files in os.walk(scanDirectory, topdown=False):
    for name in files:

        filepath = root + "/" + name
        try:
            filetype = magic.from_file(filepath)
        # print(filepath + "," + filetype)

            if filetype == "empty" and filetype.__contains__("ASCII") or filetype.__contains__("UTF-8"):
                fp = open(filepath, 'r')
                for line in fp:
                    if isbase64(line):
                        containsflag(line, filepath)
        except Exception:
            pass


                    # if isbase64(root):
                    #     slashArray = root.split("/")
                    #     for item in slashArray:
                    #         if isBase64Regex(item) and len(item) > 0:
                    #             containsflag(item, root)
                    # print(name)
                    # if isBase64Regex(name):
                    #     containsflag(name, root)

# fp = open("Files/DiffIEUser.txt", "r")
# fp = open("abc.txt", "r")

# for line in fp:
#     nl = line.split(":")
#     nameAll = nl[1:]
#     name = ((nameAll[0].split("."))[0])
#     #print nameAll
#     try:
#         decName = base64.decodestring(name)
#         print decName
#         #if "ag" in decName:
#             #print name + "  - - - - >  " + decName
#     except :
#         pass
# fp.close()
#     #print (name)