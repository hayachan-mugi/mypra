def easy_unpack(elements: tuple) -> tuple:
    x=elements[0]
    y=elements[2]
    z=elements[-2]
    return x,y,z

if __name__ == "__main__":
    print("Example:")
    print(easy_unpack((1,2,3,4,5,6,7,9)))

    assert easy_unpack((1,2,3,4,5,6,7,9)) == (1,3,7)