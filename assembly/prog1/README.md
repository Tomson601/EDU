# Notes:
Anything starting with a period is called **assembler directives**  
The .section commands brekas the program up into sections  

The ```.section .data``` starts the data section where we can list any memory storage we will need for data  

The ```.section .text``` starts the test section where the program instruction lives.  

The ```.globl _start```:  
This instruct the assembler that ```_start``` is important to remember. ```_start``` is a symbol which means that it is going to be replaced by something else during assembly ort linking.  
```.globl``` means that the assembler shouldn't discard this symbol after assembly becouse the linker will need it.
The ```.globl _start``` means the start of the program, without it the computer will not know where to start program.  

The first instruction is:  
```movl $1, %eax```  
this transfers the number 1 into the %eax register.  
source --> destination  

The dollar sign `$` refers to immediate addressing mode (loading actual number), without it we would load whatever number is at address number 1.

