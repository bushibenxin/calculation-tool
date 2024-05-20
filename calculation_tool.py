import tkinter as tk
import pickle
# import xgboost
import numpy as np
from PIL import ImageTk, Image


def custom_quantize(number, n_digits=0):
    """ 截断处理，不舍入 """
    number_lst = str(number).split(".")
    if n_digits > 0:
        if "." in str(number):
            new_number = number_lst[0] + "." + number_lst[1][:n_digits]
        else:
            new_number = number_lst[0] + "." + "0" * n_digits
    else:
        new_number = number_lst[0]
    return new_number

def calculation():
    input_data = []
    input_data.append(float(entry_in_frame1.get()))
    input_data.append(float(entry_in_frame2.get()))
    input_data.append(float(entry_in_frame3.get()))
    input_data.append(float(entry_in_frame4.get()))
    input_data.append(float(entry_in_frame5.get()))
    input_data.append(float(entry_in_frame6.get()))
    input_data.append(float(entry_in_frame7.get()))
    input_data.append(float(entry_in_frame8.get()))
    input_data.append(float(entry_in_frame9.get()))
    input_data.append(float(entry_in_frame10.get()))
    c = np.array([input_data])
    y_scores = loaded_model.predict_proba(c)
    result = custom_quantize(y_scores[0][1], 4)
    label_result.config(text=f"Prediction The Risk of colorectal cancer: {result}\n\n"
                             f"(Note: Calculation alone can never replace professional judgment\nbut only serves as a risk assessment to prompt clinicians \nto carry out follow-up diagnosis and treatment)", font=('mincho', 14))

with open('./xgboost_model.pkl', 'rb') as file:
    loaded_model = pickle.load(file)


color_use = "#708090"
# Create the main window
root = tk.Tk()
root.geometry("800x650")
root.title("Calculation Tool")
root.config(bg=color_use)

label = tk.Label(root, text="Calculation Tool For Early Colorectal Cancer Risk Prediction", font=('courier 10 pitch', 15, 'bold'), bg=color_use)
label.pack(pady=(10, 30))


# Create a frame
frame_a = tk.Frame(root, bg=color_use)
frame_a.pack(pady=10)
frame1 = tk.Frame(frame_a, bg=color_use)
frame2 = tk.Frame(frame_a, bg=color_use)

frame1.pack(side='left', padx=10)
frame2.pack(side='right', padx=10)

label_in_frame1 = tk.Label(frame1, text="  LYMPH%", font=('courier 10 pitch', 12), bg=color_use)
entry_in_frame1 = tk.Entry(frame1)

entry_in_frame1.pack(side='right')
label_in_frame1.pack(side='right')

label_in_frame2 = tk.Label(frame2, text="    TP g/L", font=('courier 10 pitch', 12), bg=color_use)
entry_in_frame2 = tk.Entry(frame2)

entry_in_frame2.pack(side='right')
label_in_frame2.pack(side='right')


frame_b = tk.Frame(root, bg=color_use)
frame_b.pack(pady=10)
frame3 = tk.Frame(frame_b, bg=color_use)
frame4 = tk.Frame(frame_b, bg=color_use)

frame3.pack(side='left', padx=10)
frame4.pack(side='right', padx=10)

label_in_frame3 = tk.Label(frame3, text="HGB g/L", font=('courier 10 pitch', 12), bg=color_use)
entry_in_frame3 = tk.Entry(frame3)

label_in_frame3.pack(side='left')
entry_in_frame3.pack(side='left')

label_in_frame4 = tk.Label(frame4, text="GLU mmol/L", font=('courier 10 pitch', 12), bg=color_use)
entry_in_frame4 = tk.Entry(frame4)

entry_in_frame4.pack(side='right')
label_in_frame4.pack(side='right')

frame_c = tk.Frame(root, bg=color_use)
frame_c.pack(pady=10)
frame5 = tk.Frame(frame_c, bg=color_use)
frame6 = tk.Frame(frame_c, bg=color_use)

frame5.pack(side='left', padx=10)
frame6.pack(side='right', padx=10)

label_in_frame5 = tk.Label(frame5, text="    HCT", font=('courier 10 pitch', 12), bg=color_use)
entry_in_frame5 = tk.Entry(frame5)

label_in_frame5.pack(side='left')
entry_in_frame5.pack(side='left')

label_in_frame6 = tk.Label(frame6, text=" CEA ng/ml", font=('courier 10 pitch', 12), bg=color_use)
entry_in_frame6 = tk.Entry(frame6)

entry_in_frame6.pack(side='right')
label_in_frame6.pack(side='right')

frame_d = tk.Frame(root, bg=color_use)
frame_d.pack(pady=10)
frame7 = tk.Frame(frame_d, bg=color_use)
frame8 = tk.Frame(frame_d, bg=color_use)

frame7.pack(side='left', padx=10)
frame8.pack(side='right', padx=10)

label_in_frame7 = tk.Label(frame7, text="  RDW %", font=('courier 10 pitch', 12), bg=color_use)
entry_in_frame7 = tk.Entry(frame7)

label_in_frame7.pack(side='left')
entry_in_frame7.pack(side='left')

label_in_frame8 = tk.Label(frame8, text="      FOBT", font=('courier 10 pitch', 12), bg=color_use)
entry_in_frame8 = tk.Entry(frame8)

entry_in_frame8.pack(side='right')
label_in_frame8.pack(side='right')

frame_e = tk.Frame(root, bg=color_use)

frame_e.pack(pady=10)
frame9 = tk.Frame(frame_e, bg=color_use)
frame10 = tk.Frame(frame_e, bg=color_use)

frame9.pack(side='left', padx=10)
frame10.pack(side='right', padx=10)

label_in_frame9 = tk.Label(frame9, text="  PDW l", font=('courier 10 pitch', 12), bg=color_use)
entry_in_frame9 = tk.Entry(frame9)

label_in_frame9.pack(side='left')
entry_in_frame9.pack(side='left')

label_in_frame10 = tk.Label(frame10, text=" μA μmol/L", font=('courier 10 pitch', 12), bg=color_use)
entry_in_frame10 = tk.Entry(frame10)

entry_in_frame10.pack(side='right')
label_in_frame10.pack(side='right')

button = tk.Button(root, text="Run", font=('courier 10 pitch', 16, 'bold'), command=calculation)
button.pack(pady=20)

label_result = tk.Label(root, text='', bg=color_use)
label_result.pack(pady=10)

photo = Image.open("bg_img.png")
photo = photo.resize((800, 170))
img_jpg = ImageTk.PhotoImage(photo)
label_img = tk.Label(root, image=img_jpg, bg=color_use)
label_img.pack(side='bottom', pady=0)

root.mainloop()
