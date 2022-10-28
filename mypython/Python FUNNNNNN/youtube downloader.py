import webbrowser
url= input("Enter the url:- ")
print(url)

download = url[:12] +"ss"+ url[12:]
webbrowser.open(download)