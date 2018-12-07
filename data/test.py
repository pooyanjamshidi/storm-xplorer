import os
import pandas as pd
import csv

folders = ['./feature6/','./feature7/','./feature8/','./feature9/',]
columns = ['topology.workers', 'component.bolt_num', 'topology.acker.executors', 'message.size', 'component.spout_num', 'topology.serialized.message.size.metrics', 'topology.max.spout.pending', 'storm.messaging.netty.min_wait_ms', 'topology.transfer.buffer.size', 'storm.messaging.netty.max_wait_ms', 'topology.level', 'topology.priority']

for folder in folders:
	myfile1 = open(folder[2:-1]+'_obj1.csv', 'w')
	myfile2 = open(folder[2:-1]+'_obj2.csv', 'w')

	writer1 = csv.writer(myfile1)
	writer2 = csv.writer(myfile2)

	header_o1 = columns + ['<$throughput']
	header_o2 = columns + ['<$latency']

	writer1.writerow(header_o1)
	writer2.writerow(header_o2)

	print '= = ' * 20
	files = [folder+f for f in os.listdir(folder) if '.yaml' in f]
	all_files = {}
	print folder, len(files)
	for f in files:
		# for yaml files
		content = open(f).readlines()
		temp = {}
		for c in content:
			t = c.strip().split(':')
			key = t[0]
			value = ''.join(t[1:]).strip()
			if key in columns:
				temp[key] = value

		# for .csv file
		csvfile = f.replace('.yaml', '.csv')
		csvcontent = pd.read_csv(csvfile)
		# getting rid of header and first 60 seconds
		csvcontent2 = csvcontent.iloc[6:]
		obj1 = csvcontent2['spout_throughput (messages/s)'].mean()
		obj2 = csvcontent2['spout_avg_complete_latency(ms)'].mean()
		row = [temp[column] for column in columns]
		assert(len(row) == len(temp.keys())), "Something is wrong"

		r1 = row + [obj1]
		r2 = row + [obj2]

		writer1.writerow(r1)
		writer2.writerow(r2)
		
	myfile1.close()
	myfile2.close()