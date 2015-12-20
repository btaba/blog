---
layout: post
title:  "Donald TrumpBot"
date:   2015-12-19 00:30:00
categories: data_science
tags: regular
comments: True
<!-- image: /assets/article_images/2014-08-29-welcome-to-jekyll/food.jpg -->
---
<script type="text/javascript" src="/assets/recurrentjs/recurrent.js"></script>
<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/jquery/2.1.4/jquery.min.js"></script>
<script type="text/javascript" src="/assets/js/spin.min.js"></script>
<!-- <script src="/assets/js/jquery-1.8.3.min.js"></script> -->
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap.min.css" integrity="sha384-1q8mTJOASx8j1Au+a5WDVnPi2lkFfwwEAa8hDDdjZlpLegxhjVME1fgjWPGmkzs7" crossorigin="anonymous">
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/css/bootstrap-theme.min.css" integrity="sha384-fLW2N01lMqjakBkx3l/M9EahuwpSfeNvV63J5ezn3uZzapT0u7EYsXMjQV+0En5r" crossorigin="anonymous">
<script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.6/js/bootstrap.min.js" integrity="sha384-0mSbJDEHialfmuBBQP6A4Qrprq5OVfW37PRR3j5ELqxss1yVqOtnepnHVP9aJ7xS" crossorigin="anonymous"></script>

<style>
  input[type=range] {
  -webkit-appearance: none;
  width: 150%;
  margin: 10.4px 0;
}
input[type=range]:focus {
  outline: none;
}
input[type=range]::-webkit-slider-runnable-track {
  width: 100%;
  height: 8.2px;
  cursor: pointer;
  box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
  background: rgba(7, 95, 102, 0.93);
  border-radius: 13.6px;
  border: 1.7px solid #010101;
}
input[type=range]::-webkit-slider-thumb {
  box-shadow: 1.4px 1.4px 1.9px #000000, 0px 0px 1.4px #0d0d0d;
  border: 1px solid #009589;
  height: 29px;
  width: 19px;
  border-radius: 0px;
  background: rgba(89, 202, 163, 0.79);
  cursor: pointer;
  -webkit-appearance: none;
  margin-top: -12.1px;
}
input[type=range]:focus::-webkit-slider-runnable-track {
  background: rgba(10, 135, 145, 0.93);
}
input[type=range]::-moz-range-track {
  width: 100%;
  height: 8.2px;
  cursor: pointer;
  box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
  background: rgba(7, 95, 102, 0.93);
  border-radius: 13.6px;
  border: 1.7px solid #010101;
}
input[type=range]::-moz-range-thumb {
  box-shadow: 1.4px 1.4px 1.9px #000000, 0px 0px 1.4px #0d0d0d;
  border: 1px solid #009589;
  height: 29px;
  width: 19px;
  border-radius: 0px;
  background: rgba(89, 202, 163, 0.79);
  cursor: pointer;
}
input[type=range]::-ms-track {
  width: 100%;
  height: 8.2px;
  cursor: pointer;
  background: transparent;
  border-color: transparent;
  color: transparent;
}
input[type=range]::-ms-fill-lower {
  background: rgba(4, 55, 59, 0.93);
  border: 1.7px solid #010101;
  border-radius: 27.2px;
  box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
}
input[type=range]::-ms-fill-upper {
  background: rgba(7, 95, 102, 0.93);
  border: 1.7px solid #010101;
  border-radius: 27.2px;
  box-shadow: 1px 1px 1px #000000, 0px 0px 1px #0d0d0d;
}
input[type=range]::-ms-thumb {
  box-shadow: 1.4px 1.4px 1.9px #000000, 0px 0px 1.4px #0d0d0d;
  border: 1px solid #009589;
  height: 29px;
  width: 19px;
  border-radius: 0px;
  background: rgba(89, 202, 163, 0.79);
  cursor: pointer;
  height: 8.2px;
}
input[type=range]:focus::-ms-fill-lower {
  background: rgba(7, 95, 102, 0.93);
}
input[type=range]:focus::-ms-fill-upper {
  background: rgba(10, 135, 145, 0.93);
}  
</style>


Donald Trump has sure been getting a lot of attention in the media lately. His speeches are pretty funny (or not). 

Well now we can all bring out the Donald Trump inside of us with Donald TrumpBot. Just type in some words in the text box below and click 'Go!' You'll have a pre-prepared Donald Trump speech in no time! The output of TrumpBot won't make sense most of the time, but occasionally it will output something amusing. Some words to try: (trump, mexico, border)


<div class="form-group">
<p style='display: inline'>Sampling Method: </p>
<div class="btn-group" data-toggle="buttons">
  <label class="btn btn-primary" id="max">
    <input type="radio" name="options" autocomplete="off" ><span style="font-size: large"> RNN Max</span>
  </label>
  <label class="btn btn-primary" id="samplemax">
    <input type="radio" name="options" autocomplete="off"><span style="font-size: large"> RNN Rand</span>
  </label>
  <label class="btn btn-primary active" id="markov">
    <input type="radio" name="options" autocomplete="off" checked><span style="font-size: large"> Markov</span>
  </label>
</div>

<div id='temp' style="display: none"><p style='display: inline'></br>
Temperature: </p>
<div class="btn-group">
  <label for="">
    <input type="range" name="points" min="0.05" max="1.0" step='.05' value='0.3' oninput="changeTemperature(this.value)" onchange="changeTemperature(this.value)">
  </label> 
  <p style='display: inline; margin-left: 70px'><span id='tempdisplay'>0.3</span></p>
</div></div>
<p style='display: inline'></br>
Sentence Length: </p>
<div class="btn-group">
  <label for="">
    <input type="range" name="points" min="15" max="1000" step='5' value='100' oninput="changeSentLength(this.value)" onchange="changeSentLength(this.value)">
  </label> 
  <p style='display: inline; margin-left: 70px'><span id='sentdisplay'>100</span></p>
</div>

## Trump it!
<div class="input-group" style="width: 100%">
  <input style="font-size: large;" type="text" class="form-control" id='speechseed' placeholder="some I assume are good people">
</div>

<div class="btn-group" style="float: right;">
  <button class="btn btn-primary" id='generate' type="button" style="font-size: large;"><span style="font-size: large">Go</span></button>
  <button class="btn btn-primary" id='generate-samp' type="button" style="font-size: large;"><span style="font-size: large">I'm feeling Lucky!</span></button>
</div>

</div>

## Share it!

<!-- <a class="icon-{{ social.icon }}" href="{{ social.share_url }}{{ social.share_title }}{{page.title | cgi_escape}}{{ social.share_link }}{{site.url}}{{page.id}}"
                  onclick="window.open(this.href, '{{ social.icon }}-share', 'width=550,height=255');return false;">
                <i class="fa fa-{{ social.icon }}"></i><span class="hidden">{{ social.icon }}</span> -->

<div>
  <div id="progress" style="display: none">
    <div class="progress"> 
      <div class="progress-bar" role="progressbar progress-bar-striped active" aria-valuenow="0" aria-valuemin="2" aria-valuemax="100" style="width: 0%;"></div>
      <img src="/assets/images/trump6301.jpg" height="24">
    </div>
  </div>
  <div id="predicted" style='background: aliceblue; font-size: x-large;'>Type in a seed sentence above.</div>
</div>
    
</br>

#### Instructions

Wait for the page to load the models. There are 3 sampling methods to choose from. The Markov sampling method takes a seed word (that must be in the dictionary) and will generate the speech word-for-word. The RNN will take in a whole sentence and generate the speech character-by-character. A low "Temperature" for the RNN will cause it to make more likely predictions, while a higher temperature will cause the RNN to take more chances. The RNN Max method, will get the most likely character prediction, while the RNN Rand will have a level of randomness.

#### Details

RNN built using a 2-layer lstm network, trained on AWS using <a href="http://keras.io/" target="_blank">Keras</a> with a <a href="http://deeplearning.net/software/theano/" target="_blank">Theano</a> backend. (max-sent-length: 120, hidden-size: 512, batch-size: 64, step: 3). The RNN runs in the browser using <a href="https://github.com/karpathy/recurrentjs" target="_blank">RecurrentJS</a>. Many thanks to the developers of Keras and Andrej Karpathy for developing RecurrentJS. Markov chain implementation based on Casey Chu's <a href="http://www.bitsofpancake.com/programming/markov-chain-text-generator/" target="_blank">blog post</a>. Speech transcripts were extracted from the following websites (let me know if you have more, since I only had 214k characters, and I think the RNN would greatly benefit from more to train on):

1. <a href="http://blogs.wsj.com/washwire/2015/06/16/donald-trump-transcript-our-country-needs-a-truly-great-leader/" target="_blank">wsj.com</a> 
2. <a href="http://www.p2016.org/photos15/summit/trump012415spt.html" target="_blank">p2016.org</a> 
3. <a href="http://www.huffingtonpost.com/seth-abramson/a-transcript-of-the-decen_b_7609908.html" target="_blank">huffingtonpost.com</a> 
4. <a href="http://time.com/4037239/second-republican-debate-transcript-cnn/" target="_blank">time.com</a> 
5. <a href="https://blog.frcaction.org/2015/09/donald-trumps-remarks-vvs-2015/" target="_blank">frcaction.org</a>  
6. <a href="http://www.msnbc.com/rachel-maddow-show/trump-crosses-new-line-endorses-database-muslim-americans" target="_blank">msnbc.com</a> 
7. <a href="http://www.whatthefolly.com/2015/08/05/transcript-donald-trumps-speech-in-phoenix-arizona-on-july-11-2015-part-1/" target="_blank">whatthefolly.com</a> 


<script>
// spinner
  var opts = {
  lines: 12 // The number of lines to draw
, length: 0 // The length of each line
, width: 15 // The line thickness
, radius: 15 // The radius of the inner circle
, scale: 0.5 // Scales overall size of the spinner
, corners: 0 // Corner roundness (0..1)
, color: '#000' // #rgb or #rrggbb or array of colors
, opacity: 0.25 // Opacity of the lines
, rotate: 30 // The rotation offset
, direction: 1 // 1: clockwise, -1: counterclockwise
, speed: 1 // Rounds per second
, trail: 38 // Afterglow percentage
, fps: 20 // Frames per second when using setTimeout() as a fallback for CSS
, zIndex: 2e9 // The z-index (defaults to 2000000000)
, className: 'spinner' // The CSS class to assign to the spinner
, top: '49%' // Top position relative to parent
, left: '100%' // Left position relative to parent
, shadow: true // Whether to render a shadow
, hwaccel: false // Whether to use hardware acceleration
, position: 'absolute' // Element positioning
}
var spinner = new Spinner(opts).spin();
</script>

<script>


// prediction params
var sample_softmax_temperature = .3; // how peaky model predictions should be
var max_chars_gen = 100; // max length of generated sentences
var samplei = false;
var train_text = {};
var markov_text = {};
var markov = true;

// Markov Model
var markov_cache = {
    '_START': []
};

// RNN Model architecture
var generator = 'lstm';

// Initialize models, we may eventually want to have more candidates' speeches
var models = {}
var mtypes = ['trump', 'hillary']
models['trump'] = {}
models['hillary'] = {}
for (m in models) {
  models[m]['hidden_sizes'] = [50, 50];
  models[m]['letter_size'] = 10;
  models[m]['letterToIndex'] = {};
  models[m]['indexToLetter'] = {};
  models[m]['vocab'] = [];
  models[m]['data_sents'] = [];
  models[m]['model'] = {};
}

var loadText = function(data, type, _callback) {
  data = data.toLowerCase();
  data = data.trim().split(/\s+/g);
  markov_text[type] = data;
  train_text[type] = data.join(' ');
  _callback(type);
}

var loadMarkovModel = function(type) {
  markov_cache['_START'].push(markov_text[type][0]);

  for (var i = 0; i < markov_text[type].length - 1; i++) {
      if (!markov_cache[markov_text[type][i]])
          markov_cache[markov_text[type][i]] = [];
      markov_cache[markov_text[type][i]].push(markov_text[type][i + 1]);
      
      if (markov_text[type][i].match(/\.$|\?$|\!$|\)$/))
          markov_cache['_START'].push(markov_text[type][i + 1]);
  }
}

var loadModel = function(j, mtype) {
  models[mtype]['hidden_sizes'] = j.hidden_sizes;
  models[mtype]['generator'] = j.generator;
  models[mtype]['letter_size'] = j.letter_size;
  model = {};
  for(var k in j.model) {
    if(j.model.hasOwnProperty(k)) {
      var matjson = j.model[k];
      model[k] = new R.Mat(1,1);
      model[k].fromJSON(matjson);
    }
  }
  models[mtype]['model'] = model;
  models[mtype]['letterToIndex'] = j['letterToIndex'];
  models[mtype]['indexToLetter'] = j['indexToLetter'];
  models[mtype]['vocab'] = j['vocab'];
}

var costfun = function(models, sent, mtype) {
  // takes a model and a sentence and
  // calculates the loss. Also returns the Graph
  // object which can be used to do backprop
  var n = sent.length;
  var G = new R.Graph();
  var log2ppl = 0.0;
  var cost = 0.0;
  var prev = {};

  var model = models[mtype]['model'];
  var letterToIndex = models[mtype]['letterToIndex'];

  for(var i=0;i<n;i++) {
    var ix_source = letterToIndex[sent[i]];
    // workaround for not having start/end tokens
    var ix_target = i === n-1 ? letterToIndex[" "] : letterToIndex[sent[i+1]];

    lh = forwardIndex(G, models, ix_source, prev, mtype);
    prev = lh;

    // set gradients into logprobabilities
    logprobs = lh.o; // interpret output as logprobs
    probs = R.softmax(logprobs); // compute the softmax probabilities

    log2ppl += -Math.log2(probs.w[ix_target]); // accumulate base 2 log prob and do smoothing
    cost += -Math.log(probs.w[ix_target]);

    // write gradients into log probabilities
    logprobs.dw = probs.w;
    logprobs.dw[ix_target] -= 1
  }
  var ppl = Math.pow(2, log2ppl / (n - 1));
  return {'G':G, 'ppl':ppl, 'cost':cost, 'prev_hidden': prev};
}

var forwardIndex = function(G, models, ix, prev, mtype) {
  var model = models[mtype]['model'];
  var hidden_sizes = models[mtype]['hidden_sizes'];
  var x = G.rowPluck(model['Wil'], ix);
  // forward prop the sequence learner
  if(generator === 'rnn') {
    var out_struct = R.forwardRNN(G, model, hidden_sizes, x, prev);
  } else {
    var out_struct = R.forwardLSTM(G, model, hidden_sizes, x, prev);
  }
  return out_struct;
}

var predictSentence = function(models, samplei, temperature, prev, sent, mtype, _callback) {
  if(typeof samplei === 'undefined') { samplei = false; }
  if(typeof temperature === 'undefined') { temperature = 1.0; }
  if(typeof prev === 'undefined') { prev = {}; }

  var $bar = $('.progress-bar');

  var G = new R.Graph(false);
  var s = sent;
  var tick = 0;

  var model = models[mtype]['model'];
  var letterToIndex = models[mtype]['letterToIndex'];
  var indexToLetter = models[mtype]['indexToLetter'];

  whileinterval = setInterval(function() {
    // RNN tick
    var ix = s.length === 0 ? letterToIndex[s] : letterToIndex[s[s.length-1]];
    var lh = forwardIndex(G, models, ix, prev, mtype);
    prev = lh;

    $bar.width(tick / max_chars_gen * 100 + '%');
    // console.log(tick / max_chars_gen * 100 + '%')

    // sample predicted letter
    logprobs = lh.o;
    if(temperature !== 1.0 && samplei) {
      // scale log probabilities by temperature and renormalize
      // if temperature is high, logprobs will go towards zero
      // and the softmax outputs will be more diffuse. if temperature is
      // very low, the softmax outputs will be more peaky
      for(var q=0,nq=logprobs.w.length;q<nq;q++) {
        logprobs.w[q] /= temperature;
      }
    }

    probs = R.softmax(logprobs);
    if(samplei) {
      var ix = R.samplei(probs.w);
    } else {
      var ix = R.maxi(probs.w);  
    }
    
    // didn't use start/end tokens...
    // if(ix === 0) break; // END token predicted, break out
    if(s.length > max_chars_gen) { 
      $('#progress').hide();
      $bar.width('0%');
      _callback(s);
      clearInterval(whileinterval);
    }

    var letter = indexToLetter[ix];
    if (tick == 0) {
      s = letter;
    } else {
      s += letter;  
    }
    tick += 1;
  }, 0);
  
}

var sampleSentence = function(sample_sentence, samplei, mtype, _callback) {
  if(typeof samplei === 'undefined') { samplei = false; }

  var sent = sample_sentence;

  // evaluate cost function on a sentence
  var cost_struct = costfun(models, sent, mtype);
  console.log("Perplexity of input sentence: " + cost_struct.ppl)

  
  predictSentence(models, samplei, sample_softmax_temperature,
    cost_struct.prev_hidden, sample_sentence[sample_sentence.length-1], mtype,
    _callback);
  
}

var sampleMarkovSentence = function(currentWord, _callback) {
  // Start with the root node
  if (typeof currentWord === 'undefined') {currentWord = '_START'}
  var s = '';
  var $bar = $('.progress-bar');

  whileinterval = setInterval(function() {

    $bar.width(s.length / max_chars_gen * 100 + '%');
    
    var rand;
    if (!markov_cache[currentWord]) {
      currentWord = '_START'
    }
    rand = Math.floor(Math.random() * markov_cache[currentWord].length);
    s += markov_cache[currentWord][rand];  
    
    
    if (!markov_cache[markov_cache[currentWord][rand]]) {
        currentWord = '_START';
        if (!markov_cache[currentWord][rand].match(/\.$/))
            s += '. ';
        else
            s += ' ';
    } else {
        currentWord = markov_cache[currentWord][rand];
        s += ' ';
    }
    
    if(s.length > max_chars_gen) { 
      $('#progress').hide();
      $bar.width('0%');
      _callback(s);
      clearInterval(whileinterval);
    }
  }, 0);

}

var cleanSeedText = function(text, vocab, byword) {
  if (byword) {
    text = text.toLowerCase().split(' '); 
  }
  else {
    text = text.toLowerCase();  
  }
  
  clean_text = [];
  for (t in text) {
    if (vocab.indexOf(text[t]) != -1) {
      clean_text.push(text[t]);
    }
  }
  if (byword)
    return clean_text.join(" ")
  return clean_text.join("")
}

var getLongestWord = function(text) {
  text = text.split(' ');
  var longest = text.sort(function (a, b) {
    return b.length - a.length; 
  });
  for (l in longest) {
    if (!longest[l].match(/\.$|\?$|\!$|\,$/))
      return longest[l]
  }
  return longest[0]
}

var changeTemperature = function(val) {
  $('#tempdisplay').html(val);
  sample_softmax_temperature = val;
}

var changeSentLength = function(val) {
  $('#sentdisplay').html(val);
  max_chars_gen = val;
}

function getRandomInt(min, max) {
  return Math.floor(Math.random() * (max - min)) + min;
}

function seedTextWrapper(text) {
  return '<span style="color: seagreen">' + text + '</span>'
}


$(document).ready(function() {
  $('#generate').prop("disabled", true);
  $('#generate-samp').prop("disabled", true);
  $('#generate').append(spinner.el);

  
  $.get("/assets/data/trump.txt", function(data) {
      loadText(data, 'trump', loadMarkovModel);
  });

  $.getJSON("/assets/data/trump_120_recurrentjs.json", function(data) {
      loadModel(data, 'trump');
      $('#generate').prop("disabled", false);
      $('#generate-samp').prop("disabled", false);
  });

  removespinner = setInterval(function() {
      if ($('#generate').prop("disabled") == false && $('#generate-samp').prop("disabled") == false) {
        $('#generate').html('<span style="font-size: large">Go</span>');
        clearInterval(removespinner);
      }
  }, 10)


  var seed_text = ''
  $('#generate').click(function() {
    $('#predicted').html(''); 
    $('#generate').prop("disabled", true);
    $('#generate-samp').prop("disabled", true);

    $('#progress').show(function() {
      seed_text = $('#speechseed').val();

      if (!markov) {
        // RNN
        seed_text = cleanSeedText(seed_text, models['trump']['vocab'], false);

        if (seed_text.length > 0) {
          seed_text += ' '
        }
        else {
          // pick a random seed from the text
          var startidx = getRandomInt(0, train_text['trump'].length - 120);
          seed_text = train_text['trump'].substring(startidx, (startidx + 120));
     
          $('#speechseed').val(seed_text);
        }

        // Sample the sentence from RNN
        sampleSentence(seed_text, samplei, 'trump', function(generated_text) {
          // console.log(generated_text);
          generated_text = seedTextWrapper(seed_text) + generated_text;
          var pred_div = '<div class="apred">'+generated_text+'</div>'
          
          $('#predicted').append(pred_div); 
          $('#generate').prop("disabled", false);
          $('#generate-samp').prop("disabled", false);
        });
      }
      else {
        // Markov
        seed_text = cleanSeedText(seed_text, Object.keys(markov_cache), true);
        if (seed_text.length > 0) {
          // get the longest word in string
          seed_text = getLongestWord(seed_text);
        }
        else {
          seed_text = undefined;
        }
        sampleMarkovSentence(seed_text, function(generated_text) {
          // console.log(generated_text);
          if (seed_text) {
            generated_text = seedTextWrapper(seed_text + ' ') + generated_text;  
          } 
          var pred_div = '<div class="apred">'+generated_text+'</div>'
          
          $('#predicted').append(pred_div); 
          $('#generate').prop("disabled", false);
          $('#generate-samp').prop("disabled", false);
        });
      }
    })
  })

  $('#generate-samp').click(function () {
    $('#predicted').html('');
    $('#generate').prop("disabled", true);
    $('#generate-samp').prop("disabled", true);

    $('#progress').show(function() {
      var startidx = getRandomInt(0, train_text['trump'].length - 120);
      var seed_text = train_text['trump'].substring(startidx, (startidx + 120));
        
      if (!markov) {
        $('#speechseed').val(seed_text);
        sampleSentence(seed_text, samplei, 'trump', function(generated_text) {
          // console.log(generated_text);
          generated_text = seedTextWrapper(seed_text) + generated_text;
          var pred_div = '<div class="apred">'+generated_text+'</div>'
          
          $('#predicted').append(pred_div);
          $('#generate').prop("disabled", false);
          $('#generate-samp').prop("disabled", false); 
        });  
      } else {
        // console.log(seed_text)
        seed_text = getLongestWord(seed_text);
        $('#speechseed').val(seed_text);
        sampleMarkovSentence(seed_text, function(generated_text) {
          // console.log(generated_text);
          if (seed_text) {
            generated_text = seedTextWrapper(seed_text + ' ') + generated_text;  
          } 
          var pred_div = '<div class="apred">'+generated_text+'</div>'
          
          $('#predicted').append(pred_div); 
          $('#generate').prop("disabled", false);
          $('#generate-samp').prop("disabled", false);
        });
      }
      
    })
    
  })

  // sample method
  $('#max').click(function() {
    $('#temp').show();
    markov = false;
    samplei = false;
  });
  $('#samplemax').click(function() {
    $('#temp').show();
    markov = false;
    samplei = true;
  });
  $('#markov').click(function() {
    markov = true;
    $('#temp').hide();
  });
  
});

</script>
