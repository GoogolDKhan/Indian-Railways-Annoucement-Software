import os
import pandas as pd
from pydub import AudioSegment
from gtts import gTTS


def textToSpeech(text, filename):
    mytext = str(text)
    language = 'hi'
    myobj = gTTS(text=mytext, lang=language, slow=True)
    myobj.save(filename)


# This function returns pydubs audio segment
def mergeAudios(audios):
    combined = AudioSegment.empty()
    for audio in audios:
        combined += AudioSegment.from_mp3(audio)
    return combined


def generateSkeleton():
    audio = AudioSegment.from_mp3('railway_audio.mp3')

    # 1.Generate 'Krupaya Dhyaan Dijiye'
    start = 88000  #88000 is 88 seconds which is 1:28 min
    finish = 90200
    audioProcessed = audio[start:finish]
    audioProcessed.export("generatedAudio/1_audio.mp3", format="mp3")

    # 2.is from city

    # 3.Generate 'se chalkar'
    start = 91000
    finish = 92200
    audioProcessed = audio[start:finish]
    audioProcessed.export("generatedAudio/3_audio.mp3", format="mp3")

    # 4.is via city

    # 5.Generate 'ke raaste'
    start = 94000
    finish = 95000
    audioProcessed = audio[start:finish]
    audioProcessed.export("generatedAudio/5_audio.mp3", format="mp3")

    # 6.is to city

    # 7.Generate 'ko jaane wali gaadi sankhya'
    start = 96000
    finish = 98900
    audioProcessed = audio[start:finish]
    audioProcessed.export("generatedAudio/7_audio.mp3", format="mp3")

    # 8.is train number and name

    # 9.Generate 'kuch hi samay me platform sankhya'
    start = 105500
    finish = 108200
    audioProcessed = audio[start:finish]
    audioProcessed.export("generatedAudio/9_audio.mp3", format="mp3")

    # 10.Platfrom number

    # 11.Generate 'par aa rahi hai'
    start = 109000
    finish = 112250
    audioProcessed = audio[start:finish]
    audioProcessed.export("generatedAudio/11_audio.mp3", format="mp3")


def generateAnnouncement(filename):
    df = pd.read_excel(filename)
    print(df)
    for index, item in df.iterrows():

        # Generate 2.is from city
        textToSpeech(item['from'], 'generatedAudio/2_audio.mp3')

        # Generate 4.is via city
        textToSpeech(item['via'], 'generatedAudio/4_audio.mp3')

        # Generate 6.is to city
        textToSpeech(item['to'], 'generatedAudio/6_audio.mp3')

        # Generate 8.is train number and name
        textToSpeech(item['train_no'] + " " +
                     item['train_name'], 'generatedAudio/8_audio.mp3')

        # Generate 10.Platfrom number
        textToSpeech(item['platform'], 'generatedAudio/10_audio.mp3')

        audios = [f"generatedAudio/{i}_audio.mp3" for i in range(1, 12)]

        announcement = mergeAudios(audios)
        announcement.export(f"Announcement/announcement_{index+1}.mp3", format="mp3")


if __name__ == '__main__':
    print("Generating Skeleton...")
    generateSkeleton()
    print("Now Generating Announcement...")
    generateAnnouncement("announce_sheet.xlsx")
