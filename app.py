from flask import Flask , request ,Response ,jsonify
import os
from moviepy.editor import VideoFileClip, concatenate_videoclips



app = Flask(__name__)

application = app
num_folder = r"website\Data"

@app.route('/' , methods=['GET' , 'POST'])
def homw():

    video = [f for f in os.listdir(num_folder)]


    return jsonify({ 'data ' : video })

@app.route('/word/' , methods=['GET' , 'POST'])
def main():
    try :
        text = request.args.get('image')

        guj_links = { }


        

        def retrieve_words(sentence):
            words = sentence.split()
            return words

        user_input = text

        words = retrieve_words(user_input)

        for word in words:
            for gj in os.listdir(num_folder):
                if word == gj:
                    guj_links[word] = os.path.join(num_folder, gj)

        video_extensions = (".mp4")

        video_files = []
        for word in words:
                if os.path.isdir(guj_links[word]):
                    files = [f for f in os.listdir(guj_links[word]) if f.endswith(video_extensions)]
                    video_files.extend(os.path.join(guj_links[word], f) for f in files)


        clips = [VideoFileClip(video) for video in video_files]

        final_clip = concatenate_videoclips(clips , method="compose")

        final_clip = final_clip.resize(0.5)

        final_clip.write_videofile("sign.mp4")
        video = "sign.mp4"

        def generate(video_path):
            with open(video_path, 'rb') as f:
                while True:
                    chunk = f.read(1024 * 1024)
                    if not chunk:
                        break
                    yield chunk

        return Response(generate(video), mimetype='video/mp4')
    except Exception as f:
        return f" Sign of { f } is not Found "


if __name__ == "__main__":
    app.run()
