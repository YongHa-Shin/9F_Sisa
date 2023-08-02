# Video is only mp4
# Audio format is wav
import moviepy.editor as mp
from Cloava_Speech_Client import ClovaSpeechClient

# file_name에 비디오명을 적으세요.
# !!주의 확장자는 제외하고 적으세요!!..
file_name = "26_1"

# Load the video
video = mp.VideoFileClip(file_name + ".mp4")
  
# Extract the audio from the video
audio_file = video.audio
audio_file_name = file_name + ".wav"
audio_file.write_audiofile(audio_file_name)

res = ClovaSpeechClient().req_upload(file=audio_file_name, completion='sync')
print(res.text)