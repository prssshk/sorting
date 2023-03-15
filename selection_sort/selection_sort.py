from wedding_class import wedding
import csv
import time


def selection_sort(array):
    n = len(array)
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if array[j] < array[min_index]:
                min_index = j
        (array[i], array[min_index]) = (array[min_index], array[i])
    return array

tmp = []
with open('couples100000.csv', newline='') as state_file:
    reader = csv.reader(state_file)
    for i in reader:
        tmp.append(wedding(i[0], i[1],i[2],i[3],i[4],i[5]))

start_time = time.time()
out = selection_sort(tmp)
end_time = time.time() - start_time
with open('time_test.csv', 'a', newline='', encoding="windows-1251") as state_file:
    writer = csv.writer(state_file)
    writer.writerow(["{} elements: {} seconds".format(len(out),end_time)])

with open('couples100000_sorted.csv', 'a', newline='', encoding="windows-1251") as state_file:
    writer = csv.writer(state_file)
    for i in out:
        writer.writerow([i.male,i.male_bday,i.female,i.female_bday,i.wedding_date,i.zags_number])


