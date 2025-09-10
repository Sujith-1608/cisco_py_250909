import pickle
flight ={ 'flight_number': 'I700','airline':'Indigo', 'capacity':225,'price':4500,'source':'Banglore','destination':'hyderabad' }

file_name='flight.dat'

print('before file:', flight)

with open(file_name,'wb') as writer:
    pickle.dump(flight, writer)
    print('Saved the flight to file')

with open(file_name,'rb') as reader:
    flight_from_file=pickle.load(reader)
    print('Flight after read from file: ',flight_from_file)