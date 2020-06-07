string = "Janet Asimov"
pattern = re.compile(r"(?<!Isaac )Asimov")  # Will match any Asimov except Isaac, and only keep "Asimov"
result = re.search(pattern, string)
if result is not None:
    print("Substring '{0}' was found in the range {1}".format(result.group(), result.span()))