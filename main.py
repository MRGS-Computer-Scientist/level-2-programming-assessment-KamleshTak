from tkinter import*

w_width = 700
w_height = 500

bg_color = ""

window = Tk()
window.geometry(str(w_width) + "x" + str(w_height))
window.title("App")

top_frame = Frame(background='grey', width=w_width, height=100)
top_frame.pack()

main_frame = Frame(background='grey', width= 700, height=400)
main_frame.pack()

home_button = Button(button_frame, text="Home", height=5, width=5 )

window.mainloop()
# Adding widgets to the root window 
