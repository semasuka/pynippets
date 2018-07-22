"""
Complete the method so that it does the following:
Removes any duplicate query string parameters from the url
Removes any query string parameters specified within the 2nd argument (optional array)


Examples:

stripUrlParams('www.codewars.com?a=1&b=2&a=2') // returns 'www.codewars.com?a=1&b=2'
stripUrlParams('www.codewars.com?a=1&b=2&a=2', ['b']) // returns 'www.codewars.com?a=1'
stripUrlParams('www.codewars.com', ['b']) // returns 'www.codewars.com'

"""
from collections import OrderedDict
def strip_url_params(url, params_to_strip = []):
    has_question_mark = False
    final_url = []
    for char in url:
        if char == "?":
            has_question_mark = True
    if has_question_mark:
        url_divided = url.split("?")
        url_original_part = url_divided[0]
        url_code_part = url_divided[1]
        # print(url_divided)
        # print(url_part)
        # print(url_original)
        url_code_part = "".join(OrderedDict.fromkeys(url_code_part))
        if params_to_strip:
            for char in url_code_part:
                if char == params_to_strip[0]:
                    url_code_part = url_code_part.replace(char,"")
                    final_url = url_original_part+"?"+url_code_part
                    break
        else:
            final_url = url_original_part+"?"+url_code_part

        return final_url
    else:
        return url

strip_url_params('www.codewars.com?a=1&b=2&a=2')