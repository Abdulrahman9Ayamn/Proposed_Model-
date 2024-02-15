import tkinter as tk

def login():
    username_str = username_entry.get()

    try:
        username = int(username_str)
    except ValueError:
        message_label.config(text="Please enter valid value in arrays" , bg='#cfd8dc' , fg="#d50000" )
        return

    if username <= 25:
        message_label.config(text="Matrix done successfully" , bg='#cfd8dc', fg="#00e676")
        enter_names_window(username)
        # فتح نافذة جديدة للمستخدم(username)

    else:
        message_label.config(
            text=" You have exceeded the allowed number. The count must be 25 or less." , bg='#cfd8dc' ,fg="#d50000")


def enter_names_window(size):
    # إنشاء نافذة Toplevel جديدة
    string_window = tk.Toplevel()
    string_window.title("Enter Names")

    # إنشاء إطارين (frames) للأعمدة والصفوف
    col_frame = tk.LabelFrame(string_window, text="Columns")
    col_frame.pack(side="left", padx=10, pady=10, fill="both", expand=True)
    row_frame = tk.LabelFrame(string_window, text="Rows")
    row_frame.pack(side="right", padx=10, pady=10, fill="both", expand=True)

    # إنشاء شبكة لعناصر إدخال البيانات (entry widgets) للأعمدة والصفوف
    col_entries = []
    row_entries = []
    for i in range(size):
        string_label = tk.Label(col_frame, text=f"Column {i+1}:")
        string_label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
        string_entry = tk.Entry(col_frame, width=20, font=("Arial", 12))
        string_entry.grid(row=i, column=1, padx=10, pady=5, sticky="ew")
        string_entry.bind("<Up>", lambda event,
                          idx=i: col_entries[(idx-1) % size].focus())
        string_entry.bind("<Down>", lambda event,
                          idx=i: col_entries[(idx+1) % size].focus())
        col_entries.append(string_entry)

        string_label = tk.Label(row_frame, text=f"Row {i+1}:")
        string_label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
        string_entry = tk.Entry(row_frame, width=20, font=("Arial", 12))
        string_entry.grid(row=i, column=1, padx=10, pady=5, sticky="ew")
        string_entry.bind("<Up>", lambda event,
                          idx=i: row_entries[(idx-1) % size].focus())
        string_entry.bind("<Down>", lambda event,
                          idx=i: row_entries[(idx+1) % size].focus())
        row_entries.append(string_entry)

    # إنشاء زر (button) لإنشاء القائمة.
    button_frame = tk.Frame(string_window)
    button_frame.pack(pady=10)
    create_button = tk.Button(button_frame, text="Create List", font=(
        "Arial", 12), command=lambda: create_list(row_entries, col_entries, size, string_window))
    create_button.pack(padx=10, pady=5)
    create_button.config(bg='#26a69a')

    # تعيين التركيز (focus) على أول عنصر إدخال البيانات في إطار الأعمدة (column frame).
    col_entries[0].focus_set()

def create_list(row_entries, col_entrie, size, string_window):
    col_list = []
    row_list = []
    for entry in row_entries:
        row_list.append(entry.get())
    for entry in col_entrie:
        col_list.append(entry.get())
    string_window.destroy()
    open_new_window(col_list, row_list, size)


def open_new_window(col_list, row_list, username):
    index = 0
    list_result = []
    window.withdraw()

    o = username

# تعريف المتغير matrix1
    matrix1 = [[0 for j in range(o)] for i in range(o)]
    # تعريف قائمة لتخزين المصفوفات السابقة
    matrix_history = []

    def display_item():
        nonlocal index
        show_list(index)

    def next_item():
        nonlocal index
        index = index + 1
        if index == len(list_result):
            index = 0
        display_item()

    def prev_item():
        nonlocal index
        index = index - 1
        if index < 0:
            index = len(list_result) - 1
        display_item()
# دالة للضرب المصفوفات المربعة
    # ليست لتخوين المصفوفات
    list_result = []

    def matrix2_multiply():
        nonlocal index
        index = index + 1
        # احصول على البيانات الجديدة من مربعات النص
        for i in range(o):
            for j in range(o):
                matrix1[i][j] = float(entry_matrix1[i][j].get())
        if index == 1:
            if not (matrix1):
                index -= 1
                return False
                # إضافة المصفوفة الحالية إلى قائمة المصفوفات السابقة
                matrix_history.append([row[:] for row in matrix1])
    # إنشاء المصفوفة الناتجة
        result = [[0 for j in range(o)] for i in range(o)]
    # ضرب المصفوفات
        for i in range(o):
            for j in range(o):
                for k in range(o):
                    result[i][j] += matrix1[i][k] * matrix1[k][j]
        list_result.append(result)

    # عرض النتيجة في مربعات النص
        for i in range(o):
            for j in range(o):
                entry_matrix1[i][j].delete(0, tk.END)
                entry_matrix1[i][j].insert(0, str(result[i][j])) 

    def show_list(index):
        for i in range(o):
            for j in range(o):
                entry_matrix1[i][j].delete(0, tk.END)
                entry_matrix1[i][j].insert(0, str(list_result[index][i][j]))
                # دالة لمسح محتوى مربعات النص لـ matrix1 واستعادة المصفوفة السابقة

    def undo_matrices():
        if len(matrix_history) > 0:
            # استرداد المصفوفة السابقة من قائمة المصفوفات السابقة
            prev_matrix = matrix_history.pop()
        # عرض المصفوفة السابقة في مربعات النص
            for i in range(o):
                for j in range(o):
                    entry_matrix1[i][j].delete(0, tk.END)
                    entry_matrix1[i][j].insert(0, str(prev_matrix[i][j]))
    # فحص مجموع الصفّ

   # دالة لمسح محتوى مربعات النص لـ matrix1

    def clear_matrices():
        for i in range(o):
            for j in range(o):
                entry_matrix1[i][j].delete(0, tk.END)

    # دالة لتقريب القيم في matrix1 إلى أقرب رقم غير صفري
    def round_nonzero():
        for i in range(o):
            for j in range(o):
                if matrix1[i][j] != .100:
                    matrix1[i][j] = round(matrix1[i][j])

    # إنشاء النافذة الرئيسية
    root = tk.Toplevel(window)
    root.geometry("950x600+250+200")
    root.title("Lattice allocation costs")
    root.configure(background='#cfd8dc')
    # bg = PhotoImage(file = "D:\6IBaa1.jpg")
    # root.configure(background=bg)

    # إضافة تسميات الصفوف
    for i in range(o):
        row_label = tk.Label(
            root, text=f"{row_list[i]}", font=('Arial', 14), bg='#cfd8dc')
        row_label.grid(row=i+2, column=0, padx=5, pady=5)

    # إضافة تسميات الأعمدة

    for j in range(o):
        col_label = tk.Label(
            root, text=f"{col_list[j]}", font=('Arial', 14), bg='#cfd8dc')
        col_label.grid(row=1, column=j+1, padx=5, pady=5)

    # إنشاء شبكة من مربعات النص لمصفوفة matrix1
    title_label = tk.Label(root, text="Lattice allocation costs", font=(
        "Arial", 18, "bold"), bg='#cfd8dc', borderwidth=2, relief="groove")
    title_label.grid(row=0, column=1, columnspan=3, pady=10, sticky="nsew")
     # شروط الاتجاهات الاربعة  في  المصفوفات  
    def handle_arrow_keys(event):
        row, col = None, None
        for i in range(len(entry_matrix1)):
            for j in range(len(entry_matrix1[i])):
                if entry_matrix1[i][j] == event.widget:
                    row, col = i, j
                    break
            if row is not None:
                break
        if row is None or col is None:
            return
        if event.keysym == 'Up' and row > 0:
            entry_matrix1[row-1][col].focus()
        elif event.keysym == 'Down' and row < len(entry_matrix1)-1:
            entry_matrix1[row+1][col].focus()
        elif event.keysym == 'Left' and col > 0:
            entry_matrix1[row][col-1].focus()
        elif event.keysym == 'Right' and col < len(entry_matrix1[row])-1:
            entry_matrix1[row][col+1].focus()


    #الاتجاهات الاربعة  في  المصفوفات 
    entry_matrix1 = []
    for i in range(o):
        row = []
        for j in range(o):
            entry = tk.Entry(root, width=5, font=('Arial', 14))
            entry.grid(row=i+2, column=j+1, padx=5, pady=5)
            entry.config(bg='#b0bec5')
            entry.bind("<Up>", handle_arrow_keys)
            entry.bind("<Down>", handle_arrow_keys)
            entry.bind("<Left>", handle_arrow_keys)
            entry.bind("<Right>", handle_arrow_keys)
            row.append(entry)
        entry_matrix1.append(row)

    for i in range(username):
        label = tk.Label(root, text=f" 1.0", font=('Arial', 14), bg='#388e3c')
        label.grid(row=i+2, column=username+1)
        label.configure(foreground="black")

    # إضافة زر الضرب
    multiply_button = tk.Button(root, text="Multiply", font=(
        'Arial', 14), command=matrix2_multiply)
    multiply_button.grid(row=o+2, column=0, padx=5, pady=5)
    multiply_button.config(bg='#26a69a')
    # إضافة زر المسح
    clear_button = tk.Button(root, text="Clear", font=(
        'Arial', 14), command=clear_matrices)
    clear_button.grid(row=o+2, column=4, padx=5, pady=5)
    clear_button.config(bg='#f44336')
    # زر الرجوع الي الخلف خطوه
    prev_button = tk.Button(root, text="Previous",                       
    font=('Arial', 14), command=prev_item)
    prev_button.grid(row=o+2, column=2, pady=10)
    prev_button.config(bg='#26a69a')
    # زر التقدم الي الامام خطوه
    next_button = tk.Button(root, text="next", font=(
        'Arial', 14), command=next_item)
    next_button.grid(row=o+2, column=1, pady=10)
    next_button.config(bg='#26a69a')
    # الى الصفحة الرئيسية إنشاء زر "عودة"
    back_button = tk.Button(root, text="Back", font=(
    'Arial', 14), command=lambda: [enter_names_window(username), root.destroy(), window.deiconify()])
    back_button.grid(row=o+2, column=3, pady=10)
    back_button.config(bg='#f44336')

    # تشغيل النافذة الرئيسية
    root.mainloop()

# إنشاء نافذة جديدة
window = tk.Tk()
# تحديد حجم النافذة
window.geometry("380x150+750+400")
window.configure(background='#cfd8dc')
# تحديد عنوان النافذة
window.title("Lattice allocation costs")
# إضافة حقل النص
username_label = tk.Label(text="Enter the value of the square matrix" , bg='#cfd8dc' )
username_entry = tk.Entry()
username_entry.focus_set()
username_label.pack()
username_entry.pack()
# إضافة زر تسجيل الدخول
login_button = tk.Button(text=" Create ", command=login )
login_button.pack()
login_button.config(bg='#26a69a')

# إضافة مساحة فارغة للفصل بين حقول النص والزر
empty_space = tk.Label()
empty_space.pack()
empty_space.config(bg='#cfd8dc')
window.bind( '<Return>' , lambda event: login_button.invoke())

# ضافة حقل الرسالة لعرض رسالة
message_label = tk.Label()
message_label.pack()
message_label.config(bg='#cfd8dc')
# تشغيل النافذة
window.mainloop()
