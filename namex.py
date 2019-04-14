from random import choice

f_namelist=[]
m_namelist=[]

with open("namelist_f.txt", "r", encoding="utf8") as f1:
    for line in f1.readlines():
        f_namelist.append(line.strip())

with open("namelist_m.txt", "r", encoding="utf8") as f2:
    for line in f2.readlines():
        m_namelist.append(line.strip())

def couples(x):
    """Takes a number as argument
        and creates that number of random couples
    """
    for couple in range(x):
        print("- {} and {}.".format(choice(m_namelist), choice(f_namelist)))

def names(g, n=1):
    """Provides a number of random names
        male (m) or female(f)
    """
    if g=="m":
        for i in range(n):
            print(choice(m_namelist))
            
    elif g=="f":
        for i in range(n):
            print(choice(f_namelist))
    else:
        print("You didn't choose a gender correctly.")

if __name__ == '__main__':
    print("\nRandom couples: ")
    couples(5)
    print("\nA random male name: ")
    names("m")
    print("\nA random female name: ")
    names("f")
