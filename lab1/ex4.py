month=input()
days=""
if month=="February":
    days="28 or 29 days"
elif month in ("January","March","May","July","August","October","December"):
    days="31 days"
else:
    days="30 days"
print(month,"has",days,"in it.")