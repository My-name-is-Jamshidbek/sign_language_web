
# Sign Language Translator Web App

This project is a Django-based web application that translates sign language gestures into text using a webcam. The application utilizes machine learning for gesture recognition, OpenCV for image processing, and MediaPipe for hand tracking.

---

## Features

- **Real-Time Sign Language Translation:** Capture hand gestures via a webcam and translate them into text.
- **Machine Learning Integration:** Uses a trained classification model for gesture recognition.
- **Webcam-Based Capture:** Interactive UI for starting and stopping translation.
- **Responsive Web App:** Accessible from various devices with a user-friendly interface.

---

## Project Structure

```
sign_language/
│
├── sign_language/               # Main Django application
│   ├── static/                        # Static files (CSS, JS, Images)
│   ├── templates/                     # HTML templates
│   ├── models.py                      # Django models (if any)
│   ├── views.py                       # View functions
│   ├── urls.py                        # App-specific URL routing
│   ├── sign_to_txt.py                 # Gesture recognition class
│   ├── forms.py                       # Forms for validation
│
├── signlang/           # Django project settings
│   ├── settings.py                    # Django settings
│   ├── urls.py                        # Project-level URL routing
│   ├── wsgi.py                        # WSGI entry point
│
├── manage.py                          # Django management script
├── requirements.txt                   # Python dependencies
└── README.md                          # Project documentation
```

---

## Prerequisites

Before running the project, ensure you have the following installed:

- Python 3.8+
- Django 4.0+
- OpenCV (`opencv-python`)
- MediaPipe
- NumPy
- A modern web browser

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ITPARKKHOREZM/sign_language.git
cd sign_language
```

### 2. Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Apply Migrations

```bash
python manage.py migrate
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

Open the application in your browser at `http://127.0.0.1:8000/`.

---

## How It Works

1. **Webcam Integration:** The application uses your webcam to capture hand gestures.
2. **Hand Tracking:** MediaPipe identifies key points on the hand.
3. **Gesture Prediction:** A trained ML model classifies the hand gesture into a corresponding letter or word.
4. **Display Translations:** Translations are shown in real-time on the web interface.

---

## Usage

1. Navigate to the home page.
2. Allow access to your webcam when prompted.
3. Click the **Start Translating** button to begin.
4. Perform sign language gestures in front of your webcam.
5. Translated text will appear below the video feed.

---

## Key Files

- **`hand_detector/main/hand_detector.py`:** Core logic for hand tracking and gesture recognition.
- **`pages/views.py`:** Django views for handling requests and processing images.
- **`pages/views.py/process_image` View:** Processes images from the webcam and returns predictions.
- **HTML & JavaScript:** Implements the frontend for video capture and translation.

---

## Future Enhancements

- **Expand Gesture Vocabulary:** Add more signs and gestures to the model.
- **Multilingual Support:** Translate signs into multiple languages.
- **Mobile Compatibility:** Enhance UI for better performance on mobile devices.
- **Voice Output:** Provide audio translations for recognized gestures.

---

## Contributing

Contributions are welcome! To contribute:

1. Fork the repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

---

## Contact

For questions or suggestions, contact:

- **Email:** jamshidbekollanazarov@outlook.com
- **GitHub:** [My-name-is-Jamshidbek](https://github.com/My-name-is-Jamshidbek)

---

Enjoy using the **Sign Language Translator Web App**! 🌟
