#poly.txt has coefficients a b c per line for ax^2 + bx + c.
# For x=2, read and write the polynomial value to poly_val.txt.
with open("poly.txt", "r") as infile, open("poly_val.txt", "w") as outfile:
    for lin in infile:
        a, b, c = map(float, lin.split())
        x=2
        poly_value = a*x**2+b*c+c
        outfile.write(f"{poly_value}\n")
        