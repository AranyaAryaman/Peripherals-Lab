;To Operate - 8000-> 0:12hr or 1:24hr clock, 8001-> 0:Disable Alarm or 1:Enable Alarm, 8002-> set seconds, 8004-8003-> Enter Alarm Time

cpu "8085.tbl"
hof "int8"

org 9000h
GTHEX: EQU 030EH
CURDT: EQU 8FF1H
UPDDT: EQU 044cH
CURAD: EQU 8FEFH
UPDAD: EQU 0440H
OUTPUT:EQU 0389H
CLEAR: EQU 02BEH
RDKBD: EQU 03BAH

LXI H,8840H
MVI M,0BH

LXI H,8841H
MVI M,01H

LXI H,8842H
MVI M,0FH

LXI H,8843H
MVI M,0AH

MVI A,00H
MVI B,00H
CALL GTHEX 											;takes initial hour and minute input from keyboard
MOV H,D
MOV L,E												;the inputted values are stored in HL register

CHECK_MIN:
	MOV A,L
	CPI 60H
	JC CHECK_HR

	;Reset Minute Value
	MVI L,00H 										;reset minute field
	JMP CHECK_HR
	
CHECK_HR:
	MOV A,H
	CPI 24H
	JC COMPUTE

	;Reset Hour Value
	MVI H,00H ;reset hour field
	JMP COMPUTE

CONV_TM:
	SUI 12H
	MOV H,A
	JMP TWENTY_FOUR

COMPUTE:
	LDA 8000H
	CPI 01H
	JZ TWENTY_FOUR
	MOV A,H
	CPI 13H
	JNC CONV_TM
TWENTY_FOUR:
	MOV A,H
	SHLD CURAD 										;stores updated hour and minute
	MVI A,00H
	STA 8002H
	CALL ALARM
	LDA 8002H 										;reset seconds field
NXT_SEC:
	STA CURDT 										;stores updated seconds value
	CALL UPDAD 										;updates address field in display
	CALL UPDDT 										;updates data field in display
	CALL SEC_DLY 										;calls one second delay routine
	LDA CURDT
	INR A 											;increment second value
	DAA 											;converts to BCD format
	CPI 60H
	JNZ NXT_SEC
	LHLD CURAD
	MOV A,L
	INR A 											;increment minute value
	DAA
	MOV L,A
	CPI 60H
	JNZ COMPUTE
	MVI L,00H 										;reset minute field
	MOV A,H
	INR A 											;increment hour value
	DAA
	MOV H,A
	CPI 24H
	JNZ COMPUTE
	LXI H,0000H
	JMP COMPUTE

;routine to create a one second delay
SEC_DLY:
	MVI C,04H
L1:
	LXI D,7DFFH
L2:
	DCX D
	MOV A,D
	ORA E
	JNZ L2
	DCR C
	JNZ L1
	RET

;alarm routine
ALARM:
	LDA 8001H
	CPI 00H
	JZ ALM_FALSE
	LDA 8003H
	CMP L
	JNZ ALM_FALSE
	LDA 8004H
	CMP H
	JNZ ALM_FALSE
	
	;Outputting Alarm Message
	MVI A,00H
	MVI B,00H

	LXI H,8840H
	CALL OUTPUT										;displays message for five seconds
	CALL SEC_DLY										;when alarm time hits,
	CALL SEC_DLY										;then resumes execution.
	CALL SEC_DLY
	CALL SEC_DLY
	CALL SEC_DLY
	CALL CLEAR
	MVI A,05H
	STA 8002H
ALM_FALSE:
	RET
