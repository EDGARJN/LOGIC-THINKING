def uni_min(data):
    sorted_data = sorted(data)
    redundancy = []
    unique = []

    for x in range(0,len(sorted_data)-1):
          if sorted_data[x] == sorted_data[x+1]:
             redundancy.append(sorted_data[x])
          else:
             continue
    for y in sorted_data:
        if y in redundancy:
           continue
        else:
           unique.append(y)
    print(data)
    print(redundancy)
    print(sorted_data)
    print(unique)
    print(f'Unique value but small is {unique[0]}')

z = uni_min([19,2,17,6,0,34,56,2,56,0,1,19,6,1,17])
z
