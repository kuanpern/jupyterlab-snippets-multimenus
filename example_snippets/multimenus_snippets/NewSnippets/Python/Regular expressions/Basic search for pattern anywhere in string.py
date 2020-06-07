string = " abc def "
pattern = re.compile(r"[a-z]+")
result = re.search(pattern, string)
if result is not None:
    print("Substring '{0}' was found in the range {1}".format(result.group(), result.span()))