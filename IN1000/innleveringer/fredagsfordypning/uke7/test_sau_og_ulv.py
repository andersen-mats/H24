from sau import Sau
from ulv import Ulv

sau = Sau("Shaun", 5)
ulv = Ulv("Ulven", 5)

assert sau.lever()
assert ulv.hent_vekt() == 20
ulv.spis_sau(sau)
assert not sau.lever()
assert ulv.hent_vekt() == 25

