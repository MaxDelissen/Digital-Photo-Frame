import cv2
import pygame


def display_video(video_path):
    video = cv2.VideoCapture(video_path)
    success, video_image = video.read()
    fps = video.get(cv2.CAP_PROP_FPS)

    window = pygame.display.set_mode(video_image.shape[1::-1])
    clock = pygame.time.Clock()

    run = success
    while run:
        clock.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        success, video_image = video.read()
        if success:
            video_surf = pygame.image.frombuffer(
                video_image.tobytes(), video_image.shape[1::-1], "BGR")
        else:
            run = False
        window.blit(video_surf, (0, 0))
        pygame.display.flip()

    video.release()
