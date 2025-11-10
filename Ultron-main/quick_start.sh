#!/bin/bash

echo "🤖 AI Voice Assistant - Quick Start Setup"
echo "=========================================="
echo

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3.7+ first."
    exit 1
fi

# Check Python version
python_version=$(python3 -c "import sys; print(f'{sys.version_info.major}.{sys.version_info.minor}')")
required_version="3.7"

if [ "$(printf '%s\n' "$required_version" "$python_version" | sort -V | head -n1)" != "$required_version" ]; then
    echo "❌ Python version $python_version is too old. Need Python 3.7+"
    exit 1
fi

echo "✅ Python $python_version detected"

# Install system dependencies (Ubuntu/Debian)
if command -v apt-get &> /dev/null; then
    echo "📦 Installing system dependencies..."
    sudo apt-get update
    sudo apt-get install -y python3-dev python3-pip
    sudo apt-get install -y libasound2-dev portaudio19-dev libportaudio2 libportaudiocpp0
    sudo apt-get install -y libopencv-dev python3-opencv
    echo "✅ System dependencies installed"
fi

# Install Python dependencies
echo "📦 Installing Python dependencies..."
python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

if [ $? -eq 0 ]; then
    echo "✅ Python dependencies installed"
else
    echo "❌ Failed to install Python dependencies"
    exit 1
fi

# Create faces directory
mkdir -p faces

echo
echo "🎉 Setup completed successfully!"
echo
echo "Next steps:"
echo "1. Run: python3 register_face.py"
echo "2. Run: python3 advanced_voice_assistant.py"
echo
echo "Or use the launcher:"
echo "python3 launch_assistant.py"
echo
echo "Enjoy your AI voice assistant! 🚀"