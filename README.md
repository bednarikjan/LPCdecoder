# LPCdecoder
The python implementation of the speech decoder using Linear Predictive Coding (LPC). The program takes the pre-trained codebook of 512 code vectors containing LPC coefficients, the pre-trained codebook containing 128 gain values and the coded signal (human speech) and computes the decoded signal as a WAV file.

## Dependencies
* Python 2.7
* NumPy
* SciPy

## Run
```
$ chmod +x run
$ ./run cb_lpc.txt cb_gain.txt in.cod out.wav
```

The program can be tested using two coded speech samples: *testmale.cod* and *testfemale.cod*.
