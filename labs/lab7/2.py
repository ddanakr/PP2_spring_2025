import pygame

pygame.init()
pygame.mixer.init()


screen = pygame.display.set_mode((800, 600))

pygame.font.init()
font = pygame.font.Font(None, 36)

running = True
n_playing = False
clock = pygame.time.Clock()

_songs = ["just_walk.mp3", "lonely_in_the_bar.mp3", "winter_wind.mp3"]

current_song = _songs[0] 

def play_next_song():
    global _songs, current_song
    _songs = _songs[1:] + [_songs[0]] 
    current_song = _songs[0] 
    pygame.mixer.music.load(current_song)
    pygame.mixer.music.play()

def play_prev_song():
    global _songs, current_song
    _songs = [_songs[-1]] + _songs[:-1]
    current_song = _songs[0] 
    pygame.mixer.music.load(current_song)
    pygame.mixer.music.play()

play_next_song()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()

                n_playing = not n_playing

            elif event.key == pygame.K_LEFT:
                play_prev_song()
            elif event.key == pygame.K_RIGHT:
                play_next_song()
            elif event.key == pygame.K_ESCAPE:
                pygame.mixer.music.stop()


    

    screen.fill((255, 255, 255))

    song_name = font.render(f"Now Playing: {current_song}", True, (0, 0, 0))
    screen.blit(song_name, (200, 250))

    pygame.display.flip()
    clock.tick(30)

