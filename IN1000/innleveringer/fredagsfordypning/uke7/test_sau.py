from sau import Sau

sau1 = Sau("Ole", 1)

assert sau1.lever()
sau1.blir_spist()
assert not sau1.lever()


