lp=input()
op=""
if lp[0].isalpha():
    if len(lp)!=6 or (not lp[:3].isalpha() and not lp[3:].isnumeric()):
        op="not valid"
    else:
        op="a valid older style plate."
else:
    if len(lp)!=7 or (not lp[:4].isnumeric() and not lp[4:].isalpha()):
        op="not valid"
    else:
        op="a valid newer style plate."

print("The plate is",op)

# Or you may use ord()