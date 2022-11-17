'''
email Validation program :

format of email :

g@g.in  ------- minmum langth of gmail is 6 charactore all small 

'''



email =input("entre Your Email ---> ")
error1,error2,error3,erorr4="mimum 6 char Requird (g@g.in)","Frist Cahr should be char","@ Error (count==1 or @ not more then 1)",". palce is not correct (use only once)"
k,j,d=0,0,0


if len(email)>=6: # mimmum langth of gmail is 6 ---> g@g.in
    if email[0].isalpha(): # email frist caractor should be an charctore ----- .isalpha function chaeck frist charctore type as chre
        if ('@'in email)and(email.count("@")==1): # this condintin is check wather @ is avaivble in email or not and if avivble then count should be one only 
            if (email[-4]=='.') ^ (email[-3]=="."): # this condition check wather . is present @ right posstion or not and using xor oprator i make sure any 0 1 = 1#if i use or then 1-1=1 {g@g..in | not valid } but we want . only for one time so i use xor oprator to for condition 1-0=1 | 0-1=1 rest false 
                for i in email:
                    if i == i.isspace():
                        k=1
                    elif i.isalpha():   # i used elif condion becuse if first condion is worng then directoly og for if blovk 
                        if i == i.upper(): # g --- G==G True g==G gives False
                            j=1
                    elif i.isdigit(): #
                        continue
                    elif i=="_" or i=="." or i =="@" :
                        continue
                    else:
                        d=1   # if any other sightn we got like # 8 ^ or any other thinng 
                if k==1 or j==1 or d==1:
                    print("worng email Spce and Upper char not allow")
                else: print("------------ Right Email ---------------------")
            else: print (f"{erorr4} :Wrong email ")
        else: print (f"{error3} : worng email")
    else:print(f"{error2} : wrong email ")
else: print(f"{error1} : wrong email ")



# import regex




