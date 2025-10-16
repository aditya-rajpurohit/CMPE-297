import os
import json
from typing import Dict, Any
from datetime import datetime

class ReportGenerator:
    """
    Generates comprehensive analysis reports
    """
    @staticmethod
    def generate_text_report(
        data_summary: Dict[str, Any], 
        descriptive_stats: Dict[str, Any], 
        correlations: Dict[str, Any], 
        outliers: Dict[str, Any],
        output_dir: str = '.'
    ) -> str:
        """
        Generate a comprehensive text report
        
        Args:
            data_summary (Dict): Summary of data
            descriptive_stats (Dict): Descriptive statistics
            correlations (Dict): Correlation analysis
            outliers (Dict): Outlier detection results
            output_dir (str): Directory to save report
        
        Returns:
            str: Path to generated report
        """
        # Create timestamp for unique report name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = os.path.join(output_dir, f'data_analysis_report_{timestamp}.txt')
        
        with open(report_path, 'w') as f:
            # Report Header
            f.write("🔬 Comprehensive Data Analysis Report\n")
            f.write("=" * 50 + "\n\n")
            f.write(f"Report Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            
            # Data Summary
            f.write("📊 DATA SUMMARY\n")
            f.write("-" * 20 + "\n")
            f.write(f"Total Rows: {data_summary['total_rows']}\n")
            f.write(f"Total Columns: {data_summary['total_columns']}\n")
            f.write("\nColumn Types:\n")
            for col, dtype in data_summary['column_types'].items():
                f.write(f"  {col}: {dtype}\n")
            
            f.write("\n🕳️ MISSING VALUES\n")
            f.write("-" * 20 + "\n")
            for col, missing in data_summary['missing_values'].items():
                f.write(f"  {col}: {missing}\n")
            
            # Descriptive Statistics
            f.write("\n📈 DESCRIPTIVE STATISTICS\n")
            f.write("-" * 25 + "\n")
            for col, stats in descriptive_stats.items():
                f.write(f"{col}:\n")
                for stat_name, value in stats.items():
                    f.write(f"  {stat_name.replace('_', ' ').title()}: {value:.4f}\n")
            
            # Correlation Analysis
            f.write("\n🔗 CORRELATION INSIGHTS\n")
            f.write("-" * 22 + "\n")
            for col, corr_data in correlations.items():
                f.write(f"{col}:\n")
                f.write("  Positive Correlations:\n")
                for corr_col, corr_value in corr_data['positive_correlations'].items():
                    f.write(f"    {corr_col}: {corr_value:.4f}\n")
                
                f.write("  Negative Correlations:\n")
                for corr_col, corr_value in corr_data['negative_correlations'].items():
                    f.write(f"    {corr_col}: {corr_value:.4f}\n")
            
            # Outlier Analysis
            f.write("\n⚠️ OUTLIER ANALYSIS\n")
            f.write("-" * 20 + "\n")
            for col, outlier_data in outliers.items():
                f.write(f"{col}:\n")
                f.write(f"  Outliers Count: {outlier_data['count']}\n")
                f.write(f"  Outliers Percentage: {outlier_data['percentage']:.2f}%\n")
                f.write(f"  Lower Bound: {outlier_data['lower_bound']:.4f}\n")
                f.write(f"  Upper Bound: {outlier_data['upper_bound']:.4f}\n")
        
        return report_path
    
    @staticmethod
    def generate_json_report(
        data_summary: Dict[str, Any], 
        descriptive_stats: Dict[str, Any], 
        correlations: Dict[str, Any], 
        outliers: Dict[str, Any],
        output_dir: str = '.'
    ) -> str:
        """
        Generate a comprehensive JSON report
        
        Args:
            Same as generate_text_report
        
        Returns:
            str: Path to generated JSON report
        """
        # Create timestamp for unique report name
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = os.path.join(output_dir, f'data_analysis_report_{timestamp}.json')
        
        report_data = {
            'metadata': {
                'generated_at': datetime.now().isoformat(),
                'total_rows': data_summary['total_rows'],
                'total_columns': data_summary['total_columns']
            },
            'data_summary': data_summary,
            'descriptive_statistics': descriptive_stats,
            'correlations': correlations,
            'outliers': outliers
        }
        
        with open(report_path, 'w') as f:
            json.dump(report_data, f, indent=2)
        
        return report_path