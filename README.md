# Laser Eyes Meme Maker /w AI

> Upload a selfie or a foto containing a face, our sofisticated AI algorithm will recognice it and add a random laser on your eyes. Send multiple times for multiple colors. Laser Eyes Meme Maker /w AI is easy and fast.

# Requirements
- git
- pip3
- python3
- docker (optional)
- docker-compose (optional)

# Running the project (first time):
- Download it:
```sh
git clone git@bitbucket.org:everlyrusher/lasereyesai.git@bitbucket
```

- Install Python dependencies:
```sh
pip3 install -r requirements.txt
```

- Running ti:
```sh
python3 app.python3
```

- Now you can access: http://0.0.0.0:8181/

# Running the project (second time):
- Running it:
```sh
python3 app.py
```

# Running the project (docker):
Docker does everything, install requirements and runs the app.
```sh
docker-compose up -d
```

# Demo: [Laser Eyes Meme Maker /w AI](https://lasereyes.everlyrusher.com/)

# Technologies used:
- [Python](https://www.python.org/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [Pillow](https://python-pillow.org/)
- [Face Recognition](https://github.com/ageitgey/face_recognition)
- [Tailwindcss](https://tailwindcss.com/)
- [Vue](https://vuejs.org/)
- [Docker](https://www.docker.com/)

# CSS
- Compile css:
```sh
npx tailwindcss-cli@latest build app.scss -o static/app.css
```

- Minify css:
```sh
csso static/app.css --output static/app.css
```

# Other things:
- How to tell flask to calm down aka development mode.
```sh
export FLASK_ENV=development
```

# Other documentation:
- [Building a vue.js drag-and-drop file component](https://stenvdb.be/articles/building-a-vuejs-drag-and-drop-file-component)
- [Escape string in jinja](https://jinja.palletsprojects.com/en/2.11.x/templates/#escaping)
- [Emojipedia](https://emojipedia.org/sparkles/)
- [PIL Docs](https://pillow.readthedocs.io/en/stable/reference/Image.html)
- [Copy to clipboard in Vue](https://daily-dev-tips.com/posts/vanilla-javascript-copy-text-to-clipboard-with-clipboard-api/)
- [EXIF rotations problem](https://github.com/ageitgey/face_recognition/wiki/Common-Errors#issue-its-not-detecting-faces-in-my-very-simple-image-i-took-with-my-iphone--android-phone)
- [Rotate EXIF in python](https://stackoverflow.com/questions/13872331/rotating-an-image-with-orientation-specified-in-exif-using-python-without-pil-in)
