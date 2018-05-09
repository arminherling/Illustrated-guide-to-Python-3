# Exercise: Go to https://unicode.org and find the symbol omega in the Greek character code
# chart. Create a string that holds the omega character, using both the Unicode code
# point (\u form) and Unicode name (\N form). The code point is the hex number in
# the chart, the name is the bolded capital name following the code point. For example,
# the theta character has the code point of 03f4 and a name of GREEK CAPITAL THETA
# SYMBOL.

omega_code = "\u03A9"
omega_name = "\N{GREEK CAPITAL LETTER OMEGA}"

print(omega_code, omega_name)