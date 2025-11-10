# AI Voice Assistant with Face Recognition

A sophisticated voice assistant that can identify your face, recognize you as master, and execute various voice commands. Built with Python using computer vision, speech recognition, and text-to-speech technologies.

## Features

### 🔐 Face Recognition
- **Master Identification**: Recognizes you as the master/owner
- **Real-time Detection**: Continuous face detection and recognition
- **Visual Feedback**: Green boxes for recognized faces, red for unknown
- **Multiple Face Support**: Can recognize multiple known faces

### 🎤 Voice Commands
- **Natural Language Processing**: Understands conversational commands
- **Multiple Command Types**: Time, date, system control, file operations
- **Voice Response**: Speaks back to confirm actions
- **Command History**: Logs all conversations for review

### 🚀 Available Commands

#### Basic Commands
- `"Hello"`, `"Hi"`, `"Hey"` - Greeting responses
- `"What time is it?"` - Get current time
- `"What's the date?"` - Get current date
- `"Help"` - List available commands
- `"Goodbye"` - Exit the assistant

#### System Commands
- `"System info"` - Display system information
- `"List files"` - Show files in current directory
- `"Open [application]"` - Launch applications
- `"Shutdown"` - Turn off the system
- `"Restart"` - Restart the system

#### Web & Search
- `"Search for [query]"` - Perform web searches
- `"Google [query]"` - Search on Google

## Installation

### Prerequisites
- Python 3.7 or higher
- Webcam for face recognition
- Microphone for voice input
- Speakers for voice output

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

**Note**: On some systems, you may need to install additional system packages:

#### Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install python3-dev python3-pip
sudo apt-get install libasound2-dev portaudio19-dev libportaudio2 libportaudiocpp0
sudo apt-get install libopencv-dev python3-opencv
```

#### macOS:
```bash
brew install portaudio
brew install opencv
```

#### Windows:
- Install Visual Studio Build Tools
- Install OpenCV from pre-built binaries

### Step 2: Face Registration
Before using the voice assistant, you need to register your face:

```bash
python register_face.py
```

**Instructions:**
1. Position your face clearly in the camera view
2. Ensure good lighting
3. Press `c` to capture your face
4. Press `q` to quit

Your face will be saved as `master.jpg` in the `faces/` directory.

### Step 3: Run the Assistant

#### Basic Version:
```bash
python voice_assistant.py
```

#### Advanced Version (Recommended):
```bash
python advanced_voice_assistant.py
```

## Usage

### Starting the Assistant
1. Run the appropriate Python script
2. The assistant will initialize and start looking for your face
3. Once your face is recognized, you'll hear "Welcome Master! I am at your service."
4. The assistant will then listen for your voice commands

### Voice Command Examples
- **"What time is it?"** → Assistant tells you the current time
- **"List files"** → Assistant shows files in current directory
- **"Search for Python tutorials"** → Opens Google search in browser
- **"Open calculator"** → Launches calculator application
- **"System info"** → Displays operating system information

### Stopping the Assistant
- Say **"Goodbye"** or **"Exit"**
- Press `q` in the camera window
- Use Ctrl+C in the terminal

## Configuration

The advanced assistant creates a configuration file `assistant_config.json` that you can modify:

```json
{
  "wake_word": "hey assistant",
  "master_name": "master",
  "system_commands": true,
  "web_search": true,
  "file_operations": true
}
```

### Configuration Options
- **wake_word**: Custom wake phrase (not yet implemented)
- **master_name**: What the assistant calls you
- **system_commands**: Enable/disable system control commands
- **web_search**: Enable/disable web search functionality
- **file_operations**: Enable/disable file listing

## Troubleshooting

### Common Issues

#### 1. Camera Not Working
```bash
# Check if camera is accessible
python -c "import cv2; cap = cv2.VideoCapture(0); print(cap.isOpened())"
```

#### 2. Microphone Issues
```bash
# Test microphone access
python -c "import speech_recognition as sr; print(sr.Microphone.list_microphone_names())"
```

#### 3. Face Recognition Not Working
- Ensure good lighting
- Face should be clearly visible
- Check if `faces/` directory contains your face image
- Verify image format (JPG, PNG, JPEG)

#### 4. Speech Recognition Issues
- Check internet connection (uses Google Speech API)
- Ensure microphone is working
- Speak clearly and at normal volume
- Reduce background noise

### Performance Tips
- Use a good quality webcam for better face recognition
- Ensure adequate lighting for face detection
- Use a noise-canceling microphone for better voice recognition
- Close unnecessary applications to free up system resources

## File Structure

```
voice-assistant/
├── voice_assistant.py          # Basic voice assistant
├── advanced_voice_assistant.py # Advanced version with more features
├── register_face.py            # Face registration tool
├── requirements.txt            # Python dependencies
├── README.md                   # This file
├── faces/                      # Directory for face images
│   └── master.jpg             # Your registered face
├── assistant_config.json       # Configuration file
└── conversation_history.json   # Command history log
```

## Security Considerations

⚠️ **Important Security Notes:**
- The assistant can execute system commands (shutdown, restart)
- Face recognition is not 100% secure
- Voice commands can be spoofed
- Use in controlled environments only
- Consider disabling system commands in production

## Customization

### Adding New Commands
You can extend the assistant by adding new command handlers in the `execute_command` method:

```python
elif "custom command" in command:
    # Your custom logic here
    self.speak("Custom action executed!")
```

### Adding New Faces
Simply add more face images to the `faces/` directory. The assistant will automatically load and recognize them.

### Voice Customization
Modify voice properties in the `setup_voice` method:
```python
self.engine.setProperty('rate', 150)      # Speech rate
self.engine.setProperty('volume', 0.9)    # Volume level
```

## Contributing

Feel free to contribute improvements:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is open source and available under the MIT License.

## Support

If you encounter issues:
1. Check the troubleshooting section
2. Review the error messages in the terminal
3. Ensure all dependencies are properly installed
4. Check system permissions for camera and microphone access

---

**Enjoy your personal AI voice assistant!** 🎉
