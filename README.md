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

## 第二步：Line官方帳號之創建與取得Token
> 我僅簡單介紹，詳細可參考[此文](https://steam.oxxostudio.tw/category/python/example/line-developer.html)，原作者寫得很清楚

### 一、進入Line Developer
網址在這 -> [連結](https://developers.line.biz/zh-hant/)
### 二、建立一個Provider
在左側選單中點選`provider`接著Create一個Provider
> 如果你寫過Discord bot的話Provider應該就類似一個**Application**

### 三、建立一個Channel 
在剛剛的Provider中Create一個Channel，記得選擇`Messaging API`
![Messaging API](https://scontent.frmq2-2.fna.fbcdn.net/v/t1.15752-9/433994174_1817362718729995_6580314643434535918_n.jpg?_nc_cat=100&ccb=1-7&_nc_sid=5f2048&_nc_ohc=7-ipoQoiP0kAb5H8cpX&_nc_ht=scontent.frmq2-2.fna&oh=03_AdV420sI2E3sfRHaeb4ryS09ZkZ9BGvrlej1OqEdu7BJYw&oe=6638402D)
接著填好必要的資訊，就建立完成了！
### 四、Channel secret與Channel access token
建立好Channel之後你會進到他的Bassic Settings
![Basic settings](https://scontent-tpe1-1.xx.fbcdn.net/v/t1.15752-9/421071721_1171088150541307_8879639398150892167_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=5f2048&_nc_ohc=_e7g2rFHPzgAb4xg4GJ&_nc_ht=scontent-tpe1-1.xx&oh=03_AdUcFHYSFTNR0zSyfU126cWodzIc7fsJ2rfVcunJavynTA&oe=663821ED)
往下滑就會看到`Channel secret了`
至於`Channel access token`要到隔壁的`Messaging API`取得
