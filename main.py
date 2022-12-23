import tkinter as tk
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import tensorflow as tf
import numpy as np
import webbrowser
from tensorflow import keras
from winsound import *
from tensorflow.keras.utils import load_img, img_to_array

#Tải và thiết lập model đã train
new_model = tf.keras.models.load_model("F:\AI\AI.h5")


# Hàm def để tải ảnh
def load_img():
    global img, image_data
    for img_display in frame.winfo_children():
        img_display.destroy()

    image_data = filedialog.askopenfilename(initialdir="/",
                                            filetypes=(("all files", "*.*"), ("png files", "*.png")))
    basewidth = 400  # Processing image for displaying
    img = Image.open(image_data)
    wpercent = (basewidth / float(img.size[0]))
    hsize = int((float(img.size[1]) * float(wpercent)))
    img = img.resize((basewidth, hsize), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)

    panel_image = tk.Label(frame, image=img).pack()


# Def CLASS

def classify():
    original = Image.open(image_data)
    original = original.resize((150, 150), Image.ANTIALIAS)
    numpy_image = img_to_array(original)
    image_batch = np.expand_dims(numpy_image, axis=0)
    result = new_model.predict(image_batch)
    global prediction
    if round(result[0][0]) == 1:
        prediction = 'Sáo trúc'
    if round(result[0][1]) == 1:
        prediction = 'Đàn bầu'
    if round(result[0][2]) == 1:
        prediction = 'Đàn nguyệt'
    if round(result[0][3]) == 1:
        prediction = 'Đàn T rung'
    if round(result[0][4]) == 1:
        prediction = 'Đàn tranh'
    if round(result[0][5]) == 1:
        prediction = 'Đàn tỳ bà'
    if round(result[0][6]) == 1:
        prediction = 'Đàn đá'
    if round(result[0][7]) == 1:
        prediction = 'Đàn đáy'

    print("Đây là :", str(prediction).upper())

    d = {"Sáo trúc": "Sáo trúc là nhạc cụ dân tộc được làm bằng ống trúc, ống nứa, trên thân sáo được khoét lỗ để khi thổi tạo ra âm thanh, bấm nốt. áo trúc có âm thanh trầm bổng, du dương, là loại nhạc cụ dân tộc được khá nhiều người yêu thích và tìm cách học thổi. Sáo trúc xuất hiện nhiều trong văn thơ Việt Nam. Từ xưa đến nay đã gắn bó với đời sống tinh thần, văn hóa của người Việt.",
        "Đàn bầu": "Đàn bầu Việt Nam , còn gọi là độc huyền cầm , là loại đàn một dây của người Việt và dân tộc Kinh ở đảo Hải Nam – Trung Quốc , thanh âm phát ra nhờ sử dụng que hay miếng gảy vào dây. Dựa theo cấu tạo của hộp cộng hưởng, đàn bầu chia hai loại là đàn thân tre và đàn hộp gỗ, đàn bầu có mặt phổ biến ở các dàn nhạc cổ truyền dân tộc Việt Nam.",
        "Đàn nguyệt": "Đàn nguyệt còn được gọi là đàn song vận (đàn 2 dây), nguyệt cầm (cây đàn hình mặt trăng), đàn kìm (từ miền trung trở vào) là một trong những nhạc cụ đặc sắc của người Việt đã gắn bó với lịch sử dân tộc từ khá sớm, là nhạc cụ dây gẩy có hộp đàn hình tròn như mặt trăng nên gọi là đàn nguyệt.",
        "Đàn T rung": "T'rưng là loại nhạc cụ gõ phổ biến ở vùng Tây Nguyên, là một loại nhạc khí thô được chế tác từ những khúc gỗ bóc vỏ phơi khô hoặc những ống nứa vót một đầu, chặt theo những độ dài khác nhau để tạo nên những âm vực ưng ý đem treo lên một cái giá đủ trở thành một cây đàn gõ phím cho một hoặc hai người diễn tấu bằng cách cầm những dùi tre gõ vào phím này.",
        "Đàn tranh": "Đàn Tranh còn được gọi là đàn thập lục do đặc điểm có 16 dây hay đàn có trụ chắn, là nhạc cụ truyền thống của người phương Đông, có xuất xứ từ Trung Quốc. Đàn thuộc họ dây, chi gảy; ngoài ra họ đàn tranh có cả chi kéo và chi gõ.Đàn tranh được sử dụng để độc tốc, hòa tấu, đệm cho người hát.",
        "Đàn tỳ bà": "Đàn tỳ bà là một loại nhạc cụ dây gẩy của người phương Đông, qua thời gian dài sử dụng đàn đã được bản địa hóa tùy theo từng vùng hoặc từng quốc gia khác nhau. Màu âm đàn tỳ bà rất trong sáng, vui tươi nên thường thể hiện tính chất tươi sáng và trữ tình. Màu âm nhạc cụ này hơi giống đàn nguyệt nhưng có phần hơi đanh và khô hơn, nhất là ở những khoảng âm cao.",
        "Đàn đá": "Đàn đá là một nhạc cụ gõ cổ nhất của Việt Nam và là một trong những loại nhạc cụ cổ sơ nhất của loài người. Đàn được làm bằng các thanh đá với kích thước dài, ngắn, dày, mỏng khác nhau.hanh đá dài, to, dày có âm vực trầm trong khi thanh đá ngắn, nhỏ, mỏng thì tiếng thanh, được UNESCO xếp vào danh sách các nhạc cụ trong Không gian văn hóa Cồng Chiêng Tây Nguyên.",
        "Đàn đáy": "Đàn đáy (chữ Nôm: 彈帶), hay còn gọi là Vô đề cầm (chữ Hán:無題琴) là một loại nhạc cụ có 3 dây, phần cán rất dài và mặt sau của thùng âm có một lỗ lớn. Đây là nhạc cụ dân tộc cổ truyền của người Việt, không chỉ độc đáo ở hình dáng, âm thanh, mà còn được kết hợp với các nhạc cụ như phách và trống đế, tạo nên loại hình ca trù nổi tiếng."}

    loainhaccu = tk.Label(wd, text=str(prediction).upper(), bg='#F0F0F0', fg='sienna', font=("", 14))
    loainhaccu.place(x=15, y=400, width= 150, height= 30)

    thongtinnhaccu = tk.Message(wd, width=560, bg='azure', justify='left', text=str(d[prediction]), font=("", 14))
    thongtinnhaccu.place(x=200, y=280)

    s = {
        "Sáo trúc": "https://www.youtube.com/watch?v=yeY498M38KY&ab_channel=GordonSuns",
        "Đàn bầu": "https://www.youtube.com/watch?v=o2PDa3sLdXo&ab_channel=D%C6%B0%C6%A1ngHuy%E1%BB%81nLy",
        "Đàn gnuyệt": "https://www.youtube.com/watch?v=ql9C6ot7uF8&ab_channel=V%C3%B5Ph%C3%BAcNguy%C3%AAn",
        "Đàn T rung": "https://www.youtube.com/watch?v=F1ApAnem1q4&ab_channel=Dis%E1%BA%A3ns%E1%BB%91",
        "Đàn tranh": "https://www.youtube.com/watch?v=2BMXuyA0xnY&ab_channel=studenthvanle",
        "Đàn tỳ bà": "https://www.youtube.com/watch?v=BtcqyIph3Fs&ab_channel=Ti%E1%BB%83uTi%E1%BB%83uSinh",
        "Đàn đá": "https://www.youtube.com/watch?v=9uScac-N2jk&ab_channel=Ng%E1%BB%8DcVi%C3%AAnNguy%E1%BB%85n",
        "Đàn đáy": "https://www.youtube.com/watch?v=Zxszf0iuCCI&ab_channel=SGK%C3%82mnh%E1%BA%A1cC%C3%A1nhdi%E1%BB%81u%28%C4%90%E1%BB%97ThanhHi%C3%AAn%29"}

    root = Tk()  # create tkinter window

    root.title("PLAY SOUND IN YOUTUBE")
    root.iconbitmap("F:\AI\download-_1_.ico")
    root.geometry('100x100')

    url = str(s[prediction])
    driver = lambda :webbrowser.open(url)
    button = Button(root, text='Play', command=driver)

    button.pack()
    root.mainloop()


# Def GIAO DIEN

wd = Tk()
wd.title('NHẠC CỤ DÂN TỘC VIỆT NAM')
wd.iconbitmap("F:\AI\download.ico")
wd.geometry('960x450')
wd.resizable(width=False, height=False)
wd.configure(background='white')
load=Image.open('bg.png')
render=ImageTk.PhotoImage(load)
img=Label(wd,image=render)
img.place(x=0,y=0)



Label01 = tk.Label(wd)
Label01["activebackground"] = "#58a5de"
Label01['font'] = ("Candara", 20)
Label01["fg"] = "#333333"
Label01['bg'] = 'azure'
Label01["justify"] = "center"
Label01["text"] = "  NHẠC CỤ DÂN TỘC VIỆT NAM "
Label01["relief"] = "flat"
Label01.place(x=0, y=0, width=960, height=50)

frame = Frame(wd)
frame['bg'] = 'grey'
frame['bd'] = 1
frame.place(x=250, y=60, width=460, height=150)

# INFORMATION:--------------------------------------------------------
Label02 = tk.Label(wd)
Label02['font'] = ("Candara", 10)
Label02["fg"] = "#000000"
Label02["bg"] = "yellow"
Label02["justify"] = "left"
Label02["text"] = "ĐÂY LÀ:"
Label02["relief"] = "flat"
Label02.place(x=30, y=360, width=118, height=30)

# Def button
Button_01 = tk.Button(wd)
Button_01["bg"] = "chocolate"
Button_01['font'] = ("Candara", 10)
Button_01["fg"] = "#000000"
Button_01["justify"] = "left"
Button_01["text"] = "THÊM ẢNH"
Button_01.place(x=30, y=280, width=118, height=30)
Button_01["command"] = load_img

# Button classify
Button_02 = tk.Button(wd)
Button_02["bg"] = "lawngreen"
Button_01['font'] = ("Candara", 10)
Button_02["fg"] = "#000000"
Button_02["justify"] = "left"
Button_02["text"] = "NHẬN DIỆN"
Button_02.place(x=30, y=320, width=116, height=30)
Button_02["command"] = classify


wd.mainloop()