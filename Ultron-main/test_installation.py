#!/usr/bin/env python3
"""
Test script to verify all dependencies are properly installed
Run this before using the voice assistant
"""

import sys
import importlib

def test_import(module_name, package_name=None):
    """Test if a module can be imported"""
    try:
        if package_name:
            importlib.import_module(module_name)
            print(f"✅ {package_name or module_name} - OK")
            return True
        else:
            importlib.import_module(module_name)
            print(f"✅ {module_name} - OK")
            return True
    except ImportError as e:
        print(f"❌ {package_name or module_name} - FAILED")
        print(f"   Error: {e}")
        return False

def test_camera():
    """Test camera access"""
    try:
        import cv2
        cap = cv2.VideoCapture(0)
        if cap.isOpened():
            print("✅ Camera - OK (accessible)")
            cap.release()
            return True
        else:
            print("❌ Camera - FAILED (not accessible)")
            return False
    except Exception as e:
        print(f"❌ Camera - FAILED")
        print(f"   Error: {e}")
        return False

def test_microphone():
    """Test microphone access"""
    try:
        import speech_recognition as sr
        mics = sr.Microphone.list_microphone_names()
        if mics:
            print(f"✅ Microphone - OK (found {len(mics)} devices)")
            return True
        else:
            print("❌ Microphone - FAILED (no devices found)")
            return False
    except Exception as e:
        print(f"❌ Microphone - FAILED")
        print(f"   Error: {e}")
        return False

def test_text_to_speech():
    """Test text-to-speech"""
    try:
        import pyttsx3
        engine = pyttsx3.init()
        voices = engine.getProperty('voices')
        if voices:
            print(f"✅ Text-to-Speech - OK (found {len(voices)} voices)")
            return True
        else:
            print("❌ Text-to-Speech - FAILED (no voices found)")
            return False
    except Exception as e:
        print(f"❌ Text-to-Speech - FAILED")
        print(f"   Error: {e}")
        return False

def main():
    """Run all tests"""
    print("🔍 Testing Voice Assistant Dependencies")
    print("=" * 50)
    
    # Test Python version
    python_version = sys.version_info
    if python_version.major >= 3 and python_version.minor >= 7:
        print(f"✅ Python {python_version.major}.{python_version.minor} - OK")
    else:
        print(f"❌ Python {python_version.major}.{python_version.minor} - FAILED (need 3.7+)")
        return False
    
    print()
    
    # Test core dependencies
    tests = [
        ("cv2", "OpenCV"),
        ("numpy", "NumPy"),
        ("PIL", "Pillow"),
        ("face_recognition", "Face Recognition"),
        ("speech_recognition", "Speech Recognition"),
        ("pyttsx3", "Text-to-Speech"),
    ]
    
    all_passed = True
    for module, name in tests:
        if not test_import(module, name):
            all_passed = False
    
    print()
    
    # Test hardware access
    print("🔧 Testing Hardware Access")
    print("-" * 30)
    
    if not test_camera():
        all_passed = False
        
    if not test_microphone():
        all_passed = False
        
    if not test_text_to_speech():
        all_passed = False
    
    print()
    print("=" * 50)
    
    if all_passed:
        print("🎉 All tests passed! You're ready to use the voice assistant.")
        print("\nNext steps:")
        print("1. Run: python register_face.py")
        print("2. Run: python advanced_voice_assistant.py")
    else:
        print("❌ Some tests failed. Please fix the issues before proceeding.")
        print("\nCommon solutions:")
        print("- Install missing packages: pip install -r requirements.txt")
        print("- Check camera and microphone permissions")
        print("- Ensure proper system dependencies are installed")
    
    return all_passed

if __name__ == "__main__":
    main()