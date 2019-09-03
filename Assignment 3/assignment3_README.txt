README 
PROJECT TITLE: TIMER WITH INTERRUPTS

Two files have been uploaded -

In file v_1, the timer is executed with a single interrupt button, KBINT, for both play and pause.
The ISR is only responsible for flipping the mode bit. Depending on the mode, either timer runs, or it is held in a loop.

In file v_2, the interrupt KBINT is used to pause, while any of the other keys are used to resume timer operation.
Here again, the ISR flips the mode bit. But to resume after pause, RDKBD call is used to receive interrupt from keyboard input.

The timer works with the help of the SEC_DLY routine, which causes a delay of a second. Every second, the time is updated and displayed on the monitor. When the timer reaches zero, it displays 'CL', and return control to monitor program.