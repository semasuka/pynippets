"""
The marketing team is spending way too much time typing in hashtags.
Let's help them with out own Hashtag Generator!

Here's the deal:

It must start with a hashtag (#).
All words must have their first letter capitalized.
If the final result is longer than 140 chars it must return false.
If the input or the result is an empty string it must return false.
Examples
" Hello there thanks for trying my Kata"  =>  "#HelloThereThanksForTryingMyKata"
"    Hello     World   "                  =>  "#HelloWorld"
""                                        =>  false
"""
def generate_hashtag(the_string):
    if len(the_string) == 0:
        return False
    the_string_list = []
    for word in the_string.split(" "):
        the_string_list.append(word.capitalize())
    #print(the_string_list)
    hashtag_string = "#"
    for word in the_string_list:
        hashtag_string += word
    #print(hashtaged_string)
    if len(hashtag_string) > 140:
        return False
    else:
        return hashtag_string

print(generate_hashtag('Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat'))