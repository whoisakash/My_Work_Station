from github import Github

# using an access tokan
g= Github("access_token")

# github Enterprise with custom hostname
g= Github(base_url= "https://github.com/appi/v3",)