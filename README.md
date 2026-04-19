# Heart Disease Risk Prediction System

ML-based web application for predicting cardiovascular disease risk.

## Features
- User authentication (Admin & Normal users)
- CSV/Excel file upload for batch prediction
- Machine learning risk classification
- Interactive charts and visualizations
- Excel and PDF report generation
- User profile management
- Activity logging and audit trail

## Tech Stack
- Django 5.0
- Scikit-learn
- Pandas, NumPy
- SQLite3
- Chart.js
- ReportLab, OpenPyXL

## Installation
```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
