# import webbrowser
#
# # webbrowser.open_new_tab("moviesverse.org.in")
# # help(webbrowser)
# # webbrowser.register(name="google-chrome",klass="Chrome('google-chrome')")
# val = webbrowser.get(using="google-chrome")
# val.open("moviesverse.org.in")
# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
AB =int(input())
BC =int(input())
CM = math.sqrt((AB**2) + (BC**2))/2
MB = math.sqrt(BC**2 - CM**2)
MBC =math.degrees(math.atan(abs(CM/MB)))
print(round(MBC),chr(176),sep="")
