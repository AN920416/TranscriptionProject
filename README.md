# TranscriptionProject
Final project for Spring 2022 Programming(ECON 1024)  
組員：經濟一 汪晁安、張程翔、耿睿棋
## 目標：
1. 輸入音訊，輸出樂譜與節拍，有多種濾鏡與表現方式(CQT, onset, Chroma_stft)，可做為轉譜基礎，也可用於走音偵測。
2. 輸入語音，輸出語音高低起伏，可用於分析人聲組成。
## 使用方式：
首先執行 PackageInstall.py 安裝所需套件  
再執行 Transcription.py(如出現套件未安裝的錯誤需重複上一步驟數次)  
  
Open：開啟音訊檔案，提供三個檔案作為範例，支援.mp3 與 .wav。  
Analyze：輸出轉換後的圖表。  
CQT / onset / Chroma stft：切換三種不同的表現方式。  
tempo：切換自動節奏顯示。  
binary mask：切換黑白濾鏡，去除不顯著的區域。  
## 分工：
張程翔：概念發想和音樂理論研究  
汪晁安：Librosa 分析與實作  
耿睿棋：GUI 實作  

## Demo video
https://www.youtube.com/watch?v=eD8Wcn2b8cs
## Demo Screenshot
更詳細的展示內容請見 Presentation.pdf  
![2024-03-31 02 41 26  ](https://github.com/AN920416/TranscriptionProject/assets/127752256/c414d94d-27a8-43d2-a806-1a17e5e19495 ){: width="50%"}
![2024-03-31 02 42 51  ](https://github.com/AN920416/TranscriptionProject/assets/127752256/b5602b28-e0ca-4b83-b28d-d49a81e29716 ){: width="50%"}
![2024-03-31 02 43 30  ](https://github.com/AN920416/TranscriptionProject/assets/127752256/8f236ed2-6f92-4dfa-a3ea-f30e19349d24 ){: width="50%"}
