# -*- coding: UTF-8 -*-
from gtts import gTTS
hello = 'buongiorno'.encode('utf-8')
tts = gTTS(text= hello, lang='it', slow=False)
tts.save('hello.mp3')