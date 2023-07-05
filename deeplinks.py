import xml.etree.ElementTree as ET
import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--file')
args = parser.parse_args()

def show_deeplinks(root):
	ns = "{http://schemas.android.com/apk/res/android}"

	for activity in root.iter('activity'):
		activity_name = activity.get(ns + "name")
		deeplinks = []
		filter_id = 0
		for filter in activity.iter('intent-filter'):
			
			for data in filter.iter('data'):
				scheme = data.get(ns + "scheme")
				host = data.get(ns + "host")
				if not scheme and not host:
					continue
				else:
					deeplinks.append([scheme if scheme else '', host if host else '', filter_id])
			filter_id += 1
			
		if len(deeplinks):
			print('Activity: ', activity_name)
			
			prev_filter = 0
			current_filter = None
			is_first_deeplink = True

			for deeplink in deeplinks:
				current_filter = deeplink[2]

				if prev_filter is not current_filter:
					prev_filter = deeplink[2]
					if not is_first_deeplink:
						print('_________________','\n')
				is_first_deeplink = False

				if deeplink[0] and deeplink[1]:
					print("Deeplink: " + deeplink[0] + '://' + deeplink[1])
				elif deeplink[0]:
					print("Scheme: " + deeplink[0] + '://')
				elif deeplink[1]:
					print("Host: " + deeplink[1])
				
			print('___________________________________________________________________________','\n')


if args.file:
	tree = ET.parse(args.file)
	root = tree.getroot()
	show_deeplinks(root)
else:
	root = ET.fromstring(sys.stdin.buffer.read())
	show_deeplinks(root)
