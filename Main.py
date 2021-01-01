# Main

def main():
    solver = int(input(
        "\nPlease select what to do..\n1) Find roots of the quadratic equation\n2) Factorise the quadratic equation\n3) Factorise the quadratic equation (with steps)\n\nEnter 1 (or) 2 (or) 3\n"))
    if solver == 1:
        import Root_Finder
        Root_Finder.root_finder()
    if solver == 2:
        import Factoriser
        Factoriser.factor_finder()
    if solver == 3:
        import Factoriser
        Factoriser.factorize()


main()
