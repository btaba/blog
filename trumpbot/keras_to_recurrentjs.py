'''
Convert an RNN that was trained with Keras and Theano
backend to be consumed by RecurrentJS

Usage:
$ python keras_to_recurrentjs.py --savepath='recurrentjs.json' --loadmodelpathh5='trump_rnn_lstm.h5' --loadmodelpathjson='trump_rnn_lstm.json' --loadmodelchars='chars.pkl'

'''

from __future__ import print_function
from keras.datasets.data_utils import get_file
from keras.models import model_from_json
from simplejson import Decimal
import simplejson as json
import numpy as np
import pickle
import argparse

def get_weights(mat):
    """Get weights from Keras and convert to json format"""
    # n rows, d columns
    # unravel matrices in row-major order
    # recurrentjs seems to have all weight matrices transposed
    mat = mat.T
    if len(mat.shape) == 1:
        d = 1
    else:
        d = mat.shape[1]
    return {
            'n': mat.shape[0],
            'd': d,
            'w': dict(enumerate([Decimal(str(m)) for m in np.ravel(mat)]))
        }

def keras_to_recurrentjs(keras_rnn_model_obj, 
                         keras_rnn_model_json, 
                         vocab, indices_char,
                         char_indices,
                         ltype='lstm'
                        ):
    """
        Convert a Keras RNN object to ReccurentJS object
        
        Word embeddings from Keras not supported yet
    """
    keras_rnn_json_layers = keras_rnn_model_json['layers']
    keras_rnn_matrix_layers = keras_rnn_model_obj.layers

    assert len(keras_rnn_json_layers) ==  len(keras_rnn_matrix_layers)
    assert len(indices_char) == len(vocab)
    assert len(char_indices) == len(vocab)
    
    num_hidden_layers = 0
    hidden_sizes = []
    letter_size = 0
    recurrentjs_json = {}
    layers = []
    
    # Get number of hidden layers and check that last two layers 
    # are dense and softmax respectively
    for idx, krjl in enumerate(keras_rnn_json_layers):
        
        if idx == len(keras_rnn_json_layers) - 2:
            assert krjl['name'] == 'Dense'

        if idx == len(keras_rnn_json_layers) - 1:
            assert krjl['name'] == 'Activation'
            assert krjl['activation'] == 'softmax'

        if krjl['name'].lower() == ltype:
            if num_hidden_layers == 0:
                letter_size, vocab_length = krjl['input_shape']
            layers.append(keras_rnn_matrix_layers[idx])
            num_hidden_layers += 1
    
    assert num_hidden_layers > 0, \
        'Found 0 hidden layers with layer type: %s. Only lstm is currently supported' %ltype
    assert (len(keras_rnn_json_layers) - 2) % num_hidden_layers == 0, \
        'Mismatch in number of hidden layers found and number of layers in Keras json'
    assert letter_size > 0, 'Inpute shape of Keras RNN has 0 input shape'
    
    print('>> Converting an %s RNN with %d layers...' % (ltype, num_hidden_layers))
        
    print('>> Creating JSON object for recurrentJS...')
    recurrentjs_json['vocab'] = list(vocab)
    recurrentjs_json['generator'] = ltype
    recurrentjs_json['letter_size'] = letter_size
    recurrentjs_json['indexToLetter'] = indices_char
    recurrentjs_json['letterToIndex'] = char_indices
    recurrentjs_json['hidden_sizes'] = []
    model = {}
    print('>> Loading Keras %s to recurrentJS json object...' %ltype)
    if ltype == 'lstm':
        for idx, layer in enumerate(layers):
            model['Wox' + str(idx)] = get_weights(layer.W_o.get_value())
            model['Wix' + str(idx)] = get_weights(layer.W_i.get_value())
            model['Wfx' + str(idx)] = get_weights(layer.W_f.get_value())
            model['Wcx' + str(idx)] = get_weights(layer.W_c.get_value())
            
            model['Woh' + str(idx)] = get_weights(layer.U_o.get_value())
            model['Wih' + str(idx)] = get_weights(layer.U_i.get_value())
            recurrentjs_json['hidden_sizes'].append(model['Wih' + str(idx)]['n'])
            model['Wfh' + str(idx)] = get_weights(layer.U_f.get_value())
            model['Wch' + str(idx)] = get_weights(layer.U_c.get_value())
            
            model['bo' + str(idx)] = get_weights(layer.b_o.get_value())
            model['bi' + str(idx)] = get_weights(layer.b_i.get_value())
            model['bf' + str(idx)] = get_weights(layer.b_f.get_value())
            model['bc' + str(idx)] = get_weights(layer.b_c.get_value())
    else:
        raise NotImplementedError('Only LSTM supported')
        
    model['Whd'] = get_weights(keras_rnn_matrix_layers[-2].W.get_value())
    model['bd'] = get_weights(keras_rnn_matrix_layers[-2].b.get_value())
    
    # Word embeddings, identity matrix if there are no embeddings
    model['Wil'] = get_weights(np.eye(len(vocab)))
    
    recurrentjs_json['model'] = model
    
    print('>> Done loading model to json object...')
    return recurrentjs_json

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert an RNN that was trained \
        with Keras and Theano backend to be consumed by RecurrentJS')
    parser.add_argument('--savepath', type=str, required=True,
                       help='file path for recurrentJS json dump')
    parser.add_argument('--loadmodelpathh5', type=str, required=True,
                       help='file path Keras h5 file')
    parser.add_argument('--loadmodelpathjson', type=str, required=True,
                       help='file path Keras json')
    parser.add_argument('--loadmodelchars', type=str, required=True,
                       help='pickled file path for set() of chars in model')

    args = parser.parse_args()

    print('>> Reading Keras model files...')
    print('>> Reading Keras json and loading model object...')
    model_json_string = open(args.loadmodelpathjson).read()
    model =  model_from_json(model_json_string)
    model_json_string = json.loads(model_json_string)
    
    print('>> Reading Keras H5 and loading weights to model...')
    model.load_weights(args.loadmodelpathh5)

    print('>> Reading vocab...')
    vocab = pickle.load( open( args.loadmodelchars, "rb" ) )
    char_indices = dict((c, i) for i, c in enumerate(vocab))
    indices_char = dict((i, c) for i, c in enumerate(vocab))

    print('>> Converting Keras to RecurrentJS...')
    print(model_json_string)

    recurrentjs_json = keras_to_recurrentjs(
                            model, 
                            model_json_string, 
                            vocab, indices_char,
                            char_indices,
                            ltype='lstm'
                         )

    print('>> Saving RecurrentJS model to json')
    with open(args.savepath, 'w') as outfile:
        json.dump(recurrentjs_json, outfile)

    print('>> Done!')

    
    