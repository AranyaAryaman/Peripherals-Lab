		         8085 PROGRAM TO GENERATE WAVEFORMS USING A 8-BIT DAC



THE ASSIGNMENT CONSISTS OF TWO DIFFERENT FILES

I)Assignment5_wave.asm:-This file holds the code to generate five different waveforms using variable frequency taken as input from
the user.The five waveforms correspond to five differnt DIP switches as follows:

INPUT          WAVEFORM

a)80h           Square
b)40h		Triangular
c)20h		Sawtooth
d)10h		Staircase
e)08h		Symmetrical Staircase

At the beginning of waveform generation we perform an inverse of the entered frequency using division function
and compute the no of cycles required as a function of the time period calculated.These values are stored at five
different memory locations for the five different waveforms

The basic idea behind each of them are as follows:-

a)Sqare:-It runs in two loops. loop1 runs while the pulse is still zero while loop2 runs when the pulse
displays a constant value of ffH for one half of the time period.

b)Triangular:-It also runs in two loops like before except that with each looping, the value of the accumulator is incremented
by 06h and at the end of each computation,the value is held for some time using tridelay routine. tloop is the loop for
positive slope while tnegloop correspondsto negative slope

c)Sawtooth:-It is a modification of the triangular waveform with the display reverting back to zero once the positive peak 
is reached. Each iteration, the accumulator is increased by 4H, and held for appropriate time by sawdelay.

d)Staircase:-It is another modification of the Sawtooth waveform except that each value is delayed for a much longer time 
than sawtooth and also the rise at each step is much steeper and discrete than sawtooth which incremented smoothly.

e)Symmetrical Staircase:-It is the final modification of Staircase with the values at each step decrementing at the same rate
and held using the same delay routine as the staircase one, only shorter by half to maintain the same frequency.


II)Assignment5_sine.asm:-This program simply stores pre-computed values of sine function in main memory and displays them onto the CRO
by looping over the memory locations first incrementally,then decrementally.
