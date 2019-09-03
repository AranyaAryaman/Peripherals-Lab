cpu "8085.tbl"
hof "int8"

org 8fbfh
JMP 8820H				;RST 7.5 is directed here

org 9000h
GTHEX: EQU 030EH			;Gets hex digits from keyboard
HXDSP: EQU 034FH			;Expands hex digits for display
OUTPUT:EQU 0389H			;Outputs characters to display
CLEAR: EQU 02BEH			;Clears the display
RDKBD: EQU 03BAH			;Reads keyboard
KBINT: EQU 3CH				;keyboard interrupt
CURDT: EQU 8FF1H			;address of monitor data field
UPDDT: EQU 044cH			;update data field
CURAD: EQU 8FEFH			;address of monitor address field
UPDAD: EQU 0440H			;update address field

MVI A,00H 					
MVI B,00H 					

LXI H,8840H
MVI M,0CH

LXI H,8841H
MVI M,11H

LXI H,8842H
MVI M,00H

LXI H,8843H
MVI M,0CH

MVI A,00H
MVI B,00H
CALL GTHEX 		;takes initial hour and minute input from keyboard
MOV H,D
MOV L,E			;the inputted values are stored in HL register
MOV A,01H
STA 8000H

CHECK_MIN:
	MOV A,L
	CPI 60H
	JC CHECK_HR
	MVI L,00H 	;reset minute field
	JMP CHECK_HR
	
CHECK_HR:
	MOV A,H
	CPI 13H
	JC START_ZERO

RESET_HR:
	MVI H,00H 	;reset hour field

START_ZERO:
	SHLD CURAD
	MVI A,00H
	JMP NXT_SEC

HR_MIN:
	SHLD CURAD 	;stores updated hour and minute
	MVI A,59H 	;reset second field
NXT_SEC:
	
	MOV B,A
	MVI A,1BH
	SIM		;sets interrupts and enables interrupts
	EI
	MOV A,B
	
	;loops when timer is in 'pause' mode. Else, continues.
	MOV B,A
	CHECK: LDA 8000H
	CPI 01H
	JNZ CONT
	CALL SEC_DLY
	JMP CHECK
	CONT: MOV A,B

	STA CURDT 	;stores updated seconds value
	CALL UPDAD 	;updates address field in display
	CALL UPDDT 	;updates data field in display
	CALL SEC_DLY 	;calls one second delay routine
	LDA CURDT
	ADI 99H 	;decrement seconds value
	DAA 		;converts to BCD format
	CPI 99H
	JNZ NXT_SEC
	LHLD CURAD
	MOV A,L
	ADI 99H 	;decrement minute value
	DAA
	MOV L,A
	CPI 99H
	JNZ HR_MIN
	MVI L,59H 	;reset minute field
	MOV A,H
	ADI 99H 	;decrement hour value
	DAA
	MOV H,A
	CPI 99H
	JNZ HR_MIN

	LXI H,8840H	;Displays 'CL' on completion
	CALL OUTPUT
	CALL RDKBD
	CALL CLEAR 
	RST 5

;routine to create a one second delay
SEC_DLY:
	MVI C,04H
L1:
	LXI D,7CFFH
L2:
	DCX D
	MOV A,D
	ORA E
	JNZ L2
	DCR C
	JNZ L1
	RET

;interrupt service routine
org 8820h
ISR:
	PUSH PSW
	LDA 8000H
	CPI 00H
	JZ PAUSE 
	MVI A,00H
	STA 8000H
	JMP END_ISR
	PAUSE:
	MVI A,01H
	STA 8000H
	
	END_ISR: POP PSW
	EI
	RET
