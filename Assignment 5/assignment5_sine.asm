cpu "8085.tbl"
hof "int8"

org 9000h 

SINE:
								;Load Accumulator from 8100 to 8124H
MVI A,00H							;with known sine values 
STA 8100h							;to create a sine lookup table
MVI A,01H
STA 8101h
MVI A,02H
STA 8102h
MVI A,04H
STA 8103h
MVI A,08H
STA 8104h
MVI A,011H
STA 8105h
MVI A,17H
STA 8106h
MVI A,1EH
STA 8107h
MVI A,25H
STA 8108h
MVI A,2DH
STA 8109h
MVI A,36H
STA 810Ah
MVI A,40H
STA 810Bh
MVI A,49H
STA 810Ch
MVI A,54H
STA 810Dh
MVI A,5EH
STA 810Eh
MVI A,69H
STA 810Fh
MVI A,74H
STA 8110h
MVI A,7FH
STA 8111h
MVI A,84H
STA 8112h
MVI A,95H
STA 8113h
MVI A,9FH
STA 8114h
MVI A,0AFH
STA 8115h
MVI A,0B4H
STA 8116h
MVI A,0C0H
STA 8117h
MVI A,0C8H
STA 8118h
MVI A,0D0H
STA 8119h
MVI A,0D8H
STA 811Ah
MVI A,0E0H
STA 811Bh
MVI A,0EAH
STA 811Ch
MVI A,0EDH
STA 811Dh
MVI A,0EFH
STA 811Eh
MVI A,0F2H
STA 811Fh
MVI A,0F9H
STA 8120h
MVI A,0FCH
STA 8121h
MVI A,0FDH
STA 8122h
MVI A,0FFH
STA 8123h
MVI A,00H
STA 8124h


MVI A,8BH ;setting 8255 to mode0 and port a o/p and port b,c i/p
OUT 43H

START:
	MVI C,24H ;counter initialized
	LXI H,8100H ;memory pointer initialized
;move up look-up table and display
POS:
	MOV A,M ;load sine value from memory
	OUT 40H	;display value
	INX H	;moving to next memory value
	DCR C
	JNZ POS
	MVI C,24H
;move down look-up table and display
NEG:
	DCX H
	MOV A,M
	OUT 40H
	DCR C
	JNZ NEG
	JMP START

RST 5
