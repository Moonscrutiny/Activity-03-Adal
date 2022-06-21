import math
class EV():

    def desired(base,ev,iv,option,level,di,modify):
        d = ((2*base[option+1]+iv[option+1]+(ev[option+1]/4))*level/100)
        return math.trunc((((di/modify)-(d))*400/level)/4)*4