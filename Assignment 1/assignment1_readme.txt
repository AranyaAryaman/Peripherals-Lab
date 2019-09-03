			PROJECT TITLE:CALCULATOR FOR x8085 MICROPROCESSOR


The current project first takes a choice for operation from memory location 8000h.The choices are:-
	1)00h:-Addition
	2)01h:-Subtraction
	3)02h:-Multiplication
	4)03h:-Division
	5)04h:-Square root

OPERATIONS:-

1)ADDITION:-
	->Two 16 bit values are loaded from memory locations 8002h & 8004h into H-L and D-E register pairs. They are loaded using lhld command, and xchg transfers one of the values to D-E.
	->They are added using "dad" command and the carry is stored in accumulator using "adc"
	->Finally the computed sum is stored at location 8050h. The carry, if present, is stored in 8052h.

2)SUBTRACTION:-
 	->Two 16 bit values are loaded from memory locations 8002h & 8004h into H-L and D-E register pairs. They are both loaded using lhld command.
	->the minuend is transferred to register pair D-E using xchg
	  the subtraction is now performed in two parts:-
	   a)the lower 8 bits of the subtrahend is subtracted from the lower 8 bits of the minuend
	   b)the higher 8 bits of the subtrahend is subtracted from the higher 8 bits of the minuend using the borrow from step a) by "sbb".
	->finally the computed difference is stored at location 8050h.


3)MULTIPLICATION:-
	->Two 16 bit values are loaded from memory locations 8002h & 8004h into H-L register pair using lhld
	->The multiplier is transferred to register pair D-E using xchg and the multiplicand is stored in stack register using sphl
	  the multiplication is now performed in two parts:-
	   a)the multiplicand is  added to H-L register pair initialized to zero and the result is stored in H-L pair while multiplier is decreased by one. If there is no overflow and the multiplier has not reduced to zero,repeat a),else go to step b)
	   b)If there is an overflow in a),increment register pair B-C and go to a). Else quit the loop
	->Finally the computed product is stored at location 8052h and 8050h combined


4)DIVISION:-
	->Two 16 bit values are loaded from memory locations 8002h & 8004h into H-L register pair using lhld
	->The divisor is transferred to register pair D-E using xchg
	  The division is now performed in two parts:-
	   a)this step is same as subtraction operation mentioned above.If the value of H-L pair is not negative,increment register pair B-C and repeat a),else go to step b)
	   b)the value of register pair H-L is added to D-E.
	->Finally the computed quotient in B-C is stored at location 8052h and the remainder in H-L is stored at 8050h.


5)SQUARE ROOT(8 bits only):-
	->It uses the logic that 1+3+...+(2*n-1)=n^2
	->Registers D & E are initialized to zero while the number is loaded into accumulator from 8002h using lda
	   The square root is now computed in two parts:-
	   a)value of D is subtracted from accumulator.If result positive,increment D by 2 and E by 1 and repeat a),else go to b)
	   b)the value of E is transferred to accumulator and decremented by one since it stores the upper value.
	->Finally we get the integral part of computed square root in the accumulator.
