def lag_interessegrupper(interesser):
    ret = dict()

    for v in interesser.values():
        ret[v] = []

    for k in interesser:
        ret[interesser[k]].append(k)

    return ret

print(lag_interessegrupper({"Per":"Mat", "Palle":"Film", "Espen":"Mat"}))
