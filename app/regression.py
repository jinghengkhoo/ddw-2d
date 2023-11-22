import numpy as np
import pandas as pd

def normalize_z(dfin, columns_means, columns_stds):
    dfout = (dfin - columns_means) / columns_stds
    return dfout, columns_means, columns_stds

def calc_linreg(X, beta):
    return np.matmul(X, beta)

def prepare_feature(df_features):
    cols = df_features.shape[1]  # get # features in case we have more than 1
    if type(df_features) == pd.DataFrame:
        np_feature = df_features.to_numpy()
    else:
        np_feature = df_features
    feature = np_feature.reshape(
        -1, cols
    )
    features = np.concatenate((np.ones((feature.shape[0], 1)), feature), axis=1)

    return features

def predict_linreg(df_feature, beta, means, stds):
    norm_data, _, _ = normalize_z(df_feature, means, stds)
    X = prepare_feature(norm_data)
    return calc_linreg(X, beta)

def wheat_pred(form):
    """

    Receives wtform inputs and returns regression model prediction

    """
    beta = np.array([[49500.02806428],
                     [60813.82235847],
                     [-5362.27106089],
                     [19977.37662043],
                     [-3262.71694991],
                     [-5432.05368039],
                     [479.66604884]])

    means = pd.DataFrame({
        'Area': [1299.396491],
        'longitude': [-95.461092],
        'latitude': [39.429363],
        'Heating Degree Days (Jun - October)': [468.010526],
        'Temperature_Difference': [24.168421],
        'Average Temperature (Jun - October)': [68.138947]
    })

    stds = pd.DataFrame({
        'Area': [1973.491332],
        'longitude': [13.918517],
        'latitude': [4.478070],
        'Heating Degree Days (Jun - October)': [361.819429],
        'Temperature_Difference': [3.663906],
        'Average Temperature (Jun - October)': [5.944342]
    })

    df_features = pd.DataFrame({
        'Area': [form.area.data],
        'longitude': [form.lon.data],
        'latitude': [form.lat.data],
        'Heating Degree Days (Jun - October)': [form.hdd.data],
        'Temperature_Difference': [form.tdiff.data],
        'Average Temperature (Jun - October)': [form.tavg.data]
    })

    return round(predict_linreg(df_features, beta, means=means, stds=stds)[0][0], 3)