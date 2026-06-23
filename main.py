import easy
import medium
import difficult

def do_easy():
     #"easy" problems
    easy.one()
    easy.two()
    easy.three()
    easy.four()
    easy.five(10)
    easy.six(8)
    easy.seven('circumlocution')
    easy.eight(24)
    easy.nine()
    easy.ten('circumlocution')
    pass # do nothing

def do_medium():
    # "medium" problems
    medium.one([3, 8, 1, 10, 5])
    medium.two([3, 8, 1, 10, 5])
    medium.three("radar")
    medium.four(10)
    medium.five([3, 8, 1, 10, 5])
    medium.six(8)
    medium.seven(25)
    medium.eight()
    medium.nine("Python loops are useful")
    medium.ten([1, 2, 3, 4], [3, 4, 5, 6])
    pass # do nothing

def do_difficult():
    difficult.one(12)
    difficult.two(8)
    difficult.three("listen")
    difficult.four(10)
    difficult.five([3, 8, 1, 10, 5])
    difficult.six(6)
    difficult.seven(12345)
    difficult.eight("Python loops are very useful")
    difficult.nine("The quick brown fox jumps over the lazy dog")
    difficult.ten()
    pass # do nothing

def main():
    do_easy()
    do_medium()
    do_difficult()

main()
