def main():
    s1 = input("Enter the first string: ").strip()
    s2 = input("Enter the Second string: ").strip()

    s3 = prefix(s1, s2)

    if s3 != None:
      print("The common prefix is " + s3)
    else:
      print("No common prefix");

def prefix(s1, s2):
    result = ""

    lentgh = min(len(s1),len(s2))
    for i in range(lentgh):
        if s1[i] == s2[i]:
            result += s1[i]
        else:
            break;

    if len(result) == 0:
        return None
    else:
        return result

main()
