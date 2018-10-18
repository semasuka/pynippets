"""
In this kata, you will make a function that converts between camelCase, snake_case, and kebab-case.

You must write a function that changes to a given case. It must be able to handle all three case types:

py> change_case("snakeCase", "snake")
"snake_case"
py> change_case("some-lisp-name", "camel")
"someLispName"
py> change_case("map_to_all", "kebab")
"map-to-all"
py> change_case("doHTMLRequest", "kebab")
"do-h-t-m-l-request"
py> change_case("invalid-inPut_bad", "kebab")
None
py> change_case("valid-input", "huh???")
None
py> change_case("", "camel")
""
Your function must deal with invalid input as shown, though it will only be passed strings. Furthermore, all valid identifiers will be lowercase except when necessary, in other words on word boundaries in camelCase.
"""
def change_case(identifier, targetCase):
    final_string = ""
    if identifier == "":
        return ""
    if targetCase == "snake":
        if "_" in identifier:
            return identifier

        isUpper = False
        heifChar = False
        for the_char in identifier:

            if the_char.isupper():
                isUpper =True
        for the_char in identifier:
            if the_char == "-":
                heifChar =True
        if isUpper and heifChar:
            return None
        else:
            for char in identifier:
                if char.isupper(): #for camel case
                    final_string += "_"+char.lower()
                elif char == "-": #for kebab case
                    final_string += "_"
                else:
                    final_string+=char
            return final_string

    elif targetCase == "kebab":
        if "-" in identifier:
            return identifier
        isUpper = False
        downChar = False
        for the_char in identifier:

            if the_char.isupper():
                isUpper =True
        for the_char in identifier:
            if the_char == "_":
                downChar =True
        if isUpper and downChar:
            return None
        else:
            for char in identifier:
                if char.isupper(): #for camel case
                    final_string += "-"+char.lower()
                elif char == "_": #for snake case
                    final_string += "-"
                else:
                    final_string+=char
            return final_string

    elif targetCase == "camel":
        for the_char in identifier:
            if the_char.isupper():
                return identifier
        heifChar = False
        downChar = False
        for the_char in identifier:

            if the_char == "-":
                heifChar =True
        for the_char in identifier:
            if the_char == "_":
                downChar =True
        if heifChar and downChar:
            return None
        else:
            if "-" in identifier:
                for word in identifier.split("-"):
                    final_string += word.title()
                final_string = final_string[0].lower() + final_string[1:]
                return final_string

            elif "_" in identifier:
                for word in identifier.split("_"):
                    final_string += word.title()
                final_string = final_string[0].lower() + final_string[1:]
                return final_string
    else:
        return None

print(change_case("littleShopOfHorrors", "camel"))
