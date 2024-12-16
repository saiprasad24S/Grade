basic_Salary = int(input("Enter the basic salary: "))
if basic_Salary < 10000:
    hra=((basic_Salary*67)/100)# 67% of the sal
    da=((basic_Salary*73)/100)#73% of the sal
elif basic_Salary > 10000 and basic_Salary <20000:
    hra=((basic_Salary*69)/100)
    da=((basic_Salary*76)/100)
else:
    hra=((basic_Salary*73)/100)
    da=((basic_Salary*89)/100)
gross_Sal= basic_Salary+hra+da
print(gross_Sal)


