.global _start
_start:					//Load data from stack into register
	LDR R0,=list		//First number (1) will be inserted into register 0
	
	LDR R1,[R0]			//Inserting data from R0 (brackets) to R1

	LDR R2,[R0,#4]!		//Load R0 index + 4 into register R2 with pre-icrement

.data					//Creating variables section
list: 
	.word 1,6,7,2,8,9	//Adding values to variablename "list" 
