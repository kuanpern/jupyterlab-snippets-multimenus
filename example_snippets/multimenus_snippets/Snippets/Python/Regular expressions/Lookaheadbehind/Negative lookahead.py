string = "Isaac Newton"
pattern = re.compile(r"Isaac(?! Asimov)")  # Match any Isaac except Asimov, and only keep the "Isaac"
result = re.match(pattern, string)
if result is not None:
    print("Substring '{0}' was found in the range {1}".format(result.group(), result.span()))