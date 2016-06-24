from display import Display
from string_display_impl import StringDisplayImpl
from string_text_display_impl import StringTextDisplayImpl
from count_display import CountDisplay
from random_display import RandomDisplay
from string_text_display_impl2 import StringTextDisplayImpl2

def main():
	d1 = Display(StringDisplayImpl("Hello, Japan!!"))
	d2 = CountDisplay(StringDisplayImpl("Hello, World!!"))
	d3 = CountDisplay(StringDisplayImpl("Hello, Universe!!"))
	d4 = RandomDisplay(StringDisplayImpl("Hello, Random!!"))
	d5 = Display(StringTextDisplayImpl("data.txt"))
	d6 = Display(StringTextDisplayImpl2("data3.txt"))
	d1.display()
	d2.display()
	d3.display()
	d3.multiDisplay(5)
	d4.randomMultiDisplay()
	d5.display()
	d6.display()

if __name__ == '__main__':
	main()