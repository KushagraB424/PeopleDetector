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

### Installation

1. Clone the repository:
```bash
git clone https://github.com/KushagraB424/PeopleDetector.git
cd PeopleDetector
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open your browser and navigate to `http://localhost:5000`

## Deployment on Render

### Step 1: Push to GitHub

1. Initialize git repository (if not already done):
```bash
cd /Users/jawaharlal/Downloads/PeopleDetector
git init
git add .
git commit -m "Initial commit: People Detector app"
```

2. Add your GitHub repository as remote:
```bash
git remote add origin https://github.com/KushagraB424/PeopleDetector.git
git branch -M main
git push -u origin main
```

### Step 2: Deploy on Render

1. Go to [Render Dashboard](https://dashboard.render.com/)
2. Click **"New +"** → **"Web Service"**
3. Connect your GitHub account if not already connected
4. Select the **PeopleDetector** repository
5. Configure the service:
   - **Name**: `people-detector` (or your preferred name)
   - **Environment**: `Python`
   - **Build Command**: `pip install -r requirements.txt`
   - **Start Command**: `gunicorn app:app --bind 0.0.0.0:$PORT`
   - **Instance Type**: Free (or your preferred tier)
6. Click **"Create Web Service"**
7. Wait for the deployment to complete (5-10 minutes)
8. Your app will be live at `https://people-detector-xxxx.onrender.com`

### Alternative: Deploy using render.yaml

Render can automatically detect the `render.yaml` file in your repository:

1. Push your code to GitHub (as shown above)
2. Go to Render Dashboard
3. Click **"New +"** → **"Blueprint"**
4. Connect your repository
5. Render will automatically use the `render.yaml` configuration
6. Click **"Apply"** to deploy

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
