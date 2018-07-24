"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domainName("http://github.com/carbonfive/raygun") == "github" 
domainName("http://www.zombie-bites.com") == "zombie-bites"
domainName("https://www.cnet.com") == "cnet"
"""

def domain_name(url):
    dot_index = []
    for count,char in enumerate(url):
        if char == "w":
            if char == ".":
                dot_index.append(count)
        else:
            if char == "/":
                dot_index.append(count)
                if char == ".":
                    dot_index.append(count)
    print(dot_index)
    # final_string = url[12:16]
    # return final_string

domain_name("http://github.com/carbonfive/raygun")

