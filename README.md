阅读中文版，请点击 [中文说明](./README._zh_CN.md).

# Buffer-solution-calculator
Buffer Concentration Calculator
## Introduction
This is a program for calculating the solution concentration required for acid-base buffer solution preparation in the laboratory. The calculation algorithm of the calculator is relatively simple, based only on the acid dissociation constant pKa of acid-base equilibrium, ignoring the effects of factors such as ionic strength, ion atmosphere, activity coefficient, and ionic strength. Therefore, the calculated results may have certain errors compared to the actual results, so precision calculation should be taken into consideration.

## Notes
1.All inputs of this program are in SI units, such as mol, L. To avoid excessively small numerical values, the outputs are in commonly used units such as ml, g. If the desired units of calculation are not in these units, please convert accordingly.

2.At present, only the pKa of the commonly used 7 buffer solutions is included, if you want to configure the buffer solution of other monoacids, please find the pKa by yourself; Due to the multi-level ionization, polyacids may have large errors in the calculation of monoacids, and it is not recommended to calculate them using this calculator.

3.All calculated results are for reference only. It is recommended to verify the results before use. The author does not take responsibility for any experimental issues caused by incorrect calculations.

4.Note that all buffer solutions have their own buffering ranges. Beyond this range, buffer effect will not be achieved. Therefore, it is recommended to verify the choice of buffer solution type before calculating.

## Usage
1.Run the program in the terminal and input the required parameters as prompted by the program. 

2.The program will calculate the required concentration and output corresponding preparation instructions. 

3.You can use these instructions to prepare buffer solutions in the laboratory.

## Contact
For any bug reports or suggestions for improvement, please contact me at pcbs1231@outlook.com.
