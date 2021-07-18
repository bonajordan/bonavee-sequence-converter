from tkinter import *
from tkinter.filedialog import *
from tkinter.scrolledtext import *
import time, threading, pyperclip
from tkinter.messagebox import *
from PIL import Image, ImageTk

#root = Label
#main = tkinter_root
#---------------------------------------------------------------
def main_tick(var, name):
    global check_buttons1

    for i in check_buttons1:
        if i != name:
            i.deselect()

                                                                        # THESE FUNCTIONS \
                                                                        #CONTROL THE SELECTION AND DESELECTION OF CHECKBUTTONS
def secondary_tick(var_, name_):
    global check_buttons2
    for j in check_buttons2:
        if j != name_:
            j.deselect()

#--------------------------------------------------------------
def instructions_pause():
    root.after(800, instructions)


def instructions():
    instructions_frame.grid()
    header_frame2.grid()
    header_frame.grid_remove()
    convert_button.grid_remove()
    frame1.grid_remove()
    frame2.grid_remove()
    frame2a.grid_remove()
    frame3.grid_remove()
                                                                                                         # THESE CONTROL THE COMING UP AND CLEARING OF THE INSTRUCTIONS SCREEN
def Ok():
    root.after(800, process)
    
def process():
    instructions_frame.grid_remove()
    header_frame2.grid_remove()
    header_frame.grid()
    frame1.grid()
    frame2.grid()
    frame2a.grid()
    frame3.grid()
    convert_button.grid()
    header.configure(text = 'Transcription and Reverse Transcription APP')
#------------------------------------------------------------------------------------------

# THESE ARE THE CONVERSION PROCESSES

# CB = CheckButton

# a is for DNA to RNA CB
# a1 is for template strand CB
# a2 is for coding strand CB
# b is for RNA to cDNA CB

def convert_pause():
        root.after(1000, convert)

def convert():
        global dna_dict
        global dna_to_rna_dict
        global rna_to_cdna_dict
        a = var1.get()
        a1 = var1a.get()
        a2 = var1b.get()
        b = var2.get()
        DNA_characters = ['a', 'c', 't', 'g']
        RNA_characters = ['a', 'u', 'c', 'g']



# IF DNA TO RNA IS TICKED AND THE SEQUENCE IS A TEMPLATE STRAND
# Checks the sequence
# Converts to the desired format
        if a == 1 and a1 == 1:
                temp1 = []
                new_sequence1 = []
                sequence_to_be_converted1 = input_.get(1.0, END)
                sequence_to_be_converted1 = sequence_to_be_converted1.lower()

                try:
                        if sequence_to_be_converted1 == '' or sequence_to_be_converted1 == '\n':
                                header.configure(text = 'You\'ve not entered a sequence')

                        if sequence_to_be_converted1 != '' and sequence_to_be_converted1 != '\n':
                                unknown1 = []
                                known1 = []
                                for character in sequence_to_be_converted1:
                                        if character not in DNA_characters and character != '\n':
                                                unknown1.append(character)
                                        if character in DNA_characters:
                                                known1.append(character)

                                num1 = len(unknown1)

                                if num1 > 0:
                                        unknown_characters = ','.join(unknown1)
                                        header.configure(text = 'Invalid character(s) encountered!\n'+unknown_characters+'\n'+ 'Check the sequence you entered')

                                if num1 == 0:
                                        for each in known1:
                                                if each in dna_to_rna_dict:
                                                        temp1.append(dna_to_rna_dict[each])

                                        new1 = ''.join(temp1).upper()
                                        result.delete(1.0, END)
                                        result.insert(END, new1)
                                        root.after(2500, done)
                except Exception as err:
                        print(err)

                                #print(temp1)




# IF DNA TO RNA IS TICKED AND THE SEQUENCE IS A CODING STRAND
        if a == 1 and a2 == 1:
                temp2 = []
                sequence_to_be_converted2 = input_.get(1.0, END)
                sequence_to_be_converted2 = sequence_to_be_converted2.lower()

                try:
                        if sequence_to_be_converted2 == '' or sequence_to_be_converted2 == '\n':
                                header.configure(text = 'You\'ve not entered a sequence')

                        if sequence_to_be_converted2 != '' and sequence_to_be_converted2 != '\n':
                                unknown2 = []
                                known2 = []
                                for character in sequence_to_be_converted2:
                                        if character not in DNA_characters and character != '\n':
                                                unknown2.append(character)
                                        if character in DNA_characters:
                                                known2.append(character)

                                num2 = len(unknown2)

                                if num2 > 0:
                                        unknown_characters = ','.join(unknown1)
                                        header.configure(text = 'Invalid character(s) encountered!\n'+unknown_characters+'\n'+ 'Check the sequence you entered')

                                if num2 == 0:
                                        for each_of in known2:
                                                temp2.append(dna_dict[each_of])
                                        print(temp2)
                                        bona = [] # Holds the characters(formally coding strands but already converted to template strands above )
                                                        # For onward conversion to RNA

                                        for content in temp2:
                                                bona.append(dna_to_rna_dict[content])
                                        new2 = ''.join(bona)
                                        result.delete(1.0, END)
                                        result.insert(END, new2)
                                        root.after(2500, done)
                except Exception as err:
                        print(err)


        if a == 0 and a1 == 0 and a2 == 0 and b == 0:
                header.configure(text = 'You have\'t ticked a command!')

        if a == 1 and a1 == 0 and a2 == 0 and b == 0:
                header.configure(text = 'Indicate if the sequence is;' + '\n a coding strand or a template strand')

        if b == 1:
                temp3 = []
                sequence_to_be_converted3 = input_.get(1.0, END)
                sequence_to_be_converted3 = sequence_to_be_converted3.lower()
                umeh = ''

                try:
                        if sequence_to_be_converted3 == '' or sequence_to_be_converted3 == '\n':
                                header.configure(text = 'You\'ve not entered a sequence')

                        if sequence_to_be_converted3 != '' and sequence_to_be_converted3 != '\n':
                                unknown3 = []
                                known3 = []
                                for character in sequence_to_be_converted3:
                                        if character not in RNA_characters and character != '\n':
                                                unknown3.append(character)
                                        if character in RNA_characters:
                                                known3.append(character)

                                num3 = len(unknown3)

                                if num3 > 0:
                                        unknown_characters = ','.join(unknown3)
                                        header.configure(text = 'Invalid character(s) encountered!\n'+unknown_characters+'\n'+ 'Check the sequence you entered')

                                if num3 == 0:
                                        for each_of in known3:
                                                temp3.append(rna_to_cdna_dict[each_of])

                                        umeh = ''.join(temp3).upper()  # Holds the new RNA sequence
                                        result.delete(1.0, END)
                                        result.insert(END, umeh)
                                        root.after(3000, done)
                except Exception as err:
                        print(err)




#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
def done():
        header.configure(text = 'Done!')
        root.after(3000, reset_message)

def reset_message():
        header.configure(text = 'Transcription and Reverse Transcription APP')


def developer_info():
        showinfo(title = 'Dev. Info.', message = 'App developed by\nBonaventure Umeh')

#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

main = Tk()
BONA = Menu()
main.configure(menu = BONA, width = 492, height = 520)
main.grid_propagate(0)
main.title('BIO INFORMATICS')



#picture = ImageTk.PhotoImage(Image.open('BonaveeUni.png'))



banner = ImageTk.PhotoImage(Image.open('background.png'))

root = Label(main, image = banner, width = 492, height = 520, state = 'normal', cursor = 'hand2')
root.grid(row = 0, column = 0)
root.grid_propagate(0)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
file_menu = Menu(tearoff = 0)
file_menu.add_command(label = 'Open')
#file_menu.add_command(label = 'Save')
#file_menu.add_command(label = 'Save As')

edit_menu = Menu(tearoff = 0)
edit_menu.add_command(label = 'Font')
#edit_menu.add_command(label = 'App settings')

info_menu = Menu(tearoff = 0)
#info_menu.add_command(label = 'Source code')
info_menu.add_command(label = 'Developer', command = developer_info)

help_menu = Menu(tearoff = 0)
help_menu.add_command(label = 'Instructions', command = instructions_pause)
#help_menu.add_command(label = 'Contact Developer')


BONA.add_cascade(label = 'File', menu = file_menu)
BONA.add_separator()
BONA.add_cascade(label = 'Edit', menu = edit_menu)
BONA.add_separator()
BONA.add_cascade(label = 'Info', menu = info_menu)
BONA.add_separator()
BONA.add_cascade(label = 'Help', menu = help_menu)



#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
header_frame = Frame(root, width = 470, height = 99, relief = 'sunken', borderwidth = 2)
header_frame.grid(row = 0, column = 0, sticky = 'we', padx = 10, pady = 10)
header_frame.grid_propagate(0)

header = Label(header_frame, text = 'Transcription and Reverse Transcription APP',\
               bg = 'black', fg = 'white', width = 40, height = 5,\
             relief = 'raised', font = ('papyrus 12 bold' ))
header.grid(row = 0, column = 0, sticky = 'we')
header.grid_propagate(0)
#----------------------------------------------------------------------------

frame1 = Frame(root, relief = 'solid', width = 491, height = 99)
frame1.grid(row = 1, column = 0, sticky = 'w', pady = 8)
frame1.grid_propagate(0)

message = Label(frame1, text = 'Result >>', font = ('Verdana 10 bold'),\
                bg = 'sienna', fg = 'white', relief = 'flat')
message.grid(row = 0, column = 0, sticky = 'nsw')

result = ScrolledText(frame1, bg = 'linen', fg = 'black', width = 44, height = 5,\
                      font = 'iskoola 12 bold', relief = 'solid')
result.grid(row = 0, column = 1, sticky = 'nse')
result.grid_propagate(0)


#-------------------------------------------------------------------------------

var1 = IntVar()
var1a = IntVar()
var1b = IntVar()
var2 = IntVar()


frame2 = Frame(root, relief = 'groove', bg = 'teal')
frame2.grid(row = 2, column = 0, sticky = 'w', pady = 8)


D_to_R = Checkbutton(frame2, bg = 'teal', text = 'DNA to RNA', font=('normal 12 bold'),\
                     variable = var1, command = lambda : main_tick(var1, D_to_R))
D_to_R.grid(row = 0, column = 0, sticky = 'w')

R_to_D = Checkbutton(frame2, bg = 'teal', text = 'RNA to cDNA',\
                     font=('normal 12 bold '), variable = var2, command = lambda : main_tick(var2, R_to_D))
R_to_D.grid(row = 1, column = 0)
#---------------------------------------------------------------------------------
frame2a = Frame(root, relief = 'groove', bg = 'teal')
frame2a.grid(row = 2, column = 0, pady = 8, sticky = 'e')


template_strand = Checkbutton(frame2a, bg = 'teal', text = 'Template Strand',\
                              font=('normal 10 bold'), variable = var1a,\
                              command = lambda : secondary_tick(var1a, template_strand))
template_strand.grid(row = 1, column = 0, sticky = 'w')

coding_strand = Checkbutton(frame2a, bg = 'teal', text = 'Coding Strand', font=('normal 10 bold'),\
                            variable = var1b, command = lambda : secondary_tick(var1b, coding_strand))
coding_strand.grid(row = 2, column = 0, sticky = 'w')

check_buttons1 = [D_to_R, R_to_D]
check_buttons2 = [template_strand, coding_strand]

#------------------------------------------------------------------------------------------------------

frame3 = Frame(root, bg = 'peru')
frame3.grid(row = 3, column = 0, sticky = 'nwe', pady = 15)



message2 = Label(frame3, text = 'Enter\nSequence >>', font = ('Verdana 10 bold'),\
                bg = 'royalblue', fg = 'white', relief = 'flat')
message2.grid(row = 0, column = 0, sticky = 'nsw')

input_ = ScrolledText(frame3, bg = 'linen', fg = 'black', width = 36, height = 5, cursor = 'tcross',\
                      font = ('papyrus 12 bold'), relief = 'solid', border = 4)
print(dir(ScrolledText))
input_.grid(row = 0, column = 1, sticky = 'ne')
input_.grid_propagate(0)

#----------------------------------------------------------------------------------
convert_button = Button(root, text = 'Convert', font = ('segoe 15'), bg = 'steelblue', command = convert_pause)
convert_button.grid(row = 4, column = 0, sticky = 'n')

#--------------------------------------------------------------------------------
header_frame2 = Frame(root, width = 470, height = 99, relief = 'raised', borderwidth = 2)
header_frame2.grid(row = 0, column = 0, sticky = 'nw', padx = 10, pady = 10)
header_frame2.grid_propagate(0)

header2 = Label(header_frame2, text = 'INSTRUCTIONS',\
               bg = 'black', fg = 'white', width = 40, height = 5,\
             relief = 'sunken', font = ('papyrus 12 bold' ))
header2.grid(row = 0, column = 0, sticky = 'nswe')
header2.grid_propagate(0)


instructions_frame = Frame(root, bg = 'darkslategray', width = 500, height = 300)
instructions_frame.grid(row = 1, column = 0, pady = 5)
instructions_frame.grid_propagate(0)

instructions_message = Label(instructions_frame, bg = 'darkslategray', fg = 'white',  text = '(1) Input a sequence \n\n(2)Tick the conversion you want done'+\
                                    '\n\n(3) If the sequence is a DNA sequence, tick to indicate if it is \n      the coding strand or the template strand',\
                                    font = ('Calibri 13'), anchor = 'n', justify = 'left', height = 12,\
                                     relief = 'flat')
instructions_message.grid(row = 0, column = 0, sticky = 'nwe', pady = 10)

ok_button = Button(instructions_frame, text = 'Ok', font = ('sans 14'), command = Ok)
ok_button.grid(row = 0, column = 0, sticky = 's')
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>




# GLOBAL VARIABLES THAT  WILL STORE VALUES

new_sequence = []

dna_dict = {'a':'t', 'c':'g', 't':'a', 'g':'c'}

dna_to_rna_dict = {'a':'u', 't':'a', 'c':'g', 'g':'c'}

rna_to_cdna_dict = {'a':'t', 'u':'a', 'c':'g', 'g':'c'}

header_frame2.grid_remove()
instructions_frame.grid_remove()
mainloop()
