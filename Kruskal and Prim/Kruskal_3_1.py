#Алгоритм Краскала


R = [(13,1,2), (18,1,3), (17,1,4), (14,1,5), (22,1,6),(26,2,3),(22,2,5),(3,3,4),(19,4,6)]
#Список ребер графа(Довжина, перша вершина, друга вершина)

Rs = sorted(R, key=lambda x: x[0])
U = set()  #Список з'єднаних вершин
D={}       #словник списку ізольованих груп вершин
T=[]       #Список ребер кістяка

for r in Rs:
    if r[1] not in U or r[2] not in U:      #перевірка для виключення циклів в скелеті
        if r[1] not in U and r[2] not in U: #якщо дві вершини не з'єднані то
            D[r[1]] = [r[1], r[2]]          #формуємо в словнику ключ з номерами вершин
            D[r[2]] = D[r[1]]               #і звязуємо їх з одним ітим же списком вершин
    else:                          #інакше
        if not D.get(r[1]):                 # якщо в словнику немає першої вершини, то 
            D[r[2]].append(r[1])            # додаємо в список першу вершину 
            D[r[1]] = D[r[2]]               # і додаємо ключ з номером першої вершини
        else:                     #інакше
            D[r[1]].append(r[2])            #все теж саме робимо з другою вершиною
            D[r[2]] = D[r[1]]
    
    T.append(r)     #додаємо ребра
    U.add(r[1])     #додаємо вершини в безліч U
    U.add(r[2])

for r in Rs:   # проходимо по ребрам другий раз і об'єднюємо розпозначені групи вершин
    if r[1] in D[r[1]] and r[2] not in D[r[1]]: # якщо вершини належать різним групам, то об'єднюємо
        T.append(r)  #додаємо ребро в скелет
        gr1 = D[r[1]]
        D[r[1]] += D[r[2]]  #об'єднюємо списки двух груп вершин
        D[r[2]] += gr1
print(T)
