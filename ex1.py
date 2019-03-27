def middle(*argv):
    value = sum(argv)/len(argv)
    return value
def main():
    print(middle(5, 6))
    print(middle(1, 6, 3, 8, 5, 3, 5))
if __name__=='__main__':
    main()