from soundshapecode.ssc_similarity.compute_ssc_similarity import computeSSCSimilaruty
class VatiantKMP(object):
    #求模式串T的next函数（修正方法）值并存入next数组
    #nextVal = [-1]
    #startIdxRes = []#写在这里，多次使用kmp时startIdxRes不会被清空而是存放了上一次的数据，影响结果
    def __init__(self, threshold):
        self.threshold = threshold
        self.nextVal = [-1]
        self.startIdxRes = []
        
    def reset(self):   
        self.nextVal = [-1]
        self.startIdxRes = []
        
    def indexKMP(self, haystack, needle, ssc_encode_way):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        """
        try:
            return haystack.index(needle)
        except:
            return -1
        """
        #子串定位，即模式匹配，可采用BF算法  也可采用KMP算法，我采用KMP算法
        # 0<=pos<= len(strS) - len(strT)) + 1
        self.getNextVal(needle, ssc_encode_way)
        i = 0
        while i< len(haystack):
            j = 0
            while i< len(haystack) and j < len(needle):
                #if j == -1 or haystack[i] == needle[j]:
                if j == -1 or computeSSCSimilaruty(haystack[i], needle[j], ssc_encode_way)>self.threshold:
                    i += 1
                    j += 1
                else:
                    j = self.nextVal[j]
            if j == len(needle):
                self.startIdxRes.append(i - len(needle))

        
            
    def getNextVal(self, strT, ssc_encode_way):
        i = 0
        j = -1
        while i < len(strT) - 1:
            #if j == -1 or strT[i] == strT[j]:
            if j == -1 or computeSSCSimilaruty(strT[i], strT[j], ssc_encode_way)>self.threshold:
                i += 1
                j += 1
                #if i < len(strT) and strT[i] == strT[j]:
                if i < len(strT) and computeSSCSimilaruty(strT[i], strT[j], ssc_encode_way)>self.threshold:
                    self.nextVal.append(self.nextVal[j])
                else:
                    self.nextVal.append(j)
            else:
                j = self.nextVal[j]
                
if __name__=="__main__":    
    """      
    strS = "mississippissipssissips"
    strT = "issip"
    tmp = VatiantKMP()
    tmp.indexKMP(strS, strT)
    print(tmp.startIdxRes)
    #print strStr(strS, strT)
    """
    chi_word1 = '紫琅路'
    chi_word2 = '国我爱你女生于无娃哇紫狼路爽晕约紫薇路又刘页列而紫粮路掩连哟罗'
    s = ['28525601038', '2J530235507', '7004220407A', '47031272927', '67030404003', 'GG010251005', '6I020104003', '5J022104124', '1J521444149', '1J501640149', '4E03222903C', 'F702143232A', '5704167164D', 'FG53C40804B', 'JI01260504A', 'DI011271206', '4E03222903C', '7J51244248G', '5704167164D', 'BI040774002', 'B7021024006', 'CI040108026', 'C7041122006', 'E0022102276', '4E03222903C', 'F742193932D', '5704167164D', 'FI43154016B', 'F742B343057', '2I411670209', '27522602078']
    t = ['4E03222903C', 'F702113132B', '5704167164D']
    tmp = VatiantKMP(0.8)
    tmp.indexKMP(s, t, "ALL")
    print(tmp.startIdxRes)