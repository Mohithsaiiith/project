from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__)
songs_directory = 'static/audio'

songs = []  # Store song filenames

for root, dirs, files in os.walk(songs_directory):
    for file in files:
        if file.endswith('.wav'):
            songs.append(file)

# Sort songs by filename in increasing order
songs.sort(key=lambda x: int(x.split('-')[1].split('.')[0]))

@app.route('/')
def index():
    return render_template('index.html', songs=songs)

@app.route('/audio/<path:filename>')
def serve_audio(filename):
    return send_from_directory(songs_directory, filename)

if __name__ == '__main__':
    app.run(debug=False)

