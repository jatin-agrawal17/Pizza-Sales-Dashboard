
# 🍕 Pizza Sales Dashboard

---

🚀 This project demonstrates a complete pipeline from **CSV to MySQL**, followed by visualization using **Tableau**.
📊 It uses `pizza_sales.csv` as the primary dataset and creates dashboards to analyze pizza sales trends.
🧭 Builds **navigator-style dashboards** that allow seamless navigation between views for better insights.
🎨 Tableau dashboards use **pizza-themed backgrounds and icons** for an engaging visual experience.


## 🚀 Live Demo

🔗 [Pizza Sales Dashboard on Tableau Public](https://public.tableau.com/app/profile/jatin.agrawal4143/viz/PizzaSalesAnalysis_17517039475160/Home)

## 🧠 Features

- Loads pizza sales data into **MySQL** using **pandas**, **mysql-connector**, and **SQLAlchemy**
- Two professional Tableau dashboards with pizza-themed backgrounds and icons
- All dashboard logic and queries documented clearly for learning and reuse

---

## 📊 Tableau Dashboards Overview

### 🔹 **1. Home Dashboard**
Provides an overview of key performance metrics and trends:
- **KPIs** like Total Revenue, Total Pizzas Sold, and Total Orders
- **Charts** showing:
  - Hourly sales trend
  - Weekly sales trend
  - Pizza sales by size
  - Pizza sales by category

### 🔹 **2. Best & Worst Seller Dashboard**
Highlights the top and bottom performers:
- **Top 5** and **Bottom 5** pizzas by:
  - Revenue
  - Number of pizzas sold
  - Total number of orders

Both dashboards use custom backgrounds (`Pizza Tableau 1.jpg`, `Pizza Tableau 2.jpg`) and pizza-themed icons from the `Pizza Sales Images/` folder for a visually appealing interface.

---

## 📊 SQL Logic for Dashboard

All SQL queries used to power the dashboard — including KPIs and chart data — are written with answers in:

📝 **`SQL Queries.docx`**

Includes:
- Query explanations
- Actual SQL statements
- Sample outputs
- Mappings between SQL outputs and dashboard visuals

---

## 🛠️ Dependencies

Install the required packages with:

```bash
pip install -r requirements.txt
```

## 📂 Project Structure


📦 Pizza Sales Dashboard
│
├── pizza_sales.csv ← Raw data file
├── export_data.py ← Script to load CSV into MySQL
├── Pizza Tableau 1.jpg ← Background for Dashboard 1 (Home)
├── Pizza Tableau 2.jpg ← Background for Dashboard 2 (Best & Worst Seller)
├── Pizza Sales Images/ ← Folder containing pizza icon/image for dashboard icon
├── requirements.txt ← Python dependencies
├── SQL Queries.docx ← SQL logic used for dashboard KPIs and charts
└── README.md ← Project documentation

### 🔧 Prerequisites
- Make sure you have **Python 3.x** and **pip** installed on your system.
- Recommended to use a **virtual environment** (optional).
- Make sure you have **tableau desktop** or **tableau public** in your system

---

### ⬇️ Step-by-step Instructions

#### 1. Clone the Repository

```bash
https://github.com/jatin-agrawal17/Pizza-Sales-Dashboard.git 
cd Pizza-Sales-Dashboard
```
#### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

## 📌 Note: This dashboard is hosted on Tableau Public.  
- For the best experience, please view it in Chrome or Edge.  
- Some features (like downloads or interactive tooltips) may be restricted by privacy-focused browsers like Brave by default.


## 📊 Dataset Used

[Pizza Sales Data](https://github.com/jatin-agrawal17/Pizza-Sales-Dashboard/blob/main/pizza_sales.csv)
## 📌 Limitations

The app uses a preloaded dataset and does not fetch live or real-time property listings or prices.
## 🙌 Acknowledgements

📚 Gained practical experience in SQL data modeling, database integration, and dashboard KPIs

🖥️ Inspired by real-world BI dashboard use-cases and best practices in data storytelling

🙏 Special thanks to MySQL and Tableau for enabling seamless data handling and rich visualizations


## 👤 Author

Jatin Agrawal  
📬 [LinkedIn](https://www.linkedin.com/in/jatin-agrawal-b80092367/)

## 📎 License

This project is open-source and available under the MIT License.
