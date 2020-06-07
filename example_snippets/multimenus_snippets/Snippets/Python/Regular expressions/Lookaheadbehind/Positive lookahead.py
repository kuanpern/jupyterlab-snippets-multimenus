string = "Isaac Asimov"
pattern = re.compile(r"Isaac(?= Asimov)")  # Only match "Isaac Asimov", but drop the " Asimov"
result = re.match(pattern, string)
if result is not None:
    print("Substring '{0}' was found in the range {1}".format(result.group(), result.span()))