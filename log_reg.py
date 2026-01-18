import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import RobustScaler, PolynomialFeatures
from sklearn.impute import SimpleImputer
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

from sklearn.linear_model import LogisticRegression

df = pd.read_csv('water_potability.csv')

target_col = 'Potability'
X = df.drop(target_col,axis=1)
y = df[target_col]

numerical_col = X.select_dtypes(include=np.number).columns

numeric_transformer_poly = Pipeline(steps=[
    ("imputer", SimpleImputer(strategy="mean")),
    ("poly", PolynomialFeatures(degree=2, include_bias=False)),
    ("scaler", RobustScaler()),
])

preprocessor_poly = ColumnTransformer( transformers=[("num", numeric_transformer_poly, numerical_col)] )

# Logistic Regression pipeline
# classifier__C': 10, 'classifier__max_iter': 1000, 'classifier__penalty': 'l2', 'classifier__solver': 'saga'
log_reg_pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor_poly),
    ("classifier", LogisticRegression(C=10, max_iter=1000,penalty='l2',solver='saga'))
])

X_test, X_train, y_test, y_train = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

log_reg_pipeline.fit(X_train, y_train)

import pickle
filename = 'model.pkl'
pickle.dump(log_reg_pipeline, open(filename, 'wb'))


