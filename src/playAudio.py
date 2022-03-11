# # This program is about to Healty Programmer...

from pygame import mixer

def playAudio(song, terminate_string):
    # strting mixer
    mixer.init()

    # loding song
    mixer.music.load(song)

    # setting volume
    mixer.music.set_volume(0.5)

    # start playing the song
    mixer.music.play(-1)

    while True:
        inp = input()
        if inp == terminate_string:
            mixer.music.stop()
            break
        else:
            print ("read the instrction!!!")
