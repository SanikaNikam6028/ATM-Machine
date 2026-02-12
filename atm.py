
import tkinter as tk
from tkinter import messagebox, simpledialog


pin = "1234"
balance = 5000
transactions = []


def show_welcome():
    welcome_frame.pack_forget()
    pin_frame.pack(pady=20)

def check_pin():
    if pin_entry.get() == pin:
        messagebox.showinfo("ATM", "PIN correct")
        pin_frame.pack_forget()
        menu_frame.pack(pady=20)
    else:
        messagebox.showerror("ATM", "Wrong PIN")

def get_amount():
    if amount_entry.get() == "":
        messagebox.showerror("Error", "Please enter amount")
        return None
    if not amount_entry.get().isdigit():
        messagebox.showerror("Error", "Enter numbers only")
        return None
    amt = int(amount_entry.get())
    if amt <= 0:
        messagebox.showerror("Error", "Amount must be greater than zero")
        return None
    return amt

def check_balance():
    messagebox.showinfo("Balance", "Your balance is Rs {balance}")

def deposit():
    global balance
    amt = get_amount()
    if amt:
        balance += amt
        transactions.append("Deposited Rs {amt}")
        messagebox.showinfo("ATM", "Money Deposited Successfully")
        amount_entry.delete(0, tk.END)

def withdraw():
    global balance
    amt = get_amount()
    if amt:
        if amt > 2000:
            messagebox.showerror("ATM", "Daily withdraw limit is Rs 2000")
        elif amt > balance:
            messagebox.showerror("ATM", "Not enough balance")
        else:
            balance -= amt
            transactions.append("Withdrawn Rs {amt}")
            messagebox.showinfo("ATM", "Collect your cash")
            amount_entry.delete(0, tk.END)

def show_history():
    if not transactions:
        messagebox.showinfo("Mini Statement", "No transactions yet")
    else:
        history = "\n".join(transactions[-5:])
        messagebox.showinfo("Mini Statement", history)

def change_pin():
    global pin
    new_pin = simpledialog.askstring("Change PIN", "Enter new 4-digit PIN", show="*")
    if new_pin and new_pin.isdigit() and len(new_pin) == 4:
        pin = new_pin
        messagebox.showinfo("ATM", "PIN changed successfully")
    else:
        messagebox.showerror("Error", "PIN must be 4 digits")

def logout():
    menu_frame.pack_forget()
    pin_entry.delete(0, tk.END)
    amount_entry.delete(0, tk.END)
    pin_frame.pack(pady=20)



root = tk.Tk()
root.title("ATM Machine")
root.geometry("320x380")
root.configure(bg="#e6f2ff")


welcome_frame = tk.Frame(root, bg="#e6f2ff")
welcome_frame.pack(pady=80)

Label = tk.Label(
    welcome_frame,
    text="Welcome to ATM",
    font=("Arial", 18, "bold"),
    bg="#e6f2ff")
Label.pack(pady=20)

Button = tk.Button(
    welcome_frame,
    text="Enter",
    font=("Arial", 12),
    width=15,
    command=show_welcome)
Button.pack()


pin_frame = tk.Frame(root, bg="#e6f2ff")

Label = tk.Label(
    pin_frame,
    text="Enter PIN",
    font=("Arial", 12),
    bg="#e6f2ff")
Label.pack(pady=5)

pin_entry = tk.Entry(pin_frame, show="*", font=("Arial", 12))
pin_entry.pack()

Button =tk.Button(
    pin_frame,
    text="Submit",
    width=15,
    command=check_pin
)
Button.pack(pady=10)


menu_frame = tk.Frame(root, bg="#e6f2ff")

Label = tk.Label(
    menu_frame,
    text="Enter Amount",
    bg="#e6f2ff",
    font=("Arial", 12)
)
Label.pack()

amount_entry = tk.Entry(menu_frame, font=("Arial", 12))
amount_entry.pack(pady=5)

Button = tk.Button(menu_frame, text="Check Balance", width=20, command=check_balance)
Button.pack(pady=3)
Button =tk.Button(menu_frame, text="Deposit", width=20, command=deposit)
Button.pack(pady=3)
Button =tk.Button(menu_frame, text="Withdraw", width=20, command=withdraw)
Button.pack(pady=3)
Button =tk.Button(menu_frame, text="Mini Statement", width=20, command=show_history)
Button.pack(pady=3)
Button =tk.Button(menu_frame, text="Change PIN", width=20, command=change_pin)
Button.pack(pady=3)
Button =tk.Button(menu_frame, text="Logout", width=20, command=logout)
Button.pack(pady=3)
Button =tk.Button(menu_frame, text="Exit", width=20, command=root.destroy)
Button.pack(pady=10)

root.mainloop()