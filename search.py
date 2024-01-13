import os

prg = "Programs"

files = os.listdir(prg)

for num, i in enumerate(files):
    print(num + 1, i)

ch = int(input("enter the choice"))


if ch == 1:
    with open("./Programs/BFS(breath).py", "r") as info:
        con = info.read()

        print(con)
    with open("1.py", "w") as file:
        file.write(con)
if ch == 2:
    with open("./Programs/A_star.py", "r") as info:
        con = info.read()
        print(con)

    with open("2.py", "w") as file:
        file.write(con)
if ch == 3:
    with open("./Programs/DFS(depth).py", "r") as info:
        con = info.read()
        print(con)

    with open("3.py", "w") as file:
        file.write(con)
if ch == 4:
    with open("./Programs/alpha_beta_pruning.py", "r") as info:
        con = info.read()
        print(con)

    with open("4.py", "w") as file:
        file.write(con)
if ch == 5:
    with open("./Programs/cryto_arthrmatic.py", "r") as info:
        con = info.read()
        print(con)

    with open("5.py", "w") as file:
        file.write(con)
if ch == 6:
    with open("./Programs/expert_system.py", "r") as info:
        con = info.read()
        print(con)

    with open("6.py", "w") as file:
        file.write(con)
if ch == 7:
    with open("./Programs/min_max.py", "r") as info:
        con = info.read()
        print(con)

    with open("7.py", "w") as file:
        file.write(con)
if ch == 8:
    with open("./Programs/Naive_Bayes.py", "r") as info:
        con = info.read()
        print(con)

    with open("8.py", "w") as file:
        file.write(con)
if ch == 9:
    with open("./Programs/NLP_token.py", "r") as info:
        con = info.read()
        print(con)

    with open("9.py", "w") as file:
        file.write(con)
if ch == 10:
    with open("./Programs/predicate-logic.py", "r") as info:
        con = info.read()
        print(con)

    with open("10.py", "w") as file:
        file.write(con)
if ch == 11:
    with open("./Programs/sematic_net.py", "r") as info:
        con = info.read()
        print(con)

    with open("11.py", "w") as file:
        file.write(con)
if ch == 12:
    with open("./Programs/spell_check.py", "r") as info:
        con = info.read()
        print(con)

    with open("12.py", "w") as file:
        file.write(con)

# x = os.getcwd()
