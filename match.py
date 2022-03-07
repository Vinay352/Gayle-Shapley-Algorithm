"""
CSCI-665:
Authors: Omkar Morogiri,om5692
         Vinay Jain,vj9898

Aim:     Implementations of Gayle shapley algorithm
"""
def take_input(n):
    asker = [[0 for i in range(n)] for j in range(n)]
    askee = [[0 for i in range(n)] for j in range(n)]
    # complexity O(n^2)
    for i in range(n):
        line = input().strip().split(" ")
        j = 0
        while j < n:
            asker[i][j] = int(line[j].strip())
            j += 1

    # print(asker)

    # complexity O(n^2)
    for i in range(n):
        line = input().strip().split(" ")
        j = 0
        while j < n:
            askee[i][j] = int(line[j].strip())
            j += 1

    # print(askee)

    return asker, askee

"""
Initialize asker array
param data: n
return: array of askers
"""
def intialize_asker_arr(n):
    #complexity O(n) for n elements
    asker_arr = [-1 for i in range(n)]
    return asker_arr

"""
Initialize askee array
param data: n
return: dictionary of askee
"""
def intialize_askee_dict(n):
    # complexity O(n) for n keys
    askee_dict = dict.fromkeys([i for i in range(n)], -1)
    return askee_dict

"""
Initialize askee stack
param data: n
return: stack of askee
"""
def initialize_asker_stk(n):
    # complexity O(n) for n elements
    turn_stk = [i for i in range(n-1, -1, -1)]
    return turn_stk


"""
gayle shapley algorithm implementation
param data: n, asker_preference, askee_preference, asker_assignment_arr, askee_assignment_dict, asker_turn_stk
return: asker array, askee dictionary
"""
def gayle_shapley(n, asker_preference, askee_preference, asker_assignment_arr, askee_assignment_dict, asker_turn_stk):
    # print(asker_preference)
    # while loop will run for length of stack times

    # Total complexity O(n^2)
    while len(asker_turn_stk) != 0: # complexity of popping n elements from a stack is O(n)
        current_asker = asker_turn_stk.pop() # complexity O(1)
        j = 0
        #while loop will run for n times - complexity O(n)
        while j < n:
            # print(current_asker, end = " ")
            # print(j)
            cur_preference_of_asker = asker_preference[current_asker][j] # O(1)
            askee_assigned_to = askee_assignment_dict.get(cur_preference_of_asker) # O(1)

            if(askee_assigned_to == -1): # O(1)
                askee_assignment_dict[cur_preference_of_asker] = current_asker
                asker_assignment_arr[current_asker] = cur_preference_of_asker
                break
            else:
                cur_priority = askee_preference[asker_preference[current_asker][j]].index(askee_assignment_dict[cur_preference_of_asker])# O(1)
                new_priority = askee_preference[asker_preference[current_asker][j]].index(current_asker) # O(1)

                if( new_priority < cur_priority ):
                    asker_assignment_arr[current_asker] = cur_preference_of_asker # O(1)
                    old_asker = askee_assignment_dict.get(cur_preference_of_asker) # O(1)
                    askee_assignment_dict[cur_preference_of_asker] = current_asker # O(1)
                    asker_assignment_arr[old_asker] = -1 # O(1)
                    asker_turn_stk.append(old_asker) # O(1)
                    break
                else:
                    pass

            j += 1

    # print(askee_assignment_dict)
    # print()
    # print(asker_assignment_arr)
    # print()

    return asker_assignment_arr, askee_assignment_dict

"""
comparing matching - if we can find a better match or not
param data: n, asker_assignment_arr, askee_assignment_dict_new
return: 
"""
def compare_matching(n, asker_assignment_arr, askee_assignment_dict_new):
    similar_count = True

    # complexity O(n)
    for i in range(n):
        if asker_assignment_arr[i] != askee_assignment_dict_new[i]:
            similar_count = False
            break

    # complexity O(1)
    if similar_count:
        print("NO")
    else:
        print("YES")

"""
THis is the main function which implements stable matching.
Here, first asker is asking askee which gives one stable matching
Then askee and asker are switched and askee ask askers which gives
us second stable mathing

We then compare these 2 outputs to see if multiple stable matching
is possible or not
"""
def main():
    # take input
    n = int(input())

    # taking input into asker and askee preference
    asker_preference, askee_preference = take_input(n)

    # which asker (index) is assigned to which askee (element of array)
    asker_assignment_arr = intialize_asker_arr(n)
    # print(asker_assignment_arr)

    # which askee (key) is assigned to which asker (value)
    askee_assignment_dict = intialize_askee_dict(n)
    # print(askee_assignment_dict)

    # initialize order of turns for the askers
    asker_turn_stk = initialize_asker_stk(n)
    # print(asker_turn_stk)
    # print(asker_turn_stk.pop())

    # implement stable matching algorithm and return which asker is assigned to
    # which askee (asker_asignment_arr) and which askee is assigned to which asker
    # (askee_assignment_dict)
    asker_assignment_arr, askee_assignment_dict = gayle_shapley(n, asker_preference, askee_preference,
                                                                asker_assignment_arr, askee_assignment_dict,
                                                                asker_turn_stk)

    # switching akser and askee
    # in other words, nor askee will the askers and previous askers will be the askee
    asker_preference, askee_preference = askee_preference, asker_preference

    asker_assignment_arr_new = intialize_asker_arr(n)
    # print(asker_assignment_arr)

    askee_assignment_dict_new = intialize_askee_dict(n)
    # print(askee_assignment_dict)

    asker_turn_stk_new = initialize_asker_stk(n)
    # print(asker_turn_stk)
    # print(asker_turn_stk.pop())

    # implement stable matching algorithm
    asker_assignment_arr_new, askee_assignment_dict_new = gayle_shapley(n, asker_preference, askee_preference,
                                                                asker_assignment_arr_new, askee_assignment_dict_new,
                                                                asker_turn_stk_new)

    # compare matchings of 2 scenarios, if same matching output NO, else YES
    # One where askers asked askees
    # second where askees asked askers
    compare_matching(n, asker_assignment_arr, askee_assignment_dict_new)

# conditional guard
if __name__ == "__main__":
    main()