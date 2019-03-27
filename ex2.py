def sorting(string):
    words = string.split()
    result = sorted(words)
    return result
def main():
    print(sorting(input('Введите предложение')))
   
if __name__ == '__main__':
    main()
