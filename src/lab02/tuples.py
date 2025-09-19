def reformat(orig):
    if type(orig[0]) != str: return ValueError
    if type(orig[1]) != str: return ValueError
    if type(orig[2]) != float: return ValueError
    name, group, gpa = orig[0].split(), orig[1], '{:.2f}'.format(round(orig[2], 2))
    if len(name) == 3: name = name[0][0].upper() + name[0][1:] + ' ' + name[1][0].upper() + '.' + name[2][0].upper() + '.'
    else: name = name[0][0].upper() + name[0][1:] + ' ' + name[1][0].upper() + '.'
    return name + ', ' + 'гр. ' + group + ', ' + 'GPA ' + gpa