
class EstimatedRM:
    """Receives the number of repetitions and the weigth lifted for that number of repetitions to estimate
    the one-Repetition Maximum (1RM). The displays 7 different equations separatedly or display all 7"""


    def __init__(self, rep, weigth):
        self.rep = rep
        self.weigth = weigth



    def Brzycki(self):
        """Estimated RM equation by Brzycki"""
        
        brzycki = round((100 * self.weigth) / (102.78 - (2.78 * self.rep)), 1)

        return brzycki



    def Epley(self):
        """Estimated RM equation by Epley"""
        
        epley = round((1 + 0.0333 * self.rep) * self.weigth, 1)

        return epley



    def Lander(self):
        """Estimated RM equation by Lander"""
    
        lander = round((100 * self.weigth) / (101.3 - 2.67123 * self.rep), 1)

        return lander



    def Lombardi(self):
        """Estimated RM equation by Lombardi"""
  
        lombardi = round(self.weigth * (self.rep ** 0.1), 1)

        return lombardi



    def Mayhew(self):
        """Estimated RM equation by Mayhew"""

        mayhew = round((100 * self.weigth) / (52.2 + 41.9 * (2.7181 ** (-0.055 * self.rep))), 1)
 
        return mayhew



    def Oconner(self):
        """Estimated RM equation by Oconner"""

        oconner = round(self.weigth * (1 + 0.025 * self.rep), 1)

        return oconner



    def Wathan(self):
        """Estimated RM equation by Epley"""

        wathan = round((100 * self.weigth) / (48.8 + 53.8 * (2.7181 ** (-0.075 * self.rep))), 1)

        return wathan



    def all_equations_mean(self):
        """Shows all estimated RM equation values and the mean of their values"""

        sum = 0
        authors = ['Brzycki', 'Epley', 'Lander', 'Lombardi', 'Mayhew', "O'Conner", 'Wathan']
        values = [self.Brzycki(), self.Epley(), self.Lander(), self.Lombardi(), self.Mayhew(), self.Oconner(), self.Wathan()]

        for author, value in zip(authors, values):
            print(f'{author}: {value:0f} kg')
            sum += value
        
        print(f'Média aritmética das equações: {sum / len(values):.0f} kg')


def validateRepWeigth(repwt):
    """Validates the repetition and weigth"""

    while True:
        try:
            valid_integer = int(input(repwt))
            return valid_integer
        except ValueError:
            print('Digite apenas números inteiros: ')
        

def validateOption(opt):
    """Validates the option (1-8) for each option of equation"""

    while True:
        try:
            valid_option = int(input(opt))
            if (valid_option == 0):
                print('Saindo do programa. Obrigado.')
                break
            elif (valid_option < 0) or (valid_option > 8):
                print('Escolha uma opção entre 1 e 8: ')
                continue
            else:
                return valid_option
        except ValueError:
            print('Digite apenas números inteiros entre 1 e 8. Para sair, digite 0.') 


def equationSwitch(equation, option):
    """Function defining which equation will be used: 1=brzycki; 2 = Epley; 3 = Lander;
    4 = Lombardi; 5= Mayhew; 6 = O'Conner; 7 = Wathan; 8 = show all"""
    
    match option:
        case 1:
            rm = equation.Brzycki()
            return rm
        case 2:
            rm = equation.Epley()
            return rm
        case 3:
            rm = equation.Lander()
            return rm
        case 4:
            rm = equation.Lombardi()
            return rm
        case 5:
            rm = equation.Mayhew()
            return rm
        case 6:
            rm = equation.Oconner()
            return rm
        case 7:
            rm = equation.Wathan()
            return rm
        case 8:
            rm = equation.all_equations_mean()
            return rm

     
########
#Programa principal
########

print('Estimativa de RM')
print('Escolha uma das equações:')
print('1 = Brzycki\n2 = Epley\n3 = Lander\n4 = Lombardi\n5 = Mayhew\n6 = O\'Conner\n7 = Wathan\n8 = Mostrar todas + média')


# validate and assign the option of RM equation
option = validateOption('Escolha uma das opções de equação: ')

# validate and assign the number of repetitions
reps = validateRepWeigth('Digite o número de repetições: ')

# validate and assign the weigth lifted
wt = validateRepWeigth('Digite o peso realizado para as repetições: ')

# create the object from the EstimatedRM class (which contains all equation's methods)
classRM = EstimatedRM(reps, wt)

# return the value from  the choose equation and selected parameters and assign to a variable
resultRM = equationSwitch(classRM, option)

# print the result rounded by one
if (option == 8):
    resultRM
else:
    print(resultRM)
