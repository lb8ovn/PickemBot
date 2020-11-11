import tensorflow as tf
import pandas as pd
from sklearn.model_selection import train_test_split

#First we gotta find the data and prep it for the neural net
data = pd.read_csv('Whatever data we find')
normalized_columns = ['Columns']
data[normalized_columns] = data[normalized_columns].apply(lambda x: (x - x.min()) / (x.max() - x.min()))

#I don't know what this does yet but once the columns are normalized we turn them into tensors or whatever
feature = tf.feature_column.numeric_column('Feature Column')
feature_columns = ["""All the prepped tf.feature data"""]
#Ok we do the train test split here, dropping our targeted column and throwing all the features into x_data
x_data = data.drop('Target Column', axis=1)
labels = data['Target Column']
X_train, X_test, y_train, y_test = train_test_split(x_data,labels,test_size=0.33, random_state=101)
#I'm not sure what this does but the class I'm in included it so here it is
input_func = tf.estimator.inputs.pandas_input_fn(x=X_train,y=y_train,batch_size=10,num_epochs=1000,shuffle=True)
#Here's where we make the model
model = tf.estimator.LinearClassifier(feature_columns=feat_cols,n_classes=2)
model.train(input_fn=input_func,steps=1000)
#Model Evaluation
eval_input_func = tf.estimator.inputs.pandas_input_fn(
      x=X_test,
      y=y_test,
      batch_size=10,
      num_epochs=1,
      shuffle=False)
results = model.evaluate(eval_input_func)
results
#Prediction time!
pred_input_func = tf.estimator.inputs.pandas_input_fn(
      x=X_test,
      batch_size=10,
      num_epochs=1,
      shuffle=False)
predictions = model.predict(pred_input_func)
list(predictions)
#Here's a classifier thing. I'm not sure if we need to include this or not
dnn_model = tf.estimator.DNNClassifier(hidden_units=[10,10,10],feature_columns=feature_columns_cols,n_classes=2)
dnn_model.train(input_fn=input_func,steps=1000)
embedded_group_column = tf.feature_column.embedding_column(assigned_group, dimension=4)
input_func = tf.estimator.inputs.pandas_input_fn(x=X_train,y=y_train,batch_size=10,num_epochs=1000,shuffle=True)
dnn_model = tf.estimator.DNNClassifier(hidden_units=[10,10,10],feature_columns=feature_columns_cols,n_classes=2)
dnn_model.train(input_fn=input_func,steps=1000)
eval_input_func = tf.estimator.inputs.pandas_input_fn(
      x=X_test,
      y=y_test,
      batch_size=10,
      num_epochs=1,
      shuffle=False)
dnn_model.evaluate(eval_input_func)