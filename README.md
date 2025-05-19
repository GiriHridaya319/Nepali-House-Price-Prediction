# 🏠 Nepali Housing Price Prediction

This project uses machine learning models to predict housing prices in Nepal based on various features such as area, location, number of bedrooms, and more. The goal is to help users estimate property prices using historical data and real-time inputs through a simple web interface.

## 🔧 Tech Stack

- **Programming Language:** Python  
- **Libraries & Tools:** Pandas, Random Forest, Linear Regression, Streamlit  

## 📌 Features

- Cleaned and preprocessed a real-world Nepali housing dataset  
- Trained two machine learning models:
  - Random Forest Regressor
  - Linear Regression  
- Developed a user-friendly **Streamlit web application** for real-time price prediction  
- Visualized trends and relationships between features and prices  

## 🚀 How to Run

1. **Clone the repository:**
   ```bash
   git clone https://github.com/GiriHridaya319/Nepali-Housing-Price-Prediction.git
   cd Nepali-Housing-Price-Prediction
````

2. **Install required packages:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app:**

   ```bash
   streamlit run app.py
   ```

## 📊 Sample Input Features

* House area (sq. ft)
* Number of bedrooms
* Location (encoded)
* Age of the house
* Distance from main road

## 🖼️ Screenshot

*(Include a screenshot of the Streamlit app here if available)*

## 📁 Project Structure

```
Nepali-Housing-Price-Prediction/
│
├── app.py                 # Streamlit application
├── model_rf.pkl           # Trained Random Forest model
├── model_lr.pkl           # Trained Linear Regression model
├── data/                  # Dataset files
├── utils.py               # Helper functions
├── requirements.txt       # List of dependencies
└── README.md              # Project documentation
```

## 📈 Future Improvements

* Add more features like house orientation, amenities, etc.
* Include price trends by district or city zone
* Deploy on a cloud platform (e.g., Streamlit Cloud or Heroku)

## 🤝 Contributions

Feel free to fork the repo and open a pull request to improve the app or models.

## 📬 Contact

Created by [Hridaya Giri](https://github.com/GiriHridaya319) – feel free to reach out!
