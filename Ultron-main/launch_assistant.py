#!/usr/bin/env python3
"""
Launcher script for the Voice Assistant
Provides a menu to choose between different options
"""

import os
import sys
import subprocess

def clear_screen():
    """Clear the terminal screen"""
    os.system('cls' if os.name == 'nt' else 'clear')

def print_banner():
    """Print the application banner"""
    print("🤖 AI Voice Assistant with Face Recognition")
    print("=" * 50)
    print()

def check_dependencies():
    """Check if dependencies are installed"""
    try:
        import cv2
        import face_recognition
        import speech_recognition
        import pyttsx3
        import numpy
        return True
    except ImportError:
        return False

def install_dependencies():
    """Install required dependencies"""
    print("📦 Installing dependencies...")
    try:
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"], check=True)
        print("✅ Dependencies installed successfully!")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False

def check_face_registration():
    """Check if face is registered"""
    faces_dir = "faces"
    if not os.path.exists(faces_dir):
        return False
    
    face_files = [f for f in os.listdir(faces_dir) if f.endswith(('.jpg', '.jpeg', '.png'))]
    return len(face_files) > 0

def register_face():
    """Launch face registration"""
    print("📷 Launching face registration...")
    try:
        subprocess.run([sys.executable, "register_face.py"])
        return True
    except Exception as e:
        print(f"❌ Failed to launch face registration: {e}")
        return False

def launch_assistant(version="advanced"):
    """Launch the voice assistant"""
    script_name = f"{version}_voice_assistant.py"
    if not os.path.exists(script_name):
        script_name = "voice_assistant.py"
    
    print(f"🚀 Launching {version} voice assistant...")
    try:
        subprocess.run([sys.executable, script_name])
        return True
    except Exception as e:
        print(f"❌ Failed to launch assistant: {e}")
        return False

def run_tests():
    """Run installation tests"""
    print("🔍 Running installation tests...")
    try:
        subprocess.run([sys.executable, "test_installation.py"])
        return True
    except Exception as e:
        print(f"❌ Failed to run tests: {e}")
        return False

def show_menu():
    """Show the main menu"""
    while True:
        clear_screen()
        print_banner()
        
        print("Available options:")
        print("1. 🧪 Run Installation Tests")
        print("2. 📦 Install Dependencies")
        print("3. 📷 Register Your Face")
        print("4. 🚀 Launch Basic Voice Assistant")
        print("5. 🚀 Launch Advanced Voice Assistant")
        print("6. 📖 View README")
        print("7. ❌ Exit")
        print()
        
        choice = input("Enter your choice (1-7): ").strip()
        
        if choice == "1":
            run_tests()
            input("\nPress Enter to continue...")
            
        elif choice == "2":
            if install_dependencies():
                input("\nPress Enter to continue...")
            else:
                input("\nPress Enter to continue...")
                
        elif choice == "3":
            if register_face():
                input("\nPress Enter to continue...")
            else:
                input("\nPress Enter to continue...")
                
        elif choice == "4":
            if check_face_registration():
                launch_assistant("basic")
            else:
                print("❌ No face registered! Please register your face first.")
                input("\nPress Enter to continue...")
                
        elif choice == "5":
            if check_face_registration():
                launch_assistant("advanced")
            else:
                print("❌ No face registered! Please register your face first.")
                input("\nPress Enter to continue...")
                
        elif choice == "6":
            clear_screen()
            try:
                with open("README.md", "r") as f:
                    content = f.read()
                    print(content)
            except FileNotFoundError:
                print("README.md not found!")
            input("\nPress Enter to continue...")
            
        elif choice == "7":
            print("👋 Goodbye!")
            break
            
        else:
            print("❌ Invalid choice. Please try again.")
            input("\nPress Enter to continue...")

def main():
    """Main function"""
    # Check if we're in the right directory
    if not os.path.exists("voice_assistant.py") and not os.path.exists("advanced_voice_assistant.py"):
        print("❌ Error: Voice assistant files not found!")
        print("Please run this script from the voice assistant directory.")
        return
    
    # Check dependencies
    if not check_dependencies():
        print("⚠️  Some dependencies are missing.")
        print("Would you like to install them now? (y/n): ", end="")
        if input().lower().startswith('y'):
            if not install_dependencies():
                print("❌ Failed to install dependencies. Please install them manually.")
                return
    
    # Show main menu
    show_menu()

if __name__ == "__main__":
    main()