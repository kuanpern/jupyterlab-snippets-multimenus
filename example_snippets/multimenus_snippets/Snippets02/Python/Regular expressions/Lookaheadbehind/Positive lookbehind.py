string = "Janet Asimov"
pattern = re.compile(r"(?<=Janet )Asimov")  # Only match "Janet Asimov", but drop the "Janet "
result = re.search(pattern, string)
if result is not None:
    print("Substring '{0}' was found in the range {1}".format(result.group(), result.span()))