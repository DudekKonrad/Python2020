import csv
import math
import matplotlib.pyplot as plt
import sys


class Vertex:

    def __init__(self, v_id, x, y):
        self.x = x
        self.y = y
        self.id = v_id

    def __repr__(self):
        return str(self.id)

    def __hash__(self):
        return hash(self.id)


class Edge:
    def __init__(self, weight, v1id, v2id):
        self.weight = weight
        self.v1id = v1id
        self.v2id = v2id

    def __repr__(self):
        result = str(self.v1id) + "-->" + str(self.v2id) + ": " + str(self.weight)
        return result

    def __lt__(self, other):
        if self.weight < other.weight:
            return False
        elif self.weight > other.weight:
            return True

    def __ge__(self, other):
        return self.weight > other.weight

    def __eq__(self, other):
        return self.v1id == other.v1id and self.v2id == other.v2id


class Graph:

    def __init__(self):
        self.clusters = 0
        self.vertices = []
        self.edges = []

    def read_graph(self, file_name):
        k = 1
        vertex_id = 0
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                v = Vertex(vertex_id, row[0], row[1])
                self.vertices.append(v)
                vertex_id += 1

        for i in range(len(self.vertices)):
            for j in range(k, len(self.vertices)):
                x_value = (float(self.vertices[j].x) - float(self.vertices[i].x)) ** 2
                y_value = (float(self.vertices[j].y) - float(self.vertices[i].y)) ** 2
                weight = math.sqrt(x_value + y_value)
                e = Edge(weight, self.vertices[i].id, self.vertices[j].id)
                self.edges.append(e)
            k += 1

    def Kruskal(self, number_of_clusters):
        sets = []

        for vertex in self.vertices:
            vertex = MySet(vertex)
            sets.append(vertex)

        self.edges.sort(reverse=True)
        number_of_sets = len(self.vertices)
        for e in self.edges:
            u = sets[e.v1id]
            v = sets[e.v2id]
            if u is not None and v is not None:
                if Find_Set(u) != Find_Set(v) and number_of_sets != number_of_clusters:
                    My_Union(sets, u, v)
                    number_of_sets -= 1
        return sets


class MySet:

    def __init__(self, x):
        self.data = {x}
        self.representative = x.id

    def __len__(self):
        return len(self.data)


def Find_Set(s):
    return s.representative


def My_Union(list_of_sets, s1, s2):
    if len(s1) > len(s2):
        s1.data.update(s2.data)
        list_of_sets[s2.representative] = None
    else:
        s2.data.update(s1.data)
        list_of_sets[s1.representative] = None


colors = ['red', 'green', 'blue', 'yellow', 'black', 'orange', 'purple', 'pink',
          'cyan', 'olive', 'gray', 'brown', 'sienna', 'palegreen', 'slategray',
          'tan', 'lime', 'royalblue', 'stateblue', 'darkorchid', 'plum', 'sandybrown']


def draw_result(filename, c):
    g = Graph()
    g.read_graph(filename)
    result = g.Kruskal(c)
    k = 0
    for s in result:
        if s is not None:
            for v in s.data:
                plt.scatter(float(v.x), float(v.y), s=30, color=colors[k])
            k += 1

    plt.title(filename)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.show()


if len(sys.argv) > 3:
    print("\nPodano za dużo arguemntów!\nProgram uruchamia się w następujący sposób:\nclustering.py [nazwa pliku csv] "
          "[ilosc klastrów]\n")
elif len(sys.argv) < 3:
    print("\nPodano za mało argumentów!\nProgram uruchamia się w następujący sposób:\nclustering.py [nazwa pliku csv] "
          "[ilosc klastrów]\n")
else:
    if int(sys.argv[2]) > len(colors):
        print("Maksymalna liczba na jaką można podzielić dane to ", len(colors))
    elif int(sys.argv[2]) < 0:
        print("Nie można dzielić na ujemną liczbę!")
    else:
        filename = sys.argv[1]
        number_of_clusters = int(sys.argv[2])
        print("Program rozpoczął prace...")
        draw_result(filename, number_of_clusters)
        print("Przetwarzanie zakończone")
