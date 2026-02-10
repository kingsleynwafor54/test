
def display_hello():
    return "Hello World"

def test_display_hello():
    assert display_hello() == "Hello World"


if __name__=="__main__":
    print(display_hello())
    
