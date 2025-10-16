#!/usr/bin/env python3
from data_analyst_agent import DataAnalystAgent

def main():
    import argparse
    
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
        default='./analysis_results', 
        help='Directory to save analysis outputs'
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # Initialize and run agent
    agent = DataAnalystAgent(output_dir=args.output_dir)
    agent.analyze(args.file, report_format=args.report_format)

if __name__ == "__main__":
    main()