def merge_sort(seq):
    if len(seq)<=1:
        return seq

    mid=int(len(seq)/2)
    left_half=merge_sort(seq[:mid])
    right_half=merge_sort(seq[mid:])
    print(f"left=={left_half},right=={right_half}")
    new_seq=merge_sort_list(right_half,left_half)
    return new_seq

def merge_sort_list(seq_a,seq_b):
    count_a,count_b=len(seq_a),len(seq_b)
    a,b=0,0
    new_sorted_seq = list()
    while a<count_a and b<count_b:
        if seq_a[a]>=seq_b[b]:
            new_sorted_seq.append(seq_a[a])
            a+=1
        else:
            new_sorted_seq.append(seq_b[b])
            b+=1

    while a<count_a:
        new_sorted_seq.append(seq_a[a])
        a+=1

    while b<count_b:
        new_sorted_seq.append(seq_b[b])
        b+=1

    return new_sorted_seq


lists=[5,3,9,8,74,5,2,6,8,7]
test=merge_sort(lists)
print(test)