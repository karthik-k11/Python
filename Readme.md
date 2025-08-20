# 💤 Drowsiness Detection System

The **Drowsiness Detection System** is an AI-powered computer vision project that helps prevent accidents caused by driver fatigue. It uses **OpenCV**, **Dlib**, and **Machine Learning** techniques to monitor eye movements and alert the user when signs of drowsiness are detected.

## 🚀 Features
- Real-time face and eye detection using OpenCV.
- Eye Aspect Ratio (EAR) calculation to detect eye closure.
- Alerts the user when drowsiness is detected.
- Lightweight and works on standard webcams.
- Can be extended for vehicle safety systems.

## 🛠️ Technologies Used
- Python  
- OpenCV  
- Dlib  
- Imutils  
- Numpy  

## 👁️ How EAR Formula Detects Drowsiness

To detect whether eyes are open or closed, we measure the **Eye Aspect Ratio (EAR)** calculated from 6 facial landmark points around each eye.

> When eyes close → vertical distances shrink → EAR value drops below threshold.

## 📐 EAR Formula

$$
EAR = \frac{ \lVert p_2 - p_6 \rVert + \lVert p_3 - p_5 \rVert }{ 2 \times \lVert p_1 - p_4 \rVert }
$$

**Where:**
- \(p_1 ... p_6\) are 6 eye landmark points  
- \(\lVert p_i - p_j \rVert\) is Euclidean distance  
- If **EAR < 0.25** for **N consecutive frames** → drowsiness alert is triggered


---

## 📌 Project Highlights
- Detects driver drowsiness by monitoring eye blink patterns.  
- Provides real-time feedback with alarms.  
- Helps improve road safety.  

## 📂 Future Enhancements
- Add yawning detection for more accurate monitoring.  
- Integrate with IoT devices for automatic vehicle control.  
- Develop a mobile application version.  

---
👨‍💻 Developed by **Karthik K**
