import numpy as np

def oxygen_rating(data):

    index = 0
    while data.shape[0] > 1:
        most_common = int(sum(data[:,index]) >= data.shape[0]/2)
        data = data[data[:,index] == most_common,:]
        index += 1
    
    return(data.flatten())

def scrubber_rating(data):

    index = 0
    while data.shape[0] > 1:
        most_common = int(sum(data[:,index]) < data.shape[0]/2)
        data = data[data[:,index] == most_common,:]
        index += 1
    
    return(data.flatten())

def binary_to_int(bool_list):
    powers = np.flip(np.power(2,np.arange(len(bool_list))))
    return(np.sum(powers*bool_list))

        

def main():
    datastream = []
    with open('day3input.txt','r') as f:
        line = f.readline()
        datastream = [np.array([int(el) for el in line.rstrip()])]
        while line:
            line = f.readline()
            if len(line) > 0:
                datastream.append(np.array([int(el) for el in line.rstrip()]))

    datastream = np.array(datastream)
    ox_rating = oxygen_rating(datastream)
    scrub_rating = scrubber_rating(datastream)
    print(ox_rating)
    print(scrub_rating)

    ls = binary_to_int(ox_rating)*binary_to_int(scrub_rating)

    print(f"The life support rating is {ls}.")

    
    

if __name__ == '__main__':
    main()