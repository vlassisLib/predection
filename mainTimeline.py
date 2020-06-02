values = [{"t" : [ 1 , 2 , 3]},
          {"D(t)" : [43,10,21,23,28,16,43]},
          {"F(t)":[]}]

mapped = zip(values[0]["t"],values[1]["D(t)"])
mapped = set(mapped)
print(mapped)