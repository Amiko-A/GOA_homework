def array_plus_array(arr1, arr2):
    res=0
    
    for i in range (len(arr1)):
        res += arr1[i]
        
    for u in range (len(arr2)):
        res += arr2[u]
        
    return res
