from __future__ import division
import csv
import collections
import sys
from pprint import pprint

city_list = ['Aikmel, Lombok Timur',
             'Alas Barat, Sumbawa',
             'Alas, Sumbawa',
             'Ambalawi, Bima',
             'Ampenan, Kota Mataram',
             'Asakota, Bima',
            'Batu Lanteh, Sumbawa',
            'Batu Layar, Lombok Barat',
            'Batukliang Utara, Lombok Tengah',
            'Batukliang, Lombok Tengah',
            'Bayan, Lombok Utara',
            'Belo, Bima',
            'Bolo, Bima',
            'Brang Ene, Sumbawa Barat',
            'Brang Rea, Sumbawa Barat',
            'Buer, Sumbawa',
            'Cakranegara, Kota Mataram',
            'Dompu, Dompu',
            'Donggo, Bima',
            'Empang, Sumbawa',
            'Gangga, Lombok Utara',
            'Gerung, Lombok Barat',
            'Gunung Sari, Lombok Barat',
            'Hu\'u, Dompu',
            'Janapria, Lombok Tengah',
            'Jereweh, Sumbawa Barat',
            'Jerowaru, Lombok Timur',
            'Jonggat, Lombok Tengah',
            'Kayangan, Lombok Utara',
            'Kediri, Lombok Barat',
            'Kempo, Dompu',
            'Keruak, Lombok Timur',
            'Kilo, Dompu',
            'Kopang, Lombok Tengah',
            'Kuripan, Lombok Barat',
            'Labangka, Sumbawa',
            'Labuapi, Lombok Barat',
            'Labuhan Badas, Sumbawa',
            'Labuhan Haji, Lombok Timur',
            'Lambitu, Bima',
            'Lambu, Bima',
            'Langgudu, Bima',
            'Lantung, Sumbawa',
            'Lape, Sumbawa',
            'Lembar, Lombok Barat',
            'Lenangguar, Sumbawa',
            'Lingsar, Lombok Barat',
            'Lopok, Sumbawa',
            'Lunyuk, Sumbawa',
            'Mada Pangga, Bima',
            'Maluk, Sumbawa Barat',
            'Manggelewa, Dompu',
            'Maronge, Sumbawa',
            'Masbagik, Lombok Timur',
            'Mataram, Kota Mataram',
            'Monta, Bima',
            'Montong Gading, Lombok Timur',
            'Moyo Utara, Sumbawa',
            'Moyohilir, Sumbawa',
            'Moyohulu, Sumbawa',
            'Mpunda, Bima',
            'Narmada, Lombok Barat',
            'Orong Telu, Sumbawa',
            'Pajo, Dompu',
            'Palibelo, Bima',
            'Parado, Bima',
            'Parewa, Bima',
            'Pekat, Dompu',
            'Pemenang, Lombok Utara',
            'Plampang, Sumbawa',
            'Poto Tano, Sumbawa Barat',
            'Praya Barat Daya, Lombok Tengah',
            'Praya Barat, Lombok Tengah',
            'Praya Tengah, Lombok Tengah',
            'Praya Timur, Lombok Tengah',
            'Praya, Lombok Tengah',
            'Pringgabaya, Lombok Timur',
            'Pringgarata, Lombok Tengah',
            'Pringgasela, Lombok Timur',
            'Pujut, Lombok Tengah',
            'Raba, Bima',
            'Rasanae Barat, Bima',
            'Rasanae Timur, Bima',
            'Rhee, Sumbawa',
            'Ropang, Sumbawa',
            'Sakra Barat, Lombok Timur',
            'Sakra Timur, Lombok Timur',
            'Sakra, Lombok Timur',
            'Sambelia, Lombok Timur',
            'Sandubaya, Kota Mataram',
            'Sanggar, Bima',
            'Sape, Bima',
            'Sekarbela, Kota Mataram',
            'Sekongkang, Sumbawa Barat',
            'Sekotong Tengah, Lombok Barat',
            'Selaparang, Kota Mataram',
            'Selong, Lombok Timur',
            'Sembalun, Lombok Timur',
            'Seteluk, Sumbawa Barat',
            'Sikur, Lombok Timur',
            'Soromandi, Bima',
            'Suela, Lombok Timur',
            'Sukamulia, Lombok Timur',
            'Sumbawa, Sumbawa',
            'Suralaga, Lombok Timur',
            'Taliwang, Sumbawa Barat',
            'Tambora, Bima',
            'Tanjung, Lombok Utara',
            'Tarano, Sumbawa',
            'Terara, Lombok Timur',
            'Unter Iwes, Sumbawa',
            'Utan, Sumbawa',
            'Wanasaba, Lombok Timur',
            'Wawo, Bima',
            'Wera, Bima',
            'Woha, Bima',
            'Woja, Dompu',
            'Maluku Utara, Indonesia',
            'Nusa Tenggara Barat, Indonesia',
            'Nusa Tenggara Timur, Indonesia',
            'North Moluccas, Indonesia',
            'Lombok Utara, Nusa Tenggara Barat',
            'Lombok Tengah, Nusa Tenggara Barat',
            'Lombok Timur, Nusa Tenggara Barat',
            'Lombok Barat, Nusa Tenggara Barat',
            'Bima, Nusa Tenggara Barat',
            'Sumbawa, Nusa Tenggara Barat',
            'Kota Mataram, Nusa Tenggara Barat',
            'Dompu, Nusa Tenggara Barat',
            'NULL',
            ]

maxInt = sys.maxsize
csv.field_size_limit(maxInt)
with open('step_3_output_concatenation_location_dataset.csv','rU') as csv_file:
    with open('step_5_output_normalizer_location_dataset.csv','wb') as csv_result:
        reader = csv.reader(csv_file,delimiter='|')
        writer = csv.writer(csv_result,delimiter='|')
        
        output = []
        
        for i, line in enumerate(reader):    
			matrix_output = []
			normalize_counter = 0.0
			print ('username :   ',line[0])
			#line[1:][0] artinya masuk kedalam item pertama dalam list untuk dapat di split
			username_city = line[1:][0]
			c = collections.Counter(username_city.split(' ; '))
			print username_city
			
			#to count total location per username
			for city in city_list:
				#print '   %s : %d' % (city, c[city])
				normalize_counter = normalize_counter + c[city]
				matrix_output.append(c[city])

			#total location
			#print matrix_output
			print normalize_counter
			divided_location = 0    
			# divide location with total location
			matrix_normalize_output = []
			for counter in matrix_output:
				if counter == 0:
					divided_location = 0.0
					#print('this value zero', divided_location)
					matrix_normalize_output.append(divided_location)
				else:
					divided_location = (counter/normalize_counter)
					print('counter  :', counter)
					print('normalize :', normalize_counter)
					print('this is normalizer : ',divided_location)
					matrix_normalize_output.append(divided_location)
				
			#print matrix_output
			print ("this is normalizer matrix")
			print matrix_normalize_output
			print ("--------")
			print ("--------")

			writer.writerow(matrix_normalize_output)
			#od[line[0]] = {}
			#od[line[0]]['city'] = c[city]
			#output.append(od)
			#pprint(output)

		

