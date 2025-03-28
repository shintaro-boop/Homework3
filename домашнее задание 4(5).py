num_people = 7
kill_num = 3
def josephus_task(num_people, kill_num):
    alive = [True] * num_people
    num_survivors, survivor, index = num_people, 0, 0
    while num_survivors:
        if alive[survivor]:
            index += 1
            if index == kill_num:
                num_survivors = num_survivors - 1
                if not num_survivors:
                    return survivor
                else:
                    alive[survivor] = False
                    index = 0
                    survivor = (survivor + 1) % num_people