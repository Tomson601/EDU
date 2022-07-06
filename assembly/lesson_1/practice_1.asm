.global _start
_start:
    MOV R0,#30          //Move decimal 30 into R0 register

    MOV R7,#1           //Moving dec 1 into R7 (special) register indicates termintating process
    SWI 0
