import os
import json
from http.server import SimpleHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import requests
import json
from bs4 import BeautifulSoup


from bs4 import BeautifulSoup

def get_all(html_content):
    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # METHOD 1: Fulfilling the exact request (finding all specified tags)
    target_tags = ['span', 'tr', 'th', 'td']
    all_elements = soup.find_all(target_tags)

    literal_request_list = []
    for tag in all_elements:
        # Check if this specific tag contains an image
        img_tag = tag.find('img')
        
        # If an image exists, grab its src
        if img_tag and img_tag.has_attr('src'):
            literal_request_list.append(img_tag['src'])
        else:
            # get_text(strip=True) extracts text while removing empty spaces/newlines
            text = tag.get_text(separator=" ", strip=True)
            if text: # Only add if it's not empty
                literal_request_list.append(text)
    
    # METHOD 2: Getting text blocks without massive nesting duplication
    lstidx = [8, 11, 15, 20, 24, 29, 33, 38, 43, 47, 48, 50, 51, 52, 53, 54]
    data = ""

    # Using a try-except block here is highly recommended. 
    # Because you are using strict hardcoded indices (lstidx), if the HTML 
    # structure changes even slightly, it will throw an IndexError and crash.
    try:
        for i in lstidx:
            data += literal_request_list[i] + "|"
    except IndexError:
        return data + "| Error: HTML structure changed, index out of range."

    return data




def getawedak(html_content):
    # 1. Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 2. Find all table rows
    rows = soup.find_all('tr')
    
    # 3. Extract and clean headers from the first row
    headers = [td.get_text(strip=True) for td in rows[0].find_all('td')]
    
    table_data = []
    
    # 4. Iterate through the remaining rows
    for row in rows[1:]:
        cells = row.find_all('td')
        
        # Skip empty rows (handles nested <tr> tags safely)
        if not cells:
            continue
            
        row_values = []
        for cell in cells:
            # Check if the cell contains an image tag
            img_tag = cell.find('img')
            
            if img_tag and img_tag.has_attr('src'):
                # If an image exists, append its src URL
                row_values.append(img_tag['src'])
            else:
                # Otherwise, just extract the text
                row_values.append(cell.get_text(strip=True))
        
        # 5. Combine headers and values into a dictionary if the columns match
        if len(headers) == len(row_values):
            table_data.append(row_values)
    
    return "|".join(table_data[0])




def getdoc(appid, docid):
    headers = {
        "Host": "bor.up.gov.in",
        "Cookie": "SameSite=Strict; SameSite=Strict; ASP.NET_SessionId=; SameSite=Strict; UserLanguage=UserLanguage=en-US",
        "Priority": "u=0, i"
    }
    response = requests.get("https://bor.up.gov.in/KAS/user/View_Documnet.aspx?new_autonogenno= "+ appid +"&doc_type=" + docid , headers=headers, verify=False)
    
    # 1. Parse the HTML
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 2. Find the specific image tag by its ID
    img_tag = soup.find('img', id='Image1')
    
    # 3. Extract the 'src' attribute safely
    retdata = img_tag['src']
    if retdata == "" or retdata == "data:image/jpg;base64,":
        return "No Image"
    else:
        return retdata










def get_allwophoto(html_content):
    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # METHOD 1: Fulfilling the exact request (finding all specified tags)
    target_tags = ['span', 'tr', 'th', 'td']
    all_elements = soup.find_all(target_tags)

    literal_request_list = []
    for tag in all_elements:
        # get_text(strip=True) extracts text while removing empty spaces/newlines
        text = tag.get_text(separator=" ", strip=True)
        if text: # Only add if it's not empty
            literal_request_list.append(text)

    # METHOD 2: Getting text blocks without massive nesting duplication
    lstidx = [10, 14, 19, 23, 28, 32, 37, 42, 46, 49, 50, 52, 53]
    data = ""

    # Using a try-except block here is highly recommended. 
    # Because you are using strict hardcoded indices (lstidx), if the HTML 
    # structure changes even slightly, it will throw an IndexError and crash.
    try:
        for i in lstidx:
            data += literal_request_list[i] + "|"
    except IndexError:
        return data + "| Error: HTML structure changed, index out of range."

    return data






def getawedakwophoto(html_content):
    # 1. Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # 2. Find all table rows
    rows = soup.find_all('tr')
    
    # 3. Extract and clean headers from the first row
    headers = [td.get_text(strip=True) for td in rows[0].find_all('td')]
    
    table_data = []
    
    # 4. Iterate through the remaining rows
    for row in rows[1:]:
        cells = row.find_all('td')
        
        # Skip empty rows (handles nested <tr> tags safely)
        if not cells:
            continue
            
        row_values = []
        for cell in cells:
            row_values.append(cell.get_text(strip=True))
        
        # 5. Combine headers and values into a dictionary if the columns match
        if len(headers) == len(row_values):
            table_data.append(row_values)
    
    return "|".join(table_data[0])







def getawedanwophoto(appid):

    url = "https://bor.up.gov.in/KAS/Cm_Dashboard/Cm_Dashboard_Drill.aspx"
    
    headers = {
        "Host": "bor.up.gov.in",
        "Cookie": "SameSite=Strict; SameSite=Strict; ASP.NET_SessionId=; SameSite=Strict; UserLanguage=UserLanguage=en-US",
        "Cache-Control": "max-age=0",
        "Sec-Ch-Ua": '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Origin": "https://bor.up.gov.in",
        "Content-Type": "application/x-www-form-urlencoded",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://bor.up.gov.in/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Priority": "u=0, i",
        "Connection": "keep-alive"
    }
    
    # The raw URL-encoded payload string
    payload = "__VIEWSTATE=%2FwEPDwULLTEyNDE2NjU4NzhkZN1G3G1NnuUej1XzOY7snUWChrXMvHTp8srsq8kskOtE&__VIEWSTATEGENERATOR=86C7D1C7&__EVENTVALIDATION=%2FwEdAAiUJUetd%2BvcvpEMbmgb3D3ZBeqeFPuw0PrR%2BxpllDNUGDdHI9oCnLy0o%2FF%2F9YXgYI%2F5qUXIxLQpsyEcdKHXB0LZPGq%2FMax17u7OOj2ETaBU8P%2FlkIe8oyXU5T9KpgRNclqAc%2FIROxUpkw94FubtI4ym5oGioCk4YdnIT%2FMGU47Jxqvl8y7FylkhLeoUFSbKcQmqIHM3f6t8fx1lVjZwms%2Bs&hdn_Vill_cd=&txt_from=&txt_to=&btn_serch=Search&txt_app_no=" + appid
    
    
    # Send the POST request
    # Set allow_redirects=True if you want Python to automatically follow 301/302 redirects
    response = requests.post(url, headers=headers, data=payload, allow_redirects=False, verify=False)
    
    # Check if the server tried to redirect
    if response.is_redirect:
        x = response.headers.get('Location').find("&rc_no=")
        base64appid = response.headers.get('Location')[x+7:]
        # The full URL including the query parameters from the GET line
    url = "https://bor.up.gov.in/KAS/user/Print_Awedan.aspx?UID=" + base64appid
    
    # Dictionary containing all the request headers
    headers = {
        "Host": "bor.up.gov.in",
        "Cookie": "SameSite=Strict; SameSite=Strict; ASP.NET_SessionId=; SameSite=Strict; UserLanguage=UserLanguage=en-US",
        "Priority": "u=0, i"
    }
    
    response = requests.get(url, headers=headers, verify=False)

    start = (response.text).index("<table")
    end = (((response.text).index("lblprintdate"))+150)
    
    start2 = ((response.text)[(start + 8):end]).index("<table") + start + 8
    end2 = ((response.text)[:end]).index("<img id=\"imgSignw1")

    html_content = (response.text)[start:start2] + (response.text)[end2:end]
    respdata = get_allwophoto(html_content) + " |"

    html_content = (response.text)[start2:((response.text)[:end]).index("</table")+8]
    respdata += getawedakwophoto(html_content)
    
    return respdata






def getawedan(appid):

    url = "https://bor.up.gov.in/KAS/Cm_Dashboard/Cm_Dashboard_Drill.aspx"
    
    headers = {
        "Host": "bor.up.gov.in",
        "Cookie": "SameSite=Strict; SameSite=Strict; ASP.NET_SessionId=; SameSite=Strict; UserLanguage=UserLanguage=en-US",
        "Cache-Control": "max-age=0",
        "Sec-Ch-Ua": '"Chromium";v="146", "Not-A.Brand";v="24", "Google Chrome";v="146"',
        "Sec-Ch-Ua-Mobile": "?0",
        "Sec-Ch-Ua-Platform": '"Windows"',
        "Origin": "https://bor.up.gov.in",
        "Content-Type": "application/x-www-form-urlencoded",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/146.0.0.0 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "Sec-Fetch-Site": "same-origin",
        "Sec-Fetch-Mode": "navigate",
        "Sec-Fetch-User": "?1",
        "Sec-Fetch-Dest": "document",
        "Referer": "https://bor.up.gov.in/",
        "Accept-Encoding": "gzip, deflate, br",
        "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8",
        "Priority": "u=0, i",
        "Connection": "keep-alive"
    }
    
    # The raw URL-encoded payload string
    payload = "__VIEWSTATE=%2FwEPDwULLTEyNDE2NjU4NzhkZN1G3G1NnuUej1XzOY7snUWChrXMvHTp8srsq8kskOtE&__VIEWSTATEGENERATOR=86C7D1C7&__EVENTVALIDATION=%2FwEdAAiUJUetd%2BvcvpEMbmgb3D3ZBeqeFPuw0PrR%2BxpllDNUGDdHI9oCnLy0o%2FF%2F9YXgYI%2F5qUXIxLQpsyEcdKHXB0LZPGq%2FMax17u7OOj2ETaBU8P%2FlkIe8oyXU5T9KpgRNclqAc%2FIROxUpkw94FubtI4ym5oGioCk4YdnIT%2FMGU47Jxqvl8y7FylkhLeoUFSbKcQmqIHM3f6t8fx1lVjZwms%2Bs&hdn_Vill_cd=&txt_from=&txt_to=&btn_serch=Search&txt_app_no=" + appid
    
    
    # Send the POST request
    # Set allow_redirects=True if you want Python to automatically follow 301/302 redirects
    response = requests.post(url, headers=headers, data=payload, allow_redirects=False, verify=False)
    
    # Check if the server tried to redirect
    if response.is_redirect:
        x = response.headers.get('Location').find("&rc_no=")
        base64appid = response.headers.get('Location')[x+7:]
        # The full URL including the query parameters from the GET line
    url = "https://bor.up.gov.in/KAS/user/Print_Awedan.aspx?UID=" + base64appid
    
    # Dictionary containing all the request headers
    headers = {
        "Host": "bor.up.gov.in",
        "Cookie": "SameSite=Strict; SameSite=Strict; ASP.NET_SessionId=; SameSite=Strict; UserLanguage=UserLanguage=en-US",
        "Priority": "u=0, i"
    }
    
    response = requests.get(url, headers=headers, verify=False)

    start = (response.text).index("<table")
    end = (((response.text).index("lblprintdate"))+150)
    
    start2 = ((response.text)[(start + 8):end]).index("<table") + start + 8
    end2 = ((response.text)[:end]).index("<img id=\"imgSignw1")

    html_content = (response.text)[start:start2] + (response.text)[end2:end]
    respdata = get_all(html_content)
    
    respdata += getdoc(appid, "1") + "|"
    respdata += getdoc(appid, "2") + "|"
    respdata += getdoc(appid, "3") + "|"
    respdata += getdoc(appid, "4") + "|"
    respdata += getdoc(appid, "5") + "|"
    respdata += getdoc(appid, "6") + "|"
    respdata += getdoc(appid, "7") + "|"
    respdata += getdoc(appid, "8") + "| |"
    
    html_content = (response.text)[start2:((response.text)[:end]).index("</table")+8]
    respdata += getawedak(html_content)
    
    return respdata


class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()
        parsed_url = urlparse(self.path)
        
        if "appno" not in parsed_url.query:
            self.wfile.write(bytes("".encode('utf-8-sig')))
            return
        
        query_params = parse_qs(parsed_url.query)
        appno = query_params.get('appno')[0]
        photo = query_params.get('photo',"1")[0]

        if(photo) == "1":
            respdata = getawedan(appno)
        else:
            respdata = getawedanwophoto(appno)

        self.wfile.write(bytes(respdata.encode('utf-8-sig')))


if __name__ == "__main__":
    host = os.environ.get('HOST', '127.0.0.1')

    # Get the PORT environment variable if it's present; otherwise, default to 8000
    port = int(os.environ.get('PORT', 80))

    server = HTTPServer((host, port), CustomHandler)
    print(f"Starting server on http://{host}:{port}")
    server.serve_forever()
