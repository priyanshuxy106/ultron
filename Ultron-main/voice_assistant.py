import cv2
import face_recognition
import speech_recognition as sr
import pyttsx3
import numpy as np
import os
import json
import time
from datetime import datetime
import threading
import queue

class VoiceAssistant:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.engine = pyttsx3.init()
        self.cap = cv2.VideoCapture(0)
        
        # Face recognition variables
        self.known_face_encodings = []
        self.known_face_names = []
        self.face_locations = []
        self.face_encodings = []
        self.face_names = []
        self.process_this_frame = True
        
        # Voice assistant state
        self.is_listening = False
        self.voice_queue = queue.Queue()
        self.master_identified = False
        
        # Initialize voice settings
        self.setup_voice()
        
        # Load known faces
        self.load_known_faces()
        
    def setup_voice(self):
        """Setup voice engine properties"""
        voices = self.engine.getProperty('voices')
        if voices:
            self.engine.setProperty('voice', voices[0].id)
        self.engine.setProperty('rate', 150)
        self.engine.setProperty('volume', 0.9)
        
    def load_known_faces(self):
        """Load known faces from the faces directory"""
        faces_dir = "faces"
        if not os.path.exists(faces_dir):
            os.makedirs(faces_dir)
            print(f"Created {faces_dir} directory. Please add your face image there.")
            return
            
        for filename in os.listdir(faces_dir):
            if filename.endswith((".jpg", ".jpeg", ".png")):
                image_path = os.path.join(faces_dir, filename)
                image = face_recognition.load_image_file(image_path)
                encoding = face_recognition.face_encodings(image)
                
                if encoding:
                    self.known_face_encodings.append(encoding[0])
                    name = os.path.splitext(filename)[0]
                    self.known_face_names.append(name)
                    print(f"Loaded face: {name}")
                    
    def speak(self, text):
        """Convert text to speech"""
        print(f"Assistant: {text}")
        self.engine.say(text)
        self.engine.runAndWait()
        
    def listen_for_command(self):
        """Listen for voice commands"""
        try:
            with self.microphone as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=0.5)
                print("Listening for command...")
                audio = self.recognizer.listen(source, timeout=5, phrase_time_limit=10)
                
            command = self.recognizer.recognize_google(audio).lower()
            print(f"Master said: {command}")
            return command
            
        except sr.WaitTimeoutError:
            return None
        except sr.UnknownValueError:
            print("Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None
            
    def identify_face(self, frame):
        """Identify faces in the frame"""
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]
        
        if self.process_this_frame:
            self.face_locations = face_recognition.face_locations(rgb_small_frame)
            self.face_encodings = face_recognition.face_encodings(rgb_small_frame, self.face_locations)
            
            self.face_names = []
            for face_encoding in self.face_encodings:
                matches = face_recognition.compare_faces(self.known_face_encodings, face_encoding)
                name = "Unknown"
                
                if True in matches:
                    first_match_index = matches.index(True)
                    name = self.known_face_names[first_match_index]
                    
                    # Check if master is identified
                    if name.lower() in ["master", "owner", "user"]:
                        self.master_identified = True
                        if not hasattr(self, 'master_greeted'):
                            self.speak("Welcome Master! I am at your service.")
                            self.master_greeted = True
                
                self.face_names.append(name)
                
        self.process_this_frame = not self.process_this_frame
        
        # Draw results on frame
        for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 255, 0), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 0.6, (255, 255, 255), 1)
            
        return frame
        
    def execute_command(self, command):
        """Execute voice commands"""
        if not command:
            return
            
        # Greeting commands
        if any(word in command for word in ["hello", "hi", "hey"]):
            self.speak("Hello Master! How can I help you today?")
            
        # Time commands
        elif "time" in command:
            current_time = datetime.now().strftime("%I:%M %p")
            self.speak(f"The current time is {current_time}")
            
        # Date commands
        elif "date" in command:
            current_date = datetime.now().strftime("%B %d, %Y")
            self.speak(f"Today is {current_date}")
            
        # Weather commands (placeholder)
        elif "weather" in command:
            self.speak("I'm sorry Master, I don't have access to weather information yet.")
            
        # System commands
        elif "shutdown" in command or "turn off" in command:
            self.speak("Shutting down the system, Master.")
            os.system("shutdown -h now")
            
        elif "restart" in command:
            self.speak("Restarting the system, Master.")
            os.system("reboot")
            
        # Help commands
        elif "help" in command or "what can you do" in command:
            self.speak("I can help you with the following tasks: tell time, tell date, shutdown or restart the system, and respond to greetings. Just ask me what you need, Master.")
            
        # Exit commands
        elif any(word in command for word in ["exit", "quit", "stop", "goodbye"]):
            self.speak("Goodbye Master! Have a great day!")
            return False
            
        else:
            self.speak("I'm sorry Master, I didn't understand that command. Please try again or say help for available commands.")
            
        return True
        
    def run(self):
        """Main run loop"""
        self.speak("Voice Assistant initialized. Looking for Master...")
        
        try:
            while True:
                # Face recognition
                ret, frame = self.cap.read()
                if not ret:
                    break
                    
                frame = self.identify_face(frame)
                
                # Show frame
                cv2.imshow('Voice Assistant - Face Recognition', frame)
                
                # Listen for commands if master is identified
                if self.master_identified:
                    if not self.is_listening:
                        self.is_listening = True
                        command = self.listen_for_command()
                        
                        if command:
                            if not self.execute_command(command):
                                break
                                
                        self.is_listening = False
                        
                # Handle key presses
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
                    
        except KeyboardInterrupt:
            print("\nShutting down...")
        finally:
            self.cleanup()
            
    def cleanup(self):
        """Clean up resources"""
        self.cap.release()
        cv2.destroyAllWindows()
        self.engine.stop()

if __name__ == "__main__":
    assistant = VoiceAssistant()
    assistant.run()