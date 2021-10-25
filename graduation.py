import itertools

def attend_graduation(n):
    attendance = list(itertools.product("AP", repeat=n))#AP denotes Absent and Present
    no_of_ways = []
    not_attend = []
    absent_str = 'AAAA'#absent for 4 or more consecutive days

    for i in attendance:
        abs_ = "".join(i)
        if absent_str not in abs_:
            no_of_ways.append(i)
            if abs_.endswith("A"):
                not_attend.append(i)
    no_to_attend = len(no_of_ways)
    prob = str(len(not_attend))+"/"+str(len(no_of_ways))
    return no_to_attend,prob
