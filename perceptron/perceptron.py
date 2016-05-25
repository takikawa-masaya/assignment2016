import sys

def read_instance(sent):
    wordList = sent.split()
    label = 0
    fvList = []
    
    for words in wordList:
        if not label:
            label = words
        else:
            fv = words.split(":")
            fvList.append(tuple(fv))

    return (label,fvList)

def read_data(afile):
    fr = open(afile)
    dataList = []
    max_index = 0

    for line in fr:
        instance = read_instance(line)
        dataList.append(instance)
    
        for fv in instance[1]:
            if max_index < int(fv[0]):
                max_index = int(fv[0])

    fr.close()
    return dataList,max_index

def add_fv(fvtmp):
    for fv in fvtmp:
        weight[fv[0]] += fv[1]

def sub_fv(fvtmp):
    for fv in fvtmp:
        weight[fv[0]] -= fv[1]

def mult_fv(fvtmp):
    dot = 0
    for fv in fvtmp:
        if(max_index < fv[0]):
            continue
        dot += weight[fv[0]] * fv[1]
    return dot

if __name__ == "__main__":
    train_data, max_index = read_data(sys.argv[1])
    weight = [0] * (max_index + 1)
    print(weight)
