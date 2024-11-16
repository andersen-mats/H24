from kube import Kube

kube1 = Kube(3,2,3)
kube2 = Kube(4,2,7)
kube3 = Kube(7,5,3)
kube4 = Kube(1,2,3)
kube5 = Kube(3,2,3)

kuber = [kube1,kube2,kube3,kube4]

print(repr(kube1))

print(kube2 > kube1)

print(sorted(kuber))

print(kube1)

print(kube1 == kube5)
