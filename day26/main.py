# numbers=[1,2,3]
# new_list=[number+1 for number in numbers]
#
# print(new_list)

# double=[n*2 for n in range(1,5)]
# print(double)

names=["Alex","Beth","Caroline","Dave","Eleanor","Freddie"]
name_upper=[name.upper() for name in names if len(name)>5]
print(name_upper)