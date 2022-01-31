#!/usr/bin/env python
# coding: utf-8

# ##### Copyright 2019 The TensorFlow Authors.

# In[ ]:


#@title Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# Modifed from https://www.tensorflow.org/tutorials/quickstart/beginner for use with DRBL for AI.


# # TensorFlow 2 quickstart for beginners

# This short introduction uses [Keras](https://www.tensorflow.org/guide/keras/overview) to:
# 
# 1. Build a neural network that classifies images.
# 2. Train this neural network.
# 3. And, finally, evaluate the accuracy of the model.

# In[ ]:


import tensorflow as tf
import albumentations

# Load and prepare the [MNIST dataset](http://yann.lecun.com/exdb/mnist/). Convert the samples from integers to floating-point numbers:

# In[ ]:


mnist = tf.keras.datasets.mnist

(x_train, y_train), (x_test, y_test) = mnist.load_data()
x_train, x_test = x_train / 255.0, x_test / 255.0


# Build the `tf.keras.Sequential` model by stacking layers. Choose an optimizer and loss function for training:

# In[ ]:


model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(input_shape=(28, 28)),
  tf.keras.layers.Dense(128, activation='relu'),
  tf.keras.layers.Dropout(0.2),
  tf.keras.layers.Dense(10)
])


# For each example the model returns a vector of "[logits](https://developers.google.com/machine-learning/glossary#logits)" or "[log-odds](https://developers.google.com/machine-learning/glossary#log-odds)" scores, one for each class.

# In[ ]:


predictions = model(x_train[:1]).numpy()
predictions


# The `tf.nn.softmax` function converts these logits to "probabilities" for each class: 

# In[ ]:


tf.nn.softmax(predictions).numpy()


# Note: It is possible to bake this `tf.nn.softmax` in as the activation function for the last layer of the network. While this can make the model output more directly interpretable, this approach is discouraged as it's impossible to
# provide an exact and numerically stable loss calculation for all models when using a softmax output. 

# The `losses.SparseCategoricalCrossentropy` loss takes a vector of logits and a `True` index and returns a scalar loss for each example.

# In[ ]:


loss_fn = tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True)


# This loss is equal to the negative log probability of the true class:
# It is zero if the model is sure of the correct class.
# 
# This untrained model gives probabilities close to random (1/10 for each class), so the initial loss should be close to `-tf.log(1/10) ~= 2.3`.

# In[ ]:


loss_fn(y_train[:1], predictions).numpy()


# In[ ]:


model.compile(optimizer='adam',
              loss=loss_fn,
              metrics=['accuracy'])


# The `Model.fit` method adjusts the model parameters to minimize the loss: 

# In[ ]:


model.fit(x_train, y_train, epochs=5)


# The `Model.evaluate` method checks the models performance, usually on a "[Validation-set](https://developers.google.com/machine-learning/glossary#validation-set)" or "[Test-set](https://developers.google.com/machine-learning/glossary#test-set)".

# In[ ]:


model.evaluate(x_test,  y_test, verbose=2)


# The image classifier is now trained to ~98% accuracy on this dataset. To learn more, read the [TensorFlow tutorials](https://www.tensorflow.org/tutorials/).

# If you want your model to return a probability, you can wrap the trained model, and attach the softmax to it:

# In[ ]:


probability_model = tf.keras.Sequential([
  model,
  tf.keras.layers.Softmax()
])


# In[ ]:


probability_model(x_test[:5])

