import pickle
import pkg_resources

class FourCornerMethod(object):
    def __init__(self):
        data_file = pkg_resources.resource_filename(__name__, "data/data.pkl")
        with open(data_file, 'rb') as f:
            self.data = pickle.load(f)
    
    def query(self, input_char, default=None):
        return self.data.get(input_char, default)
    
if __name__ == "__main__":
    """
    i参考:
    1. 四角号码为什么是5位数字编码：https://zhidao.baidu.com/question/1667714057688997667.html
    """
    fcm = FourCornerMethod()
    #result = fcm.query('日')#量、日；门、闫、闩

    #print(result)
    print(fcm.query('量'))
    print(fcm.query('日'))
    
    print(fcm.query('门'))
    print(fcm.query('闫'))
    print(fcm.query('闩'))
    
    print(fcm.query('王'))