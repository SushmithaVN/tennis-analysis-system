# 🎾 Tennis Analysis System

A computer vision–based tennis analytics system that automatically detects players, tracks the tennis ball, estimates court geometry, and computes player movement speed and ball shot speed from match videos.

This project demonstrates end-to-end sports video analysis using deep learning, geometric reasoning, and real-world measurements.

---

# 📽️ Output Demo

![Tennis Analysis System Demo](output_videos/demo_preview.gif)

*Above: Preview showing player tracking, ball detection, and speed analytics*  
[📥 Download full output video](output_videos/output_video2.mp4)

---

## 🚀 Project Overview

The Tennis Analysis System performs the following tasks:

- Detects **players** and the **tennis ball** using YOLOv8  
- Tracks players consistently across frames
- Detects **court keypoints** using a ResNet-50–based regression model
- Projects player and ball positions onto a **mini-court** with real tennis dimensions
- Computes:
  - Ball shot speed (km/h)
  - Player movement speed (km/h)
- Overlays analytics and statistics directly on the video

---

## 🧠 Key Concepts Used

- Object Detection & Tracking (YOLOv8, anchor-free)
- Keypoint Regression (ResNet-50)
- Camera-to-world scaling using known court dimensions
- Feature pyramid–based multi-scale detection
- Interpolation for missing detections
- Pixel-to-meter conversion for real-world speed estimation

