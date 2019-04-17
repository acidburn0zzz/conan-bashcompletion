from __future__ import print_function
import yaml
import os

home=os.getenv('HOME')
f = open(home+"/.conan/settings.yml")
yaml_file = yaml.safe_load(f)


def serialize(x,prefix,isKey):
	for sample in x:
		#print("type of ",prefix+sample,"=",type(x[sample]))
		new_prefix=prefix		
		if isKey:		
			if prefix == "":			
				new_prefix=sample
			else:
				new_prefix=prefix+"."+sample
    			print(new_prefix+"=",end='')
			if type(x[sample]) is dict or type(x[sample]) is list:
				for y in x[sample]:
					print(y," ",end='')
				print("")
		if type(x[sample]) is dict:
			serialize(x[sample],new_prefix,not isKey)
		
serialize(yaml_file,"",True)

