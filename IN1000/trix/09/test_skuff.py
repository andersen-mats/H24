from sokk import Sokk
from skuff import Skuff

skuffen = Skuff()

sokk1 = Sokk("H")
sokk2 = Sokk("V")

skuffen.sett_inn_sokk(sokk1)
skuffen.sjekk_status()
skuffen.sett_inn_sokk(sokk2)
skuffen.sjekk_status()
