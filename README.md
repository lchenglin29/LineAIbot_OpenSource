# 開源LINE機器人
本文使用Python的requests模組向Gemini的API發送請求
* 功能
  * 讀取文字：使用`Gemini pro`
  * 讀取圖片：使用`Gemini pro vision`
* 缺點
  * 因為LINE一次傳送只能傳送一則訊息，所以無法對傳送出去的圖片做描述

以下將簡單介紹取得Gemini api token的方法
## 第一步：Google AI Studio
前往[Google AI Studio](https://aistudio.google.com/)
