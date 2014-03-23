A simple program for calculating error propagations and formatting them for excel.

The format of 'expression:' is (a^x*b^y*...)/(c^w*d^z*...). Here are two examples:

expression:a^2*b^3/d
final result:  SQRT((((2*a*b^3)/(1*d))*ERROR[a])^2+(((3*a^2*b^2,0)/(1*d))*ERROR[b])^2+(((-1*a^2*b^3)/(1*d^2,0))*ERROR[d])^2)

expression:a*b/2
final result:  SQRT((((1*1*b)/(1*2))*ERROR[a])^2+(((1*a*1)/(1*2))*ERROR[b])^2+0)

The program doesn't differentiate between having or not having parentheses, which
speeds things up, but the notation in the result is admittedly pretty ugly so far,
but it does calculate the error propagation, so there's that. Note that if you put
any other characters in the expression, like a parentesis somewhere in the middle,
the program will either assume it's part of the name of the variable, in which case
it's a nuisance, or part of the power, in which case it will freak out. Don't
mistreat errorexpression.py, it had a rough childhood and is fragile. 

What errorexpression.py does so far:

	-accept expressions as fractions or multiplications with powers (so also
	 accepts some basic sqrts)

	-accept constants if they are written as a number and return 0 when
	 doing their error propagation (ugly but doesn't affect result)

what errorexpression.py hopes to do in the future:

	-expressions with sums and substractions

	-expressions with logs and exponents

	-expressions with square roots of sums or subtractions

	-expressions with combinations of all of that

	-less cluttered notation on the final result

	-read mail, lest it be replaced by a program that can
