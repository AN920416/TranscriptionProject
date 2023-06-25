# TranscriptionProject
Final project for Spring 2022 Programming(ECON 1024)  
組員：經濟一 汪晁安、張程翔、耿睿棋
## 目標：
1. 輸入音訊，輸出樂譜與節拍，有多種濾鏡與表現方式(CQT, onset, Chroma_stft)，可做為轉譜基礎，也可用於走音偵測。
2. 輸入語音，輸出語音高低起伏，可用於分析人聲組成。
## 使用方式：
執行 PackageInstall.py 安裝所需套件  
執行 Transcription.py  
  
Open：開啟音訊檔案，提供三個檔案作為範例，支援.mp3 與 .wav。  
Analyze：輸出轉換後的圖表。  
CQT / onset / Chroma stft：切換三種不同的表現方式。  
tempo：切換自動節奏顯示。  
binary mask：切換黑白濾鏡，去除不顯著的區域。  
## 分工：
張程翔：概念發想和音樂理論研究  
汪晁安：Librosa 分析與實作  
耿睿棋：GUI 實作  
