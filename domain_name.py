"""
Write a function that when given a URL as a string, parses out just the domain name and returns it as a string. For example:

domainName("http://github.com/carbonfive/raygun") == "github" 
domainName("http://www.zombie-bites.com") == "zombie-bites"
domainName("https://www.cnet.com") == "cnet"
"""
def delimiter_index_func(url,has_www):
    indexes = []
    slash_count = 0
    #when there is wwww
    if has_www:
        for count,char in enumerate(url):
            if char == ".":
                indexes.append(count)
    #when there is no www
    else:
        for char in url:
            if char == "/":
                slash_count += 1
                if slash_count == 2:
                    indexes.append(url.index(char)+1)
                continue
            elif char == ".":
                indexes.append(url.index(char))


    return indexes
def domain_name(url):
    has_www = False
    slash_count = 0
    delimiter_index = []
    for char in url:
        if char == "/":
            slash_count += 1
            if slash_count == 2:
                #if www is present is the string
                if url[url.index(char)+2] == "w":
                    has_www = True
                    delimiter_index = delimiter_index_func(url,has_www)
                #if www aint there
                else:
                    delimiter_index = delimiter_index_func(url,has_www)
                    pass

    final_string = url[delimiter_index[0]+1:delimiter_index[1]]
    return final_string




print(domain_name("https://www.cnet.com"))
#delimiter_index_func("https://cnet.com",False)
