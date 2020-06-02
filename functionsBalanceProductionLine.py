works_times = [ {"Works" : ["A","B","C","D","E","F","G","H","I","J","K"]},
                {"Times" : [50 , 16 , 14 , 55 , 20 , 17 , 17 , 17 , 17 , 13 , 14]},
                {"preWork" : [None , "A" , "B" , None , "D" , "C" , "C" , "E" , "E" , ["F","G","H","I"] , "J"]},
                {"timeType" : ["Minute"]}
                ]


# Making a method that sees the Work that doesnt have preWork and the greater time
# Making a method that finds the cycle time and production stations
class balanceProduction:
    
    def __init__(self,a_list):
        self.a_list = a_list

    def cycleTime(self):
        productionRythm = input("Enter the production that is needed: ")
        timeForProduction = input("Enter the time for the production: ")
        if productionRythm == 0 and timeForProduction == 0:
            cycleTime = max(works_times[1]["Times"])
        elif works_times[3]["timeType"][0] == "Minute":
            timeForProductionType = timeForProduction*60
            cycleTime = timeForProductionType/productionRythm
            print("{0:.2f}".format(cycleTime))

        # elif works_times[3]["timeType"] == "Second":


balance_production = balanceProduction(works_times)
balance_production.cycleTime()

