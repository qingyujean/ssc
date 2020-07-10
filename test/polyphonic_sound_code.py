from pypinyin import pinyin, load_phrases_dict
import pypinyin
from pyhanlp import HanLP
import os, sys

src_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "../src"))
sys.path.append(f'{src_path}')

from soundshapecode import ssc
from soundshapecode.variant_kmp import VatiantKMP


SIMILARITY_THRESHOLD = 0.8
SSC_ENCODE_WAY = 'SOUND'#'ALL','SOUND','SHAPE'

load_phrases_dict({'沌口': [['zhuàn'], ['kǒu']]})


if __name__=="__main__":
    analyzer = HanLP.newSegment('perceptron')

    chi_word1 = '沌口'
    chi_word2 = '我住在钻口'
    ssc.getHanziStrokesDict()
    ssc.getHanziStructureDict()
    
    chi_word1_ssc = ssc.getSSC_sentence(chi_word1, SSC_ENCODE_WAY, analyzer)
    print(chi_word1_ssc)
    
    chi_word2_ssc = ssc.getSSC_sentence(chi_word2, SSC_ENCODE_WAY, analyzer)
    print(chi_word2_ssc)
    
    #应用串的模式匹配KMP算法，找变异词。效率比BF算法高
    kmp = VatiantKMP(SIMILARITY_THRESHOLD)
    kmp.indexKMP(chi_word2_ssc, chi_word1_ssc, SSC_ENCODE_WAY)#主串S、模式串T
    print(kmp.startIdxRes)
    
    if kmp.startIdxRes:
        variabt_word = set()
        for i in kmp.startIdxRes:
            variabt_word.add(chi_word2[i:i+len(chi_word1)])
        print('变异词：', variabt_word)
    else:
        print('变异词没有找到')
