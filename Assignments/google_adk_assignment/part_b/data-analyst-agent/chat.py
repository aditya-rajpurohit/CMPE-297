import argparse
from src.data_analyst_agent import DataAnalystAgent, start_chat_interface

def main():
    parser = argparse.ArgumentParser(description="AI-Powered Data Analyst Agent")
    
    # Add a mutually exclusive group for different modes
    mode_group = parser.add_mutually_exclusive_group()
    
    # File analysis mode
    mode_group.add_argument(
        'file', 
        nargs='?', 
        help='Path to data file (CSV, XLSX, JSON)'
    )
    
    # Chat mode
    mode_group.add_argument(
        '--chat', 
        action='store_true', 
        help='Start interactive chat interface'
    )
    
    # Additional arguments for file analysis
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
    
    # Determine mode of operation
    if args.chat:
        # Start chat interface
        start_chat_interface()
    elif args.file:
        # Perform file analysis
        agent = DataAnalystAgent(output_dir=args.output_dir)
        agent.analyze(args.file, report_format=args.report_format)
    else:
        # If no mode specified, show help
        parser.print_help()

if __name__ == "__main__":
    main()