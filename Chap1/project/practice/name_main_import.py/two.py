"""
[python - What does if __name__ == "__main__": do? - Stack Overflow](https://stackoverflow.com/questions/419163/what-does-if-name-main-do?rq=1)
"""
import one

one.f()

if __name__ == '__main__':
    print("This is script two running")
else:
    print("This is script one running")
