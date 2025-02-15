
def what_distance(list1,list2):
    distance =[]
    total=0
    for i in range(len(list1)):  
        for n in range(len(list1)-i-1):
        
            if  list1[n] > list1[n+1]:
                list1[n], list1[n+1] = list1[n+1], list1[n]


    for i in range(len(list2)):  
        for n in range(len(list2)-i-1):
        
            if  list2[n] > list2[n+1]:
                list2[n], list2[n+1] = list2[n+1], list2[n]

     
    for i in range(len(list2)):
        distance.append(list1[i] - list2[i]) 


    for i in range(len(distance)):
        total+=distance[i]

    return total


def main():
    # Test data
    list1 = [5, 3, 5, 2, 1, 2, 3]
    list2 = [4, 5, 6, 4, 3, 2, 9]
    
    # Call the function and print the result
    result = what_distance(list1, list2)
    print(result)

if __name__ == "__main__":
    main()
