#!/bin/bash

# Color codes for better output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check Python version
if ! command -v python3 &> /dev/null
then
    echo -e "${YELLOW}❌ Python 3 is not installed. Please install Python 3.8 or higher.${NC}"
    exit 1
fi

# Verify Python version
PYTHON_VERSION=$(python3 --version | cut -d' ' -f2)
REQUIRED_VERSION="3.8.0"

if [ "$(printf '%s\n' "$REQUIRED_VERSION" "$PYTHON_VERSION" | sort -V | head -n1)" != "$REQUIRED_VERSION" ]; then
    echo -e "${YELLOW}❌ Python version must be 3.8 or higher. Current version: $PYTHON_VERSION${NC}"
    exit 1
fi

# Create virtual environment
echo -e "${GREEN}🔧 Creating virtual environment...${NC}"
python3 -m venv venv

# Activate virtual environment
source venv/bin/activate

# Upgrade pip
pip install --upgrade pip

# Install requirements
echo -e "${GREEN}📦 Installing project dependencies...${NC}"
pip install -r requirements.txt

# Optional: Install development dependencies
pip install pytest pylint black

# Create output directory for reports
mkdir -p ./analysis_results

# Make main script executable
chmod +x main.py

echo -e "${GREEN}✅ Data Analyst Agent environment setup complete!${NC}"
echo -e "${YELLOW}To activate: source venv/bin/activate${NC}"
echo -e "${YELLOW}To run: python main.py <your_data_file>${NC}"