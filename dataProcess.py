# main program 
from dataProcessClass import *
                
supported_extensions = ["csv", "json", "xls", "xlsx", "xlsm", "xlsb", "xltx", "xltm"]
while True:
   path = input("Enter the path of your dataset: ")
   extension = path.strip().split(".")[-1]
   if extension not in supported_extensions:
             print(ValueError(f"Unsupported file extension: {extension}. Only JSON, CSV, and Excel files are supported."))
             print("Again, ", end = "")
   else:
       break     
dtprocess = dataProcess(path)
print("=============== Samples of data ===============")
print(dtprocess.show_df())  
print("=============== Samples of info ===============")
print(dtprocess.info_df())
print("=============== Samples of General description ===============")
print("Shape = ", dtprocess.shape, "\nColumns are : \n", list(dtprocess.columns), end = "\n\n")
print(dtprocess.describe_df())
if dtprocess.num_missingValues().sum() !=0:
        print("============= Before ==================")
        print(dtprocess.num_missingValues())
        dtprocess.handle_missing()
        print("============= After ===================")
        print(dtprocess.num_missingValues())
else : 
        print("The data does not have missing values :) ") 
