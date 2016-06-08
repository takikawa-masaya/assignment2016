import sys
import math
import random

def read_instance(sent):
    wordList = sent.split()
    label = 0
    fvList = []
    ltwo = 0
    
    for words in wordList:
        if not label:
            label = int(words)
        else:
            fv = words.split(":")
            fv = list(map(int,fv))
            ltwo += fv[1]*fv[1]
            fvList.append(fv)

    NormfvList = []
    for fvl in fvList:
        NormfvList.append((fvl[0],fvl[1]/math.sqrt(ltwo)))

    NormfvList.append((0,1))
    return (label, NormfvList)

def read_data(afile):
    dataList = []
    max_index = 0

    for line in open(afile):
        instance = read_instance(line)
        dataList.append(instance)
    
        for fv in instance[1]:
            if max_index < fv[0]:
                max_index = fv[0]

    return dataList,max_index

def add_fv(fvtmp):
    for fv in fvtmp:
        weight[fv[0]] += fv[1]
        global nupdates
        tmp_weight[fv[0]] += nupdates*fv[1]

def sub_fv(fvtmp):
    for fv in fvtmp:
        weight[fv[0]] -= fv[1]
        global nupdates
        tmp_weight[fv[0]] -= nupdates*fv[1]

def mult_fv(fvtmp):
    dot = 0
    for fv in fvtmp:
        if(max_index < fv[0]):
            continue
        dot += weight[fv[0]] * fv[1]
    return dot

def update_weight(train_data):
    random.shuffle(train_data)
    for instance in train_data:
        dot = mult_fv(instance[1])
        if dot*instance[0] <= 0 or math.fabs(dot) < 0.1:
            global nupdates
            nupdates += 1
            if instance[0] > 0:
                add_fv(instance[1])
            else:
                sub_fv(instance[1])

def averaged_weight():
    global nupdates

    ave_weight = [x - y/(nupdates+1) for (x, y) in zip(weight, tmp_weight)]
    return ave_weight

def mult_ave(fvtmp,ave_weight):
    dot = 0
    for fv in fvtmp:
        if(max_index < fv[0]):
            continue
        dot += ave_weight[fv[0]] * fv[1]
    return dot

def evaluate(test_data):
    count = 0
    for instance in test_data:
        if mult_ave(instance[1],averaged_weight())*instance[0] > 0:
            count += 1

    return count, len(test_data), count/len(test_data)

if __name__ == "__main__":
    train_data, max_index = read_data(sys.argv[1])
    weight = [0] * (max_index + 1)
    tmp_weight = [0] * (max_index + 1)
    nupdates = 0
    test_data, test_index = read_data(sys.argv[2])

    random.seed(0)

    for i in range(100):
        update_weight(train_data)

    print(evaluate(test_data))        
