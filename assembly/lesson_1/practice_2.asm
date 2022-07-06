.global _start
_start:					//Load data from stack into register
	LDR R0,=list		//R0 stores values from list
	
	LDR R1,[R0]			//Inserting data from R0 (brackets) to R1

	LDR R2,[R0,#4]!		//Load R0 index + 4 into register R2 with pre-icrement
	MOV R7,#1
	SWI 0

.data					//Creating variables section
list: 
	.word 1,6,7,2,8,9	//Adding values to variablename "list" 
