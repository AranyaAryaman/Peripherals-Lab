cpu "8085.tbl"
hof "int8"

gthex: equ 030eh          ;      this routinue collects the hex digits entered from keyboard
output: equ 0389h         ;      outputs characters to display
clear: equ 02beh          ;      clears the display 

org 9000h 

call clear
mvi a,00h
mvi b,00h
call gthex   ; take input frequency
mov h,d
mov l,e
shld 8200h
call clear

; dividend for square wave
lxi h,07d00h
shld 8300h
call division
lhld 8400h
shld 8202h

; dividend for step wave
lxi h,02400h
shld 8300h
call division
lhld 8400h
shld 8204h

; dividend for symmetric step wave
lxi h,01200h
shld 8300h
call division
lhld 8400h
shld 8206h

; dividend for sawtooth wave
lxi h,03a8h
shld 8300h
call division
lhld 8400h
shld 8208h

; dividend for triangle wave
lxi h,02a4h
shld 8300h
call division
lhld 8400h
shld 820ah


mvi a,8bh		;setting 8255 to mode0 and port a o/p and port b,c i/p
mvi b,00h
out 03h

; function to chooose the waveform based on input from lci
; dip switches are in order
; 1st--> square
; 2nd--> triangular
; 3rd--> sawtooth
; 4th--> staircase
; 5th--> symstaircase
wavetype:
	in 01h

	cpi 80h		 
	jz square

	cpi 40h		 
	jz triangular

	cpi 20h		 
	jz sawtooth

	cpi 10h		 
	jz staircase

	cpi 08h		 
	jz symstaircase


mvi a,80h
out 43h

square:
	mvi a,00h
	sta 9500h
	lhld 8202h
	mov b,h 
	mov c,l
	
	loop1: ;delays for half a time period
		lda 9500h
		out 40h
		dcx b
		mov a,b                   
		ora c
		jnz loop1

	mvi a,0ffh
	sta 9500h
	lhld 8202h
	mov b,h 
	mov c,l

	loop2:
	lda 9500h
	out 40h
	dcx b
	mov a,b                   
	ora c
	jnz loop2
jmp wavetype


triangular:
mvi a,00h
sta 9500h
	tloop: ;incrementing acc. value till it reaches max
		lda 9500h
		adi 06h
		out 40h
		sta 9500h
		lhld 820ah
		mov b,h 
		mov c,l
		tridelay: ;appropriate delay after each increment
			lda 9500h
			out 40h
			dcx b
			mov a,b                   
			ora c
		jnz tridelay
	lda 9500h
	cpi 0fch
	jnz tloop

	tnegloop: ;decrementing acc. till it reaches zero 
		lda 9500h
		sbi 06h
		out 40h
		sta 9500h
		lhld 820ah
		mov b,h 
		mov c,l
		tridelay2:
			lda 9500h
			out 40h
			dcx b
			mov a,b                   
			ora c
		jnz tridelay2
		lda 9500h
		cpi 00h
		jnz tnegloop

jmp wavetype


sawtooth:
	mvi a,00h
	sta 9500h
	sawloop:
		lda 9500h
		adi 04h
		out 40h
		sta 9500h
		lhld 8208h
		mov b,h 
		mov c,l
		sawdelay:
			lda 9500h
			out 40h
			dcx b
			mov a,b                   
			ora c
		jnz sawdelay
	lda 9500h
	cpi 0fch
	jnz sawloop
jmp wavetype



staircase:
	mvi a,00h
	sta 9500h
	stairloop: ; each iteration is for one step in staircase
		lhld 8204h
		mov b,h 
		mov c,l
		stairdelay: ;creating a delay for each step
			lda 9500h
			out 40h
			dcx b
			mov a,b                   
			ora c
		jnz stairdelay
		lda 9500h
		adi 20h
		cpi 0e0h
		sta 9500h
	jnz stairloop

	mov a,00h
	sta 9500h
	out 40h

jmp wavetype



symstaircase:
mvi a,00h
sta 9500h
symstairloop: ; iterating up the staircase
	lhld 8206h
	mov b,h 
	mov c,l
	symstairdelay:
		lda 9500h
		out 40h
		dcx b
		mov a,b                   
		ora c
	jnz symstairdelay

		lda 9500h
		adi 20h
		cpi 0e0h
		sta 9500h
	jnz symstairloop

symstairloop2: ; iterating down the staircase
	lhld 8206h
	mov b,h 
	mov c,l
	symstairdelay2:
		lda 9500h
		out 40h
		dcx b
		mov a,b                   
		ora c
		jnz symstairdelay2
	lda 9500h
	sbi 20h
	sta 9500h
	jnz symstairloop2

jmp wavetype


division:

mvi b,00h ; bc will have quotient
mvi c,00h

lhld 8200h
mov d,h 
mov e,l 

lhld 8300h
label2:  ; repeated subtraction 
mov a,l
sub e
mov l,a
mov a,h
sbb d
mov h,a
jc label1 ; when remainder becomes negative stop incrmenting quotient 
inx b
jmp label2

label1: 
dad d    ; add to hl pair , de pair

mov a,b
sta 8401h
mov a,c
sta 8400h

ret  

rst 5
