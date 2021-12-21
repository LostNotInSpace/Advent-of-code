import numpy as np

def gamma_rate(counts, l):
    return(counts > l/2)

def binary_to_int(bool_list):
    powers = np.flip(np.power(2,np.arange(len(bool_list))))
    return(np.sum(powers*bool_list))



def main():
    counts = None
    with open('day3input.txt','r') as f:
        line = f.readline()
        counts = np.array([int(el) for el in line.rstrip()])
        l = 1
        while line:
            line = f.readline()
            if len(line) > 0:
                counts += np.array([int(el) for el in line.rstrip()])
                l += 1
            
    gr = gamma_rate(counts,l)
    er = np.logical_not(gr)
    gr = binary_to_int(gr)
    er = binary_to_int(er)
    print(gr*er)
    

if __name__ == '__main__':
    main()