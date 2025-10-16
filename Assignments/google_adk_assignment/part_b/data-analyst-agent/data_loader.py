import os
import pandas as pd
import numpy as np
import chardet
from typing import Union, Dict, Any

class DataLoader:
    """
    Advanced data loading class with robust error handling and encoding detection
    """
    @staticmethod
    def detect_encoding(file_path: str) -> str:
        """
        Detect file encoding using chardet
        
        Args:
            file_path (str): Path to the file
        
        Returns:
            str: Detected file encoding
        """
        try:
            with open(file_path, 'rb') as file:
                raw_data = file.read(10000)  # Read first 10000 bytes
                result = chardet.detect(raw_data)
                detected_encoding = result['encoding']
                confidence = result['confidence']
                
                print(f"🔍 Detected Encoding: {detected_encoding}")
                print(f"📊 Confidence: {confidence * 100:.2f}%")
                
                # Fallback to UTF-8 if confidence is low
                return detected_encoding if confidence > 0.5 else 'utf-8'
        except Exception as e:
            print(f"❌ Encoding detection error: {e}")
            return 'utf-8'  # Default fallback
    
    @staticmethod
    def load_data(file_path: str) -> pd.DataFrame:
        """
        Load data from various file formats with advanced error handling
        
        Args:
            file_path (str): Path to the data file
        
        Returns:
            pd.DataFrame: Loaded data
        
        Raises:
            ValueError: If file cannot be loaded
        """
        # Validate file existence
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"❌ File not found: {file_path}")
        
        # List of encodings to try
        encodings_to_try = [
            'utf-8', 
            'latin-1', 
            'iso-8859-1', 
            'cp1252', 
            'utf-16'
        ]
        
        # Detect file encoding first
        detected_encoding = DataLoader.detect_encoding(file_path)
        encodings_to_try.insert(0, detected_encoding)
        
        # Remove duplicates while preserving order
        encodings_to_try = list(dict.fromkeys(encodings_to_try))
        
        # Try different encodings
        for encoding in encodings_to_try:
            try:
                # Determine file type
                if file_path.endswith('.csv'):
                    df = pd.read_csv(
                        file_path, 
                        encoding=encoding, 
                        low_memory=False,  # Handle large files
                        on_bad_lines='skip'  # Skip problematic rows
                    )
                elif file_path.endswith('.xlsx'):
                    df = pd.read_excel(file_path, engine='openpyxl')
                elif file_path.endswith('.json'):
                    df = pd.read_json(file_path, encoding=encoding)
                else:
                    raise ValueError("Unsupported file format. Use CSV, XLSX, or JSON.")
                
                print(f"✅ Successfully loaded file with {encoding} encoding")
                return df
            
            except (UnicodeDecodeError, pd.errors.ParserError) as e:
                print(f"⚠️ Failed to load with {encoding} encoding. Error: {e}")
                continue
            except Exception as e:
                print(f"❌ Unexpected error: {e}")
                continue
        
        # If no encoding works
        raise ValueError(f"Could not read the file with any of these encodings: {encodings_to_try}")
    
    @staticmethod
    def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
        """
        Perform basic data preprocessing
        
        Args:
            df (pd.DataFrame): Input DataFrame
        
        Returns:
            pd.DataFrame: Preprocessed DataFrame
        """
        # Remove duplicate rows
        df = df.drop_duplicates()
        
        # Handle missing values
        # Numeric columns: fill with median
        # Categorical columns: fill with mode
        numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns
        categorical_cols = df.select_dtypes(include=['object']).columns
        
        for col in numeric_cols:
            df[col].fillna(df[col].median(), inplace=True)
        
        for col in categorical_cols:
            df[col].fillna(df[col].mode()[0], inplace=True)
        
        return df
    
    @staticmethod
    def get_data_summary(df: pd.DataFrame) -> Dict[str, Any]:
        """
        Generate a comprehensive summary of the DataFrame
        
        Args:
            df (pd.DataFrame): Input DataFrame
        
        Returns:
            Dict with data summary
        """
        summary = {
            'total_rows': len(df),
            'total_columns': len(df.columns),
            'column_types': df.dtypes.to_dict(),
            'missing_values': df.isnull().sum().to_dict(),
            'data_overview': {
                'numeric_columns': list(df.select_dtypes(include=[np.number]).columns),
                'categorical_columns': list(df.select_dtypes(include=['object']).columns),
                'datetime_columns': list(df.select_dtypes(include=['datetime64']).columns)
            }
        }
        
        return summary