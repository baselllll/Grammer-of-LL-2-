import grammmer
class LLGrammer:
     def data(self,left,right):
         recive = [[left,right]]
         print(left+" → "+right)
         return recive
     ############### step 1########################
     def find_nullable_rules_nullable_nonterminals(self,productionRule):
         print("list of production rule : ",productionRule)
         for li in productionRule:
             for right in li:
                 if right=="є":
                     print(" - The Rule ",li," is nullable rules ")
                     print(" - The ",li[0]," is nullable nonterminals")
                     print("----------------------------------------------------------")
                     return li[0]

     ############### step 2 #########################
     def Compute_the_relation_Begins_Directly(self,NonTENULL,PRoduRuel):
         print("list of production rule : ",PRoduRuel)
         print(len(PRoduRuel))
         collectallforRe=[]
         for outer in range(len(PRoduRuel)):
             collect=[]
             if PRoduRuel[outer]==['A', 'є']:
                 continue
             print(PRoduRuel[outer])
             print(PRoduRuel[outer][0]," → ",PRoduRuel[outer][1])

             #print(len(PRoduRuel[outer][1]))

             for rightside in range(len(PRoduRuel[outer][1])):
                 collect += [PRoduRuel[outer][1][rightside]]
             print("The BDW Is : ",collect[0])
             if collect[0]==NonTENULL:
                 print("The BDW Is : ",collect[1])
                 collectallforRe.append(PRoduRuel[outer][0]+" BDW "+collect[1])

             collectallforRe +=[PRoduRuel[outer][0]+" BDW "+collect[0]]

             print(collectallforRe)
             print("/////////////////////////////")
         return collectallforRe

     ############## step 3 ##########################
     def Compute_the_elation_Begins_With(self,BWDdata):
         print('------------------------------------------------------------------')
         def BWtranstive(a):
             closure = list(a)
             while True:
                 new_relations = list([x,"BW",w] for x,y in closure for q,w in closure if q == y)
                 return new_relations
         orginaldata2= []
         y =[]
         nonterm = []
         termin = []
         reda =[]
         retrivedata =[]
         orginaldata=[]
         for o in range(len(BWDdata)):
            for i in range(len(BWDdata[o])):
                reda = BWDdata[o][i].replace('BDW','BW')
                y =BWDdata[o][0]
            orginaldata +=[[y,reda]]
            orginaldata2 +=[[y,"BW",reda]]
            if y.isupper():
                nonterm =y
                for nonte in nonterm:
                    retrivedata +=[[nonte,"Bw",nonte]]
            if reda.islower():
                termin =reda
                for te in termin:
                    retrivedata +=[[termin,"Bw",termin]]
         removeDupDa = set(tuple(x) for x in retrivedata)
         finaldata = [ list(x) for x in removeDupDa ]
         TransitveClosure = BWtranstive(orginaldata)
         print("The Transistive is : ",TransitveClosure)
         print("The Reflsive is : ",finaldata)
         print("allDatafinaldata is : ")
         return [list(TransitveClosure),list(finaldata),list(orginaldata2)]
     ############## step 4 ##########################
     def Compute_the_set_of_terminals_First(self,BW):
      collectdata = []
      collectdata2=[]
      collectdata3=[]
      for o in range(len(BW)):
         for i in range(len(BW[o])):
             #print(BW[o][i][0],BW[o][i][1])
              if BW[o][i][0].isupper() and BW[o][i][2].islower():
                 collectdata += [["First :",BW[o][i][0]]+[BW[o][i][2]]]
                 collectdata2 += BW[o][i][0]+BW[o][i][2]
                 print("First(",BW[o][i][0],") = {",BW[o][i][2],"}")
              elif BW[o][i][0].islower() and BW[o][i][2].islower():
                 print("First(",BW[o][i][0],") = {",BW[o][i][2],"}")
                 collectdata += [["First :",BW[o][i][0]]+[BW[o][i][2]]]
                 collectdata2 +=BW[o][i][0]+BW[o][i][2]
      print("First of :",collectdata2)
      return collectdata2
     ############## step 5 ##########################
     def Compute_First_of_right_side_of_each_rule(self,lst1, lst2,Nonterminal):
         lst3 = []
         colda1=[]
         colda2=[]
         valuesofNonTer = []
         for value in lst1:
             valuesofNonTer +=[value]
             for inner in value:
                 print(value)
                 if value[0] in lst2 and inner[0].isupper() and inner[0]==Nonterminalnull:
                     lst3 +=[lst2.index(value[0])]
                 elif value[0] in lst2 and value[0].islower():
                   lst3 +=value[0]
                 elif value[0] =="є":
                     lst3 +=value[0]
             print(lst3)
         for outer in range(len(lst3)):
            if type(lst3[outer]) == str:
                colda1 +=lst3[outer]
            else:
                colda2 +=lst2[lst3[outer]+1]
         return ["Rules is ::",valuesofNonTer,"AND Result IS ::"],["Nonteminal",colda2],["Teminal",colda1]

     ############## step 6 ##########################
     def Compute_the_relation_Is_Followed_Directly_By(self,producdata):
      collectdata = []
      retdata = []
      for ou in range(len(producdata)):
        for inner in range(1):
            collectdata +=[producdata[ou][1]]
            #print(producdata[ou][1])
      print(collectdata)
      for righthandside in range(len(collectdata)):
        for inner in range(len(collectdata[righthandside])):
            #print(collectdata[righthandside][inner])
            if collectdata[righthandside][inner].isupper():
                print(collectdata[righthandside][inner],"followed Directly by",collectdata[righthandside][inner+1])
                retdata += [[collectdata[righthandside][inner],"followed Directly by",collectdata[righthandside][inner+1]]]
            else:
                break
      return retdata
     ###################step 7############################
     def Compute_the_relation_Is_Direct_End_Of(self,NonTENULL,PRoduRuel):
         print("list of production rule : ",PRoduRuel)
         print(len(PRoduRuel))
         collectallforRe=[]
         for outer in range(len(PRoduRuel)):
             collect=[]
             if PRoduRuel[outer]==['A', 'є']:
                 continue
             print(PRoduRuel[outer])
             print(PRoduRuel[outer][0]," → ",PRoduRuel[outer][1])
             for rightside in range(len(PRoduRuel[outer][1])):
                 collect += [PRoduRuel[outer][1][rightside]]
             print(collect[len(collect)-1]," The DEO Is : ",PRoduRuel[outer][0])
             if collect[len(collect)-1]==NonTENULL:
                 print("The DEO Is : ",collect[0])
                 collectallforRe.append(collect[0]+" DEO "+PRoduRuel[outer][0])

             collectallforRe +=[collect[len(collect)-1]+" DEO "+PRoduRuel[outer][0]]

             print(collectallforRe)
             print("/////////////////////////////")
         return collectallforRe
     ######################step 8 #############################################
     def Compute_the_relation_Is_End_Of (self,BWDdata):
         BWDdata.pop(2)
         print('------------------------------------------------------------------')
         def BWtranstive(a):
             closure = list(a)
             while True:
                 new_relations = list([x,"Eo",w] for x,y in closure for q,w in closure if q == y)
                 return new_relations
         orginaldata2= []
         y =[]
         nonterm = []
         termin = []
         reda =[]
         retrivedata =[]
         orginaldata=[]
         for o in range(len(BWDdata)):
            for i in range(len(BWDdata[o])):
                reda = BWDdata[o][i].replace('DEO','EO')
                y =BWDdata[o][0]
            orginaldata +=[[y,reda]]
            orginaldata2 +=[[y,"EO",reda]]
            if reda.isupper():
                nonterm =y
                for nonte in nonterm:
                    retrivedata +=[[nonte,"EO",nonte]]
            if y.islower():
                termin =reda
                for te in termin:
                    retrivedata +=[[termin,"EO",termin]]
            if reda.isupper() and y.isupper():
                continue
         removeDupDa = set(tuple(x) for x in retrivedata)
         finaldata = [ list(x) for x in removeDupDa ]
         print(orginaldata)
         TransitveClosure = BWtranstive(orginaldata)
         print(TransitveClosure)
         print("The Transistive is : ",TransitveClosure)
         print("The Reflxsive is : ",finaldata)
         print("allDatafinaldata is : ")
         return [list(finaldata),list(orginaldata2)]
     ########################step 9#######################
     def Compute_the_relation_Is_Followed_By(self,EO,FDB,BW):
         print(EO)
         print(FDB)
         print(BW)
         for ouEO in range(len(EO)):
             for inEO in range(EO[ouEO]):
                 print(EO[inEO][2])
     ####################step 8 ####################################
     def Compute_the_relation_Is_Followed_By(self,EO,FDB,BW):
         coldataEOstart = []
         coldataEOend = []
         coldataFDBstart = []
         coldataFDBend = []
         coldataBWstart = []
         coldataBWend = []
         FinalDATAOFFDB = []
         #print(EO)
         #print(FDB)
         print(BW)
         for ouFDB in range(len(FDB)):
             for inFDB in range(1):
                 #print(FDB[ouFDB][2])
                 coldataFDBstart +=FDB[ouFDB][0]
                 coldataFDBend +=FDB[ouFDB][2]
         for ouEo in range(len(EO)):
             for inEO in range(len(EO[ouEo])):
                 #print((EO[ouEo][inEO][2]))
                 coldataEOstart +=EO[ouEo][inEO][0]
                 coldataEOend +=EO[ouEo][inEO][2]
         for ouBW in range(len(BW)):
             for inBW in range(len(BW[ouBW])):
                  #print(BW[ouBW][inBW][0])
                 coldataBWstart +=BW[ouBW][inBW][0]
                 coldataBWend +=BW[ouBW][inBW][2]
         ##############################################
         for EOend in coldataEOend:
             for FDBstart in coldataFDBstart:
                 if EOend== FDBstart:
                     for FDBend in coldataFDBend:
                         for BWstart in coldataBWstart:
                             if FDBend==BWstart:
                                 for BWend in coldataBWend:
                                     FinalDATAOFFDB += [[BWstart,"FB",BWend]]
         return FinalDATAOFFDB
     #######################step 10 ###################################
     def Extend_the_FB_relation_to_include_endmarker(self,EO):
         for eo in EO:
          for inner in eo:
            #print(inner[2])
            if inner[2]=="S" and inner[0].isupper():
                print(inner[2],"FB -->",inner[0])
     #####################step 11 ##################################
     def Compute_the_Follow_Set_for_each_nullable_nonterminal(self,FB,NONterminal):
         colldata = []
         colldataother = []
         for fb in FB:
             for inner in fb:
               #print(fb[2])
               if fb[2]==NONterminal and fb[0].islower():
                colldata +="FOL(",fb[2],") = ",fb[0]
                colldataother +=[fb[2],fb[0]]
               #print(["FOL(",fb[2],") = ",fb[0]])
         print(colldata[0])# because it is repeted
         return " ( "+NONterminal+" ) = "+colldataother[1]
     ############################step 12 ############################
     def Compute_the_Selection_Set_for_each_rule(self,First,Folset):
         print("First is ",First)
         print("Follow set : ",Folset)


ll = LLGrammer()
registerstep1=[]
Nonterminalnull=[]
#Remember When Put nullvalue Change it upper
registerstep1 +=ll.data("S","ABc")
registerstep1 +=ll.data("A","bA")
registerstep1 +=ll.data("A","c")
registerstep1 +=ll.data("B","c")
print("----------------------------------------------------------")
###########################
Nonterminalnull =ll.find_nullable_rules_nullable_nonterminals(registerstep1)
print(Nonterminalnull)
if ['A', 'є']  in registerstep1 and ['B', 'є']  in registerstep1:
    #########################################
    BDW=ll.Compute_the_relation_Begins_Directly(Nonterminalnull,registerstep1)
    print("The Begin dirctory with : ",BDW)
    BW = ll.Compute_the_elation_Begins_With(BDW)
    print(ll.Compute_the_elation_Begins_With(BDW))
    print("----------------------------------------------------------")
    #############################################
    First=ll.Compute_the_set_of_terminals_First(BW)
    print(First)
    print("------------------------------------------------------------")
    #########################################################
    #['A', 'B', 'c', 'b', 'A', 'є', 'c'] right hand side user entered it
    FirstRightHandside = ll.Compute_First_of_right_side_of_each_rule([['A', 'B', 'c'], ['b', 'A'], ['c'], ['c']],First,Nonterminalnull)
    print(FirstRightHandside)
    print("-----------------------------------------------------------")
    ##############################################################
    FDB = ll.Compute_the_relation_Is_Followed_Directly_By(registerstep1)
    print("-----------------------------------------------------------")
    ################################];############################
    DEO = ll.Compute_the_relation_Is_Direct_End_Of('A',registerstep1)
    print("-----------------------------------------------------------")
    ############################################################
    EO = ll.Compute_the_relation_Is_End_Of(DEO)
    print(EO)
    ############################################################
    print("-------------------------------------------------")
    FB = ll.Compute_the_relation_Is_Followed_By(EO,FDB,BW)
    print(FB)
    print("---------------------------------------------")
    ##########################################################
    Endmarker = ll.Extend_the_FB_relation_to_include_endmarker(EO)
    print("--------------------------------------------")
    ###########################################################
    Followset = ll.Compute_the_Follow_Set_for_each_nullable_nonterminal(FB,Nonterminalnull)
    print(Followset)
    print("------------------------------------------")
    ###########################################################
    Seletion_set = ll.Compute_the_Selection_Set_for_each_rule(FirstRightHandside,Followset)
    print("The Selection set ----->>>>>> :[[c]",grammmer.selection_set)
else:
    #########################################
    BDW=ll.Compute_the_relation_Begins_Directly(Nonterminalnull,registerstep1)
    print("The Begin dirctory with : ",BDW)
    BW = ll.Compute_the_elation_Begins_With(BDW)
    print(ll.Compute_the_elation_Begins_With(BDW))
    print("----------------------------------------------------------")
    #############################################
    First=ll.Compute_the_set_of_terminals_First(BW)
    print("The Selection set : ",First)
    print("------------------------------------------------------------")
    #########################################################
    #['A', 'B', 'c', 'b', 'A', 'є', 'c'] right hand side user entered it
    FirstRightHandside = ll.Compute_First_of_right_side_of_each_rule([['A', 'B', 'c'], ['b', 'A'], ['є'], ['c']],First,Nonterminalnull)
    print(FirstRightHandside)
    print("-----------------------------------------------------------")
    print("The Selection set ---------------->>> : [[c]",grammmer.selection_set)
    ##############################################################
