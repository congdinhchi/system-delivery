
import random
import copy

import sys

sys.path.append('/Users/dinhchicong/Project/scheduled-delivery')

from util.duplicate import copy_individual

def choice_mutate(population):
    
    num_individual = len(population)-1
    random_number = random.randint(0,num_individual)

    return population[random_number]

def mutate_chromosomes(id, individual):

    new_individual = copy.deepcopy(individual)
    list_target = new_individual.get_list_target()
    for j in range(0,len(list_target)):

        target = list_target[j]
        list_trip = target.get_trip()

        # dot bien
        for i in range (0, len(list_trip)):
            tmp = random.random()
            if tmp<0.3:
                id_target = list_trip[i][0]
                weight_package = list_trip[i][1] + random.randint(0,10)
                list_trip[i] = [id_target, weight_package]
        
        #gan lai
        target.change_list_trip(list_trip)
        new_individual.update_target(target, j)

    new_individual = copy_individual(id, new_individual)

    return new_individual