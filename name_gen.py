from random import choice
from sys import argv

def namer(n):
    """
        Generates random names.
        Argument: number of random names
    """
    first_names = ["Andrea", "Andrew", "Ichabod", "Jeremy", "Frank", "Tom", "Dean", "Charlie", "James", "Otis", "Barry", "Art", "Harvey", "Gabriel", "Robert", "Joe", "Vincent", "Eddie", "Eva", "Danielle", "Katie", "Iris", "Matthias", "Phineas", "Rafael", "Burkhart", "Isabel", "Bernard", "Anne", "Bertha", "Olivia", "Grace", "Mia", "Ella", "Mario", "Marcellus", "Jessica", "Sienna", "Alice", "Esther", "Maurice", "Scarlett", "Chloe", "Rosie", "Lola", "Mila", "Raquel", "Summer", "Martha", "Arabella", "Bonnie", "Silas", "Sarah", "Petros", "Moses", "Lydia", "Konstantinos", "Dimitri", "Zoe", "Margarita", "Viriato", "Yassin", "Pierre", "Kirollos", "Mark", "Fadi", "Mamadou", "Junior", "Fatima", "Marie", "Aya", "Salma", "Precious", "Mariam", "Santiago", "Mateo", "Alysha", "Valentina", "Emilia", "Martina", "Hamza", "Moussa", "Omar", "Amina", "Noam", "George", "Adam", "Adi", "Minato", "Tatsuki", "Yerasyl", "Khaled", "Kiran", "Nathaniel", "Min-jun", "Seo-jun", "Chih-ming", "Reem", "Ai", "Ting", "Saanvi", "Tamar", "Marc", "Lukas", "Maximilian", "Louis", "Liam", "Stefan", "Oliver", "Rasmus", "Robin", "Jules", "Leon", "Malik", "Bence", "Francesco", "Lorenzo", "Zoran", "Iker", "Goran", "Nikola", "Antoni", "Hugo", "Pablo", "Aimar", "Jon", "Marti", "Artem", "Amelia", "Laia", "Emma", "Louise", "Elise", "Leyla", "Lucie", "Yasmine", "Teresa", "Alma", "Freja", "Eleni", "Daisy", "Lili", "Lara", "Hiro"]
    last_names = ["Smith", "Wallace", "Jones", "Brighton", "Taylor", "Carrey", "Mosley", "Moriarty", "Roberts", "Johnson", "McNamara", "O'Reilly", "Herdandez", "DeLauney", "Vandeley", "Lozano", "Mendoza", "Maringola", "Soto", "Alba", "Wong", "Williams", "Brown", "Martin", "Davis", "Anderson", "Clark", "Robinson", "Rossi", "Novak", "Harutyunyan", "Grigoryan", "Mammadov", "Aliyev", "Ali", "Khan", "Bishwas", "Li", "Chen", "Hu", "Lin", "Gelashvili", "Dahan", "Cohen", "Friedman", "Azoulay", "Sato", "Suzuki", "Takahashi", "Ito", "Nakamura", "Yamada", "Ogawa", "Choi", "Kim", "Yoon", "Shin", "Pereira", "de Silva", "Bandara", "Mohamed", "Ranasinghe", "Herath", "Yilmaz", "Demir", "Özdemir", "Nguyen", "Phan", "Gruber", "Wagner", "Bauer", "Mueller", "Berger", "Fischer", "Fisher", "Schmid", "Winkler", "Weber", "Horvat", "Kucera", "Nielsen", "Hansen", "Larsen", "Rasmussen", "Virtanen", "Johansson", "Bernard", "Dubois", "Petit", "Durand", "Leroy", "Moreau", "Simon", "Laurent", "Mercier", "Lambert", "Bonnet", "Schneider", "Becker", "Nagy", "Murphy", "O'Kelly", "McCarthy", "Lynch", "Russo", "Esposito", "Bianchi", "Greco", "Romano", "Gallo", "Conti", "Mancini", "Barbieri", "Moretti", "De Jong", "Jansen", "De Vries", "Van Dijk", "De Boer", "Oliveira", "Sousa", "Almeida", "Pinto", "Carvalho", "Popescu", "Ionescu", "Smirnov", "Varga", "Ruiz", "Moreno", "Alonso", "Ramos", "Blanco", "Green", "Scott", "Driscoll", "Correa", "Rocha", "Alves", "Morais"]
    names = []
    for i in range(n):
        names.append("{0} {1}".format(choice(first_names), choice(last_names)))
    return set(names)

if __name__ == '__main__':
    number=int(argv[1])
    names=namer(number)
    with open("random_names.txt", "w") as f:
        for name in names:
            f.write("{}\n".format(name))
    for name in names:
        print(name)
    print("List of {} random names saved as random_names.txt".format(number))