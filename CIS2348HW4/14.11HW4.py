def selection_sort_descend_trace(int_list):
    for i in range(len(int_list)-1):
        lnumbers = i
        for x in range(i + 1, len(int_list)):
            if int_list[lnumbers] < int_list[x]:
                lnumbers = x
        int_list[i], int_list[lnumbers] = int_list[lnumbers], int_list[i]
        for inputnumber in int_list:
            print(inputnumber,end=" ")
        print()
    return int_list

if __name__ == "__main__":
    desc_list = [int(inputnumber) for inputnumber in input("").split()]
    selection_sort_descend_trace(desc_list)