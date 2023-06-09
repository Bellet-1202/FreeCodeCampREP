def arithmetic_arranger(problems,val=False):
  if any(isinstance(el,list) for el in problems):
      problems0 = problems
  else:
      problems0 = problems, True
  tab = [[]]
  spl = []
  arranged_problems = ""
  if len(problems0[0]) > 5:
      return("Error: Too many problems.")
  for i in problems0[0]:
      spl += i.split(" ")
    
  spl_iterator = 0
  for tab_i in range(0,len(problems0[0])):
      tab[tab_i].insert(0, spl[spl_iterator])
      spl_iterator += 1
      tab[tab_i].insert(1, spl[spl_iterator])
      spl_iterator += 1
      tab[tab_i].insert(2, spl[spl_iterator])
      spl_iterator += 1
      if tab_i < len(problems0[0])-1:
          tab.append([])


  for i in range(len(problems0[0])-1):
      if not tab[i][0].isdigit() or not tab[i][2].isdigit():
        return("Error: Numbers must only contain digits.")
    
      if tab[i][1] != '+' and tab[i][1] != '-':
        return("Error: Operator must be '+' or '-'.")
    
      if len(tab[i][0]) > 4 or len(tab[i][2]) > 4:
        return("Error: Numbers cannot be more than four digits.")
    ###########################################################
  operation_size_list = []    #CALCOLO DELLA DIMENSIONE ORIZZONTALE DELLE OPERAZIONI
  for i in tab:  
    long_num = "0"
    operation_size = 0
    for el in i: 
      if(el.isdigit() and int(long_num) < int(el)):
        long_num = el
    operation_size = len(long_num) + 2
    operation_size_list.append(operation_size)
    
  tab_i = 0   #CICLO STAMPA DEI PRIMI NUMERI
  operation_size_i=0
  for i in tab:
    arranged_problems += " " *(operation_size_list[operation_size_i] - len(i[tab_i]) ) + i[tab_i] + " "*4
    operation_size_i +=1
  arranged_problems = arranged_problems.rstrip()
  arranged_problems +="\n"
    
  tab_i = 2   #CICLO STAMPA DEI SECONDI NUMERI
  operation_size_i=0
  for i in tab:   
    arranged_problems += i[1] + " " *(operation_size_list[operation_size_i] - len(i[tab_i])-1 ) + i[tab_i] + " "*4 
    operation_size_i +=1
  arranged_problems = arranged_problems.rstrip()
  arranged_problems += "\n"
    
  for i in operation_size_list:   #CICLO STAMPA DEI DASH
    arranged_problems += "-" * i + " "*4
  arranged_problems = arranged_problems.rstrip()
  arranged_problems += "\n"


  if(val):  #CICLO STAMPA DEI RISULTATI
    operation_size_i=0
    for i in tab:
      if i[1] == '+':
         tab_i = int(i[0]) + int(i[2])
      else:
          tab_i = int(i[0]) - int(i[2])
      arranged_problems += " " *(operation_size_list[operation_size_i] - len(str(tab_i))) + str(tab_i) + " "*4
      operation_size_i +=1
  arranged_problems = arranged_problems.rstrip()
  return arranged_problems