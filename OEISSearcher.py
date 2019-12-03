terms = input("Enter your terms as comma-separated integers.")
error = input("How much error will you allow? Integer please.")

#For my purposes, and the code I'll write for now, error = 1.
error = 1

needToLookup = []

def recursiveSequenceGenerator(error, sequence, path, depthLeft, totalDepth):
    global needToLookup
    if(depthLeft == 0):
        for i in range(-1 * error, error + 1):
            needToLookup += [path + [sequence[totalDepth] + i]]
    else:
        for i in range(-1 * error, error + 1):
            path2 = path + [sequence[totalDepth - depthLeft] + i]
            recursiveSequenceGenerator(error, sequence, path2, depthLeft - 1, totalDepth)

def beginRecursion (error, sequence):
    length = len(sequence)
    recursiveSequenceGenerator(error, sequence, [], length - 1, length - 1)

beginRecursion(error, terms)

sequenceIds = []

import pyoeis
c = pyoeis.OEISClient()

for i in needToLookup:
    sequences = map(lambda a : a.id, c.lookup_by_terms(i))
    sequenceIds = list(set(sequenceIds + sequences))
    print(i)

toFormat = str(sequenceIds)
toFormat = toFormat.replace("[","").replace("]","").replace("u","").replace("\'","").replace(",","\n")

print("Your sequence IDs are: " + toFormat)
