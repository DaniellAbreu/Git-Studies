K = int(input())
Ntrain, Ntest = map(int, input().split())

matrix_train = []

for _ in range(Ntrain):
    x_train = list(input().split())
    matrix_train.append(x_train)

y_label = []
for _ in range(Ntrain):
    y_train = input()
    y_label.append(y_train)

matrix_test = []
for _ in range(Ntest):
    x_test = list(input().split())
    matrix_test.append(x_test)


cap_shape = {"b": 0, "c": 1, "x": 2, "f": 3, "k": 4, "s": 5}
cap_surface = {"f": 0, "g": 1, "y": 2, "s": 3}
cap_color = {"n": 0, "b": 1, "g": 2, "r": 3, "p": 4, "u": 5, "e": 6, "w": 7, "y": 8}
bruises = {"t": 0, "f": 1}
odor = {"a": 0, "l": 1, "c": 2, "y": 3, "f": 4, "m": 5, "n": 6,"p": 7, "s": 8}
gill_attachment = {"a": 0, "d": 1, "f": 2, "n": 3}
gill_spacing = {"c": 0, "w": 1, "d": 2}
gill_size = {"b": 0, "n": 1}
gill_color = { "k": 0, "n": 1, "b": 2, "h": 3, "g": 4, "r": 5, "o": 6, "p": 7, "u": 8, "e": 9, "w": 10, "y": 11 }
stalk_shape = {"e": 0, "t": 1}
stalk_root = {"b": 0, "c": 1, "u": 2, "e": 3, "z": 4, "r": 5, "?": 6}
stalk_surface_above_below_ring = {"f": 0, "y": 1, "k": 2, "s": 3}
stalk_color_above_below_ring = {"n": 0, "b": 1, "c": 2, "g": 3, "o": 4, "p": 5, "e": 6, "w": 7, "y": 8}
veil_type = {"p": 0, "u": 1}
veil_color = {"n": 0, "o": 1, "w": 2, "y": 3} 
ring_number = {"n": 0, "o": 1, "t": 2}
ring_type = {"c": 0, "e": 1, "f": 2, "l": 3, "n": 4, "p": 5, "s": 6, "z": 7}
spore_print_color = {"k": 0, "n": 1, "b": 2, "h": 3, "r": 4, "o": 5, "u": 6, "w": 7, "y": 8}
population = {"a": 0, "c": 1, "n": 2, "s": 3, "v": 4, "y": 5}
habitat = {"g": 0, "l": 1, "m": 2, "p": 3, "u": 4, "w": 5, "d": 6}

for x in matrix_train:
    x[0] = cap_shape[x[0]]    
    x[1] = cap_surface[x[1]]
    x[2] = cap_color[x[2]]
    x[3] = bruises[x[3]]
    x[4] = odor[x[4]]
    x[5] = gill_attachment[x[5]]
    x[6] = gill_spacing[x[6]]
    x[7] = gill_size[x[7]]
    x[8] = gill_color[x[8]]
    x[9] = stalk_shape[x[9]]
    x[10] = stalk_root[x[10]]
    x[11] = stalk_surface_above_below_ring[x[11]]
    x[12] = stalk_surface_above_below_ring[x[12]]
    x[13] = stalk_color_above_below_ring[x[13]]
    x[14] = stalk_color_above_below_ring[x[14]]
    x[15] = veil_type[x[15]]
    x[16] = veil_color[x[16]]
    x[17] = ring_number[x[17]]
    x[18] = ring_type[x[18]]
    x[19] = spore_print_color[x[19]]
    x[20] = population[x[20]]
    x[21] = habitat[x[21]]
    
vector_u = []

for i in range(22):
    total = 0
    for x in matrix_train:
        total += x[i]

    vector_u.append(total / Ntrain)

vector_o = []

for i in range(22):
    total = 0
    for x in matrix_train:
        total += (x[i] - vector_u[i]) ** 2
    
    o = ((1 / Ntrain) * total) ** 0.5
    
    vector_o.append(o)
    
normalized_matrix = [[] for _ in range(22)]

for i in range(22):

    for x in matrix_train:
        if vector_o[i] == 0:
            normalized_x = 0
            normalized_matrix[i].append(normalized_x)
        else:
            normalized_x = (x[i] - vector_u[i]) / vector_o[i]
            normalized_matrix[i].append(normalized_x)

#Transposição da Matriz
normalized_matrix = [[normalized_matrix[j][i] for j in range(len(normalized_matrix))] for i in range(len(normalized_matrix[0]))]

    
for x in matrix_test:
    x[0] = cap_shape[x[0]]    
    x[1] = cap_surface[x[1]]
    x[2] = cap_color[x[2]]
    x[3] = bruises[x[3]]
    x[4] = odor[x[4]]
    x[5] = gill_attachment[x[5]]
    x[6] = gill_spacing[x[6]]
    x[7] = gill_size[x[7]]
    x[8] = gill_color[x[8]]
    x[9] = stalk_shape[x[9]]
    x[10] = stalk_root[x[10]]
    x[11] = stalk_surface_above_below_ring[x[11]]
    x[12] = stalk_surface_above_below_ring[x[12]]
    x[13] = stalk_color_above_below_ring[x[13]]
    x[14] = stalk_color_above_below_ring[x[14]]
    x[15] = veil_type[x[15]]
    x[16] = veil_color[x[16]]
    x[17] = ring_number[x[17]]
    x[18] = ring_type[x[18]]
    x[19] = spore_print_color[x[19]]
    x[20] = population[x[20]]
    x[21] = habitat[x[21]]
    
normalized_matrix_test = [[] for _ in range(22)]

for i in range(22):

    for x in matrix_test:
        if vector_o[i] == 0:
            normalized_x = 0
            normalized_matrix_test[i].append(normalized_x)
        else:
            normalized_x = (x[i] - vector_u[i]) / vector_o[i]
            normalized_matrix_test[i].append(normalized_x)

normalized_matrix_test = [[normalized_matrix_test[j][i] for j in range(len(normalized_matrix_test))] for i in range(len(normalized_matrix_test[0]))]

#Calculo da Distância Euclidiana.
distances = [[] for _ in range(Ntest)]

for k in range(Ntest):
    for i in range(Ntrain):
        euclidian_distance = sum((normalized_matrix_test[k][j] - normalized_matrix[i][j]) ** 2 for j in range(22)) ** 0.5
        
        distances[k].append((euclidian_distance, y_label[i]))
            
#Encontrar K vizinhos mais próximos.
for data in distances:
    data.sort()

for i in range(Ntest):
    k_nearest_neighbors = distances[i][:K]
    k_nearest_neighbors = [label for _, label in k_nearest_neighbors]
    if k_nearest_neighbors.count('p') > k_nearest_neighbors.count('e'):
        print('p')
    else:
        print('e')
