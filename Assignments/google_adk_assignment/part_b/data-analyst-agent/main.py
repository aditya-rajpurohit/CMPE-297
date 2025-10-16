import os
import argparse
from typing import Optional

from .data_loader import DataLoader
from .statistical_analyzer import StatisticalAnalyzer
from .report_generator import ReportGenerator

class DataAnalystAgent:
    """
    Orchestrates the entire data analysis workflow
    """
    def __init__(self, output_dir: Optional[str] = None):
        """
        Initialize the Data Analyst Agent
        
        Args:
            output_dir (str, optional): Directory to save analysis outputs
        """
        self.output_dir = output_dir or '.'
        os.makedirs(self.output_dir, exist_ok=True)
    
    def analyze(self, file_path: str, report_format: str = 'txt'):
        """
        Perform comprehensive data analysis
        
        Args:
            file_path (str): Path to data file
            report_format (str): Format of report ('txt' or 'json')
        
        Returns:
            str: Path to generated report
        """
        try:
            # 1. Load Data
            df = DataLoader.load_data(file_path)
            
            # 2. Preprocess Data
            df = DataLoader.preprocess_data(df)
            
            # 3. Get Data Summary
            data_summary = DataLoader.get_data_summary(df)
            
            # 4. Descriptive Statistics
            descriptive_stats = StatisticalAnalyzer.descriptive_statistics(df)
            
            # 5. Correlation Analysis
            correlations = StatisticalAnalyzer.correlation_analysis(
                df, 
                output_dir=self.output_dir
            )
            
            # 6. Outlier Detection
            outliers = StatisticalAnalyzer.detect_outliers(df)
            
            # 7. Generate Report
            if report_format.lower() == 'json':
                report_path = ReportGenerator.generate_json_report(
                    data_summary, 
                    descriptive_stats, 
                    correlations, 
                    outliers,
                    output_dir=self.output_dir
                )
            else:
                report_path = ReportGenerator.generate_text_report(
                    data_summary, 
                    descriptive_stats, 
                    correlations, 
                    outliers,
                    output_dir=self.output_dir
                )
            
            print(f"✅ Analysis complete. Report saved at: {report_path}")
            print(f"✅ Correlation matrix visualization saved at: {self.output_dir}/correlation_matrix.png")
            
            return report_path
        
        except Exception as e:
            print(f"❌ Analysis failed: {e}")
            raise

def main():
    # Setup argument parser
    parser = argparse.ArgumentParser(description="AI-Powered Data Analyst Agent")
    parser.add_argument('file', help='Path to data file (CSV, XLSX, JSON)')
    parser.add_argument(
        '--report-format', 
        choices=['txt', 'json'], 
        default='txt', 
        help='Format of the analysis report'
    )
    parser.add_argument(
        '--output-dir', 
        default='.', 
        help='Directory to save analysis outputs'
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # Initialize and run agent
    agent = DataAnalystAgent(output_dir=args.output_dir)
    agent.analyze(args.file, report_format=args.report_format)

if __name__ == "__main__":
    main()