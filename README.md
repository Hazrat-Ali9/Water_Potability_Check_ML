# Hazrat Ali 

# Software Engineer || CEO and Founder HMSofttecH Innovation 

# Water Potability Check (ML)

This project predicts the **potability of water** using machine learning models.  
After experimenting with multiple algorithms (Logistic Regression, Random Forest, Gradient Boosting, KNN, etc.), the final selected model was chosen based on accuracy, precision/recall, and overall robustness.

---

## 📊 Dataset
- Source: [Kaggle - Water Quality Dataset](https://www.kaggle.com/datasets/adityakadiwal/water-potability)  
- Features include:
  - pH
  - Hardness
  - Solids
  - Chloramines
  - Sulfate
  - Conductivity
  - Organic Carbon
  - Trihalomethanes
  - Turbidity
- Target: **Potability** (0 = Not Potable, 1 = Potable)

---

## ⚙️ Workflow
1. **Data Preprocessing**
   - Handling missing values
   - Normalization/standardization
   - Train-test split

2. **Model Selection**
   - Tested multiple models:
     - Logistic Regression With Plolynominal Feature Engineering
     - Logistic Regression Without Plolynominal Feature Engineering
     - Random Forest
     - Gradient Boosting
     - KNN
   - Compared performance using metrics: Accuracy, Precision, Recall, F1-score

3. **Final Model**
   - Selected model: **[Logistic Regression With Plolynominal Feature Engineering]**
   - Achieved best balance between accuracy and generalization.

---

## 🚀 Colab Testing Phase
Colab link: 
[Colab Test  Phase - Water Quality Dataset](https://colab.research.google.com/drive/1LffJ4bIOBPo2nMxOoVXfuNJNvgS5HNgz?usp=sharing) 
