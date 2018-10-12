
# coding: utf-8

# In[15]:


# 加载包
import requests
from bs4 import BeautifulSoup
import csv
import time
import pandas as pd
import datetime


# In[2]:


# 参数设置
## 增加重连次数
requests.adapters.DEFAULT_RETRIES = 5
base_url = 'http://www.ochirly.com.cn'
url_mid = 'list-'
url_end = '-40-listedDate%20desc-0-0-0-0-0.shtml'
header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 UBrowser/6.1.2107.204 Safari/537.36', 
          'Connection':'close'}


# In[28]:


# 读取商品分类信息:ochirly_category.csv
ochirly_category = pd.read_table('/Users/yunshan/Documents/Jeremy-python/01_data_processing/web_scraping/ochirly/ochirly_category.csv', 
                                 sep = ',', 
                                 encoding = 'gbk')
ochirly_category



# In[21]:


# 爬取商品的场景分类

print('开始爬取商品的场景分类')
cj_start_time = datetime.datetime.fromtimestamp(time.time())
cj_start_time2 = datetime.datetime.strftime(cj_start_time, '%H:%M:%S')
print('开始时间： ' + cj_start_time2)

## 从ochirly_category表中筛选场景购的信息
ochirly_changjing = ochirly_category.loc[ochirly_category.cat1 == '场景',]
## 重置row index为从0开始
ochirly_changjing = ochirly_changjing.reset_index(drop = True)
## 打开一个 csv 文件，把goods_id 和场景名称写入
csv_file = open('/Users/yunshan/Documents/Jeremy-python/01_data_processing/web_scraping/ochirly/ochirly_goods_changjing.csv', 
                'w', 
                newline = '', 
                encoding = 'utf-8-sig')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['goods_id', 'changjing'])
## 获取 goods_id 和场景名称
for row_num in range(ochirly_changjing.shape[0]):
    changjing = ochirly_changjing.loc[row_num, 'cat2']
    for page_num in range(ochirly_changjing.loc[row_num, 'page_num']):
        url1 = base_url + ochirly_changjing.loc[row_num, 'url'] + url_mid + str(page_num+1) + url_end
        page1 = requests.get(url1, headers = header)
        source1 = BeautifulSoup(page1.content, 'html.parser', from_encoding = 'gb18030')
        goods_infos = source1.find('div', class_ = 'product_list').find_all('li')
        for goods_info in goods_infos:
            goods_href = goods_info.find('a').get('href')
            url2 = base_url + goods_href
            page2 = requests.get(url2, headers = header)
            source2 = BeautifulSoup(page2.content, 'html.parser', from_encoding = 'gb18030')
            goods_id = source2.find('p', class_ = 'number').string.replace('编号 ', '')
            ## 把结果写入到 csv 文件中
            csv_writer.writerow([goods_id, changjing])
        # 休息一下
        time.sleep(3)
# 关闭 csv_file
csv_file.close()

print('场景分类爬取完成！')
cj_end_time = datetime.datetime.fromtimestamp(time.time())
cj_end_time2 = datetime.datetime.strftime(cj_end_time, '%H:%M:%S')
print('完成时间： ' + cj_end_time2)
cj_use_time = cj_end_time - cj_start_time
print('用时： ' + str(cj_use_time.seconds) + ' 秒')
print('=========================')


# In[27]:


# 爬取商品的上市日期

print('开始爬取商品的上市日期')
xp_start_time = datetime.datetime.fromtimestamp(time.time())
xp_start_time2 = datetime.datetime.strftime(xp_start_time, '%H:%M:%S')
print('开始时间： ' + xp_start_time2)

## 从ochirly_category表中筛选新品
ochirly_newin = ochirly_category.loc[ochirly_category.cat1 == '新品',]
## 重置row index为从0开始
ochirly_newin = ochirly_newin.reset_index(drop = True)
## 打开一个 csv 文件，把goods_id 和上市日期写入
csv_file = open('/Users/yunshan/Documents/Jeremy-python/01_data_processing/web_scraping/ochirly/ochirly_goods_newin.csv', 
                'w', 
                newline = '', 
                encoding = 'utf-8-sig')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['goods_id', 'newin_date'])
## 获取 goods_id 和上市日期
for row_num in range(ochirly_newin.shape[0]):
    newin_date = ochirly_newin.loc[row_num, 'cat2'].replace('到店', '').replace('月', '-').replace('日','')
    for page_num in range(ochirly_newin.loc[row_num, 'page_num']):
        url1 = base_url + ochirly_newin.loc[row_num, 'url'] + url_mid + str(page_num+1) + url_end
        page1 = requests.get(url1, headers = header)
        source1 = BeautifulSoup(page1.content, 'html.parser', from_encoding = 'gb18030')
        goods_infos = source1.find('div', class_ = 'product_list').find_all('li')
        for goods_info in goods_infos:
            goods_href = goods_info.find('a').get('href')
            url2 = base_url + goods_href
            page2 = requests.get(url2, headers = header)
            source2 = BeautifulSoup(page2.content, 'html.parser', from_encoding = 'gb18030')
            goods_id = source2.find('p', class_ = 'number').string.replace('编号 ', '')
            ## 把结果写入到 csv 文件中
            csv_writer.writerow([goods_id, newin_date])
        # 休息一下
        time.sleep(3)
# 关闭 csv_file
csv_file.close()

print('新品上市日期爬取完成！')
xp_end_time = datetime.datetime.fromtimestamp(time.time())
xp_end_time2 = datetime.datetime.strftime(xp_end_time, '%H:%M:%S')
print('完成时间： ' + xp_end_time2)
xp_use_time = xp_end_time - xp_start_time
print('用时： ' + str(xp_use_time.seconds) + ' 秒')
print('=========================')


# In[30]:


# ==================================================================
# 爬取所有服装商品 ===================================================
# 多个大类一起爬取
# ==================================================================

print('开始爬取服装')
fz_start_time = datetime.datetime.fromtimestamp(time.time())
fz_start_time2 = datetime.datetime.strftime(fz_start_time, '%H:%M:%S')
print('开始时间： ' + fz_start_time2)

## 从ochirly_category表中筛选服装的信息
ochirly_yifu = ochirly_category.loc[ochirly_category.cat1 == '服装',]
## 重置row index为从0开始
ochirly_yifu = ochirly_yifu.reset_index(drop = True)
## 打开一个 csv 文件，写入商品信息
csv_file = open('/Users/yunshan/Documents/Jeremy-python/01_data_processing/web_scraping/ochirly/ochirly_goods_info.csv', 
                'w', 
                newline = '', 
                encoding = 'utf-8-sig')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['category','goods_id','goods_name','color','sale_price','origin_price',
                     'design', 'material', 'stereotype', 'length', 'page_num'])
## 获取商品信息
for row_num in range(ochirly_yifu.shape[0]):
    category = ochirly_yifu.loc[row_num, 'cat2']
    for page_num in range(ochirly_yifu.loc[row_num, 'page_num']):
        url1 = base_url + ochirly_yifu.loc[row_num, 'url'] + url_mid + str(page_num+1) + url_end
        page1 = requests.get(url1, headers = header)
        source1 = BeautifulSoup(page1.content, 'html.parser', from_encoding = 'gb18030')
        goods_infos = source1.find('div', class_ = 'product_list').find_all('li')
        for goods_info in goods_infos:
            goods_href = goods_info.find('a').get('href')
            url2 = base_url + goods_href
            page2 = requests.get(url2, headers = header)
            source2 = BeautifulSoup(page2.content, 'html.parser', from_encoding = 'gb18030')
            goods_id = source2.find('p', class_ = 'number').string.replace('编号 ', '')
            try:
                goods_name = source2.find('p', class_ = 'title').string.replace('\n', '').replace('	', '')
            except Exception as e:
                goods_name = None
            try:
                color = source2.find('div', class_ = 'color clearfix').a.find('div', class_ = 'arrow').p.string
            except Exception as e:
                color = None
            try:
                price = source2.find('p', class_ = 'price').em.children
                sale_price = next(price).replace('￥','')
                origin_price = next(price).string.replace('￥','')
            except Exception as e:
                sale_price = source2.find('p', class_ = 'price').string.replace('\n', '').replace('	', '').replace('￥','')
                origin_price = source2.find('p', class_ = 'price').string.replace('\n', '').replace('	', '').replace('￥','')
            try:
                design = source2.find(attrs = {'id':'detailContent1'}).find_all('li')[0].p.string
            except Exception as e:
                design = None
            try:
                material = source2.find(attrs = {'id':'detailContent1'}).find_all('li')[1].p.string.replace('面料:','')
            except Exception as e:
                material = None
            try:
                stereotype = source2.find(attrs = {'id':'detailContent2'}).find_all('li')[0].p.string
            except Exception as e:
                stereotype = None
            try:
                length = source2.find(attrs = {'id':'detailContent2'}).find_all('li')[1].p.string
            except Exception as e:
                length = None
            ## 把结果写入到 csv 文件中
            csv_writer.writerow([category,goods_id,goods_name,color,sale_price,origin_price,
                                 design,material,stereotype,length,page_num+1])
            
            ## 由于图片比较耗资源，暂时不爬取图片
            '''
            ## 爬取主图片
            main_src = source2.find('ul', class_ = 'lineone').find('div', class_ = 'big_img').find('img').get('data-src')
            img = requests.get(main_src, timeout = 3)
            img_name = 'ochirly_goods_image/' + goods_id + '.jpg'
            fp = open(img_name, 'wb')
            fp.write(img.content)
            fp.close()
            time.sleep(2)
            ## 爬取展示图片
            show_src1 = source2.find('ul', class_ = 'linetwo clearfix').find_all('li')[0].find('img').get('data-src')
            img = requests.get(show_src1, timeout = 3)
            img_name = 'ochirly_goods_image/' + goods_id + '-show1' + '.jpg'
            fp = open(img_name, 'wb')
            fp.write(img.content)
            fp.close()
            time.sleep(2)
            show_src2 = source2.find('ul', class_ = 'linetwo clearfix').find_all('li')[1].find('img').get('data-src')
            img = requests.get(show_src2, timeout = 3)
            img_name = 'ochirly_goods_image/' + goods_id + '-show2' + '.jpg'
            fp = open(img_name, 'wb')
            fp.write(img.content)
            fp.close()
            time.sleep(2)
            show_src3 = source2.find('ul', class_ = 'linetwo clearfix').find_all('li')[2].find('img').get('data-src')
            img = requests.get(show_src3, timeout = 3)
            img_name = 'ochirly_goods_image/' + goods_id + '-show3' + '.jpg'
            fp = open(img_name, 'wb')
            fp.write(img.content)
            fp.close()
            time.sleep(2)
            show_src4 = source2.find('ul', class_ = 'linetwo clearfix').find_all('li')[3].find('img').get('data-src')
            img = requests.get(show_src4, timeout = 3)
            img_name = 'ochirly_goods_image/' + goods_id + '-show4' + '.jpg'
            fp = open(img_name, 'wb')
            fp.write(img.content)
            fp.close()
            time.sleep(2)
            ## 爬取细节图片
            detail_src1 = source2.find('ul', class_ = 'linethree clearfix').find_all('li')[0].find('img').get('data-src')
            img = requests.get(detail_src1, timeout = 3)
            img_name = 'ochirly_goods_image/' + goods_id + '-detail1' + '.jpg'
            fp = open(img_name, 'wb')
            fp.write(img.content)
            fp.close()
            time.sleep(2)
            detail_src2 = source2.find('ul', class_ = 'linethree clearfix').find_all('li')[1].find('img').get('data-src')
            img = requests.get(detail_src2, timeout = 3)
            img_name = 'ochirly_goods_image/' + goods_id + '-detail2' + '.jpg'
            fp = open(img_name, 'wb')
            fp.write(img.content)
            fp.close()
            time.sleep(2)
            detail_src3 = source2.find('ul', class_ = 'linethree clearfix').find_all('li')[2].find('img').get('data-src')
            img = requests.get(detail_src3, timeout = 3)
            img_name = 'ochirly_goods_image/' + goods_id + '-detail3' + '.jpg'
            fp = open(img_name, 'wb')
            fp.write(img.content)
            fp.close()
            time.sleep(2)
            '''
        # 显示进度
        print(category, '第', page_num+1, '页')
        print('------------')
        # 每爬取一页，休息一下
        time.sleep(30)
# 每爬取一个品类，休息一下
time.sleep(300)
# 关闭 csv_file
csv_file.close()

print('服装爬取完成！')
fz_end_time = datetime.datetime.fromtimestamp(time.time())
fz_end_time2 = datetime.datetime.strftime(fz_end_time, '%H:%M:%S')
print('完成时间： ' + fz_end_time2)
fz_use_time = fz_end_time - fz_start_time
print('用时： ' + str(fz_use_time.seconds) + ' 秒')
print('=========================')
