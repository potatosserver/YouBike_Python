# 高雄 YouBike 站點搜尋
**一個簡單的YouBike站點搜尋器**

---

**簡介**

此專案為一個簡單的網頁應用程式，提供使用者可以搜尋高雄市的 YouBike 站點資訊，並查看各站點的車輛狀況。

使用者可以透過輸入站點名稱或定位，快速查詢 YouBike 2.0 站點的資訊，包括：
* 站點名稱
* 距離
* 地區
* 地址
* YouBike 2.0 數量
* YouBike 2.0E 數量
* 可停空位數

**其他功能**
* 附件站點
* Google 地圖跳轉
* PWA 應用程式安裝
* 定位開關
* 黑暗模式
* 自動定時更新

## 使用方式

1. 請前往 [potatosserver.github.io/YouBike](https://potatosserver.github.io/YouBike/) 即可使用本服務。
2.在搜尋框輸入關鍵字查詢
3. 可開啟定位啟用最近站點與距離計算。
4. 點擊卡片可開啟站點的Google地圖。
5. 可使用卡片右上角的星星釘選車站
6. 點擊右下角的按鈕，切換色彩模式及安裝PWA應用程式

## 備註

1. PWA(Progressive Web App)是指一種網頁應用程式的設計理念，旨在提供類似原生應用程式的使用體驗。PWA可以在各種設備上運行，包括桌面和移動設備，並且可以離線使用。PWA的特點包括快速加載、可靠性和可安裝性。PWA的目標是讓網頁應用程式像原生應用程式一樣流暢和易於使用。
2. 建議使用Chrome、Microsoft Edge 等瀏覽器，其他瀏覽器對於PWA的支援較差，可能會導致安裝失敗或無法正常運行。
3. 目前僅支援高雄市的YouBike站點資訊，未來可能會擴展到其他城市的YouBike資訊。

## 資料來源

- [資料來自高雄市資料開放平台API](https://api.kcg.gov.tw/ServiceList/Detail/b4dd9c40-9027-4125-8666-06bef1756092)
-  [YouBike 官網](https://www.youbike.com.tw)

## 版權與聲明

本專案皆可自由共享與修改。  
本專案不可用於盈利。  
本工具不屬於高雄市政府及 YouBike 公司

## 已知錯誤

* 暫無

## 貢獻

歡迎對本專案感興趣的開發者一起參與貢獻！您可以透過 GitHub 提交 Pull Request 來改善程式碼、新增功能或修復錯誤.

## 貢獻者

* [AndrewCho0531](https://github.com/AndrewCho0531):邏輯編寫、UI設計
* [KEVIN970712](https://github.com/KEVIN970712):題材發想、錯誤修正

## 補充

1. 在修改程式時，請注意YouBike 官方API的請求時間間隔，避免大量請求造成IP封鎖
2. 複製儲存庫後記得更改部分資料，避免造成PWA應用安裝失敗 
