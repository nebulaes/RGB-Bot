def get_all_ranks_label():
    list = []
    for rank in ranks:
        if rank['label'] not in list:
            list.append(rank['label'])
    return list

def get_ranks_to_remove(rank):
    all_ranks = get_all_ranks_label()
    all_ranks.remove(rank)
    return all_ranks

ranks = [
    {
        'label':'Copper',
        'level':'4',
        'ref':1
    },
    {
        'label':'Copper',
        'level':'3',
        'ref':2
    },
    {
        'label':'Copper',
        'level':'2',
        'ref':3
    },
    {
        'label':'Copper',
        'level':'1',
        'ref':4
    },
    {
        'label':'Bronze',
        'level':'4',
        'ref':5
    },
    {
        'label':'Bronze',
        'level':'3',
        'ref':6
    },
    {
        'label':'Bronze',
        'level':'2',
        'ref':7
    },
    {
        'label':'Bronze',
        'level':'1',
        'ref':8
    },
    {
        'label':'Silver',
        'level':'4',
        'ref':9
    },
    {
        'label':'Silver',
        'level':'3',
        'ref':10
    },
    {
        'label':'Silver',
        'level':'2',
        'ref':11
    },
    {
        'label':'Silver',
        'level':'1',
        'ref':12
    },
    {
        'label':'Gold',
        'level':'4',
        'ref':13
    },
    {
        'label':'Gold',
        'level':'3',
        'ref':14
    },
    {
        'label':'Gold',
        'level':'2',
        'ref':15
    },
    {
        'label':'Gold',
        'level':'1',
        'ref':16
    },
    {
        'label':'Platinum',
        'level':'3',
        'ref':17
    },
    {
        'label':'Platinum',
        'level':'2',
        'ref':18
    },
    {
        'label':'Platinum',
        'level':'1',
        'ref':19
    },
    {
        'label':'Diamond',
        'level':'1',
        'ref':20
    }
]
