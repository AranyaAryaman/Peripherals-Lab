cpu "8085.tbl"
hof "int8"

RDKBD: EQU 03BAH
org 9000h

MVI A,8BH
OUT 43H 			;setting A as o/p port, B and C as i/p port

INIT:

MVI A,01H
STA 8000H 			;8000h stores current lighted LED - Ex. value 0000 0010 implies LED2 is on 

IN 41H
ANI 04H 			;check terminating condition
JZ END
IN 41H
ANI 40H				;play condition
JNZ INIT
IN 41H
ANI 20H				;pause condition
JZ INIT

START:

IN 41H
ANI 04H
JZ END
LDA 8000H
OUT 40H				;output LED specified in address 8000h
RLC 				;move to next LED (logical circular left shift of A)
STA 8000H
CALL SEC_DLY

IN 41H
ANI 20H
CPI 0H
JZ INIT
JMP START

;second delay routine
SEC_DLY:        
MVI C,03H
OUTLOOP:
LXI H,0DF00H
INLOOP:       			;repeatedly run inloop as many times as
DCX H       			;frequency of microprocessor
MOV A,H
ORA L
JNZ INLOOP
DCR C
JNZ OUTLOOP
RET

END: 
RST 5
