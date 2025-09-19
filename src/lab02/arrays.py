def min_max(orig):
    if orig == []: return ValueError
    else: return tuple([min(orig), max(orig)])
    
def unique_sorted(orig):
    return sorted(list(set(orig)))

def flatten(orig):
    out = []
    for i in orig:
        if type(i) in [list,tuple]: 
            if i != []:
                for j in i: out.append(j)
        else: return TypeError
    return out