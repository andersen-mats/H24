from node import Node

def main():

    node1 = Node(5)
    node2 = Node(4)
    node3 = Node(3)
    node4 = Node(2)
    node5 = Node(1)

    noder = [node1,node2,node3,node4,node5]

    for i in range(len(noder)):
        if i + 1 == len(noder):
            break
        noder[i].ny_etterfolger(noder[i+1])

    #for node in noder:
        #print("Node:", node.hent_innhold())
        #if node.hent_neste() is not None:
            #print ("Neste:", node.hent_neste().hent_innhold())

    node6 = Node(0)
    noder.append(node6)

    for node in noder:
        if node.hent_neste() is None:
            node.ny_etterfolger(node6)
            break
    for node in noder:
        print("Node:", node.hent_innhold())
        if node.hent_neste() is not None:
            print ("Neste:", node.hent_neste().hent_innhold())


if __name__ == "__main__":
    main()
