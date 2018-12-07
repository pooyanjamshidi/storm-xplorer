import os

folders = ['./features6/','./features7/','./features8/','./features9/',]

for folder in folders:
	print '= = ' * 20
	files = [folder+f for f in os.listdir(folder) if '.yaml' in f]
	all_files = {}
	print len(files), files[0]
	for f in files:
		content = open(f).readlines()
		for c in content:
			t = c.strip().split(':')
			key = t[0]
			value = ''.join(t[1:]).strip()
			if key not in all_files.keys():
				all_files[key]=[value]
			else:
				# print key, value, 
				all_files[key].append(value)
				# print len(all_files[key]), all_files[key]
				all_files[key]=list(set(all_files[key]))

	count = 0
	for key in all_files.keys():
		if len(all_files[key]) > 1:
			print count, key, len(all_files[key]), all_files[key]
			count += 1