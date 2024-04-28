import serial
import pygame

# Initialize serial connection
ser = serial.Serial('COM10', 9600)  # Adjust the port and baud rate as needed

# Initialize pygame mixer
pygame.mixer.init()
pygame.mixer.music.load('main.mp3')
pygame.mixer.music.play()
while True:
    # Read data from serial port
    data = ser.readline().strip()

    # Check if data indicates to play MP3
    if data == b'coin':
        # Load and play the MP3 file
        pygame.mixer.music.load('coin-trimmed.mp3')
        pygame.mixer.music.play()
    
    if data== b'collision':
        pygame.mixer.music.load('collision.mp3')
        pygame.mixer.music.play()
    
    if data== b'bush':
        pygame.mixer.music.load('bush.mp3')
        pygame.mixer.music.play()
    
    if data== b'Ground':
        pygame.mixer.music.load('ground_hit.mp3')
        pygame.mixer.music.play()
    
    if data== b'thunder':
        pygame.mixer.music.load('thunder.mp3')
        pygame.mixer.music.play()
