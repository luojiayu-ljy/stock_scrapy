import json
import tushare as ts  
import pandas as pd  
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

def parse(path):
    file = open(path,'r',encoding='utf-8')
    lines = len(file.readlines())
    print(lines)
    errorStock = 0
    file.seek(0)
    while 1:
        
        try:
            data = eval(file.readline())
            #print(type(data))
            #print(data)
            #print(type(data['Code']))
            stockData = ts.get_hist_data(data['code'])
            print(data['code'])
            print(stockData)
            
            if stockData is not None:
                #print(stockData)
             
                stockData.index = pd.to_datetime(stockData.index)
           
                #print(stockData.tail())
                plt.plot(stockData['close'],label=u'收盘价')
                plt.plot(stockData['ma5'],label=u'MA5')
                plt.plot(stockData['ma10'],label=u'MA10')
                plt.legend()
                plt.xlabel(u'日期')
                plt.ylabel(u'股价')
                plt.title(u'%s收盘价，MA5,MA10 K线图' % data['code'])
                

                stockData_Return = ((stockData['close']-stockData['close'].shift(1))/(stockData['close'].shift(1))).dropna()
                #print(stockData_Return)
                        
                #plt.plot(stockData_Return)

                print('%s的平均日收益率为：' % data['code'],stockData_Return.mean(),'\n%s的收益率标准差为：' % data['code'],stockData_Return.std())

                plt.show()
            else:
                errorStock += 1
                print(errorStock)

        except SyntaxError as syn:
            print(syn)
            break

        except Exception as ex:
            print(ex)
            break

    file.close()

if __name__ == '__main__':
    parse('stock.txt')
