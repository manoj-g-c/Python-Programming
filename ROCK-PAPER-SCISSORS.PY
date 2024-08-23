					ROCK-PAPER-SCISSORS-02
#importrandommodule import
random
#printmultilineinstruction
#performstring concatenationofstring
print('WinningrulesofthegameROCKPAPERSCISSORSare:\n'
+"RockvsPaper-> Paperwins \n"
+"Rockvs Scissors->Rockwins \n"
+"PapervsScissors->Scissorwins\n") while
True:
print("Enteryourchoice\n1-Rock\n2-Paper\n3-Scissors\n") # take
the input from user
choice=int(input("Enteryourchoice:"))
# OR is the short-circuit operator
#ifanyoneoftheconditionistrue #
then it return True value
#loopinguntiluserenterinvalidinput while
choice > 3 or choice <1:
choice=int(input('Enteravalidchoiceplease☺'))
#initializevalueofchoice_namevariable #
corresponding to the choice value
if choice == 1:
choice_name='Rock'
elif choice == 2:
choice_name='Paper'
else:
choice_name='Scissors'
#print userchoice
print('Userchoiceis\n',choice_name)
print('Now its Computers Turn. ..')
#Computerchoosesrandomlyanynumber
#among 1, 2and3. Usingrandintmethod #
of random module
comp_choice=random.randint(1,3)
#loopinguntilcomp_choicevalue #
is equal to the choice value while
comp_choice == choice:
comp_choice=random.randint(1,3)
#initializevalueofcomp_choice_name
#variablecorrespondingtothechoicevalue if
comp_choice == 1:
comp_choice_name='rocK' elif
comp_choice == 2:
comp_choice_name='papeR'el
se:
comp_choice_name='scissoR'
print("Computerchoiceis\n",comp_choice_name)
print(choice_name,'Vs',comp_choice_name)
#weneedtocheckofadraw if
choice == comp_choice:
print('ItsaDraw',end="")
result="DRAW"
#conditionforwinning
if(choice==1andcomp_choice==2):
print('paper wins =>',end="")
result='papeR'
elif(choice==2andcomp_choice==1):
print('paper wins =>',end="")
result='Paper'
if(choice==1andcomp_choice==3):
print('Rock wins =>\n',end= "")
result='Rock'
elif(choice==3andcomp_choice==1):
print('Rock wins =>\n',end= "")
result='rocK'
if(choice==2andcomp_choice==3):
print('Scissors wins =>',end="")
result='scissoR'
elif(choice==3andcomp_choice==2):
print('Scissors wins =>',end="")
result='Rock'
#Printingeitheruserorcomputerwinsordraw if
result == 'DRAW':
print("<==Itsatie==>") if
result == choice_name:
print("<==Userwins==>")
else:
print("<== Computer wins ==>")
print("Do you want to play again? (Y/N)")
#ifuserinputnorNthenconditionisTrue ans =
input().lower
ifans=='n':
break
#aftercomingoutofthewhileloop #
we print thanks for playing
print("thanks for playing")
