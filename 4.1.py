def func(s):
    sim_cou = {}
    for sim in s:
        sim_cou[sim] = sim_cou.get(sim,0) + 1
    for sim, count in sim_cou.items():

        print(sim,count)

func('kdkkdkd')