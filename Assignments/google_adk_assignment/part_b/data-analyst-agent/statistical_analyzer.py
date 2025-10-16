import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from typing import List, Dict, Any

class StatisticalAnalyzer:
    """
    Performs in-depth statistical analysis on data
    """
    @staticmethod
    def descriptive_statistics(df: pd.DataFrame) -> Dict[str, Any]:
        """
        Generate comprehensive descriptive statistics
        
        Args:
            df (pd.DataFrame): Input DataFrame
        
        Returns:
            Dict with descriptive statistics
        """
        # Select numeric columns
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        
        # Compute descriptive stats
        stats = {}
        for col in numeric_cols:
            stats[col] = {
                'mean': df[col].mean(),
                'median': df[col].median(),
                'std_dev': df[col].std(),
                'min': df[col].min(),
                'max': df[col].max(),
                '25th_percentile': df[col].quantile(0.25),
                '75th_percentile': df[col].quantile(0.75)
            }
        
        return stats
    
    @staticmethod
    def correlation_analysis(df: pd.DataFrame, output_dir: str = '.') -> Dict[str, Any]:
        """
        Perform correlation analysis and create visualization
        
        Args:
            df (pd.DataFrame): Input DataFrame
            output_dir (str): Directory to save correlation matrix plot
        
        Returns:
            Dict with correlation insights
        """
        # Select numeric columns
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        correlation_matrix = df[numeric_cols].corr()
        
        # Visualization
        plt.figure(figsize=(12, 10))
        sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', 
                    linewidths=0.5, fmt=".2f", square=True)
        plt.title('Correlation Matrix of Numeric Features')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/correlation_matrix.png')
        plt.close()
        
        # Find top correlations
        top_correlations = {}
        for col in correlation_matrix.columns:
            # Sort correlations, exclude self-correlation
            correlations = correlation_matrix[col].drop(col)
            top_pos = correlations[correlations > 0.5].nlargest(3)
            top_neg = correlations[correlations < -0.5].nsmallest(3)
            
            top_correlations[col] = {
                'positive_correlations': dict(top_pos),
                'negative_correlations': dict(top_neg)
            }
        
        return top_correlations
    
    @staticmethod
    def detect_outliers(df: pd.DataFrame) -> Dict[str, List[Any]]:
        """
        Detect outliers using Interquartile Range (IQR) method
        
        Args:
            df (pd.DataFrame): Input DataFrame
        
        Returns:
            Dict with outliers for each numeric column
        """
        numeric_cols = df.select_dtypes(include=[np.number]).columns
        outliers = {}
        
        for col in numeric_cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            
            # Define outlier bounds
            lower_bound = Q1 - 1.5 * IQR
            upper_bound = Q3 + 1.5 * IQR
            
            # Find outliers
            column_outliers = df[(df[col] < lower_bound) | (df[col] > upper_bound)][col].tolist()
            
            outliers[col] = {
                'outliers': column_outliers,
                'count': len(column_outliers),
                'percentage': len(column_outliers) / len(df) * 100,
                'lower_bound': lower_bound,
                'upper_bound': upper_bound
            }
        
        return outliers