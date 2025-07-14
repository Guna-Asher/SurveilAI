## 🧠 SurveilAI 

SurveilAI is a real-time object detection dashboard built using **Flask** and **YOLOv8n**, designed to monitor objects through image uploads or live camera feeds. With a modern TailwindCSS interface and seamless model integration, this project showcases practical AI deployment for smart surveillance.

Developed as part of the MCA capstone Project at **DSCE Bengaluru**.

---

### 📸 Core Features

- 🖼️ **Image Detection**: Upload photos and run object detection using YOLOv8n.
- 📷 **Live Camera Detection**: Switch between laptop webcam or IP camera for real-time analysis.
- 🧠 **Model Explorer**: Explore capabilities of YOLOv8n and SSD with visual insights.
- 🎨 **Dashboard UI**: Sleek TailwindCSS frontend with intuitive layout and transitions.

---

### 🛠 Tech Stack

| Layer          | Technologies Used                        |
|----------------|------------------------------------------|
| Backend        | Python, Flask                            |
| Model          | YOLOv8n (Ultralytics)                     |
| Computer Vision| OpenCV, NumPy, Pillow                    |
| Frontend       | HTML, TailwindCSS, JavaScript            |
| Deployment     | Localhost / Cloud platforms (e.g. Heroku)|

---

### 🚀 Setup Instructions

#### 1. Clone the Repo

```bash
git clone https://github.com/Guna-Asher/surveilai.git
cd surveilai
```

#### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4. Launch the App

```bash
python app.py
```

Then open your browser at: `http://127.0.0.1:5000/`

---

### 🖼️ Detection Options

#### ✅ Image Upload
- Navigate to **Image Detection**
- Select any image and click **Detect from Image**
- Visual results will be displayed in the preview pane

#### 📡 Camera Feed
- Choose between **Laptop** or **IP Camera**
- Click **Start Selected Camera Feed** to view detection
- Make sure your IP stream is live if using IP option

Update `ip_url` in `app.py`:

```python
ip_url = "http://<your-ip>:<port>/video"
```

You can use the **IP Webcam** Android app for local streaming.

---

### 🧪 File Structure

```
surveilai/
│
├── app.py                 # Flask server + detection logic
├── templates/
│   └── index.html         # TailwindCSS-powered dashboard
├── static/                # Optional frontend assets
├── requirements.txt       # Python dependencies
└── README.md              # Full project documentation
```
---

### 📚 Resources

- [YOLOv8n Documentation](https://docs.ultralytics.com/)
- [Flask Docs](https://flask.palletsprojects.com/)
- [TailwindCSS Docs](https://tailwindcss.com/docs)

---
