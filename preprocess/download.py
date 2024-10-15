import requests
from bs4 import BeautifulSoup

# 目标网页的 URL 模板
url_template = 'https://m.37novel.com/lightnovel/421/{}.html'

# 要爬取的页面范围
start_page = 143229
end_page = 143234

# 循环遍历每个页面
for page_num in range(start_page, end_page + 1):
    url = url_template.format(page_num)
    
    # 发送请求获取网页内容
    response = requests.get(url)
    
    # 检查请求是否成功
    if response.status_code == 200:
        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # 提取页面中的所有文字
        page_text = soup.get_text()
        
        # 将爬取的内容写入文件，每个页面保存为一个独立的文件
        filename = f'content_{page_num}.txt'
        with open(filename, 'w', encoding='utf-8') as file:
            file.write(page_text)
        
        print(f"页面 {page_num} 的内容已保存到 {filename} 文件中")
    else:
        print(f"无法访问页面 {page_num}，状态码: {response.status_code}")
