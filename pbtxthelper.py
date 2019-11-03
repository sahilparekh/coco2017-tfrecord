from google.protobuf import text_format
import label_pb2

def dictToPbtxt(dict, filepath):

	wholelist = label_pb2.StringIntLabelMap()

	for k, v in dict.items():
		item = wholelist.item.add()
		print(v)
		item.name = v['name']
		item.display_name = v['name']
		item.id = int(k)

	wholelist_txt = text_format.MessageToString(wholelist)

	with open(filepath, "w") as f:
		f.write(wholelist_txt)

	print('Written pbtxt file')