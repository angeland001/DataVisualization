#Create dictionary of data
ExampleData = { "India" :
              [8880,8670,8147,7338,5704],
              "China" :
              [5123, 6682, 3308, 1863, 1527]
             }

import pandas as pd
 
 #Make a data frame using pandas
DFofCountries = pd.DataFrame(Dictionary)

#assign indexes to dataframe
DfofCountries.index([1980,1981,1982,1983,1984])

#Print off Dataframe
print(DFofCountries)

#To Plot it with line chart use
DfofCountries.plot(kind="line")

#To Plot it with histogram tied a specific country.
DfofCountries["India"].plot(kind="hist")
