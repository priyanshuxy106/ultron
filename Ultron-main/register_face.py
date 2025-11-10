import cv2
import face_recognition
import os
import numpy as np

def register_face():
    """Register a new face for recognition"""
    print("Face Registration Tool")
    print("=====================")
    
    # Create faces directory if it doesn't exist
    faces_dir = "faces"
    if not os.path.exists(faces_dir):
        os.makedirs(faces_dir)
    
    # Initialize camera
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open camera")
        return
    
    print("\nInstructions:")
    print("1. Position your face in the camera view")
    print("2. Press 'c' to capture your face")
    print("3. Press 'q' to quit")
    print("\nMake sure your face is clearly visible and well-lit!")
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Display frame
        cv2.imshow('Face Registration - Press c to capture, q to quit', frame)
        
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('c'):
            # Detect faces in the frame
            face_locations = face_recognition.face_locations(frame)
            
            if len(face_locations) == 0:
                print("No face detected! Please position your face in the camera view.")
            elif len(face_locations) > 1:
                print("Multiple faces detected! Please ensure only your face is visible.")
            else:
                # Get the first (and should be only) face
                top, right, bottom, left = face_locations[0]
                
                # Extract face region
                face_image = frame[top:bottom, left:right]
                
                # Encode the face
                face_encoding = face_recognition.face_encodings(frame, [face_locations[0]])
                
                if len(face_encoding) > 0:
                    # Save the face image
                    face_filename = "master.jpg"
                    face_path = os.path.join(faces_dir, face_filename)
                    
                    # Resize face image for better quality
                    face_image_resized = cv2.resize(face_image, (200, 200))
                    
                    cv2.imwrite(face_path, face_image_resized)
                    
                    print(f"\nFace captured and saved as '{face_filename}'!")
                    print("You can now run the voice assistant.")
                    break
                else:
                    print("Could not encode face. Please try again.")
        
        elif key == ord('q'):
            print("\nRegistration cancelled.")
            break
    
    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    register_face()