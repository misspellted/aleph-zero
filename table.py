
import sys

if len(sys.argv) == 2:
  places = 0

  try:
    places = int(sys.argv[1])
  except:
    places = 1 # Generate an example table on errant input.

  ncol = "Natural"
  rcol = "Real"

  nlen = max(len(ncol), places)
  rlen = max(len(rcol), places + 2) # For the '0.' prefix.
  clen = max(nlen, rlen) # Keep the column divider in the middle.

  table = list()
  table.append(f"{ncol.rjust(clen)}|{rcol.ljust(clen)}")
  table.append(f"{'-' * clen}+{'-' * clen}")

  for value in range(10 ** places):
    svalue = f"{value:0{places}d}"
    table.append(f"{svalue.rjust(clen)}|0.{svalue.ljust(clen)}")

  for row in table:
    print(f"{row}")

else:
  print("Usage:")
  print("  python table.py <places>")
  print()
  print("Example:")
  print("  python table.py 2")
  print()
  print("If the table is to be used elsewhere, save it to a file:")
  print("  python table.py <places> > <filename>")
  print()
  print("Example:")
  print("  python table.py 2 > two.txt")

