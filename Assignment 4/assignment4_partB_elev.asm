cpu "8085.tbl"
hof "int8"

RDKBD: EQU 03BAH
org 9000h

LDA 8200h 		;Stores Current Boss Floor. Should be set initially.
MOV H,A
MVI A,8BH
OUT 43H 		;Setting A as o/p port, B and C as i/p port

FLOOR0:
MVI B,01H
MVI A,00H 
STA 8202H 		;8202h stores current floor of elevator
OUT 40H
CALL SEC_DLY
IN 41H			;checks if boss switch is on
ANA H
CMP H
JZ BOSS
IN 41H			;checks if floor zero the only switch pressed
CPI 00H 		;else, moves up to floor 1
JZ FLOOR0
JZ FLOOR1

FLOOR1:
MVI A,01H 
STA 8202H
OUT 40H
CALL SEC_DLY
IN 41H			;checks if floor 1 the only switch pressed
ANI 01H	
CPI 01H
JZ FLOOR1		
IN 41H			;checks if boss switch is on
ANA H
CMP H
JZ BOSS
MOV A,B			;checks if only lower floor switches pressed
CPI 00H 		;if so, move one floor down. else move up one floor.
JZ FLOOR0
IN 41H
CPI 01H
MVI B,00H
JC FLOOR0
JZ FLOOR1
MVI B,01H
JMP FLOOR2

FLOOR2:
MVI A,02H 
STA 8202H
OUT 40H
CALL SEC_DLY
IN 41H			;checks if floor 2 the only switch pressed
ANI 02H
CPI 02H
JZ FLOOR2
IN 41H			;checks if boss switch is on
ANA H
CMP H
JZ BOSS
MOV A,B			;checks if only lower floor switches pressed
CPI 00H 		;if so, move one floor down. else move up one floor.
JZ FLOOR1
IN 41H
CPI 02H
MVI B,00H
JC FLOOR1
JZ FLOOR2
MVI B,01H
JMP FLOOR3

FLOOR3:
MVI A,04H 
STA 8202H
OUT 40H
CALL SEC_DLY
IN 41H			;checks if floor 3 the only switch pressed
ANI 04H
CPI 04H
JZ FLOOR3
IN 41H			;checks if boss switch is on
ANA H
CMP H
JZ BOSS
MOV A,B			;checks if only lower floor switches pressed
CPI 00H 		;if so, move one floor down. else move up one floor.
JZ FLOOR2
IN 41H
CPI 04H
MVI B,00H
JC FLOOR2
JZ FLOOR3
MVI B,01H
JMP FLOOR4

FLOOR4:
MVI A,08H 
STA 8202H
OUT 40H
CALL SEC_DLY
IN 41H			;checks if floor 4 the only switch pressed
ANI 08H
CPI 08H
JZ FLOOR4
IN 41H			;checks if boss switch is on
ANA H
CMP H
JZ BOSS
MOV A,B			;checks if only lower floor switches pressed
CPI 00H 		;if so, move one floor down. else move up one floor.
JZ FLOOR3
IN 41H
CPI 08H
MVI B,00H
JC FLOOR3
JZ FLOOR4
MVI B,01H
JMP FLOOR5

FLOOR5:
MVI A,10H 
STA 8202H
OUT 40H
CALL SEC_DLY
IN 41H			;checks if floor 5 the only switch pressed
ANI 10H
CPI 10H
JZ FLOOR5
IN 41H			;checks if boss switch is on
ANA H
CMP H
JZ BOSS
MOV A,B			;checks if only lower floor switches pressed
CPI 00H 		;if so, move one floor down. else move up one floor.
JZ FLOOR4
IN 41H
CPI 10H
MVI B,00H
JC FLOOR4
JZ FLOOR5
MVI B,01H
JMP FLOOR6

FLOOR6:
MVI A,20H 
STA 8202H
OUT 40H
CALL SEC_DLY
IN 41H			;checks if floor 6 the only switch pressed
ANI 20H
CPI 20H
JZ FLOOR6
IN 41H			;checks if boss switch is on
ANA H
CMP H
JZ BOSS
MOV A,B			;checks if only lower floor switches pressed
CPI 00H 		;if so, move one floor down. else move up one floor.
JZ FLOOR5
IN 41H
CPI 20H
MVI B,00H
JC FLOOR5
JZ FLOOR6
MVI B,01H
JMP FLOOR7

FLOOR7:
MVI A,40H 
STA 8202H
OUT 40H
CALL SEC_DLY	
IN 41H			;checks if floor 7 the only switch pressed
ANI 40H
CPI 40H
JZ FLOOR7
IN 41H			;checks if boss switch is on
ANA H
CMP H
JZ BOSS	
MOV A,B			;checks if only lower floor switches pressed
CPI 00H 		;if so, move one floor down. else move up one floor.
JZ FLOOR6
IN 41H
ANI 0C0H
CPI 40H
MVI B,00H
JC FLOOR6
JZ FLOOR7
MVI B,01H
JMP FLOOR8

FLOOR8:
MVI B, 00H
MVI A,80H 
STA 8202H
OUT 40H
CALL SEC_DLY
IN 41H			;checks if floor 8 the only switch pressed
ANI 80H
CPI 80H
JZ FLOOR8
IN 41H			;checks if boss switch is on
ANA H
CMP H
JZ BOSS			;checks if only lower floor switches pressed
IN 41H			;check if any lower floor switches pressed. If so, move down. Else, stay.
ANI 080H
CPI 80H
JC FLOOR7
JZ FLOOR8

;second delay routine
SEC_DLY:
MVI C,03H
OUTLOOP:
LXI D,0DF00H
INLOOP:				;reapeatedly run inloop as many times as
DCX D  				;frequency of microprocessor                             
MOV A,D
ORA E                             
JNZ INLOOP
DCR C
JNZ OUTLOOP
RET

;BOSS subroutine
BOSS:                 
LDA 8202H
CMP H                 		;Compares BOSS floor with current floor(8202H memory location)
JC HIGHBOSS           		;If boss floor is higher than present location, goes to HIGHBOSS subroutine
JZ WAITS                     	;If boss is at same floor jumps to Wait1 subroutine
JMP LOWBOSS             	;If boss floor is lower than present floror, jumps to LOWBOSS subroutine

HIGHBOSS:
LDA 8202H                 	;changes elevator position to boss position(incrementing) A, then jumps to Wait1
CPI 00H
JZ INCREMENT              	;ensures A has a 1 bit somewhere in its 8 bits (highboss can be called from floor0 as well)
RLC                       	;logical left circular shift of accumulator(A)
STA 8202H
RETURN: OUT 40H
CALL SEC_DLY
LDA 8202H
CMP H
JC HIGHBOSS
JZ WAITS

LOWBOSS:                      	;changes elevator position to boss position(decrementing) A, then jumps to Wait1
LDA 8202H
RRC
STA 8202H
OUT 40H
CALL SEC_DLY
LDA 8202H
CMP H
JZ WAITS
JMP LOWBOSS

WAITS:                          ;Waits for boss floor request to go low, then goes to TOZERO subroutine
IN 41H
ANA H
CMP H
JZ WAITS
CALL SEC_DLY

TOZERO:                         ;Takes elevator with boss in it to ground floor (floor0)
LDA 8202H
RRC                             ;moves one floor down (logical circular right shift of A)
STA 8202H
OUT 40H
CALL SEC_DLY
LDA 8202H
CPI 01H
JZ FLOOR0                       ;Jumps to floor0 subroutine after boss reaches floor0
JMP TOZERO
INCREMENT:                      ;INCREMENTS location 8202H (for HIGHBOSS call from floor0)
ADI 01H
STA 8202H
JMP RETURN
