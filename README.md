# Assignment 3b: Scientific E notation

Scientific E notation is a way of presenting very large or very small numbers in scientific notation (i.e. standard form) without the `×` symbol, superscripts, or subscripts.

### Example

The following examples show text-based scientific notation on the left and scientific E notation on the right:

1. `"1.03x10^7"` → `"1.03E7"`
2. `"2.008x10^-5"` → `"2.008E-5"`

In both examples, the letter `x` represents the 'multiply' mathematical operator, while the caret symbol (`^`) represents the 'power of' mathematical operator. In example 1, the `1.03` part of the number is called the **mantissa** (or *significand*), while the power of 10, i.e. the `7`, is called the **exponent**.

Write program code to:

1. Ask the user to input a number in valid scientific notation
2. Extract the mantissa and exponent from user input  
   You may assume that the user input will be valid.
4. Print the number in scientific E notation.

*Hint: You can search for the positions of special characters in scientific notation to extract substrings from user input.*

### Expected output:

    Enter a number in scientific notation: 1.1x10^-3
    This number in E notation is 1.1E-3.
    
    Enter a number in scientific notation: -1.5x10^3
    This number in E notation is -1.5E3.
    
# Submission

Before submitting, run the tests on your final code.
