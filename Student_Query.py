
import urllib.request
import json
import xls_json

student_info = xls_json.get_studentinfo()

def get_degreeavggpa(url):
	response = urllib.request.urlopen(url)
	response_json = json.loads(response.read())
	return str(response_json['data'])

def get_createscore(url):
	response = urllib.request.urlopen(url)
	response_json = json.loads(response.read())
	return str(response_json['total'])

def get_levelscore(url):
	response = urllib.request.urlopen(url)
	response_json = json.loads(response.read())
	result_list = []
	for i in range(len(response_json)):
		djksmc = response_json[i]['djksmc']
		cj = response_json[i]['cj']
		ksrq = response_json[i]['ksrq']
		result = {ksrq: {djksmc: cj}}
		result_list.append(result)
	return result_list

def get_failed(url):
	response = urllib.request.urlopen(url)
	response_json = json.loads(response.read())
	result_list = []
	if response_json != []:
		for i in range(len(response_json)):
			kcmc = response_json[i]['kcmc']
			kcxz = response_json[i]['kcxz']
			xf = response_json[i]['xf']
			cj = response_json[i]['cj']
			response_list = [kcmc, kcxz, xf, cj]
		return response_list
	# else:
	#

def get_info():
	info = input("请输入学号或姓名：")
	if 48 < ord(info[:1]) < 57:
		XH = info
	else:
		XM = info
		for no, value in student_info.items():
			if value[0] == XM:
				XH = no
	return XH

def levelscore_action_out(result_list):
	for item in result_list:
		for time, value in item.items():
			for cet, score in value.items():
				print(time + ": " + cet + ": " + score)

def failed_action_out(result_list):
	print("未通过科目：")
	for value in result_list:
		if value[-2:-1] == ".":
			print("\n学分:" + value + " 成绩:", end="")
		else:
			print(value + " ", end="")
	print()

# change to [{},{}] ?
def query_record(no, name, proname, degreeavggpa, createscore):
	query_data = json.dumps({no:[name, proname, degreeavggpa, createscore]})
	with open('query_record', 'a+', encoding='utf-8') as f:
		f.write(query_data + "\n")
		f.close()

if __name__ == '__main__':

	XH = get_info()
	XM = str(student_info[XH][0])
	proname = str(student_info[XH][2])
	path = "http://***"
	degreeavggpa_action = "Degreeavggpa?XH="
	createscore_action = "createscore?XH="
	levelscore_action = "getLevelScore?XH="
	failed_action = "getfailByXH?XH="
	degreeavggpa_url = path + degreeavggpa_action + XH
	createscore_url = path + createscore_action + XH
	levelscore_url = path + levelscore_action + XH
	failed_url = path + failed_action + XH

	degreeavggpa = get_degreeavggpa(degreeavggpa_url)
	createscore = get_createscore(createscore_url)
	levelscore = get_levelscore(levelscore_url)
	failed = get_failed(failed_url)




	action_out = "学位课平均绩点：" + degreeavggpa + "\n创新创业学分：" + createscore
	print("\n学号：" + XH)
	print("姓名：" + XM)
	print("专业：" + proname)
	print(action_out)
	print("四六级成绩：")
	levelscore_action_out(levelscore)
	failed_action_out(failed)
	query_record(XH, XM, proname, degreeavggpa, createscore)
	