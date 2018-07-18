def solution(s):
    splited_s_list = []
    splited_s = [str(s[i:i+2]) for i in range(0,len(s),2)]
    for duo in splited_s:
        try:
            duo[1]
        except IndexError:
            duo += "_"
        finally:
            splited_s_list.append(duo)
    return splited_s_list




solution("asdfadsfjkeyh")