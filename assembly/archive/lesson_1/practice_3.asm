.global _start

_start:
    LDR R0,=list1
    LDR R1,=list2

    LDR R2,[R0]
    LDR R3,[R1]

    MOV R7,#1
    SWI 0

.data
list1:
    .word 1,2,3,4,5,6
list2:
    .word 6,5,4,3,2,1
