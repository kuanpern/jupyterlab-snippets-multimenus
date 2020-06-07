string = "John Doe lives at 221B Baker Street."
pattern = re.compile(r"""
    ([a-zA-Z ]+)      # Save as many letters and spaces as possible to group 1
    \ lives\ at\      # Match " lives at "
    (?P<address>.*)   # Save everything in between as a group named `address`
    \.                # Match the period at the end
""", re.VERBOSE)
new_string = re.sub(pattern, r"\g<address> is occupied by \1.", string)
print("New string is '{0}'".format(new_string))