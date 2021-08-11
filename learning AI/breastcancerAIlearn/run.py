import pandas as pd
from sklearn.model_selection import train_test_split
import tensorflow as tf


dataset = pd.read_csv('cancer.csv')


x = dataset.drop(columns=['diagnosis(1=m, 0=b)'])
y = dataset['diagnosis(1=m, 0=b)']


x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)


model = tf.keras.models.load_model("breastcancerai.h5")



evaled = model.evaluate(x_test, y_test)