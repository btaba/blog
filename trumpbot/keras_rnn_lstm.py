'''
Example script from Keras documentation to train LSTM
on some text

Usage:
$ python keras_rnn_lstm.py --inputfile trump --outputfile trump_model 
'''

from __future__ import print_function
from keras.models import Sequential
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.datasets.data_utils import get_file
from keras.models import model_from_json
from nltk.tokenize import word_tokenize
import numpy as np
import argparse
import pickle
import random
import sys
import re


MODEL_DIR = './blog_models/'


def get_text(ttype='nietzsche'):

    if ttype == 'nietzsche':
        path = get_file('nietzsche.txt', origin="https://s3.amazonaws.com/text-datasets/nietzsche.txt")
        text = open(path).read().lower()
    elif ttype == 'trump':
        # there should be a better way to fix these encodings...
        text = open('./trump.txt', 'rb').read().lower().decode('utf-8')
    elif ttype == 'hillary':
        text = open('./hillary.txt', 'rb').read().lower().decode('utf-8')
    elif ttype == 'obama':
        pass

    # Get rid of newline characters, join by spaces, and then strip extra spaces
    text = re.sub(' +',' ',' '.join(text.splitlines()))    
    print('corpus length:', len(text))
    return text


def train_lstm(text, maxlen, step,
    hidden_size=[512, 512],
    dropout=[.2, .2], n_iters=60, batch_size=128,
    model_path=MODEL_DIR + 'lstm',
    load_model=False, char_rnn=True):
    
    mpath = model_path
    model_json_path = model_path + '.json'
    model_path = model_path + '.h5'
    
    if not load_model:
        if char_rnn == False:
            text = word_tokenize(text)
        chars = set(text)
        print(chars)
        pickle.dump( chars, open( model_path + "_chars.pkl", "wb" ) )
        print('total chars:', len(chars))
    else:
        print('Loading chars')
        chars = pickle.load(open( mpath + "_chars.pkl", "rb" ) )
        
    char_indices = dict((c, i) for i, c in enumerate(chars))
    indices_char = dict((i, c) for i, c in enumerate(chars))

    # cut the text in semi-redundant sequences of maxlen characters
    maxlen = maxlen
    step = step
    sentences = []
    next_chars = []
    for i in range(0, len(text) - maxlen, step):
        sentences.append(text[i: i + maxlen])
        next_chars.append(text[i + maxlen])
    print('nb sequences:', len(sentences))

    print('Vectorization...')
    X = np.zeros((len(sentences), maxlen, len(chars)), dtype=np.bool)
    y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
    for i, sentence in enumerate(sentences):
        for t, char in enumerate(sentence):
            X[i, t, char_indices[char]] = 1
        y[i, char_indices[next_chars[i]]] = 1

    if not load_model:
        # build the model: 2 stacked LSTM
        print('Build model...')
        model = Sequential()
        model.add(LSTM(hidden_size[0], return_sequences=True, input_shape=(maxlen, len(chars))))
        model.add(Dropout(dropout[0]))
        model.add(LSTM(hidden_size[1], return_sequences=False))
        model.add(Dropout(dropout[1]))
        model.add(Dense(len(chars)))
        model.add(Activation('softmax'))

        model.compile(loss='categorical_crossentropy', optimizer='rmsprop')
    else:
        print('Loading model json')
        model =  model_from_json(open(model_json_path).read())
        print('Loading model weights')
        model.load_weights(model_path)

    def sample(a, temperature=1.0):
        # helper function to sample an index from a probability array
        a = np.log(a) / temperature
        a = np.exp(a) / np.sum(np.exp(a))
        return np.argmax(np.random.multinomial(1, a, 1))

    # train the model, output generated text after each iteration
    for iteration in range(1, n_iters):
        print()
        print('-' * 50)
        print('Iteration', iteration)
        model.fit(X, y, batch_size=batch_size, nb_epoch=1)

        start_index = random.randint(0, len(text) - maxlen - 1)

        if iteration % 1 == 0:
            print('Saving models...')
            json_string = model.to_json()
            open(model_json_path, 'w').write(json_string)
            model.save_weights(model_path, overwrite=True)
        
        for diversity in [0.2, 0.5, 1.0, 1.2]:
            print()
            print('----- diversity:', diversity)

            generated = ''
            sentence = text[start_index: start_index + maxlen]
            
            if char_rnn:
                generated += sentence
                sent = sentence
            else:
                generated += ' '.join(sentence)
                sent = ' '.join(sentence)
            
            print('----- Generating with seed: "' + sent + '"')
            sys.stdout.write(generated)

            for iteration in range(400):
                x = np.zeros((1, maxlen, len(chars)))
                for t, char in enumerate(sentence):
                    x[0, t, char_indices[char]] = 1.

                preds = model.predict(x, verbose=0)[0]
                next_index = sample(preds, diversity)
                next_char = indices_char[next_index]
                
                if char_rnn:
                    generated += next_char
                    sentence = sentence[1:] + next_char
                else:
                    generated += ' ' + next_char
                    sentence.append(next_char)
                    sentence = sentence[1:]
                    next_char = ' ' + next_char
                    

                sys.stdout.write(next_char)
                sys.stdout.flush()
            print()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Train LSTM \
        with Keras and Theano backend')
    parser.add_argument('--inputfile', type=str, required=True,
                       help='file path for text to trian on')
    parser.add_argument('--outputfile', type=str, required=True,
                       help='model output file name')
    parser.add_argument('--load', type=bool, required=False,
                       help='load model?')

    args = parser.parse_args()

    text = get_text(args.inputfile)

    train_lstm(text, maxlen=60, step=3, 
        hidden_size=[400, 400],
        dropout=[.2, .2], n_iters=80, batch_size=64,
        model_path=MODEL_DIR + args.outputfile,
        load_model=False,
        char_rnn=False)


