# Thirukkural written by Machine
Text generation using LSTM model in keras with Thirukural

After reading the article by Andrej Karpathy on [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/), I was super excited to apply LSTM on different dataset.

Finally, I chose [Thirukkural](https://en.wikipedia.org/wiki/Tirukku%E1%B9%9Ba%E1%B8%B7) which is one the most widely translated non-religious works in the world. It is written in one of the oldest classical languages of the world [Tamil](https://en.wikipedia.org/wiki/Tamil_language).
 
    

### Results

Start Word : "சாதலின் "
```
            இல்லாய் நினிபன் பெருந்தகை 
சிலையார் யாணென்னும் பயர்.
```
```
            ற் பொருட்செல்வம் தாண்டற்றும் மருந்து 
கேணல் சிறப்பின் இரந்து.
```
Start Word : "   காதல்"
```
            ல்லாது செய்யார் முன்றி தீயும் 
அருவியல் போர் கேது.
```
```
            டு யாதெனின் நெஞ்சத்தான் கண்ணுடையார் க
ேதலிற் கொள்வாரோட்க்கு விருந்து.
```
Start Word : "  காமம் "
```
            ன்தும் இடும்பை பஇடைச் சிறப்பின் இரவுருமாடு 
ஒரிவது குறவினும் பெறும்.
```
```
            ணிடும் பெறுப்சின் செய்யும் அவர்தென்பீர் 
கண்ட செல்வம் தரும்.
```

Start Word : " இறைவன் "
```
            பத் தலையபின் துணையாகை 
நீக்கிக் காமந்த நூர்.
```
```
            முன்றினும் உய்வாத்தல் இருவறுப் 
துணையாது விழைந்து விடல்.
```

Start Word : "  ஒழுக்க"
```
            த் தலையபின் துணையாது நீங்கி 
விருமுங்க்கல்ல செய்யார் மாத்து.
```

Start Word : " உயர்ந்த"
```
            தஒழில் தூழ்கச் சிறப்பின் 
இரந்தவற்று விகர்முடியார் அனைத்து.
```
```
            யஇருள் நோக்கெச் சுடைத்து வேநீால் 
வடிவார் என்றார் அனைத்து.
```

Start Word : " பெருமை "
```
             எய்தார் முற்றியது எண்ணிக் 
 கூடியமை என்னும் செருக்கு.
```
```
            கூற்றம் காதல் அல்லசெய்தல் 
இன்னை அருமாப் படும்.
```

### References
* [The Unreasonable Effectiveness of Recurrent Neural Networks](http://karpathy.github.io/2015/05/21/rnn-effectiveness/)
* [Obama-RNN — Machine generated political speeches.](https://medium.com/@samim/obama-rnn-machine-generated-political-speeches-c8abd18a2ea0)
* [Understanding LSTM Networks](http://colah.github.io/posts/2015-08-Understanding-LSTMs/)
* [Keras LSTM text generation](https://github.com/fchollet/keras/blob/master/examples/lstm_text_generation.py)