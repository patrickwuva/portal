from helpers.check_api import check_api

print(check_api())


def main():
    if not check_api():
        print("not signed in")

if __name__ == "__main__":
    main()
