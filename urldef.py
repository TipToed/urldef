import os
import urllib.request
import webbrowser
import socket

try:
    from termcolor import colored
    import requests
    from bs4 import BeautifulSoup
except:
    try:
        os.system("pip3 install termcolor")
        os.system("pip3 install requests")
        os.system("pip3 install beautifulsoup4")
        from termcolor import colored
        import requests
    except:
        os.system("pip install termcolor")
        os.system("pip install requests")
        os.system("pip install beautifulsoup4")
        from termcolor import colored
        import requests

#needed_toplevels = 
while True:
    URL = input(colored("Enter Url: ", 'blue'))
    if "http" in URL:
        print(colored('[+]Starting url defenition reader....', 'blue'))
        if "https://" in URL:
            print(colored('[+]Https url, ssl availaible, site is secure', 'green'))
            Security = "https"
            Remove_Extra = URL.replace('https://','')
            if '/' in Remove_Extra:
                Pos = Remove_Extra.find('/')
                Page = Remove_Extra[Pos+1::]
                Domain_unsplit = Remove_Extra.replace('/'+str(Page), '')
                Domain_split = Domain_unsplit.split('.')
                TopLevelDomain = str(Domain_split[-1])
                Full_Domain = Domain_unsplit.replace("."+TopLevelDomain,'')
                
            else:
                Page = None
                Domain_unsplit = Remove_Extra.split('.')
                TopLevelDomain = str(Domain_unsplit[-1])
                Full_Domain = Remove_Extra.replace("."+str(TopLevelDomain),'')
        elif "http://" in URL:
            print(colored('[+]Http url, no ssl availaible, site is not secure', 'red'))
            Security = "http"
            Remove_Extra = URL.replace('http://','')
            if '/' in Remove_Extra:
                Pos = Remove_Extra.find('/')
                Page = Remove_Extra[Pos+1::]
                Domain_unsplit = Remove_Extra.replace('/'+str(Page), '')
                Domain_split = Domain_unsplit.split('.')
                TopLevelDomain = str(Domain_split[-1])
                Full_Domain = Domain_unsplit.replace("."+TopLevelDomain,'')
                
            else:
                Page = None
                Domain_unsplit = Remove_Extra.split('.')
                TopLevelDomain = str(Domain_unsplit[-1])
                Full_Domain = Remove_Extra.replace("."+str(TopLevelDomain),'')
        else:
            print("please use http:// or https:// before url")

        print("")
        print(colored("[+]STARTING TO LOAD INFORATION ABOUT '"+URL+"'", 'blue'))
        print("")
        if Security == "https":
            print(colored("URL TYPE: ",'blue')+colored(Security,'green'))
            print(colored("URL DOMAIN: ",'blue')+colored(Full_Domain,'green'))
            print(colored("URL TOPLEVEL: ",'blue')+colored(TopLevelDomain,'green'))
            print(colored("URL ADDITIONAL PAGES: ",'blue')+colored(Page,'green'))
            
        elif Security == "http":
            print(colored("URL TYPE: ",'blue')+colored(Security,'red'))
            print(colored("URL DOMAIN: ",'blue')+colored(Full_Domain,'red'))
            print(colored("URL TOPLEVEL: ",'blue')+colored(TopLevelDomain,'red'))
            print(colored("URL ADDITIONAL PAGES: ",'blue')+colored(Page,'red'))

        print("")
        print(colored("[+]STARTING VALIDITY CHECKER '"+URL+"'", 'blue'))
        print("")
        try:
            response = requests.get(URL)
            print(colored("URL is valid and exists on the internet", 'green'))
            print("")
            RQSE = input(colored("[+]SAVE HTML OF WEB IN URL[y/n|Small Only](def N): ", 'blue'))
            if RQSE == 'y':
                urllib.request.urlretrieve(URL, Full_Domain+".html")
                print(colored("Saved!", 'green'))
            print("")
            OPN = input(colored("[+]OPEN URL[y/n|Small Only](def N): ", 'blue'))
            if OPN == 'y':
                print(colored("Opening url!", 'green'))
                webbrowser.open(URL)
            print("")
            print(colored("[+]STARTING LINK LOOK", 'blue'))
            print("")
            url = URL
            reqs = requests.get(url)
            soup = BeautifulSoup(reqs.text, 'html.parser')

            urls = []
            print(colored("In Url's Found Are:", 'green'))
            for link in soup.find_all('a'):
                try:
                    if "http" in link.get('href'):
                        print(colored(link.get('href'), 'green'))
                        print("")
                except:
                    print(colored("Error!", 'red'))
                    print("")
                else:
                    pass
            r = requests.get(URL)
            print(colored("[+]TRYING ADVANCED SEARCH", 'blue'))
            try:
                IP_addres = socket.gethostbyname(Remove_Extra)
                url = f'http://ipinfo.io/{IP_addres}/json'
                response = requests.get(url).json()
                data = response

                IP=data['ip']
                org=data['org']
                city = data['city']
                country=data['country']
                region=data['region']

                print (colored('Your IP detail\n ', 'green'))
                print (colored('IP : {4} \nRegion : {1} \nCountry : {2} \nCity : {3} \nOrg : {0}'.format(org,region,country,city,IP), 'green'))
            except:
                print(colored("NO ADVANCED RESULTS FOUND",'red'))
                print("")
        except requests.ConnectionError as exception:
            print(colored("URL does not exist on Internet", 'red'))

    elif URL == "exit":
        break
    else:
        print(colored("INVALID URL FORMAT", "red"))
        print("")
    
    

    


            


