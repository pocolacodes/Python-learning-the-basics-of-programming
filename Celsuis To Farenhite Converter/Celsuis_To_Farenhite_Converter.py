
#Celsusis_To_Fahrenhite_Calculator

# Asks the user the tempreture type(Whether it is Celsuis Or Fahenrite) :
What_Tempreture_Are_You_Converting_From = input("\nAre You Converting From Celsuis To Farenhite or Farenhite to Celsuis:?      ")
# it checks whether the user types Celsuis 
# IF IT DOES IT PERFORMS THE CELSUIS CALCULATION
if What_Tempreture_Are_You_Converting_From == "Celsuis" :
# This Is The Function That Converts The Celsuis Value To Farenhite 

    def Celsuis_to_Farenhite():
# Celsuis Input
       Celsuis = int(input("\nType Your Tempreture In Celsuis:?(`C)  "))
# Celsuis_Conversion
       Celsuis_to_Farenhite =  (Celsuis * 1.8) + 32 
# Celsuis_Display
       print(str(Celsuis_to_Farenhite)+"`F")
# this Line Of Code Ensures that this Function Works 
    Celsuis_to_Farenhite()
elif What_Tempreture_Are_You_Converting_From =="Farenhite":
    def Farenhite_to_Celsuis():
# Farenhite_Input
      Farenhite = int(input("\nType Your Tempreture In farenhite?(`F) "))
# Farenheite_to_celsuis 
      Farenhite_to_Celsuis = (Farenhite - 32 )/1.8
# Display_The_Tempreture_in_Farenhite 
      print(str(Farenhite_to_Celsuis)+"`C")
    Farenhite_to_Celsuis()







  
