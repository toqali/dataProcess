import pandas as pd

class dataProcess:
    def __init__(self, data_path):
        # Initialize the dataProcess object with the provided data_path
        self.data_path = data_path
        self.result = None
        
        # Read the file and store it in self.df
        self.df = self.read_file()
        
        # Get the shape and column names of the DataFrame
        self.shape = self.df.shape
        self.columns = self.df.columns
        
    def get_extension(self):
        # Extract the file extension from the data_path
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
            # Raise an error if there is an issue reading the file
            raise ValueError(f"Error reading file: {str(e)}")
            
    def show_df(self, rows=5):
        # Display the first 'rows' rows of the DataFrame
        return self.df.head(rows)
    
    def describe_df(self):
        # Generate descriptive statistics of the DataFrame
        return self.df.describe()
    
    def info_df(self):
        # Display information about the DataFrame
        return self.df.info()
    
    def num_missingValues(self):
        # Count the number of missing values in each column
        return self.df.isna().sum()
    
    def handle_missing(self):
        # Handle missing values in the DataFrame
        
        # Get the columns with missing values
        missing_cols = self.df.columns[self.df.isnull().any()].tolist()
        
        # Fill missing values based on data type of each column
        for col in missing_cols:
            if self.df[col].dtype in ["int64", "float64"]:
                # For numerical columns, fill with median
                self.df[col] = self.df[col].fillna(self.df[col].median())
            elif self.df[col].dtype in ["object", "bool"]:
                # For categorical columns, fill with mode
                mode_value = self.df[col].mode()[0] 
                self.df[col] = self.df[col].fillna(mode_value)
