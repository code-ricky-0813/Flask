#Flask 留言板 + RESTful API 專案

這是一個使用 Flask 製作的簡易留言板應用程式，支援表單送出留言、顯示所有留言，並提供 RESTful API 接口，可從 `/api/messages` 取得所有留言資料（JSON 格式）。

## 專案功能
- 使用者可透過表單送出「名字」與「留言」
- 所有留言依時間倒序顯示於頁面下方
- 提供 RESTful API：
  - `GET /api/messages`：取得所有留言（JSON）

## 使用技術
- Python 3
- Flask
- Flask-WTF（表單與驗證）
- Flask-Bootstrap（簡易前端樣式）
- Flask-SQLAlchemy（SQLite 資料庫）
- RESTful API (JSON 輸出)

## 專案結構
flask_final_app/
├── venv/
├── app.py
├── forms.py
├── templates/
│   └── index.html
├── instance/
│   └── message.db

## PythonAnywhere 網址
https://rickycode2.pythonanywhere.com/

## RESTful API
你可以透過以下網址取得所有留言的 JSON 資料：https://rickycode2.pythonanywhere.com/api/messages
這是一個簡單的 GET API，回傳的內容為：[{"id": 1, "name": "測試", "message": "0-0", "timestamp": "2025-06-18 22:47:02"}]
