from src.Nodes import Nodes


def main():
    test = ((1, 2), (1, 3), (3, 4))
    n = Nodes(test)
    n.getConnections()
    return 0


if __name__ == "__main__":
    main()
