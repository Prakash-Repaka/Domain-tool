import whois

def whois_lookup(domain):
    w = whois.whois(domain)
    return (w)


def main():
    domain = input("Enter domain name: ")
    whois_info = whois_lookup(domain)
    print("WHOIS Information for", domain)
    print(whois_info)

if __name__ == "__main__":
    main()
