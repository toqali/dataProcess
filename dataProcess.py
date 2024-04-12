import pandas as pd

class dataProcess:
    def __init__(self, data_path):
        self.data_path = data_path
        self.result = None
        self.shape = self.read_file().shape
        self.columns = self.read_file().columns
        self.df = self.read_file()
    def get_extension(self):
        return self.data_path.split(".")[-1]

    def read_file(self):
        """
        Reads files with extensions: json, csv, or excel.
        """ 
        extension = self.get_extension()        
        try:
            if extension == "csv":
                df = pd.read_csv(self.data_path)
            elif extension == "json":
                df = pd.read_json(self.data_path)
            else:
                df = pd.read_excel(self.data_path)
            return df
        except Exception as e:
            raise ValueError(f"Error reading file: {str(e)}")
    def show_df(self, rows = 5):
            return self.read_file().head(rows)
    def describe_df(self) : 
        return  self.read_file().describe()
    def info_df(self) : 
        return self.read_file().info()
    def num_missingValues(self):
        return self.read_file().isna().sum()
    def handle_missing(self):
        for col in self.columns:
            if self.df[col].dtypes in ["int64", "float64"]:
                self.df[col].fillna(self.df[col].median(), inplace = True)
            if self.df[col].dtypes in ["object", "bool"]  :
               mode_value = self.df[col].mode()[0] 
               self.df[col].fillna(mode_value, inplace=True)
    def show_process_dfinfo(self):
        print("=============== Samples of data ===============")
        print(self.show_df())  
        print("=============== Samples of info ===============")
        print(self.info_df())
        print("=============== Samples of General description ===============")
        print("Shape = ", self.shape, "\nColumns are ", list(self.columns))
        print(self.describe_df)
        if self.num_missingValues().sum() !=0:
            print("============= Before ==================")
            print(self.num_missingValues())
            self.handle_missing()
            print("============= After ===================")
            print(self.num_missingValues())
        else : 
            print("The data does not have missing values :) ")    
        
        
    

