import timeit
t = timeit.Timer("pc.prime_list_maker_1(10000)","import prime_list_maker.prime_list_maker_1 as pc")
u = timeit.Timer("pc.prime_list_maker_2(10000)","import prime_list_maker.prime_list_maker_2 as pc")

print(t.timeit(1))
print(t.timeit(2))

