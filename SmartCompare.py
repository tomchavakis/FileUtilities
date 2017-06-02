import pickle

fp1 = 'Files/vss1.txt'
fp2 = 'Files/vssFinal.txt'

fp1 = open(fp1, 'r')
fp2 = open(fp2, 'r')

lines1 = fp1.read().splitlines()
lines2 = fp2.read().splitlines()

same = set(lines1).intersection(lines2)

different = set(lines1).difference(lines2)

different2 = set(lines2).difference(lines1)
different.update(different2)
identical = open("./same", 'w')
diff = open("./different", 'w')

pickle.dump(same, identical)
pickle.dump(different, diff)
diff.close()
