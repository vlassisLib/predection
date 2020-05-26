values = [{"t" : [ 1 , 2 , 3 , 4 , 5]},
          {"D(t)" : [100,80,110,115,105,110,125,120]},
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
    def cfeExponentialSmoothing(self):
        cfe_exponential_smoothing = classPrediction.Prediction(values)
        cfe_exponential_smoothing.exponentialSmoothing()
        leng = len(self.a_list[1]["D(t)"])
        cfe = 0

        for i in range(1,leng):
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
        mean = mse/leng_Ft
        print("The MSE error for Naive Prediction is: " , mean)







error = Errors(values)
error.cfeMovingAverage(3)



    
    

        
        

