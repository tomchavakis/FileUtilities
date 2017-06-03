import os
import magic
import sys
import argparse

# total number of args
total = len(sys.argv)

# argument list
cmdargs = str(sys.argv)

print(total)
print(cmdargs)

parser = argparse.ArgumentParser(description='This script find all the objects with a specific data type.')
parser.add_argument('-i', '--input', help='Input file name', required=True)
parser.add_argument('-o', '--output', help='Output file name', required=True)
parser.add_argument('-t', '--type', help='type ex.png', required=True)
args = parser.parse_args()

## show values ##
print ("Input file: %s" % args.input)
print ("Output file: %s" % args.output)
print("Type is:%s" % args.type)

scanDirectory = str(args.input)
output = str(args.output)

fw = open(output, 'w')
m = magic.Magic(mime=True);
for root, dirs, files in os.walk(scanDirectory, topdown=False):
    for name in files:
        try:
            filepath = root + "/" + name
            filetype = m.from_file(filepath)
            print(filetype, name)
            inputType = str(args.type).upper()
            if inputType == 'TXT':
                if filetype.__contains__("text/plain"):
                    print(filepath)
                    fw.write(filepath + "\n")
            elif inputType == 'PNG' or inputType == 'JPG' or inputType == 'GIF' or inputType == 'TIFF':
                if inputType == 'PNG' and filetype == 'image/png':
                    print(filepath)
                    fw.write(filepath + "\n")
                elif inputType == 'JPG' or inputType == 'JPEG' and filetype == 'image/jpeg':
                    print(filepath)
                    fw.write(filepath + "\n")
        except Exception:
            pass
fw.close()
