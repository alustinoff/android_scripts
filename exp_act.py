import xml.etree.ElementTree as ET
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file')
args = parser.parse_args()

def show_exp_activity(root):
	ns = "{http://schemas.android.com/apk/res/android}"

	for act in root.iter('activity'):
		name = act.get(ns + "name")
		isExported = act.get(ns + "exported")
		if not isExported == 'false':
			intent_list = []

			for filter in act.iter('intent-filter'):
				for action in filter.iter('action'):
					intent_list.append(action.get(ns + "name"))

			if len(intent_list):
				print('Activity: ', name)
				print('Is exported: ', isExported if isExported else 'Not defined')
				for intent in intent_list:
					print("Intent action: ", intent)
				print('___________________________________________________________________________','\n')	

if args.file:
	tree = ET.parse(args.file)
	root = tree.getroot()
	show_exp_activity(root)
else:
	root = ET.fromstring(sys.stdin.buffer.read())
	show_exp_activity(root)
