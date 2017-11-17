import numpy as np
import csv

if __name__ == "__main__":
    #header = np.genfromtxt('titanic.csv',delimiter=',',max_rows=1,dtype=None)
    with open('titanic.csv', 'rb') as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        headers = next(reader,None)
        print(headers)
        converters = [int,int,str,str,str,str,str,str]
        data = np.array([[conv(col) for col, conv in zip(row, converters)] for row in reader])

        total = len(data)
        print(total)
        survived = len(data[data[:,0] == '1'])
        not_survived = len(data[data[:,0] == '0'])
        print(survived,not_survived,survived + not_survived)
        #conditional probability of survival, FIX!!!!
        for gender in ['female', 'male']:
            for Pclass in ['1', '2', '3']:
                survivors = data[(data[:,0] == '1') & (data[:,1] == Pclass) & (data[:,3] == gender)]
                all_found = data[(data[:,1] == Pclass) & (data[:,3] == gender)]
                print('{:.3f}'.format(len(survivors)/float(len(all_found))))

        #conditional probability of children surviving
        [children, surviving_children] = [0,0]
        for row in data:
            if row[1] == '3' and float(row[4]) < 11:
                children += 1
                if row[0] == '1':
                    surviving_children += 1
        print(children, surviving_children)

        #expected faire for each passenger class
        for Pclass in ['1', '2', '3']:
            total_class_faire = sum([float(row[7]) for row in data[data[:,1] == Pclass]])
            print(total_class_faire / len(data[(data[:,1] == Pclass)]))

