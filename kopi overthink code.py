import random
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Product info with categories
menu_items = {
    "HOT DRINKS": {
        "Americano": 70.00,
        "Cafe Latte": 65.00,
        "Cappuccino": 80.00,
        "Black Coffee": 70.00,
        "Mocha Coffee": 75.00,
        "Vanilla Coffee": 60.00
    },
    "ICE COFFEE DRINK": {
        "Americano Iced Coffee": 70.00,
        "Vanilla Iced Coffee": 60.00,
        "Iced Coffee with Milk": 80.00
    },
    "PASTRY": {
        "Chocolate Cake": 95.00,
        "Choco Cookies": 60.00,
        "Choco Cupcake": 80.00
    }
}

cart = {}
users = {}

COLOR_BG = "#E6E6E6"
COLOR_PANEL = "#B8B0B0"
COLOR_ACCENT = "#D5A6BD"
COLOR_BUTTON = "#945586"
COLOR_HEADER = "#FFA726"
COLOR_PURCHASE = "#A2EBF7"

QUOTES = [
    "Kape lang, hindi ka niya iiwan! ☕😂",
    "Walang forever, pero may refill sa kape! 😆",
    "Ang tunay na pagmamahal, parang kape—mapait pero masarap! 😁",
    "Mas okay pang mawalan ng jowa kaysa mawalan ng kape! 😜",
    "Kape muna bago umasa. 😅",
    "Kung hindi ka niya mahal, kape na lang! ☕",
    "Sa kape lang ako nagpapakatatag, hindi sa'yo! 🤭",
    "Ang kape, parang ikaw—nakaka-adik! 😏",
    "Kape: Solusyon sa lahat ng problema, maliban sa pag-ibig! 😂",
    "Kung may problema ka, kape ka muna! ☕"
]

PRODUCT_HUGOT = {
    "Americano": "Kahit mapait, masarap pa rin basta kape. Parang pag-ibig mo.",
    "Cafe Latte": "Latte ka ba? Kasi kahit anong halo, bumabalik pa rin ako sa’yo.",
    "Cappuccino": "Cappuccino: Parang feelings ko, may foam pero walang label.",
    "Black Coffee": "Black coffee—tulad ng pagmamahal ko, puro at walang halong iba.",
    "Mocha Coffee": "Mocha: Tamang timpla ng tamis at pait, parang tayo noon.",
    "Vanilla Coffee": "Vanilla coffee—kahit simple, ikaw pa rin ang hanap ko.",
    "Americano Iced Coffee": "Kahit malamig, Americano pa rin. Parang ikaw, malamig na nga, mahal pa rin.",
    "Vanilla Iced Coffee": "Vanilla iced—kahit malamig, may tamis pa rin.",
    "Iced Coffee with Milk": "Iced coffee with milk—kahit malamig ang panahon, may lambing pa rin.",
    "Chocolate Cake": "Chocolate cake—matamis, pero baka sa huli, magka-sakit ka rin.",
    "Choco Cookies": "Choco cookies—parang ikaw, minsan lang dumaan pero hindi malilimutan.",
    "Choco Cupcake": "Choco cupcake—maliit pero punong-puno ng saya, parang kilig ko sa’yo."
}

class KopiOverthinkApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kopi Overthink - Coffee Shop")
        self.root.state('zoomed')
        self.root.configure(bg=COLOR_BG)
        self.login_screen()

    def clear_root(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def login_screen(self):
        self.clear_root()
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        header = Label(
            self.root,
            text="KOPI OVERTHINK - COFFEE SHOP",
            bg=COLOR_BG,
            fg=COLOR_ACCENT,
            font=("Arial", 18, "bold"),
            anchor="e"
        )
        header.grid(row=0, column=0, sticky="ne", padx=30, pady=(20, 0))

        frame = Frame(self.root, bg=COLOR_BG)
        frame.grid(row=1, column=0, sticky="n", padx=40, pady=20)

        Label(frame, text="Sign Up", font=("Arial", 24, "bold"), fg="darkgreen", bg=COLOR_BG, anchor="w").grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 0))
        Label(frame, text="Doesn't have account? ", bg=COLOR_BG, anchor="w").grid(row=1, column=0, sticky="w")

        create_account_label = Label(
            frame,
            text="Create  an account",
            fg=COLOR_ACCENT,
            bg=COLOR_BG,
            cursor="hand2",
            anchor="w"
        )
        create_account_label.grid(row=1, column=1, sticky="w")
        create_account_label.bind("<Button-1>", lambda e: self.signup_screen())

        Label(frame, text="\U0001F464", font=("Arial", 18), bg=COLOR_BG).grid(row=2, column=0, sticky="e", pady=(20, 0), padx=(0, 5))
        self.username_entry = Entry(frame, width=30, font=("Arial", 14))
        self.username_entry.grid(row=2, column=1, pady=(20, 0), sticky="w")

        Label(frame, text="\U0001F511", font=("Arial", 18), bg=COLOR_BG).grid(row=3, column=0, sticky="e", pady=(20, 0), padx=(0, 5))
        self.password_entry = Entry(frame, show="*", width=30, font=("Arial", 14))
        self.password_entry.grid(row=3, column=1, pady=(20, 0), sticky="w")

        Label(frame, text="Forgot Password?", fg="pink", bg=COLOR_BG, anchor="e").grid(row=4, column=1, sticky="e", pady=(5, 0))

        Button(
            frame,
            text="Sign In",
            bg=COLOR_BUTTON,
            fg="white",
            font=("Arial", 12, "bold"),
            command=self.authenticate_user
        ).grid(row=5, column=0, columnspan=2, pady=(20, 0), sticky="ew")

    def signup_screen(self):
        self.clear_root()
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        header = Label(
            self.root,
            text="KOPI OVERTHINK - COFFEE SHOP",
            bg=COLOR_BG,
            fg=COLOR_ACCENT,
            font=("Arial", 18, "bold"),
            anchor="e"
        )
        header.grid(row=0, column=0, sticky="ne", padx=30, pady=(20, 0))

        frame = Frame(self.root, bg=COLOR_BG)
        frame.grid(row=1, column=0, sticky="n", padx=40, pady=20)

        Label(frame, text="Create Account", font=("Arial", 24, "bold"), fg="darkgreen", bg=COLOR_BG, anchor="w").grid(row=0, column=0, columnspan=2, sticky="w", pady=(0, 0))
        Label(frame, text="Already have an account? ", bg=COLOR_BG, anchor="w").grid(row=1, column=0, sticky="w")

        back_to_login_label = Label(
            frame,
            text="Sign In",
            fg=COLOR_ACCENT,
            bg=COLOR_BG,
            cursor="hand2",
            anchor="w"
        )
        back_to_login_label.grid(row=1, column=1, sticky="w")
        back_to_login_label.bind("<Button-1>", lambda e: self.login_screen())

        Label(frame, text="\U0001F464", font=("Arial", 18), bg=COLOR_BG).grid(row=2, column=0, sticky="e", pady=(20, 0), padx=(0, 5))
        self.signup_username = Entry(frame, width=30, font=("Arial", 14))
        self.signup_username.grid(row=2, column=1, pady=(20, 0), sticky="w")

        Label(frame, text="\U0001F511", font=("Arial", 18), bg=COLOR_BG).grid(row=3, column=0, sticky="e", pady=(20, 0), padx=(0, 5))
        self.signup_password = Entry(frame, show="*", width=30, font=("Arial", 14))
        self.signup_password.grid(row=3, column=1, pady=(20, 0), sticky="w")

        Button(
            frame,
            text="Register",
            bg=COLOR_BUTTON,
            fg="white",
            font=("Arial", 12, "bold"),
            command=self.register_user
        ).grid(row=4, column=0, columnspan=2, pady=(20, 0), sticky="ew")

    def register_user(self):
        username = self.signup_username.get().strip()
        password = self.signup_password.get().strip()
        if not username or not password:
            messagebox.showwarning("Missing Info", "Please fill in both fields.")
            return
        if username in users:
            messagebox.showwarning("Already Exists", "Username already exists. Try a different one.")
        else:
            users[username] = password
            messagebox.showinfo("Success", "Account created successfully!")
            self.login_screen()

    def authenticate_user(self):
        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()
        if users.get(username) == password:
            messagebox.showinfo("Login Success", f"Welcome, {username}!")
            self.menu_screen()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def menu_screen(self):
        self.clear_root()
        header_frame = Frame(self.root, bg=COLOR_HEADER)
        header_frame.pack(fill="x")
        Label(
            header_frame,
            text="KOPI OVERTHINK - COFFEE SHOP",
            font=("Arial", 22, "bold"),
            bg=COLOR_HEADER,
            fg="white"
        ).pack(side="left", padx=20, pady=5)
        Button(
            header_frame,
            text="Log Out",
            bg=COLOR_BUTTON,
            fg="white",
            font=("Arial", 12, "bold"),
            command=self.login_screen
        ).pack(side="right", padx=20, pady=5)

        main_frame = Frame(self.root, bg=COLOR_BG)
        main_frame.pack(fill="both", expand=True, padx=30, pady=30)
        main_frame.grid_rowconfigure(0, weight=1)
        main_frame.grid_columnconfigure(0, weight=1)
        main_frame.grid_columnconfigure(1, weight=2)

        # Cart/Receipt Panel
        cart_panel = Frame(main_frame, bg=COLOR_PANEL, bd=2, relief="solid")
        cart_panel.grid(row=0, column=0, sticky="nsew", padx=(0, 40), ipadx=10, ipady=10)
        Label(cart_panel, text="🧾 ORDER RECEIPT", font=("Arial", 13, "bold"), fg=COLOR_BUTTON, bg=COLOR_PANEL).pack(pady=(5, 10))

        columns = ("item", "qty", "price")
        self.cart_tree = ttk.Treeview(cart_panel, columns=columns, show="headings", height=10)
        self.cart_tree.heading("item", text="SELECT")
        self.cart_tree.heading("qty", text="QUANTITY")
        self.cart_tree.heading("price", text="PRICE")
        self.cart_tree.column("item", width=120, anchor="center")
        self.cart_tree.column("qty", width=80, anchor="center")
        self.cart_tree.column("price", width=80, anchor="center")
        self.cart_tree.pack(padx=10, pady=5, fill="both", expand=True)

        Button(cart_panel, text="Remove Selected", bg="#ff6666", fg="white", command=self.remove_selected_from_cart).pack(pady=(0, 10))

        self.cart_total_var = StringVar(value="TOTAL: ₱0.00")
        Label(cart_panel, textvariable=self.cart_total_var, bg=COLOR_PANEL, fg="black", font=("Arial", 12, "bold")).pack(pady=(0, 5))
        self.purchase_btn = Button(cart_panel, text="PURCHASE", bg=COLOR_PURCHASE, fg="black", font=("Arial", 12, "bold"), command=self.purchase)
        self.purchase_btn.pack(pady=(0, 10))
        quote = random.choice(QUOTES)
        Label(cart_panel, text=f"“{quote}”", bg=COLOR_PANEL, fg=COLOR_ACCENT, font=("Arial", 10, "italic"), wraplength=200, justify="center").pack(pady=(10, 0))

        # Menu Products Panel as Cards
        menu_panel = Frame(main_frame, bg=COLOR_BG)
        menu_panel.grid(row=0, column=1, sticky="nsew")

        canvas = Canvas(menu_panel, bg=COLOR_BG, highlightthickness=0)
        scrollbar = Scrollbar(menu_panel, orient="vertical", command=canvas.yview)
        scrollable_frame = Frame(canvas, bg=COLOR_BG)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )
        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        CARD_WIDTH = 200
        CARD_HEIGHT = 180

        card_row = 0
        for category, items in menu_items.items():
            Label(
                scrollable_frame,
                text=category,
                font=("Arial", 15, "bold"),
                bg=COLOR_BG,
                fg=COLOR_BUTTON
            ).grid(row=card_row, column=0, columnspan=3, sticky="w", pady=(10, 5))
            card_row += 1
            col = 0
            for item, price in items.items():
                card = Frame(
                    scrollable_frame,
                    bg="white",
                    bd=2,
                    relief="ridge",
                    width=CARD_WIDTH,
                    height=CARD_HEIGHT
                )
                card.grid(row=card_row, column=col, padx=18, pady=15, sticky="n")
                card.grid_propagate(False)

                Label(
                    card,
                    text=item,
                    font=("Arial", 13, "bold"),
                    bg="white",
                    fg=COLOR_BUTTON
                ).pack(anchor="center", pady=(8, 0))

                hugot = PRODUCT_HUGOT.get(item, "")
                Label(
                    card,
                    text=hugot,
                    font=("Arial", 9, "italic"),
                    bg="white",
                    fg=COLOR_ACCENT,
                    wraplength=170,
                    justify="center"
                ).pack(anchor="center", pady=(0, 8))

                Label(
                    card,
                    text=f"₱{price:.2f}",
                    font=("Arial", 12),
                    bg="white",
                    fg="black"
                ).pack(anchor="center", pady=(0, 5))

                Button(
                    card,
                    text="Add to Cart",
                    bg=COLOR_PURCHASE,
                    fg="black",
                    font=("Arial", 11, "bold"),
                    command=lambda i=item, p=price: self.add_to_cart(i, p)
                ).pack(anchor="center", pady=(5, 0), ipadx=8, ipady=2)

                col += 1
                if col > 2:
                    col = 0
                    card_row += 1
            card_row += 1

        self.update_cart_tree()

    def update_cart_tree(self):
        for row in self.cart_tree.get_children():
            self.cart_tree.delete(row)
        total = 0
        for item, qty in cart.items():
            price = next((p[item] for p in menu_items.values() if item in p), 0)
            item_total = price * qty
            total += item_total
            self.cart_tree.insert("", "end", values=(item, qty, f"₱{item_total:.2f}"))
        self.cart_total_var.set(f"TOTAL: ₱{total:.2f}")
        if cart:
            self.purchase_btn.config(state=NORMAL)
        else:
            self.purchase_btn.config(state=DISABLED)

    def add_to_cart(self, item, price):
        cart[item] = cart.get(item, 0) + 1
        self.update_cart_tree()

    def remove_selected_from_cart(self):
        selected = self.cart_tree.selection()
        for sel in selected:
            item_name = self.cart_tree.item(sel, "values")[0]
            if item_name in cart:
                del cart[item_name]
        self.update_cart_tree()

    def purchase(self):
        if not cart:
            messagebox.showwarning("Empty Cart", "Your cart is empty. Please add items before purchasing.")
            return
        items_lines = []
        total = 0
        for item, qty in cart.items():
            price = next((p[item] for p in menu_items.values() if item in p), 0)
            item_total = price * qty
            total += item_total
            items_lines.append(f"{item} x{qty} - ₱{item_total:.2f}")
        items_list = "\n".join(items_lines)
        quote = random.choice(QUOTES)
        receipt = (
            f"Thank you for your purchase!\n\n"
            f"Items:\n{items_list}\n\n"
            f"TOTAL: ₱{total:.2f}\n\n"
            f"Quote:\n\"{quote}\""
        )
        messagebox.showinfo("Receipt", receipt)
        cart.clear()
        self.update_cart_tree()

root = Tk()
app = KopiOverthinkApp(root)
root.mainloop()