#缓冲液浓度计算
#公式：c = 10 ^ (-x) + 10 ^ (pH - pKa - x) pKa(HAc) = 4.757
import math
while True:
    def concentration(c, pH, pKa):
        x = float(math.log10((1 + 10 ** (pH - pKa))/ c ))
        return x 

    #给定pH找出最适的缓冲液
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

    #定义缓冲液的信息的类，内容分别为：缓冲液名称，配制的试剂种类，缓冲液pKa，酸碱摩尔质量，酸碱密度
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

    #常用缓冲液信息列表
    Sodium_formate = Solution('甲酸钠缓冲液','HCOOH','HCOONa',3.745,46.03,1.23,68.01,0)
    Sodium_acetate = Solution('乙酸钠缓冲液','HAc','NaAC',4.757,60.05,1.05,80.03,0)
    Disodium_malonate = Solution('丙二酸钠缓冲液','NaHMA','Na2MA',5.696,112.06,0,142.07,0)
    Sodium_dihydrogen_phosphate = Solution('中性PBS缓冲液','NaH2PO4','Na2HPO4',7.199,119.98,0,141.96,0)
    ammonium_chloride = Solution('氯化铵缓冲液','NH4Cl','NH3·H2O',9.25,53.49,0,35.05,0.91)
    sodium_carbonate = Solution('碳酸钠缓冲液','NaHCO3','Na2CO3',10.25,84.01,0,105.99,0)
    Disodium_hydrogen_phosphate = Solution('碱性PBS缓冲液','Na2HPO4','Na3PO4',12.35,141.96,0,163.94,0)

    #缓冲液列表
    buffer_solution = [Sodium_formate,Sodium_acetate,Disodium_malonate,
                       Sodium_dihydrogen_phosphate,ammonium_chloride,
                       sodium_carbonate,Disodium_hydrogen_phosphate]

    #利用buffer_solution建立一个数组，每个元素为一种缓冲液的pKa值
    buffer_pKa = []
    for i in buffer_solution:
        buffer_pKa.append(i.pKa)

    #列出程序收录的缓冲液数据
    form_title = ['序号','缓冲液名称','配制的试剂种类','缓冲液pKa']
    print()
    print("-"*26+"常用缓冲液列表"+"-"*26)
    print()
    print(f"{form_title[0]:<5}\t{form_title[1]:<17}\t{form_title[2]:<10}\t{form_title[3]:<5}")
    print()

    #用f-string打印出缓冲液信息的表格，第一列是从1开始的序号，表格用占位符对齐
    j = 1
    for i in buffer_solution:
        print(f" {j:<4}\t{i.name:<13}\t{i.formula_acid}-{i.formula_alkali:<15}\t{i.pKa:<10}")
        j += 1
    print('-'*66)

    Choise = input('请输入要配制的缓冲液的序号，如果未确定缓冲液的选择，或待计算缓冲液不再列表中，请输入def:')
    if Choise == 'def':
        Choise_2 = input('请选择模式，输入1自定义缓冲液，输入0可帮助选择最适缓冲液:')
        if Choise_2 == '1':
            pKa = float(input('请自行查阅缓冲液的酸或酸式盐的pKa值'))
        if Choise_2 == '0':
            pH = float(input('请输入目标缓冲液的pH值'))
            buffer_index = find_pKa(buffer_pKa,pH)
            best_buffer_index = best_pKa(buffer_pKa,pH)
            print()
            print(f'由于你需求的缓冲溶液的pH为{pH}，下面的缓冲液可满足要求')
            for a in buffer_index:
                print(f'{buffer_solution[a].name:<13} pKa={buffer_solution[a].pKa}')
            if len(buffer_index) == 0:
                print('这个pH的缓冲液的性能都不太好，但可以参考下面的建议')

            if len(best_buffer_index) == 1:
            # 如果只有一个元素，直接根据索引获取缓冲液的名字，并用f-string格式化输出
                output = f"比较适合的缓冲液为-{buffer_solution[best_buffer_index[0]].name}"
            elif len(best_buffer_index) == 2:
            # 如果有两个元素，分别根据索引获取缓冲液的名字，并用f-string格式化输出，并用破折号和“和”连接
                output = f"比较适合的缓冲液为-{buffer_solution[best_buffer_index[0]].name}-和-{buffer_solution[best_buffer_index[1]].name}-"
            # 打印输出
            print(output)
            print()
            input('请自行选择最适的缓冲液，按enter重新开始')
            continue

    #缓冲液选择
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
        print(f'你选择的缓冲液为{buffer_solution[int(Choise)-1].name}，pKa为{pKa}')
    else:
        print('输入错误,请重新输入')
        continue

    #缓冲液参数输入
    pH = float(input('请输入缓冲液目标pH:'))
    c = float(input('请输入缓冲液溶质的总浓度，单位mol/L：'))
    if Choise != 'def':
        v = float(input('请输入要配制的体积(单位：L)，只算浓度的话就输入0：'))
    else:
        v = 0

    #缓冲液配方计算
    x = concentration(c, pH, pKa)
    c_acid =  10 ** (-x)
    c_alkali = 10 ** (pH - pKa - x)
    print("缓冲液配方计算完毕，下面是条件与配方")
    print("-"*26+"缓冲液条件"+"-"*26)
    if Choise != 'def':
        print(f'名称：{buffer_solution[int(Choise)-1].name}')
    else:
        print(f'pKa： {pKa}')
    print(f'pH：  {pH}')
    print(f'浓度：{c}mol/L')
    if v != 0:
        print(f'体积：{v}L')
    print("-"*26+"缓冲液配方"+"-"*26)
    if Choise == 'def':
        print(f'酸的浓度{c_acid}mol/L')
        print(f'碱的浓度{c_alkali}mol/L')
    else:
        print(f'{formula_acid:<10}的浓度{c_acid}mol/L')
        print(f'{formula_alkali:<10}的浓度{c_alkali}mol/L')
        if v != 0:
            m_acid_g = c_acid * v * M_acid
            m_alkali_g = c_alkali * v * M_alkali
            print()
            if d_acid != 0:
                v_acid_ml = m_acid_g / d_acid
                print(f'{formula_acid:<10}的体积{v_acid_ml}ml')
            else:
                print(f'{formula_acid:<10}的质量{m_acid_g}g')
            if d_alkali != 0:
                v_alkali_ml = m_alkali_g / d_alkali
                print(f'{formula_alkali:<10}的体积{v_alkali_ml}ml')
            else:
                print(f'{formula_alkali:<10}的质量{m_alkali_g}g')
            print(f'加蒸馏水定容至{v}L即可')
            
    print('-'*62)
    if abs(pH - pKa) > 1 and Choise != 'def':
        print('温馨提示：')
        print(f'{buffer_solution[int(Choise)-1].name}的最佳缓冲范围为{pKa-1}-{pKa+1}')
        print(f'pH为{pH}的缓冲液不建议用{buffer_solution[int(Choise)-1].name}配制')
    if v != 0:
        if d_acid != 0 and v_acid_ml < 0.00001:
            print(f"{formula_acid}的体积较少，准确量取可能较困难，建议用大体系或者更换缓冲液")
        elif d_acid == 0 and m_acid_g < 0.001:
            print(f"{formula_acid}的质量较少，准确称可能较困难，建议用大体系或者更换缓冲液")
        if d_alkali != 0 and v_alkali_ml < 0.00001:
            print(f"{formula_alkali}的体积较少，准确量取可能较困难，建议用大体系或者更换缓冲液")
        elif d_alkali == 0 and m_alkali_g < 0.001:
            print(f"{formula_alkali}的质量较少，准确量取可能较困难，建议用大体系或者更换缓冲液")
    print('-'*62)
    print()
    m_acid_g = m_alkali_g = v_acid_ml = v_alkali_ml = v = 0
    input('按enter键重新开始计算')