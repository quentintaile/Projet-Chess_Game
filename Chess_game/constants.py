import pygame
import os

Width, Height = 760,760
Rows, Cols = 8,8
Square = Width//Rows


brown = (87,16,16)
white = (255,255,255)

Path = "Chess_game/chess_images"

#Pieces Noir
# Pièces Noires
Black_Knight = pygame.transform.scale(pygame.image.load(os.path.join(Path, "bKn.png")), (Square, Square))
Black_Bishop = pygame.transform.scale(pygame.image.load(os.path.join(Path, "bB.png")), (Square, Square))
Black_King = pygame.transform.scale(pygame.image.load(os.path.join(Path, "bK.png")), (Square, Square))
Black_Pawn = pygame.transform.scale(pygame.image.load(os.path.join(Path, "bP.png")), (Square, Square))
Black_Queen = pygame.transform.scale(pygame.image.load(os.path.join(Path, "bQ.png")), (Square, Square))
Black_Rook = pygame.transform.scale(pygame.image.load(os.path.join(Path, "bR.png")), (Square, Square))

# Pièces Blanches
White_Knight = pygame.transform.scale(pygame.image.load(os.path.join(Path, "wkn.png")), (Square, Square))
White_Bishop = pygame.transform.scale(pygame.image.load(os.path.join(Path, "wB.png")), (Square, Square))
White_King = pygame.transform.scale(pygame.image.load(os.path.join(Path, "wK.png")), (Square, Square))
White_Pawn = pygame.transform.scale(pygame.image.load(os.path.join(Path, "wP.png")), (Square, Square))
White_Queen = pygame.transform.scale(pygame.image.load(os.path.join(Path, "wQ.png")), (Square, Square))
White_Rook = pygame.transform.scale(pygame.image.load(os.path.join(Path, "wR.png")), (Square, Square))
