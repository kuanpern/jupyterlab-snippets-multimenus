string = " abc def "
pattern = re.compile(r"[a-z]+")
new_string = re.sub(pattern, "something", string)
print("New string is '{0}'".format(new_string))