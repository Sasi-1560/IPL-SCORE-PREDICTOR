# IPL Score Predictor
This Streamlit webapp enables user to predict total runs between teams using current runs and wickets.
## Libraries Used

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.neighbors import KNeighborsRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.tree import DecisionTreeRegressor
from sklearn.svm import SVR
import xgboost as xgb
import optuna
import pickle

---

## Algorithms Implemented

1. Linear Regression
2. K-Nearest Neighbors Regressor (KNN)
3. XGBoost Regressor
4. Random Forest Regressor
5. Decision Tree Regressor
6. Support Vector Regressor (SVR)
**Hyperparamter Optimization:**

Used optuna for paramter optimization.

**Dataset:**

The dataset comprises of over by over details of matches and runs from 2008 to 2025.

Dataset Used: ipl_data.csv

* mid - match id
* date - when matches are played
* venue - place where matches aew played
* bat_team - batting team
* bowl_team - bowling team
* batsman - batsman
* bowler - bowler
* runs - runs scored
* wickets - wickets
* overs - overs - next 3 are based on this
* run_last_5 - runs scored in last 5 overs
* wicket_last_5 - wickets in last 5 overs
* stricker - batsman playing as main 1
* non-striker - batsman playing as runner up - not main 0
* total - total score (target variable)

Used streamlit web frame work
