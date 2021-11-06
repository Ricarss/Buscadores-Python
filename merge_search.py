def merge_join(l):

    if len(l) > 1:

        mid = len(l)//2
        left = l[:mid]
        right = l[mid:]

        print(f'left= {left}, right={right}, mid={mid}')

        merge_join(left)
        merge_join(right)

        b_l = l
        i = 0
        j = 0
        k = 0

        while i < len(left) and j < len(right):

            if left[i] < right[j]:
                b_l[k] = left[i]
                i+=1
            else:
                b_l[k] = right[j]
                j+=1
            
            print(l)
            
            k+=1

        while i < len(left):

            b_l[k] = left[i]
            i += 1
            k += 1

        while j < len(right):

            b_l[k] = right[j]
            j += 1
            k += 1

    return l

if __name__ == '__main__':

    ar = [3,9,4,6]
    ar = merge_join(ar)
    print(ar)
