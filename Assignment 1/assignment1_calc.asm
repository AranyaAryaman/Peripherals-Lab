cpu "8085.tbl"
hof "int8"

org 9000h     ; starting address of code segment

lda 8000h     ; check the operand at 8000h

cpi 00h         ; (operand,operator) = (0,add) (1,subtract) (2,multiply) (3,division) (4,square_root)
jz OP0
cpi 01h
jz OP1
cpi 02h			; jump to different labels depending on the above 
jz OP2
cpi 03h
jz OP3
cpi 04h
jz OP4
jmp HALT

//Addition
OP0:
	lhld 8002h         ; load first two numbers into h and l registers
	xchg                ; store it in d and e
	lhld 8004h			; load second numbers into h & l now
	dad d  				; add d to l 
	mvi a,00h			
	adc a				; store the carry in a register
	sta 8052			; store the final answer in 8052
	shld 8050
	jmp HALT			; final answers are stored in h&l ,halt once done

//Subtraction
OP1:
	lhld 8002h               ; similar to addition , load first into h& l
	xchg					; exchange it with d & e
	lhld 8004h			; load next two numbers in h& l respectively
	mov a,e				; move value in e to accumalator a register
	sub l				; subtract l from value stored in accumulator
	sta 8052			; store the result at address 8052
	mov a,d				; move value of d in a
	sbb h				; subtract h with borrow(if any) from previous subtraction from the value stored in accumulator i.e. register a 
	sta 8053			; store this result in 8053
	jmp HALT			; the final answer is stored in 8053_8052 i.e. first 8 bits in 8053 and last 8 bits in 8052, once done halt the program

//Multiplication
OP2:
	lhld 8002h		;Load the first data in HL pair.
	sphl 			;Move content of HL pair to stack pointer.
	lhld 8004h		;Load the second data in HL pair and move it to DE.
	xchg			;Make H register as 00H and L register as 00H.

	lxi h, 0000h                 
	lxi b, 0000h

	L21:
	dad sp			;ADD HL pair and stack pointer.
	jnc L22			;Check for carry if carry increment it by 1 else move to next step.
	inx b

	L22:
	dcx d
	mov a,e		;Then move E to A and perform OR operation with accumulator and register D.
	ora d
	jnz L21		;The value of operation is zero, then store the value else goto step 3

	shld 8050
	mov h,b
	mov l,c
	shld 8052
	jmp HALT

//Division
OP3:
	lxi b,0000h   ;Intialise register BC as 0000H for Quotient.
	lhld 8002		;Load the divisor in HL pair and save it in DE register pair.
	xchg
	lhld 8004		;Load the dividend in HL pair.

	L31:
	mov a,l
	sub e		 ;Subtract the content of accumulator with E register.
	mov l,a			; Move the content A to C and H to A.
	mov a,h
	sbb d		;Subtract with borrow the content of A with D
	mov h,a		;Move the value of accumulator to H
	jm L32		;If CY=1, goto L32, otherwise next step.
	inx b		;Increment register B and jump to step 4
	jmp L31

	L32:
	dad d			;ADD both contents of DE and HL.
	shld 8050		;Store the remainder in memory.
	mov l,c
	mov h,b			;Move the content of C to L & B to H.
	shld 8052		;Store the quotient in memory.
	jmp HALT		; Halt once done

//Square Root
OP4:
	mvi d, 01
	mvi e, 01 		; using the notion that sum of first n odd numbers is n^2 , we start subtracting odd numbers by incrementing by 2 every time 
	lda 8002h		; load the 8 bit number into 8002h
	L41: 
	sub d			; start by subtracting the number from 1
	mvi h, 00		; if difference is 0 , jump to L42 , store the result in a and halt 
	cmp h
	jm L42		
	inr d			; else increment d twice (since two consecutive odd numbers have a difference of 2)
	inr d
	inr e			; continue the loop till the condition is satisfied
	jmp L41
	L42:
	mov a,e			; storing of the answer in register a i.e. accumulator
	dcr a

HALT:
	rst 5
