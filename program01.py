# -*- coding: utf-8 -*-

def decode_XKCD_tuple(xkcd_values : tuple[str, ...], k : int) -> list[int]:
    '''
    Receives as arguments a list of strings representing values in the
    XKCD format, and a positive integer k <= len(xkcd_values).
    Decodes all XKCD formatted values and return the k higher values
    sorted in decreasing order.

    Parameters
    xkcd_values : list[str]     list of strings (values) in XKCD format
    k : int                     how many values to return
    Returns
    list[int]                   k maximum values in decreasing order
    '''
    # ADD HERE YOUR CODE
    result=[]
    for l in xkcd_values:
        li = list(l)
        weights=[l[0]]
        j=0
        for i in range(1,len(l)):
            if li[i]=="1" or li[i]=="5":
                j+=1
                weights.append(li[i])
            else:
                weights[j]=weights[j]+li[i]
        weights=list(map(int,weights))
        ans = weights[len(weights)-1]
        x=len(weights)
        for i in weights[-2::-1]:
            x-=1
            if i>=weights[x]:
                ans+=i
            else:
                ans-=i
        result.append(ans)
        result.sort(reverse=True)
    return result[:k]


def decode_value(xkcd : str ) -> int:
    '''
    Decode a string representing a value in XKCD format
    and returns the corresponding decimal value (integer).

    Parameters
    xkcd : str                  string in XKCD format
    Returns
    int                         the corresponding value
    
    E.g.: '10010010010100511' -> 397
    '''
    # ADD HERE YOUR CODE
    li = list(xkcd)
    weights=[xkcd[0]]
    j=0
    for i in range(1,len(xkcd)):
        if li[i]=="1" or li[i]=="5":
            j+=1
            weights.append(li[i])
        else:
            weights[j]=weights[j]+li[i]
    weights=list(map(int,weights))
    ans = weights[len(weights)-1]
    x=len(weights)
    for i in weights[-2::-1]:
        x-=1
        if i>=weights[x]:
            ans+=i
        else:
            ans-=i
    return ans 
    


def xkcd_to_list_of_weights(xkcd : str) -> list[int]:
    '''
    Splits an XKCD formatted string into the corresponding
    list of weights, each corresponding to one of the original roman 
    numeral symbols the encoding is based on.

    Parameters
    xkcd : str              XKCD formatted string
    Returns
    list[int]               list of 'weights' corresponding to roman symbols

    E.g.: '10010010010100511' -> [100, 100, 100, 10, 100, 5, 1, 1,]
    '''
    # ADD HERE YOUR CODE
    li = list(xkcd)
    weights=[xkcd[0]]
    j=0
    for i in range(1,len(xkcd)):
        if li[i]=="1" or li[i]=="5":
            j+=1
            weights.append(li[i])
        else:
            weights[j]=weights[j]+li[i]
    weights=list(map(int,weights))
    return weights


def list_of_weights_to_number(weights : list[int] ) -> int:
    '''
    Transforms a list of weights obtained from the XKCD format
    to the corresponding decimal value, by using the 'sum/subtract' rules.

    Parameters
    weights : list[int]    list of 'weights' of Roman numerals
    Returns
    int                    corresponding integer value
    
    E.g.: [100, 100, 100, 10, 100, 5, 1, 1,] -> 397
    '''
    # ADD HERE YOUR CODE
    ans = weights[len(weights)-1]
    x=len(weights)
    for i in weights[-2::-1]:
        x-=1
        if i>=weights[x]:
            ans+=i
        else:
            ans-=i
    return ans 

if __name__ == '__main__':
