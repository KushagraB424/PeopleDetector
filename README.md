# People Detector 👥

A Flask-based web application that detects people in images using OpenCV's HOG (Histogram of Oriented Gradients) descriptor.

## Features

- Upload images through a clean web interface
- Automatic people detection using HOG + SVM
- Visual results with bounding boxes around detected people
- Responsive and modern UI

## Technologies Used

- **Flask**: Web framework
- **OpenCV**: Computer vision and people detection
- **Gunicorn**: Production WSGI server
- **HTML/CSS**: Frontend interface

## Local Development

### Prerequisites

- Python 3.8 or higher
- pip

## Project Structure

```
PeopleDetector/
├── app.py                 # Main Flask application
├── detect.py             # People detection logic
├── requirements.txt      # Python dependencies
├── render.yaml          # Render deployment config
├── .gitignore           # Git ignore rules
├── static/
│   ├── style.css        # CSS styling
│   ├── uploads/         # Uploaded images (not tracked)
│   └── results/         # Detection results (not tracked)
└── templates/
    └── index.html       # Main HTML template
```

## How It Works

1. User uploads an image through the web interface
2. Image is saved to the `static/uploads/` directory
3. OpenCV's HOG descriptor detects people in the image
4. Bounding boxes are drawn around detected people
5. Result image is saved to `static/results/` directory
6. Result is displayed to the user

## Notes

- The app uses `opencv-python-headless` for Render deployment (no GUI dependencies)
- Upload and result directories are created automatically if they don't exist
- Old uploaded/result images are not automatically cleaned up

## License

MIT License - feel free to use this project for learning and development!
