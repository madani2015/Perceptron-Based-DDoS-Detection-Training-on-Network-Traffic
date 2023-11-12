import csv
import random as rd
import math


def read_document(name):
    ''' allow to read a CSV
    input the path of the document
    output a list containing the row'''
    list = []
    with open(name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=';')
        for row in csv_reader:
            list.append([int(row[0]),int(row[1])])
    return list 

def save_dataset(list, name):
    ''' Save the list as a csv'''
    file = open("dataset/"+name, 'w')
    for k in range(len(list)):
        row = ""
        for i in range(len(list[k])):
            row = row + str(list[k][i])+";"
        row = row[:-1] + "\n"
        file.write(row)
    file.close()

def generate_data(namenor, nameddo, nb, prob_ddos = 0.5, nb_attacker = 1):
    '''create a list of data with mixed element and DDoS element'''
    list_normal = []
    list_ddos = []
    list = []
    for k in range(1, nb+1):
        list_normal.append(read_document("CSV/"+namenor+str(k)+".csv"))
        list_ddos.append(read_document("CSV/"+nameddo+str(k)+".csv"))
    n = len(list_normal[0])
    max = math.floor(2*nb*n *0.8) # compute the maximun number of packet in the list
    for k in range(max):
        nb_list = rd.randint(0,4)
        nb_element = rd.randint(0, n-1)
        if rd.random() > prob_ddos:
            list.append(list_normal[nb_list][nb_element])
        else:
            attacker= rd.randint(1, nb_attacker)
            for i in range(attacker):
                list.append(list_ddos[nb_list][nb_element])
    list.sort()
    return list

def generate_data_one_type(name, nb, capacity = 0.8, ddos = False, nb_attacker= 1):
    """ Generate a normal or a DDoS data"""
    list = []
    res = []
    for k in range(1, nb+1):
        list.append(read_document("CSV/"+name+str(k)+".csv"))
    n = len(list[0])
    max = math.floor(2*nb*n * capacity) # compute the maximun number of packet in the list
    for k in range(max):
        nb_list = rd.randint(0,4) # a packet are randomly selected from the simulation CSV
        nb_element = rd.randint(0, n-1)
        if ddos and nb_attacker != 1: # define if many packet of the same size are sent or not
            attacker= rd.randint(1, nb_attacker)
            for i in range(attacker):
                res.append(list[nb_list][nb_element])
        else:
            res.append(list[nb_list][nb_element])
    res.sort()
    return res


def generate_dataset(list, value_time):
    '''Compute the number of packet and the total size during value_time '''
    cmpt = 0 # count the number of packet
    time = value_time
    n = len(list)
    res = []
    while cmpt != n:
        elem_size = [0,0]
        while cmpt < n and list[cmpt][0] < time:
            elem_size[0] += 1
            elem_size[1] += list[cmpt][1]
            if cmpt != n:
                cmpt += 1

        if elem_size[0] != 0:
            res.append(elem_size)
        time += value_time
    return res


list = generate_data("Normal","DDoS",5, 0.5)
res = generate_dataset(list, 10)

list_attacker = generate_data("Normal", "DDoS", 5, 0.4, 5)
res_attacker = generate_dataset(list_attacker, 10)

# Dataset of a normal traffic
list_norm = generate_data_one_type("Normal", 5)
res_norm = generate_dataset(list_norm,10)

# Dataset of DDoS attack with multiple attacker
list_ddos_full = generate_data_one_type("Normal", 5, 1, True, 5)
res_ddos_full = generate_dataset(list_ddos_full, 10)

# Dataset of DDoS attack with big packet
list_ddos = generate_data_one_type("DDoS", 5)
res_ddos = generate_dataset(list_ddos, 10)

# Dataset of a normal traffic using all the channel
list_norm_full = generate_data_one_type("Normal", 5, 1)
res_norm_full = generate_dataset(list_norm_full, 10)

# Dataset of DDoS with mix element of big packet and multiple attackers
list_ddos_att = generate_data_one_type("DDoS", 5, 0.8 , True, 5)
res_ddos_att = generate_dataset(list_ddos_att, 10)

# the two dataset below are not used in the project because they are very complex to analyse 
save_dataset(res, "mix_dataset.csv")
save_dataset(res_attacker, "mix_attacker_dataset.csv")

#The dataset below are used in the project
save_dataset(res_norm, "norm_dataset.csv")
save_dataset(res_norm_full, "normal_full_dataset.csv")
save_dataset(res_ddos_full, "ddos_full_dataset.csv")
save_dataset(res_ddos, "ddos_dataset.csv")
save_dataset(res_ddos_att, "ddos_att_dataset.csv")