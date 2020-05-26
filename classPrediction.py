values = [{"t" : [ 1 , 2 , 3 , 4 , 5]},
          {"D(t)" : [100,80,110,115,105,110,125,120]},
          {"F(t)":[]},
          {"f(t)":[]},
          {"T(t)":[]}
          ]


class Prediction:
    def __init__(self,a_list):
        self.a_list = a_list
    
    def naivePrediction(self):
        self.a_list[2]["F(t)"].append(None)
        for i in range(len(self.a_list[1]["D(t)"][1::])):
            self.a_list[2]["F(t)"].append(self.a_list[1]["D(t)"][i])
        print(self.a_list[1]["D(t)"])
        print(self.a_list[2]["F(t)"])
    
    def movingAverage(self,k):
        
        for i in range(len(self.a_list[1]["D(t)"][0:k])):
            self.a_list[2]["F(t)"].append(None)
        for i in range(len(self.a_list[1]["D(t)"][k::])):
            diviation = sum(self.a_list[1]["D(t)"][i:(k+i)])/k
            self.a_list[2]["F(t)"].append("%.2f" %diviation)
        print(self.a_list[1]["D(t)"])
        print(self.a_list[2]["F(t)"])
        return k
    
    def stationaryMobileMedia(self,k):
        
        vectorList = []

        for i in range(k):
            vector_W = input("Enter your W: ")
            vectorList.append(vector_W)
        print(vectorList)
        for i in range(len(self.a_list[1]["D(t)"][0:k])):
            self.a_list[2]["F(t)"].append(None)
        
        sumOfVector = sum(vectorList[0::])
        
        if sumOfVector == 1.0:
            # this for is for how many appends i need to do
            for i in range(len(self.a_list[1]["D(t)"][k::])):
                
                sumMult = 0
                 # this for is for calculate the value of the F(t)
                for y in range(len(self.a_list[1]["D(t)"][i:k+i])):
                    mult = vectorList[y]*self.a_list[1]["D(t)"][y+i]
                    sumMult = sumMult + mult
                self.a_list[2]["F(t)"].append(sumMult)
            print(self.a_list[2]["F(t)"])
        return k

    def exponentialSmoothing(self):
        self.a_list[2]["F(t)"].append(None)
        self.a_list[2]["F(t)"].append(self.a_list[1]["D(t)"][0])
        
        a = input("Enter your a here: ")
        leng = len(self.a_list[1]["D(t)"])

        if a < 1 and a > 0:
            for i in range(2,leng):
                error = (self.a_list[1]["D(t)"][i-1] - self.a_list[2]["F(t)"][i-1])
                forecast = (self.a_list[2]["F(t)"][i-1] + a*(error))
                self.a_list[2]["F(t)"].append(forecast)
        print(self.a_list[2]["F(t)"])    
            
    def customizedExponentialSmoothing(self):
        self.a_list[2]["F(t)"].append(None)
        self.a_list[2]["F(t)"].append(self.a_list[1]["D(t)"][0])
        self.a_list[3]["f(t)"].append(None)
        self.a_list[3]["f(t)"].append(self.a_list[1]["D(t)"][0])
        self.a_list[4]["T(t)"].append(None)
        self.a_list[4]["T(t)"].append(0)
       
        a = input("Enter your a here: ")
        b = input("Enter your b here: ")
        leng = len(self.a_list[1]["D(t)"])

        if a < 1 and a > 0 and b < 1 and b > 0 :
            for i in range(2,leng):
                error = (self.a_list[1]["D(t)"][i-1] - self.a_list[2]["F(t)"][i-1])
                forecast = (self.a_list[2]["F(t)"][i-1] + a*(error))
                self.a_list[3]["f(t)"].append(forecast)
                trend = (self.a_list[4]["T(t)"][i-1] + b*(forecast - self.a_list[2]["F(t)"][i-1]))
                self.a_list[4]["T(t)"].append(trend)
                customizedExp = forecast + trend
                self.a_list[2]["F(t)"].append(customizedExp)
            print(self.a_list[2]["F(t)"])
            print(self.a_list[3]["f(t)"])
            print(self.a_list[4]["T(t)"])

                

values_prediction = Prediction(values)
values_prediction.movingAverage(3)








