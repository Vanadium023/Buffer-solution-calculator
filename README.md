阅读中文版，请点击 [中文说明](docs/README._zh_CN.md).

# Buffer-solution-calculator
Buffer Concentration Calculator
## Introduction
This program is designed for calculating the required concentration of solutions for preparing acid-base buffer solutions in the laboratory. The calculation algorithm of this calculator is relatively simple, based solely on the equilibrium constant Ka of acid-base reactions, ignoring factors such as ionic strength, activity coefficients, ion atmosphere, and the effect of common ion, so the calculated results may have little errors compared to actual results.

## Notes
1.All inputs of this program are in SI units, such as mol, L. To avoid excessively small numerical values, the outputs are in commonly used units such as ml, g. If the desired units of calculation are not in these units, please convert accordingly.

2.Currently, only the pKa values of commonly used acetic acid-sodium acetate buffer solutions are included. If you want to prepare buffer solutions of other monoprotic acids, please search and input their corresponding pKa values. For polyprotic acids, due to their multiple ionization levels, calculating based on the method used for monoprotic acids may have significant errors, so it is not recommended to use this calculator for such calculations.

3.All calculated results are for reference only. It is recommended to verify the results before use. The author does not take responsibility for any experimental issues caused by incorrect calculations.

4.Note that all buffer solutions have their own buffering ranges. Beyond this range, buffer effect will not be achieved. Therefore, it is recommended to verify the choice of buffer solution type before calculating.

## Usage
1.Run the program in the terminal and input the required parameters as prompted by the program. 

2.The program will calculate the required concentration and output corresponding preparation instructions. 

3.You can use these instructions to prepare buffer solutions in the laboratory.

## Contact
For any bug reports or suggestions for improvement, please contact me at pcbs1231@outlook.com.
