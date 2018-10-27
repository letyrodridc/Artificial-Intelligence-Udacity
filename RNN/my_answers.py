import numpy as np

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import keras


# TODO: fill out the function below that transforms the input series 
# and window-size into a set of input/output pairs for use with our RNN model
def window_transform_series(series,window_size):
    # containers for input/output pairs
    X = [ series[s:s+window_size] for s in range(0,len(series)-window_size)]
    y = [ series[s] for s in range(window_size,len(series))]    


    # reshape each 
    X = np.asarray(X)
    X.shape = (np.shape(X)[0:2])
    y = np.asarray(y)
    y.shape = (len(y),1)
    
    return X,y

# TODO: build an RNN to perform regression on our time series input/output data
def build_part1_RNN(step_size, window_size):

	# given - fix random seed - so we can all reproduce the same results on our default time series
	np.random.seed(0)


	# TODO: build an RNN to perform regression on our time series input/output data

	model = Sequential()
	model.add(LSTM(64, input_shape=(window_size, 1)))
	model.add(Dense(1, activation='tanh'))


	# build model using keras documentation recommended optimizer initialization
	optimizer = keras.optimizers.RMSprop(lr=0.0002, rho=0.9, epsilon=1e-08, decay=0.0)

	# compile the model
	model.compile(loss='mean_squared_error', optimizer=optimizer)


### TODO: list all unique characters in the text and remove any non-english ones
def clean_text(text):
	# find all unique characters in the text
	all_chars = set([x for x in text])
	
	# List the valid chars
	valid_chars = set(x for x in "1234567890qwertyuiopasdfghjklzxcvbnm ")

	# Make the difference and keep the chars to remove
	to_remove = all_chars.difference(valid_chars)

	# remove as many non-english characters and character sequences as you can 

	for c in to_remove:
	    text = text.replace(c, '')

	# shorten any extra dead space created above
	text = text.replace('  ',' ')



### TODO: fill out the function below that transforms the input text and window-size into a set of input/output pairs for use with our RNN model
def window_transform_text(text,window_size,step_size):
    # containers for input/output pairs
    inputs = [ text[s:s+window_size] for s in range(0,len(text)-window_size,step_size)]
    outputs = [ text[s] for s in range(window_size,len(text),step_size)]    
    
    # reshape each 
    inputs = np.asarray(inputs)
    inputs.shape = (np.shape(inputs)[0:window_size])
    outputs = np.asarray(outputs)
    #outputs.shape = (len(outputs),1)
    
    return inputs,outputs