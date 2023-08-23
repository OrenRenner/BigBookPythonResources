import sys

from bagels import bagels
from birthdayparadox import birthdayparadox
from bitmapmessage import bitmapmessage


if __name__ == "__main__":
    if len(sys.argv[1:]) != 1:
        raise ValueError("You set not only one argument!")

    running_module = sys.argv[1:][0]
    if running_module == "bagels":
        bagels.main()
    elif running_module == "birthdayparadox":
        birthdayparadox.main()
    elif running_module == "bitmapmessage":
        bitmapmessage.main()
    else:
        raise ValueError("We have no this type of program!")
