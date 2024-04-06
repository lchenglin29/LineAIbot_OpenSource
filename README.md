# LINE AI聊天機器人
本文使用Python的requests模組向**Gemini**的API發送請求，以建成AI聊天機器人
* 功能
  * 讀取文字：使用`Gemini pro`
  * 讀取圖片：使用`Gemini pro vision`
* 缺點
  * 因為LINE一次傳送只能傳送一則訊息，所以無法對傳送出去的圖片做描述
* 參考
  * [LINE BOT 教學( Python ) - STEAM 教育學習網](https://steam.oxxostudio.tw/category/python/example/line-bot.html)
  * [Google Gemini 系列模型：最新LLM 模型的技術剖析與實作介紹](https://blog.infuseai.io/google-gemini-model-intro-a302d6ae87c3)
  * [Google官方說明文件](https://ai.google.dev/docs?hl=zh-tw)

以下將簡單介紹取得程式中引用之token的方法
## 第一步：Google AI Studio
> ⚠️本文撰寫時(2024/4/6)Gemini的API還是免費的，因為我沒有填任何付款資訊。未來若有變動應參考Google官方之說明！

前往[Google AI Studio](https://aistudio.google.com/)
在左側的選單中，點選第一個選項`get API key`
接著按`Create API key`，就會得到一組API key了
在程式中對應的就是
```py
gemini_api_key = os.environ['api_key']
```
你可以將`os.environ['api_key']`替換為你剛才取得的token，或者如果你會設置環境變數也行

## 第二步：Line官方帳號
