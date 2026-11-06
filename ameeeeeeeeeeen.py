import tkinter as tk
from tkinter import scrolledtext
import random

root = tk.Tk()
root.title("مفاجأتي إلك ❤️")
root.geometry("850x700")
root.configure(bg="#160d18")
root.resizable(False, False)

canvas = None
animation_job = None
particles = []
selected = None

STICKERS = [
    "❤️", "💗", "💕", "💖", "🌹",
    "🌷", "💐", "أحبج", "أريدج", "🥰"
]

COLORS = ["#ffb6c1", "#ff69b4", "#ffffff", "#ffd1dc"]


def clear_screen():
    global animation_job, canvas, particles, selected

    if animation_job:
        try:
            root.after_cancel(animation_job)
        except tk.TclError:
            pass

    animation_job = None
    canvas = None
    particles = []
    selected = None

    for widget in root.winfo_children():
        widget.destroy()


def make_canvas(bg="#160d18"):
    global canvas

    canvas = tk.Canvas(
        root,
        bg=bg,
        highlightthickness=0
    )
    canvas.pack(fill="both", expand=True)

    canvas.bind("<Button-1>", touch_item)
    canvas.bind("<B1-Motion>", move_item)
    canvas.bind("<ButtonRelease-1>", release_item)


# إنشاء ملصق متحرك
def add_particle(x=None, y=None, text=None):
    if x is None:
        x = random.randint(30, 820)

    if y is None:
        y = random.randint(30, 650)

    if text is None:
        text = random.choice(STICKERS)

    item = canvas.create_text(
        x, y,
        text=text,
        fill=random.choice(COLORS),
        font=("Arial", random.randint(17, 27), "bold")
    )

    particles.append({
        "id": item,
        "dx": random.choice([-2, -1, 1, 2]),
        "dy": random.choice([-2, -1, 1, 2])
    })


# لمس الملصق
def touch_item(event):
    global selected

    found = canvas.find_closest(event.x, event.y)

    if found:
        selected = found[0]


# تحريك الملصق باللمس أو الماوس
def move_item(event):
    if selected is not None:
        canvas.coords(selected, event.x, event.y)


def release_item(event):
    global selected
    selected = None


# تحريك الملصقات تلقائياً
def animate():
    global animation_job

    if canvas is None:
        return

    for particle in particles:
        item = particle["id"]

        if item == selected:
            continue

        canvas.move(
            item,
            particle["dx"],
            particle["dy"]
        )

        x, y = canvas.coords(item)

        if x < 20 or x > 830:
            particle["dx"] *= -1

        if y < 20 or y > 670:
            particle["dy"] *= -1

    animation_job = root.after(45, animate)


def first_screen():
    clear_screen()
    make_canvas("black")

    for _ in range(45):
        add_particle()

    canvas.create_text(
        425, 230,
        text="هل انتي فتومتي؟",
        fill="white",
        font=("Arial", 32, "bold")
    )

    button = tk.Button(
        root,
        text="اييي ❤️",
        font=("Arial", 20, "bold"),
        bg="#ffb6c1",
        command=start_love,
        padx=30,
        pady=10
    )

    canvas.create_window(425, 320, window=button)
    animate()


# شاشة القلوب والورود
def start_love():
    clear_screen()
    make_canvas("black")

    for _ in range(65):
        add_particle()

    canvas.create_text(
        425, 300,
        text="أحبج هواية ❤️🌹",
        fill="#ffb6c1",
        font=("Arial", 32, "bold")
    )

    canvas.create_text(
        425, 360,
        text="أريدج تبقين فرحتي دائماً 💗",
        fill="white",
        font=("Arial", 22, "bold")
    )

    animate()
    root.after(30000, sticker_screen)


# شاشة الملصقات قبل الرسالة
def sticker_screen():
    clear_screen()
    make_canvas("#160d18")

    for _ in range(75):
        add_particle()

    canvas.create_text(
        425, 180,
        text="إنتِ أحلى حكاية ❤️",
        fill="white",
        font=("Arial", 29, "bold")
    )

    canvas.create_text(
        425, 240,
        text="المسي القلوب والورود وحركيها 🌹",
        fill="#ffb6c1",
        font=("Arial", 18, "bold")
    )

    button = tk.Button(
        root,
        text="افتح رسالتي ❤️",
        font=("Arial", 19, "bold"),
        bg="#ffb6c1",
        fg="black",
        command=open_letter,
        padx=25,
        pady=10
    )

    canvas.create_window(425, 330, window=button)
    animate()


# نفس الكلام العاطفي والتكرارات
def build_letter():
    parts = [
        "إلى أحلى إنسانة بحياتي ❤️🌹\n\n",

        "أريدج تعرفين شكد وجودج يفرحني، "
        "وشكد كلامج وابتسامتج يخلّون يومي أحلى.\n\n",

        "أتمنى تبقين دائماً بخير وراحة بال، "
        "وتتحقق كل أمنياتج.\n\n",

        "يمكن ما أعرف أوصف كل اللي بداخلي بالكلام، "
        "بس أعرف إنج شخص عزيز وغالي، "
        "وأتمنى أكون سبب ابتسامة وفرحة إلج.\n\n",

        "الله يحفظج ويسعد قلبج، ويبعد عنج كل حزن وتعب، "
        "ويرزقج أيام حلوة على قد طيبة قلبج.\n\n",

        ("والله احبج ❤️💞\n") * 100,

        "\n"
    ]

    parts.extend(
        f"{i}. والله أموت عليج ❤️\n"
        for i in range(101, 201)
    )

    parts.append(
        "\nكل عام وإنتِ فرحتي، وكل يوم وإنتِ بخير. ❤️🌹"
    )

    return "".join(parts)


# فتح الرسالة
def open_letter():
    clear_screen()
    root.configure(bg="#fff0f5")

    tk.Label(
        root,
        text="💐 رسالة من القلب إلك 💐",
        bg="#fff0f5",
        fg="#9b2455",
        font=("Arial", 24, "bold")
    ).pack(pady=12)

    box = scrolledtext.ScrolledText(
        root,
        wrap=tk.WORD,
        font=("Arial", 15),
        bg="white",
        fg="#54213b",
        padx=18,
        pady=15,
        width=66,
        height=24
    )

    box.pack(
        padx=18,
        pady=8,
        fill="both",
        expand=True
    )

    box.insert("1.0", build_letter())
    box.configure(state="disabled")

    tk.Button(
        root,
        text="رجوع للقلوب ❤️",
        font=("Arial", 14, "bold"),
        bg="#ffb6c1",
        command=sticker_screen
    ).pack(pady=10)


first_screen()
root.mainloop()