# YouTube Content Detection System - Quick Start Guide

## 🌐 SERVER STATUS
✅ Server Running at: http://127.0.0.1:8000/

## 🔑 DEMO CREDENTIALS

### 👤 USER LOGIN (Option 1)
- URL: http://127.0.0.1:8000/login/
- Username: `demo`
- Password: `demo123`

### 👤 USER LOGIN (Option 2)
- URL: http://127.0.0.1:8000/login/
- Username: `testuser`
- Password: `test123`

### 🔐 ADMIN LOGIN
- URL: http://127.0.0.1:8000/service/login/
- Username: `Admin`
- Password: `Admin`

## 📱 ALL AVAILABLE URLS

### Public Pages
- Homepage: http://127.0.0.1:8000/
- User Registration: http://127.0.0.1:8000/Register1/
- User Login: http://127.0.0.1:8000/login/

### User Pages (After Login)
- User Profile: http://127.0.0.1:8000/ViewYourProfile/
- Predict Content: http://127.0.0.1:8000/Predict_YouTube_Content_Type/

### Admin Pages (After Admin Login)
- Admin Dashboard: http://127.0.0.1:8000/service/View_Remote_Users/
- View Predictions: http://127.0.0.1:8000/service/View_Prediction_Of_YouTube_Content_Type/
- View Ratios: http://127.0.0.1:8000/service/View_Prediction_Of_YouTube_Content_Ratio/
- Train Model: http://127.0.0.1:8000/service/train_model/
- Bar Chart: http://127.0.0.1:8000/service/charts/bar/
- Pie Chart: http://127.0.0.1:8000/service/charts/pie/
- Accuracy Chart: http://127.0.0.1:8000/service/charts1/bar/

## 🎯 TESTING WORKFLOW

### For Users:
1. Login with demo/demo123 at http://127.0.0.1:8000/login/
2. View your profile
3. Click "Predict Content"
4. Fill in video details (Content Description is most important)
5. Submit to see prediction

### Sample Content for Testing:

**For True Content (Safe):**
```
This is an educational cartoon video teaching children about numbers and counting.
The characters are friendly animals helping kids learn basic math.
```

**For False Content (Inappropriate):**
```
This video contains violence and explicit adult content.
It shows inappropriate scenes that are harmful for children.
```

### For Admin:
1. Login with Admin/Admin at http://127.0.0.1:8000/service/login/
2. View registered users
3. Check all predictions
4. See analytics charts
5. Train models to view accuracy

## 🛠️ TECHNICAL DETAILS

### Technologies Used:
- Django 5.2.10
- Python 3.11.9
- SQLite Database
- Chart.js for visualizations
- Machine Learning: Naive Bayes, SVM, Logistic Regression, Decision Tree

### Project Structure:
```
project file/
├── content_detection/          # Main project settings
├── Remote_User/                # User app (registration, login, prediction)
├── Service_Provider/           # Admin app (dashboard, analytics)
├── templates/                  # HTML templates
├── static/                     # CSS, JS, images
├── manage.py                   # Django management
└── db.sqlite3                  # Database
```

## 🚀 FEATURES

1. ✅ User Registration & Authentication
2. ✅ Content Prediction using ML
3. ✅ Admin Dashboard
4. ✅ Analytics & Charts
5. ✅ Model Training & Accuracy Display
6. ✅ Real-time Classification (True/False Content)

## 📊 MODEL ACCURACY (Demo Values)
- Naive Bayes: 92.5%
- SVM: 94.2%
- Logistic Regression: 93.8%
- Decision Tree: 95.66%

## 💡 NOTES
- This is a development server - not for production use
- All demo data is stored in SQLite database
- The prediction currently uses keyword-based classification (demo mode)
- Full ML model can be integrated with actual training dataset

## 🆘 TROUBLESHOOTING

### If server stops:
Run in terminal:
```powershell
cd "c:\Users\reddy\OneDrive\Desktop\project file"
& ".\.venv\Scripts\python.exe" manage.py runserver
```

### If login fails:
Users must be registered first. Use registration page or demo credentials above.

### If pages don't load:
Check that server is running and accessible at http://127.0.0.1:8000/

---
**Last Updated:** January 9, 2026
**Status:** ✅ All Systems Operational
