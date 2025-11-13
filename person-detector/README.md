# CogniPixel

![Demo](images/pic_x1.png)

A lightweight, serverless person detection tool running entirely in your browser using TensorFlow.js. Identifies multiple people and highlights the main subject.

---

## 中文說明

### 專案簡介

這是一個完全在使用者瀏覽器中運行的輕量級 AI 人物偵測工具。它不需要任何後端伺服器，只需一個 `index.html` 檔案即可運作。

此專案的核心功能是利用 [TensorFlow.js](https://www.tensorflow.org/js) 和預訓練的 COCO-SSD 模型，對使用者上傳的圖片進行即時分析，標示出圖片中的所有人物，並特別高亮顯示視覺上最主要（距離最近，即邊界框面積最大）的人物。

這個專案可以作為一個有趣的範例，展示如何賦予 AI 或其他自動化程式一雙簡單的「眼睛」，讓它們能夠感知環境中是否有人，並作出相應的互動，例如在偵測到人時觸發一個打招呼的動作。

### 功能特色

*   **純客戶端運行：** 無需伺服器，保護使用者隱私。
*   **單檔案部署：** 所有程式碼都在一個 `index.html` 檔案中，極其輕便。
*   **多人物偵測：** 可同時識別並框出圖片中的多個人物。
*   **主要人物高亮：** 自動計算並高亮標示畫面中最主要的人物。
*   **支援拖放與點擊上傳：** 提供友善的使用者體驗。

### 如何使用

這個專案的使用方法非常簡單：

1.  下載專案中的 `index.html` 檔案。
2.  直接在您的網頁瀏覽器（如 Chrome, Firefox, Edge）中打開這個檔案。
3.  點擊「選擇圖片」按鈕或將圖片拖放到指定區域即可開始偵測。

### 核心程式碼範例 (最低運作範例)

整個 `index.html` 本身就是一個完整的可運作範例。其核心邏輯圍繞著載入模型和執行偵測兩個部分。

**1. 載入 AI 模型:**
```javascript
// 透過 CDN 引入函式庫
// <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@latest/dist/tf.min.js"></script>
// <script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/coco-ssd@latest/dist/coco-ssd.min.js"></script>

// 在你的程式碼中載入模型
const model = await cocoSsd.load();
```

**2. 偵測圖片中的物件:**
```javascript
// `imageElement` 可以是一個 <img>, <video>, 或 <canvas> 元素
const predictions = await model.detect(imageElement);

// `predictions` 將會是一個包含偵測結果的陣列
// [{
//   bbox: [x, y, width, height],
//   class: "person",
//   score: 0.89
// }, ...]
```

---

## English

### Introduction

This is a lightweight AI person detection tool that runs entirely in the user's browser. It requires no backend server and works with a single `index.html` file.

The core function of this project is to use [TensorFlow.js](https://www.tensorflow.org/js) and the pre-trained COCO-SSD model to perform real-time analysis on user-uploaded images. It identifies all individuals in the image, draws bounding boxes around them, and specifically highlights the main person (visually closest, i.e., the one with the largest bounding box area).

This project serves as an interesting example of how to give an AI or other automated programs a simple pair of "eyes," enabling them to perceive if a person is present and react accordingly, such as triggering a greeting action upon detection.

### Features

*   **Purely Client-Side:** No server required, ensuring user privacy.
*   **Single-File Deployment:** All code is contained within a single `index.html` file, making it extremely portable.
*   **Multi-Person Detection:** Capable of identifying and boxing multiple people in an image simultaneously.
*   **Main Person Highlight:** Automatically calculates and highlights the most prominent person in the frame.
*   **Drag-and-Drop & Click-to-Upload:** Provides a user-friendly experience.

### How to Use

Using this project is incredibly simple:

1.  Download the `index.html` file from this repository.
2.  Open the file directly in your web browser (e.g., Chrome, Firefox, Edge).
3.  Click the "Select Image" button or drag and drop an image onto the designated area to start detection.

### Core Code Example (Minimum Working Example)

The entire `index.html` file is a complete working example in itself. Its core logic revolves around loading the model and performing detection.

**1. Load the AI Model:**
```javascript
// Include the libraries via CDN
// <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@latest/dist/tf.min.js"></script>
// <script src="https://cdn.jsdelivr.net/npm/@tensorflow-models/coco-ssd@latest/dist/coco-ssd.min.js"></script>

// Load the model in your code
const model = await cocoSsd.load();
```

**2. Detect Objects in an Image:**
```javascript
// `imageElement` can be an <img>, <video>, or <canvas> element
const predictions = await model.detect(imageElement);

// `predictions` will be an array of detected objects
// [{
//   bbox: [x, y, width, height],
//   class: "person",
//   score: 0.89
// }, ...]
```
