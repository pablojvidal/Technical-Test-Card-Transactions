import os

months = [{'id':'01', 'month':'january'},
		{'id':'02', 'month':'february'},
		{'id':'03', 'month':'march'},
		{'id':'04', 'month':'april'},
		{'id':'05', 'month':'may'},
		{'id':'06', 'month':'june'},
		{'id':'07', 'month':'july'},
		{'id':'08', 'month':'august'},
		{'id':'09', 'month':'september'},
		{'id':'10', 'month':'october'},
		{'id':'11', 'month':'november'},
		{'id':'12', 'month':'december'},		]

files_path = "D:/DATA SCIENCE/old dataset"
files_path_output = "D:/DATA SCIENCE/renamed_datasets"

filesRename = [file for file in os.listdir(files_path) if '.xls' in file]
# Iterate
for file in os.listdir(files_path):
	# Checking if the file is present in the list
	if file in filesRename:
		oldName = os.path.join(files_path, file)
		
		n = os.path.splitext(file)[0].split('-')
		matching_month = list(
    		filter( lambda x: x.get('month') == n[3], months )
		)
		if len(matching_month) > 0:
			b = n[4] + '-' + matching_month[0].get("id")+ '.xls'
			print(b)
			newName = os.path.join(files_path_output, b)
			# Rename the file
			os.rename(oldName, newName)

res = os.listdir(files_path_output)
print(res)




