#coding=utf-8
'''
Created on 2019-4-8

@author: Yoga
'''
strokesDictReverse = {'1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10,
               'B':11, 'C':12, 'D':13, 'E':14, 'F':15, 'G':16, 'H':17, 'I':18, 'J':19, 'K':20,
               'L':21, 'M':22, 'N':23, 'O':24, 'P':25, 'Q':26, 'R':27, 'S':28, 'T':29, 'U':30,
               'V':31, 'W':32, 'X':33, 'Y':34, 'Z':35, '0':0}

soundWeight=0.5
shapeWeight=0.5
def computeSoundCodeSimilarity(soundCode1, soundCode2):#soundCode=['2', '8', '5', '2']
    featureSize=len(soundCode1)
    wights=[0.4,0.4,0.1,0.1]
    multiplier=[]
    for i in range(featureSize):
        if soundCode1[i]==soundCode2[i]:
            multiplier.append(1)
        else:
            multiplier.append(0)
    soundSimilarity=0
    for i in range(featureSize):
        soundSimilarity += wights[i]*multiplier[i]
    return soundSimilarity
    
def computeShapeCodeSimilarity(shapeCode1, shapeCode2):#shapeCode=['5', '6', '0', '1', '0', '3', '8']
    featureSize=len(shapeCode1)
    wights=[0.25,0.1,0.1,0.1,0.1,0.1,0.25]
    multiplier=[]
    for i in range(featureSize-1):
        if shapeCode1[i]==shapeCode2[i]:
            multiplier.append(1)
        else:
            multiplier.append(0)
    multiplier.append(1- abs(strokesDictReverse[shapeCode1[-1]]-strokesDictReverse[shapeCode2[-1]])*1.0 / max(strokesDictReverse[shapeCode1[-1]],strokesDictReverse[shapeCode2[-1]]) )
    shapeSimilarity=0
    for i in range(featureSize):
        shapeSimilarity += wights[i]*multiplier[i]
    return shapeSimilarity

def computeSSCSimilaruty(ssc1, ssc2, ssc_encode_way):
    #return 0.5*computeSoundCodeSimilarity(ssc1[:4], ssc2[:4])+0.5*computeShapeCodeSimilarity(ssc1[4:], ssc2[4:])
    if ssc_encode_way=="SOUND":
        return computeSoundCodeSimilarity(ssc1, ssc2)
    elif ssc_encode_way=="SHAPE":
        return computeShapeCodeSimilarity(ssc1, ssc2)
    else:
        soundSimi=computeSoundCodeSimilarity(ssc1[:4], ssc2[:4])
        shapeSimi=computeShapeCodeSimilarity(ssc1[4:], ssc2[4:])
        return soundWeight*soundSimi+shapeWeight*shapeSimi
