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
    def cfeCustomizedExponentialSmoothing(self,start):
        cfe_exponential_smoothing = classPrediction.Prediction(values)
        cfe_exponential_smoothing.customizedExponentialSmoothing(start)
        leng = len(self.a_list[1]["D(t)"])
        cfe = 0
        
        for i in range(start,leng):
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
            print(Ed)
        mean = mse/(leng_Ft-1)
        print("The MSE error for Naive Prediction is: " , mean)

    # MSE FOR MOVING AVERAGE
    def mseMovingAverage(self,k):
        mse_moving_average = classPrediction.Prediction(values)
        mse_moving_average.movingAverage(k)
        leng_Dt = len(self.a_list[1]["D(t)"])
        leng_Ft = len(self.a_list[2]["F(t)"])
        mse = 0
        for i in range(k,leng_Dt):
            Ed = (self.a_list[1]["D(t)"][i] - self.a_list[2]["F(t)"][i])**2
            print(Ed)
            mse = mse + Ed
        
        mean = mse / (leng_Ft-k)
        print("The MSE error for Moving Average is: " , mean)

    # MSE FOR STATIONARY MOBILE MEDIA
    def mseStationaryMobileMedia(self,k):
        mse_stationery_mobile_media = classPrediction.Prediction(values)
        mse_stationery_mobile_media.stationaryMobileMedia(k)
        leng_Dt = len(self.a_list[1]["D(t)"])
        leng_Ft = len(self.a_list[2]["F(t)"])
        mse = 0
        for i in range(k,leng_Dt):
            Ed = (self.a_list[1]["D(t)"][i] - self.a_list[2]["F(t)"][i])**2
            print(Ed)
            mse = mse + Ed
        
        
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
        mse_customized_exponential_smoothing = classPrediction.Prediction(values)
        mse_customized_exponential_smoothing.customizedExponentialSmoothing(start)
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
        print("The MSE error for Customized Exponential Smoothing is: ", mean)

    # MAD ERRORS

    # MAD FOR NAIVE PREDICTION
    def madNaivePrediction(self):
        mad_naive_prediction = classPrediction.Prediction(values)
        mad_naive_prediction.naivePrediction()
        leng_Dt = len(self.a_list[1]["D(t)"])
        leng_Ft = len(self.a_list[2]["F(t)"])
        mad = 0

        for i in range(1,leng_Dt):
            Ed = abs(self.a_list[1]["D(t)"][i] - self.a_list[2]["F(t)"][i])
            mad = mad + Ed
            print(Ed)
        
        mean = mad / (leng_Ft - 1)
        print("The MAD error for Naive Prediction is: ",mean)
    
    # MAD FOR MOVING AVERAGE 
    def madMovingAverage(self,k):
        mad_moving_Average = classPrediction.Prediction(values)
        mad_moving_Average.movingAverage(k)
        leng_Dt = len(self.a_list[1]["D(t)"])
        leng_Ft = len(self.a_list[2]["F(t)"])
        mad = 0

        for i in range(k,leng_Dt):
            Ed = abs(self.a_list[1]["D(t)"][i] - self.a_list[2]["F(t)"][i])
            print(Ed)
            mad = mad + Ed
        
        mean = mad / (leng_Ft-k)
        print("The MAD error for Moving Average is: " , mean)

    # MAD FOR STATIONARY MOBILE MEDIA
    def madStationaryMobileMedia(self,k):
        mad_stationary_mobile_media = classPrediction.Prediction(values)
        mad_stationary_mobile_media.stationaryMobileMedia(k)
        leng_Dt = len(self.a_list[1]["D(t)"])
        leng_Ft = len(self.a_list[2]["F(t)"])
        mad = 0
        
        for i in range(k,leng_Dt):
            Ed = abs(self.a_list[1]["D(t)"][i] - self.a_list[2]["F(t)"][i])
            print(Ed)
            mad = mad + Ed
        mean = mad / (leng_Ft-k)
        print("The MAD error for Stationary Mobile Media is: ",mean)

    # MAD FOR EXPONENTIAL SMOOTHING
    def madExponentialSmoothing(self,start):
        mad_exponential_smoothing = classPrediction.Prediction(values)
        mad_exponential_smoothing.exponentialSmoothing(start)
        leng_Dt = len(self.a_list[1]["D(t)"])
        leng_Ft = len(self.a_list[2]["F(t)"])
        mad = 0

        for i in range(start,leng_Dt):
            Ed = abs(self.a_list[1]["D(t)"][i] - self.a_list[2]["F(t)"][i])
            print(Ed)
            mad = mad + Ed
        mean = mad / (leng_Ft - start)
        print("The MAD error for Exponential Smoothing is: " , mean)
    # MAPE FOR NAIVE PREDICTION
    def mapeNaivePrediction(self):
        mape_naive_prediction = classPrediction.Prediction(values)
        mape_naive_prediction.naivePrediction()
        leng_Dt = len(self.a_list[1]["D(t)"])
        leng_Ft = len(self.a_list[2]["F(t)"])
        mape = 0

        for i in range(1,leng_Dt):
            Ed = (abs(self.a_list[1]["D(t)"][i] - self.a_list[2]["F(t)"][i]) / self.a_list[1]["D(t)"][i]) 
            print(Ed)
            mape = mape + Ed
        mean = mape / (leng_Ft - 1)
        print("The MAPE error for Naive Prediction is: {} % ".format(mean*100))

    # MAPE FOR MOVING AVERAGE
    def mapeMovingAverage(self,k):
        mape_moving_average = classPrediction.Prediction(values)
        mape_moving_average.movingAverage(k)
        leng_Dt = len(self.a_list[1]["D(t)"])
        leng_Ft = len(self.a_list[2]["F(t)"])
        mape = 0

        for i  in range(k,leng_Dt):
            Ed = (abs(self.a_list[1]["D(t)"][i] - self.a_list[2]["F(t)"][i]) / self.a_list[1]["D(t)"][i]) 
            print(Ed)
            mape = mape + Ed
        mean = mape / (leng_Ft - k)
        print("The MAPE error for Moving Average is {} %".format(mean*100))

    # MAPE FOR STATIONARY MOBILE MEDIA 
    def mapeStationaryMobileMedia(self,k):
        mape_stationary_mobile_media = classPrediction.Prediction(values)
        mape_stationary_mobile_media.stationaryMobileMedia(k)
        leng_Dt = len(self.a_list[1]["D(t)"])
        leng_Ft = len(self.a_list[2]["F(t)"])
        mape = 0

        for i  in range(k,leng_Dt):
            Ed = (abs(self.a_list[1]["D(t)"][i] - self.a_list[2]["F(t)"][i]) / self.a_list[1]["D(t)"][i])
            print(Ed)
            mape = mape + Ed
        mean = mape / (leng_Ft - k)
        print("The MAPE error for Stationary Mobile Media is {} %".format(mean*100))

    # MAPE FOR EXPONENTIAL SMOOTHING
    def mapeExponentialSmoothing(self,start):
        mape_exponential_smoothing = classPrediction.Prediction(values)
        mape_exponential_smoothing.exponentialSmoothing(start)
        leng_Dt = len(self.a_list[1]["D(t)"])
        leng_Ft = len(self.a_list[2]["F(t)"])
        mape = 0

        for i in range(start,leng_Dt):
            Ed = (abs(self.a_list[1]["D(t)"][i] - self.a_list[2]["F(t)"][i]) / self.a_list[1]["D(t)"][i])
            print(Ed)
            mape = mape + Ed 
        mean = mape / (leng_Ft - start)
        print("The MAPE error for Exponential Smoothing is {} %".format(mean*100))
    
    # MAPE FOR CUSTOMIZED EXPONENTIAL SMOOTHING 
    def mapeCustomizedExponentialSmoothing(self,start):
        mape_customized_exponential_smoothing = classPrediction.Prediction(values)
        mape_customized_exponential_smoothing.customizedExponentialSmoothing(start)
        leng_Dt = len(self.a_list[1]["D(t)"])
        leng_Ft = len(self.a_list[2]["F(t)"])
        mape = 0

        for i in range(start,leng_Dt):
            Ed = (abs(self.a_list[1]["D(t)"][i] - self.a_list[2]["F(t)"][i]) / self.a_list[1]["D(t)"][i])
            print(Ed)
            mape = mape + Ed 
        mean = mape / (leng_Ft - start)
        print("The MAPE error for Exponential Smoothing is {} %".format(mean*100))

                   





error = Errors(values)
error.cfeCustomizedExponentialSmoothing(2)



    
    

        
        

