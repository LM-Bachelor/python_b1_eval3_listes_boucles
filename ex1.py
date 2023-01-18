# EV3 : Liste et boucle - Exercice 1
# 1
print("1")
list_nb = []
    
for i in range(0,10):
    print(i)
    nb = int(input("Saisir un nombre entre 0 et 10 : "))
    if nb >= 0 and nb <= 10:
        list_nb.append(nb)
sum_nb = sum(list_nb)
print(sum_nb)

# 2
# print("2")
# list_nb = []
# while len(list_nb) != 10:
#     nb = int(input("Saisir un nombre entre 0 et 10 : "))
#     if nb >= 0 and nb <= 10:
#         list_nb.append(nb)
# sum_nb = sum(list_nb)
# print(sum_nb)

# # 3
# print("3")
# for i in range(10,-1,-1):
#     print(i)
# print("BOUM")