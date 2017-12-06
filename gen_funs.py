def CalcGCcont(dna):
    gcnt = 0
    ccnt = 0
    
    for p in dna: 
        if p == 'G': 
            gcnt += 1;
        if p == 'C':
            ccnt += 1;  
    
    total = gcnt + ccnt 
    prop = total/len(dna)
    
    return prop 

def SeqOverlap(dna, window_size = 10):
    
    if window_size > len(dna):
        print('size of window to big')
        return 
    if window_size <= 0:
        print('negative window size is forbidden')
    
    #calculate max no of overlapping windows
    #plus one due to starting at 0 
    maxWins = len(dna)+1 - (window_size)
    windows = []
    ind = 0
    for i in range(maxWins): 
        window = dna[ind:ind+window_size]
        windows.append(window)
        ind +=1 
    
    return windows

def windowGCprop(dna, window):
    seqs = SeqOverlap(dna, window)
    gc_prop_list = []
    for seq in seqs:
        gc_prop_list.append(CalcGCcont(seq))
    return gc_prop_list

