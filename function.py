import tempfile
from gtts import gTTS
from playsound import playsound
import datetime


def speak(sentence):
    with tempfile.NamedTemporaryFile(delete=True) as fp:
        tts = gTTS(text=sentence,lang='zh-tw')
        tts.save('{}.mp3'.format(fp.name))
        playsound('{}.mp3'.format(fp.name))

def gettime():
    current = datetime.datetime.now()
    if current.hour > 12 :
        speak("現在時間，下午%d點%d分" % (current.hour-12 , current.minute))
    else:
        speak("現在時間，上午%d點%d分" % (current.hour, current.minute))

