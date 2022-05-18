from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import mean_squared_error
import pandas as pd
import numpy as np

def predictor(gender, country, bmi):
    temp = pd.read_csv("RegressionData.csv")
    
    temp_0 = temp[temp.Gender == "Population, " + gender.lower()]

    enc = OneHotEncoder(handle_unknown = "ignore")
    X = np.array(temp_0.get(["country"]))
    enc.fit(X)

    df_X = pd.DataFrame(enc.transform(X).toarray(), columns = enc.get_feature_names())
    df_Y = pd.DataFrame(temp_0["LifeExpectancy"])

    BMI = np.array(temp_0["BMI"]).reshape(len(temp_0), 1)
    scaler = StandardScaler().fit(BMI)
    BMI_scaled = scaler.transform(BMI)
    df_X["BMI"] = BMI_scaled

    reg2 = LinearRegression().fit(np.array(df_X), np.array(df_Y))
    
    input0 = enc.transform([[country]]).toarray()
    scaled_BMI_input = scaler.transform([[bmi]])
    input0 = np.append(input0, scaled_BMI_input[0]).reshape(1, len(df_X.columns))
    pred = reg2.predict(input0)[0][0]
    
    return pred