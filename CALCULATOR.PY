					CALCULATOR-1
def addition():
os.system('cls'ifos.name=='nt'else'clear')
print('Addition')
continue_calc='y'
num_1 = float(input('Enter a number: '))
num_2=float(input('Enteranothernumber:'))
ans = num_1 + num_2
values_entered = 2
print(f'Currentresult:{ans}')
while continue_calc.lower() == 'y':
continue_calc=(input('Entermore(y/n):'))
while continue_calc.lower() not in ['y', 'n']:
print('Please enter \'y\' or \'n\'')
continue_calc=(input('Entermore(y/n):'))
ifcontinue_calc.lower()=='n':
break
num=float(input('Enteranothernumber:'))
ans += num
print(f'Currentresult:{ans}')
values_entered += 1
return[ans,values_entered]
def subtraction():
os.system('cls'ifos.name=='nt'else'clear')
print('Subtraction')
continue_calc='y'
num_1 = float(input('Enter a number: '))
num_2=float(input('Enteranothernumber:'))
ans = num_1 - num_2
values_entered = 2
print(f'Currentresult:{ans}')
while continue_calc.lower() == 'y':
continue_calc=(input('Entermore(y/n):'))
while continue_calc.lower() not in ['y', 'n']:
print('Please enter \'y\' or \'n\'')
continue_calc=(input('Entermore(y/n):'))
ifcontinue_calc.lower()=='n':
break
num=float(input('Enteranothernumber:'))
ans -= num
print(f'Currentresult:{ans}')
values_entered += 1
return[ans,values_entered]
defmultiplication():
os.system('cls'ifos.name=='nt'else'clear')
print('Multiplication')
continue_calc='y'
num_1 = float(input('Enter a number: '))
num_2=float(input('Enteranothernumber:'))
ans = num_1 * num_2
values_entered =2
print(f'Currentresult:{ans}')
while continue_calc.lower() == 'y':
continue_calc=(input('Entermore(y/n):'))
while continue_calc.lower() not in ['y', 'n']:
print('Please enter \'y\' or \'n\'')
continue_calc=(input('Entermore(y/n):'))
ifcontinue_calc.lower()=='n':
break
num=float(input('Enteranothernumber:'))
ans *= num
print(f'Currentresult:{ans}')
values_entered += 1
return[ans,values_entered]
def division():
os.system('cls'ifos.name=='nt'else'clear')
print('Division')
continue_calc='y'
num_1=float(input('Enteranumber:'))
num_2=float(input('Enteranothernumber:'))
while num_2 == 0.0:
print('Please enter a second number > 0')
num_2=float(input('Enteranothernumber:'))
ans = num_1 / num_2
values_entered = 2
print(f'Currentresult:{ans}')
while continue_calc.lower() == 'y':
continue_calc=(input('Entermore(y/n):'))
while continue_calc.lower() not in ['y', 'n']:
print('Please enter \'y\' or \'n\'')
continue_calc=(input('Entermore(y/n):'))
ifcontinue_calc.lower()=='n':
break
num=float(input('Enteranothernumber:'))
while num == 0.0:
print('Pleaseenter anumber>0')
num=float(input('Enteranothernumber:')) ans
/= num
print(f'Currentresult:{ans}')
values_entered += 1
return[ans,values_entered]
defcalculator():
quit = False
whilenotquit:
results=[]
print('SimpleCalculatorinPython!')
print('Enter \'a\' for addition')
print('Enter \'s\' for substraction')
print('Enter\'m\'formultiplication')
print('Enter \'d\' for division')
print('Enter \'q\' to quit')
choice=input('Selection:')
ifchoice=='q': quit
= True continue
if choice == 'a':
results=addition()
print('Ans=',results[0],'totalinputs:',results[1]) elif
choice == 's':
results=subtraction()
print('Ans=',results[0],'totalinputs:',results[1]) elif
choice == 'm':
results=multiplication()
print('Ans=',results[0],'totalinputs:',results[1]) elif
choice == 'd':
results=division()
print('Ans=',results[0],'totalinputs:',results[1]) else:
print('Sorry,invalidcharacter')
if name =='main':
calculator()

