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
        return self.weight < other.weight

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
        uf = UnionFind()

        for vertex in self.vertices:
            uf.create(vertex)

        self.edges.sort()
        number_of_sets = len(self.vertices)
        print(number_of_sets)
        for e in self.edges:
            u = self.vertices[e.v1id]
            v = self.vertices[e.v2id]
            if uf.find(u) != uf.find(v) and number_of_sets != number_of_clusters:
                uf.union(u, v)
                number_of_sets -= 1
        return uf.parent


class UnionFind:

    def __init__(self):
        self.parent = {}

    def create(self, x):
        if x not in self.parent:
            self.parent[x] = x

    def find(self, x):
        return self.parent[x]

    def union(self, x, y):
        z = self.parent[x]
        if z == self.parent[y]:
            return
        for x in self.parent:
            if self.parent[x] == z:
                self.parent[x] = self.parent[y]



def draw_result(filename, c):
    g = Graph()
    g.read_graph(filename)
    result = g.Kruskal(c)
    for i in result:
        plt.scatter(float(i.x), float(i.y), s=2, color=('C' + str(result[i].id)))

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
    if int(sys.argv[2]) < 0:
        print("Nie można dzielić na ujemną liczbę!")
    else:
        filename = sys.argv[1]
        number_of_clusters = int(sys.argv[2])
        print("Program rozpoczął prace...")
        draw_result(filename, number_of_clusters)
        print("Przetwarzanie zakończone")
 
