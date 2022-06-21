import math
class Status():

    def hpReturn(base,iv,ev,lvl):
        return math.trunc((((2 * base[1] + iv[1] + (ev[2] / 4)) * lvl) / 100) + lvl + 10)

    def attackReturn(base,iv,ev,level,atknat):
        return math.trunc((((((2 * base[2] + iv[2] + (ev[2] / 4)) * level) / 100) + 5) * atknat))
        
    def defenseReturn(base,iv,ev,level,defnat):
        return math.trunc((((((2 * base[3] + iv[3] + (ev[3] / 4)) * level) / 100) + 5) * defnat))

    def spattackReturn(base,iv,ev,level,spatknat):
        return math.trunc((((((2 * base[4] + iv[4] + (ev[4] / 4)) * level) / 100) + 5) * spatknat))  

    def spdefenseReturn(base,iv,ev,level,spdefnat):
        return math.trunc((((((2 * base[5] + iv[5] + (ev[5] / 4)) * level) / 100) + 5) * spdefnat))

    def speedReturn(base,iv,ev,level,spdnat):
        return math.trunc((((((2 * base[6] + iv[6] + (ev[6] / 4)) * level) / 100) + 5) * spdnat))