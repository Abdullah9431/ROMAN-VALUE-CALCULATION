xkcd = "10010010010100511"
def gt(xkcd :str):
    li = list(xkcd)
    new=[xkcd[0]]
    i,j=0,0
    while i<len(xkcd)-1:
        i+=1
        if li[i]=="1" or li[i]=="5":
            j+=1
            new.append(li[i])
        else:
            new[j]=new[j]+li[i]
    return new
            
        
        