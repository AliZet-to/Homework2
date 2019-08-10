# Data input
side_AB_len = float(input("Please input AB side length \n"))
side_BC_len = float(input("Please input BC side length \n"))
side_AC_len = float(input("Please input AC side length \n"))

# Verification for a triangle existence
if (side_AB_len + side_BC_len) > side_AC_len and (side_BC_len + side_AC_len) > side_AB_len and (side_AB_len + side_AC_len) > side_BC_len:
    print("It is a triangle")
else:
    print("It is not a triangle")

#Calculation workflow
p = 0.5 * (side_AB_len + side_BC_len + side_AC_len)

#The first Height calculation, Hbc
Hbc = ((p * (p - side_BC_len) * (p - side_AC_len) * (p - side_AB_len))**0.5 * 2) / side_BC_len

#The second Height calculation, Hac
Hac = ((p * (p - side_BC_len) * (p - side_AC_len) * (p - side_AB_len))**0.5 * 2) / side_AC_len

#The first Height calculation, Hab
Hab = ((p * (p - side_BC_len) * (p - side_AC_len) * (p - side_AB_len))**0.5 * 2) / side_AB_len

print("Hbc = ", Hbc)
print("Hac = ", Hac)
print("Hab = ", Hab)

if (Hab >= Hbc) and (Hab >= Hac):
    print("The biggest height is Hab = ", Hab)
elif (Hbc >= Hab) and (Hbc >= Hac):
    print("The biggest height is Hbc = ", Hbc)
else:
    print("The biggest height is Hac = ", Hac)
