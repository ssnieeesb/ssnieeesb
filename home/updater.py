import requests
import os



def changer(file):
    return
    base_url = "https://powercloudieeesb.stdcdn.com/ieeesb_public/home_templates/"
    if(requests.get(base_url+'check.html').content.decode('utf-8')!='404: Not Found'):
        template_folder='home/templates/'
        f=open(template_folder+file,"r+")
        s=""
        html_content=requests.get(base_url+file)
        f.write(html_content.content.decode("utf-8"))
        f.close()
