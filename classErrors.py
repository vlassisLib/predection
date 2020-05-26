values = [{"t" : [ 1 , 2 , 3 , 4 , 5]},
          {"D(t)" : [100.0,80.0,110.0,115.0,105.0,110.0,125.00,120.0]},
          {"F(t)":[]},
          {"f(t)":[]},
          {"T(t)":[]}
          ]
import classPrediction


class Errors:  
    def __init__(self,a_list):
        self.a_list = a_list                                        

    # CFE ERRORS
      
    # CFE FOR NAIVE PREDECTION 
    def cfeNaivePrediction(self):
        
        cfe_naive_prediction = classPrediction.Prediction(values)
        cfe_naive_prediction.naivePrediction()
        leng = len(self.a_list[1]["D(t)"])
        cfe = 0
        
        for i in range(1,leng):
            Ed = self.a_list[1]["D(t)"][i] - self.a_list[2]["F(t)"][i]
            cfe = cfe + Ed
            print(Ed)
        print("The CFE for Naive Prediction is: " , cfe)

    # CFE FOR MOVING AVERAGE
    def cfeMovingAverage(self,k):

        cfe_moving_average = classPrediction.Prediction(values)
        leng = len(self.a_list[1]["D(t)"])
        cfe = 0
        
        for i in range(cfe_moving_average.movingAverage(k),leng):
            Ed = self.a_list[1]["D(t)"][i] - self.a_list[2]["F(t)"][i]
            cfe = cfe + Ed
            print(Ed)
        print("The CFE  for Moving Average is: ",cfe)

    # CFE FOR STATIONARY MOBILE MEDIA
    def cfeStationaryMobileMedia(self,k):

        cfe_stationary_mobile_media = classPrediction.Prediction(values)
        leng = len(self.a_list[1]["D(t)"])
        cfe = 0

        for i in range(cfe_stationary_mobile_media.stationaryMobileMedia(k),leng):
            Ed = self.a_list[1]["D(t)"][i] - self.a_list[2]["F(t)"][i]
            cfe = cfe + Ed
            print(Ed)
        print("The CFE  for Stationary Mobile Media is: ",cfe)

    # CFE FOR EXPONENTIAL SMOOTHING
    def cfeExponentialSmoothing(self,start):
        cfe_exponential_smoothing = classPrediction.Prediction(values)
        cfe_exponential_smoothing.exponentialSmoothing(start)
        leng = len(self.a_list[1]["D(t)"])
        cfe = 0

        for i in range(start,leng):
            Ed = self.a_list[1]["D(t)"][i] - self.a_list[2]["F(t)"][i]
            cfe = cfe + Ed
            print(Ed) 
        print("The CFE for Exponential Smoothing is: " , cfe)

    # CFE FOR CUSTOMIZED EXPONENTIAL SMOOTHING 
    def cfeCustomizedExponentialSmoothing(self):
        cfe_exponential_smoothing = classPrediction.Prediction(values)
        cfe_exponential_smoothing.customizedExponentialSmoothing()
        leng = len(self.a_list[1]["D(t)"])
        cfe = 0
        
        for i in range(1,leng):
            Ed = self.a_list[1]["D(t)"][i] - self.a_list[2]["F(t)"][i]
            cfe = cfe + Ed
            print(Ed) 
        print("The CFE for Customized Exponential Smoothing is: ", cfe)

    # MSE ERRORS

    # MSE FOR NAIVE PREDICTION
    def mseNaivePrediction(self):
        mse_naive_prediction = classPrediction.Prediction(values)
        mse_naive_prediction.naivePrediction()
        leng_Dt = len(self.a_list[1]["D(t)"])
        leng_Ft = len(self.a_list[2]["F(t)"])
        mse = 0
        for i in range(1,leng_Dt):
            Ed = (self.a_list[1]["D(t)"][i] - self.a_list[2]["F(t)"][i])**2
            mse = mse + Ed
            print(mse)
        mean = mse/(leng_Ft-1)
        print("The MSE error for Naive Prediction is: " , mean)

    # MSE FOR MOVING AVERAGE
    def mseMovingAverage(self,k):
        mse_moving_average = classPrediction.Prediction(values)
        leng_Dt = len(self.a_list[1]["D(t)"])
        mse = 0
        for i in range(mse_moving_average.movingAverage(k),leng_Dt):
            Ed = (self.a_list[1]["D(t)"][i] - self.a_list[2]["F(t)"][i])**2
            print(Ed)
            mse = mse + Ed
        print(mse)
        leng_Ft = len(self.a_list[2]["F(t)"])
        mean = mse / (leng_Ft-k)
        print("The MSE error for Moving Average is: " , mean)

    # MSE FOR STATIONARY MOBILE MEDIA
    def mseStationaryMobileMedia(self,k):
        mse_stationery_mobile_media = classPrediction.Prediction(values)
        leng_Dt = len(self.a_list[1]["D(t)"])
        mse = 0
        for i in range(mse_stationery_mobile_media.stationaryMobileMedia(k),leng_Dt):
            Ed = (self.a_list[1]["D(t)"][i] - self.a_list[2]["F(t)"][i])**2
            print(Ed)
            mse = mse + Ed
        print(mse)
        leng_Ft = len(self.a_list[2]["F(t)"])
        mean = mse /(leng_Ft-k)
        print("The MSE error for Stationary Mobile Media is: ", mean)

    # MSE FOR EXPONENTIAL SMOOTHING
    def mseExponentionalSmoothing(self,start):
        mse_exponential_smoothing = classPrediction.Prediction(values)
        mse_exponential_smoothing.exponentialSmoothing(start)
        leng_Dt = len(self.a_list[1]["D(t)"])
        leng_Ft = len(self.a_list[2]["F(t)"])
        mse = 0
        print(self.a_list[1]["D(t)"])
        print(self.a_list[2]["F(t)"])
        
        for i in range(start,leng_Dt):
            Ed = (self.a_list[1]["D(t)"][i] - self.a_list[2]["F(t)"][i])**2
            print(Ed)
            mse = mse + Ed
        mean = mse / (leng_Ft-start)
        print("The MSE error for Exponential Smoothing is: ", mean)

    # MSE FOR CUSTOMIZED EXPONENTIAL SMOOTHING
    def mseCustomizedExponentialSmoothing(self,start):
        





error = Errors(values)
error.cfeExponentialSmoothing(2)



    
    

        
        

