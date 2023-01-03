import cv2
from utils.app import FashionPose
import tkinter as tk
from PIL import Image, ImageTk
import numpy as np
show_webcam = True
import mediapipe as mp
import matplotlib.pyplot as plt
from utils.background import load_background


def run_outfit(outfit):
    # Inicjalizacja klasy FashionPose
    draw_skeleton = FashionPose(show_webcam, outfit_type=outfit)
    # Inicjalizacja webcamu
    cap = cv2.VideoCapture(0)

    # podstawowe tło zdjęciowe
    bg_image = cv2.imread('images/backgrounds/2.png')

    #ustawianie outfit w konstruktorze
    draw_skeleton.outfit_type = outfit

    while cap.isOpened():

        # Czytanie framów
        ret, frame = cap.read()

        keyboard = cv2.waitKey(1)
        bg_image = load_background(keyboard, bg_image)

        selfie_segmentation = mp.solutions.selfie_segmentation.SelfieSegmentation(1)
        # Ustawianie obrazu z kamery horyzontalnie
        frame = cv2.flip(frame, 1)

        # wczytywanie funkcji do rysowania ouffitu
        ret, skeleton_image = draw_skeleton(frame)

        #przycinanie zdjęć na tło
        webcam_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        webcam_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        bg_image = cv2.resize(bg_image, (webcam_width, webcam_height), interpolation=cv2.INTER_AREA)
        # bg_image = cv2.cvtColor(bg_image, cv2.COLOR_BGR2RGB)

        # rysowanie tła
        results = selfie_segmentation.process(frame)
        condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
        output_image = np.where(condition, skeleton_image, bg_image)
        if not ret:
            continue

        # wyświetlanie outfitu oraz tła i czekanie na przycisk zamknięcia
        cv2.imshow("Fashion", output_image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # zamykanie wszystkich okien po wyjściu z kamery
    cv2.destroyAllWindows()

# kontury i tło gif
def run_outfit1(outfit):
    # Inicjalizacja klasy FashionPose
    draw_skeleton = FashionPose(show_webcam, outfit_type=outfit)
    # Inicjalizacja webcamu
    cap = cv2.VideoCapture(0)

    cap1 = cv2.VideoCapture('images/backgrounds/1.gif')

    # ustawianie outfit w konstruktorze
    draw_skeleton.outfit_type = outfit

    while cap.isOpened():

        # Czytanie framów
        ret, frame = cap.read()
        success1, bg_image = cap1.read()
        # background loop
        if not success1:
            cap1 = cv2.VideoCapture('images/backgrounds/4.gif')
            cap1.set(cv2.CAP_PROP_POS_FRAMES, 0)
            continue

        selfie_segmentation = mp.solutions.selfie_segmentation.SelfieSegmentation(1)
        # Ustawianie obrazu z kamery horyzontalnie
        frame = cv2.flip(frame, 1)

        # wczytywanie funkcji do rysowania ouffitu
        ret, skeleton_image = draw_skeleton(frame)

        #przycinanie gif do okna
        webcam_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        webcam_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        bg_image = cv2.resize(bg_image, (webcam_width, webcam_height), interpolation=cv2.INTER_AREA)

        # rysowanie tła
        results = selfie_segmentation.process(frame)
        condition = np.stack((results.segmentation_mask,) * 3, axis=-1) > 0.1
        output_image = np.where(condition, skeleton_image, bg_image)
        if not ret:
            continue

        # wyświetlanie outfitu oraz tła i czekanie na przycisk zamknięcia
        cv2.imshow("Fashion", output_image)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



    # zamykanie wszystkich okien po wyjściu z kamery
    cv2.destroyAllWindows()
