#Buffer concentration calculation
#formula:c = 10 ^ (-x) + 10 ^ (pH - pKa - x)
import math
while True:
    def concentration(c, pH, pKa):
        x = float(math.log10((1 + 10 ** (pH - pKa))/ c ))
        return x 

    #Find the optimal buffer for a given pH
    def best_pKa(pKa,pH):
        abs_pKa = [abs(x - pH) for x in pKa]
        best_buffer_index = [i for i, x in enumerate(abs_pKa) if x == min(abs_pKa)]
        return best_buffer_index

    def find_pKa(pKa,pH):
        abs_pKa = [abs(x - pH) for x in pKa]
        buffer_index = []
        for i, x in enumerate(abs_pKa):
            if x < 1:
                buffer_index.append(i)
        return buffer_index

    #The class of buffer information that defines the buffer, namely: 
    # buffer name, type of reagent prepared, buffer pKa, acid-base molar mass, acid-base density
    class Solution:
        def __init__(self,name,formula_acid,formula_alkali,pKa,M_acid,d_acid,M_alkali,d_alkali):
            self.name = name
            self.formula_acid = formula_acid
            self.formula_alkali = formula_alkali
            self.pKa = pKa
            self.M_acid = M_acid
            self.d_acid = d_acid
            self.M_alkali = M_alkali
            self.d_alkali = d_alkali

    #List of commonly used buffer information
    Sodium_formate = Solution('Sodium_formate','HCOOH','HCOONa',3.745,46.03,1.23,68.01,0)
    Sodium_acetate = Solution('Sodium_acetate','HAc','NaAC',4.757,60.05,1.05,80.03,0)
    Disodium_malonate = Solution('Disodium_malonate','NaHMA','Na2MA',5.696,112.06,0,142.07,0)
    Sodium_dihydrogen_phosphate = Solution('Neutral PBS buffer','NaH2PO4','Na2HPO4',7.199,119.98,0,141.96,0)
    ammonium_chloride = Solution('ammonium_chloride','NH4Cl','NH3·H2O',9.25,53.49,0,35.05,0.91)
    sodium_carbonate = Solution('sodium_carbonate','NaHCO3','Na2CO3',10.25,84.01,0,105.99,0)
    Disodium_hydrogen_phosphate = Solution('Alkaline PBS buffer','Na2HPO4','Na3PO4',12.35,141.96,0,163.94,0)

    #List of buffers
    buffer_solution = [Sodium_formate,Sodium_acetate,Disodium_malonate,
                       Sodium_dihydrogen_phosphate,ammonium_chloride,
                       sodium_carbonate,Disodium_hydrogen_phosphate]

    buffer_pKa = []
    for i in buffer_solution:
        buffer_pKa.append(i.pKa)

    #List the buffer data included in the program
    form_title = ['numbering', 'Buffer name', 'formulation', 'Buffer pKa']
    print()
    print("-"*26+"commonly used buffers"+"-"*26)
    print()
    print(f"{form_title[0]:<0}\t{form_title[1]:<6}\t{form_title[2]:<20}\t{form_title[3]:<5}")
    print()

    j = 1
    for i in buffer_solution:
        print(f" {j:<4}\t{i.name:<20}\t{i.formula_acid}-{i.formula_alkali:<15}\t{i.pKa:<10}")
        j += 1
    print('-'*66)

    Choise = input('Please enter the index of the buffer solution to be configured. If the buffer solution selection is not yet determined, or the desired buffer solution is not in the list, please enter‘def’:')
    if Choise == 'def':
        Choise_2 = input('Select mode: Enter 1 for custom buffer solution, 0 for assistance in selecting the most suitable buffer solution:')
        if Choise_2 == '1':
            pKa = float(input('Please refer to the pKa values of the acid or acid salt in the buffer solution'))
        if Choise_2 == '0':
            pH = float(input('Please enter the pH of the buffer of interest:'))
            buffer_index = find_pKa(buffer_pKa,pH)
            best_buffer_index = best_pKa(buffer_pKa,pH)
            print()
            print(f'Since the pH of the buffer solution you need is {pH}, the buffer below will suffice')
            for a in buffer_index:
                print(f'{buffer_solution[a].name:<13} pKa={buffer_solution[a].pKa}')
            if len(buffer_index) == 0:
                print('The performance of this pH buffer is not very good, but you can refer to the recommendations below')

            if len(best_buffer_index) == 1:
            # If there is only one element, get the name of the buffer directly from the index and format the output with f-string
                output = f"A suitable buffer solution is -{buffer_solution[best_buffer_index[0]].name}"
            elif len(best_buffer_index) == 2:
            # If there are two elements, get the name of the buffer according to the index, respectively, and format the output with f-string, concatenated with dashes and "and"
                output = f"A suitable buffer solution is -{buffer_solution[best_buffer_index[0]].name}-and-{buffer_solution[best_buffer_index[1]].name}-"
            
            print(output)
            print()
            input('Please choose the most suitable buffer and press Enter to start over')
            continue

    #Buffer selection
    elif Choise in ['1','2','3','4','5','6']:
        pKa = buffer_solution[int(Choise)-1].pKa
        M_acid = buffer_solution[int(Choise)-1].M_acid
        M_alkali = buffer_solution[int(Choise)-1].M_alkali
        formula_acid = buffer_solution[int(Choise)-1].formula_acid
        formula_alkali = buffer_solution[int(Choise)-1].formula_alkali
        if buffer_solution[int(Choise)-1].d_acid != 0:
            d_acid = buffer_solution[int(Choise)-1].d_acid
        else:
            d_acid = 0
        if buffer_solution[int(Choise)-1].d_alkali != 0:
            d_alkali = buffer_solution[int(Choise)-1].d_alkali
        else:
            d_alkali = 0
        print(f'The buffer solution of your choice is{buffer_solution[int(Choise)-1].name}，pKa为{pKa}')
    else:
        print('Input error, please re-enter')
        continue

    #Buffer parameter input
    pH = float(input('Please enter the buffer target pH:'))
    c = float(input('Please enter the total concentration of buffer solute in mol/L:'))
    if Choise != 'def':
        v = float(input('Please enter the volume (unit: L) to be prepared, and enter 0 if you only calculate the concentration:'))
    else:
        v = 0

    #Buffer recipe calculation
    x = concentration(c, pH, pKa)
    c_acid =  10 ** (-x)
    c_alkali = 10 ** (pH - pKa - x)
    print("After the buffer recipe is calculated, here are the conditions and recipes")
    print("-"*26+"Buffer conditions"+"-"*26)
    if Choise != 'def':
        print(f'name:{buffer_solution[int(Choise)-1].name}')
    else:
        print(f'pKa: {pKa}')
    print(f'pH:  {pH}')
    print(f'concentration:{c}mol/L')
    if v != 0:
        print(f'volume:{v}L')
    print("-"*26+"Buffer formulation"+"-"*26)
    if Choise == 'def':
        print(f'The concentration of acid{c_acid}mol/L')
        print(f'The concentration of alkali{c_alkali}mol/L')
    else:
        print(f'The concentration of{formula_acid:<10}is{c_acid}mol/L')
        print(f'The concentration of{formula_alkali:<10}is{c_alkali}mol/L')
        if v != 0:
            m_acid_g = c_acid * v * M_acid
            m_alkali_g = c_alkali * v * M_alkali
            print()
            if d_acid != 0:
                v_acid_ml = m_acid_g / d_acid
                print(f'The volume of{formula_acid:<10}is{v_acid_ml}ml')
            else:
                print(f'The mass of{formula_acid:<10}is{m_acid_g}g')
            if d_alkali != 0:
                v_alkali_ml = m_alkali_g / d_alkali
                print(f'The volume of{formula_alkali:<10}is{v_alkali_ml}ml')
            else:
                print(f'The mass of{formula_alkali:<10}is{m_alkali_g}g')
            print(f'Add distilled water to set the volume to {v}L')
            
    print('-'*62)
    if abs(pH - pKa) > 1 and Choise != 'def':
        print('Tips:')
        print(f'The optimal buffer range for {buffer_solution[int(Choise)-1].name}is{pKa-1}-{pKa+1}')
        print(f'Buffers with a pH of {pH} are not recommended to be prepared with {buffer_solution[int(Choise)-1].name}')
    if v != 0:
        if d_acid != 0 and v_acid_ml < 0.00001:
            print(f"The volume of {formula_acid} is small, accurate measurement may be difficult, it is recommended to use a large system or change buffer")
        elif d_acid == 0 and m_acid_g < 0.001:
            print(f"{formula_acid} has less mass, accurate weighing may be difficult, and it is recommended to use a large system or change buffer")
        if d_alkali != 0 and v_alkali_ml < 0.00001:
            print(f"The volume of {formula_alkali} is small, and accurate measurement may be difficult, it is recommended to use a large system or change buffer")
        elif d_alkali == 0 and m_alkali_g < 0.001:
            print(f"{formula_alkali} has less mass, accurate measurement may be difficult, it is recommended to use a large system or change buffer")
    print('-'*62)
    print()
    m_acid_g = m_alkali_g = v_acid_ml = v_alkali_ml = v = 0
    input('Press Enter to restart the calculation')