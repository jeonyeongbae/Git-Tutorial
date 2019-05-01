import requests
from bs4 import BeautifulSoup


####################################################################################
def list_print(key):

	f = open('data/' + key + '.html', 'w')

	img_url = 'http://www.youngartdg.com/php/getList.php?type=img&limit=1000&order=uid&Pstart=0&cate='+ key +'&order=uid'

	img_r = requests.get(img_url)
	img_soup = BeautifulSoup(img_r.text, 'html.parser')
	img = img_soup.findAll('image')
	link = img_soup.findAll('price')
	name = img_soup.findAll('name')

	# 이미지 링크 출력
    
	# print(key + '카테고리')

	n = 0
	while n < len(img):
	    data = '<img src="http://youngartdg.com/' + img[n].text + '">\n'
	    f.write(data)
	    n = n + 1

	f.close()

####################################################################################	  

cate_url = 'http://www.youngartdg.com/index.php'
cate_r = requests.get(cate_url)
cate_soup = BeautifulSoup(cate_r.text, 'html.parser')
cate = cate_soup.findAll('span', {'class' : 'hand'})

# 카테고리 값 출력
cate_list = []

# Loop Count
count = 0


for i in cate:
	cate_list.append(i.attrs['onclick'].split('=')[3][:3])
	list_print(cate_list[count])
	count += 1

print(count)

# while count < len(cate):
# 	list_print(cate_list[count])
# 	count = count + 1
