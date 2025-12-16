import tkinter as tk
from tkinter import ttk, messagebox

class CallChargeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Long Distance Call Charge Calculator")
        self.root.geometry("550x450")

        # Rates Table
        self.rates = {
            "American Region":  {"Day": (50, 3), "Night": (45, 3)},
            "Asian  Region":    {"Day": (30, 2), "Night": (27, 2)},
            "African Region":   {"Day": (40, 3), "Night": (36, 3)},
            "European Region":  {"Day": (35, 2), "Night": (30, 2)},
        }

        # MAIN INPUT FRAME
        user_frame = tk.LabelFrame(root, text="User Inputs", padx=10, pady=10)
        user_frame.pack(padx=15, pady=10, fill="x")

        # Duration
        tk.Label(user_frame, text="Length of Call (in minutes):").grid(row=0, column=0, sticky="w")
        self.minutes_var = tk.StringVar()
        tk.Entry(user_frame, textvariable=self.minutes_var, width=15).grid(row=0, column=1, sticky="w")

        # Destination
        tk.Label(user_frame, text="Destination Code:").grid(row=1, column=0, sticky="w")
        self.dest_var = tk.StringVar()
        ttk.Combobox(
            user_frame, textvariable=self.dest_var, state="readonly",
            values=list(self.rates.keys())
        ).grid(row=1, column=1, sticky="w")

        # Time Code (in its own small frame)
        tk.Label(user_frame, text="Time Code:").grid(row=2, column=0, sticky="w")

        time_frame = tk.Frame(user_frame)
        time_frame.grid(row=2, column=1, sticky="w")

        self.time_var = tk.StringVar()   # no auto-select
        tk.Radiobutton(time_frame, text="Day Time",
                       variable=self.time_var, value="Day").pack(anchor="w")
        tk.Radiobutton(time_frame, text="Night Time",
                       variable=self.time_var, value="Night").pack(anchor="w")

        # OUTPUT FRAME
        output_frame = tk.LabelFrame(root, text="Transaction Summary", padx=10, pady=10)
        output_frame.pack(padx=15, pady=5, fill="both", expand=True)

        self.output = tk.Text(output_frame, width=60, height=7)
        self.output.pack()

        # BUTTONS
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=10)

        tk.Button(btn_frame, text="Compute Charge", width=15, command=self.compute).grid(row=0, column=0, padx=5)
        tk.Button(btn_frame, text="Reset",          width=15, command=self.reset).grid(row=0, column=1, padx=5)
        tk.Button(btn_frame, text="About",          width=15, command=self.about).grid(row=0, column=2, padx=5)
        tk.Button(btn_frame, text="Close",          width=15, command=root.destroy).grid(row=0, column=3, padx=5)

    # -------------------- COMPUTE FUNCTION --------------------
    def compute(self):
        # duration validation
        try:
            minutes = int(self.minutes_var.get())
            if minutes <= 0:
                raise ValueError
        except:
            messagebox.showerror("Error", "Duration must be a positive integer.")
            return

        destination = self.dest_var.get()
        timecode = self.time_var.get()

        if not destination or not timecode:
            messagebox.showerror("Error", "Please complete all fields.")
            return

        # get rate values
        rate, per_minute = self.rates[destination][timecode]
        total = (minutes / per_minute) * rate

        # update output box
        self.output.delete("1.0", tk.END)
        summary = (
            f"Duration of Call:   {minutes} minutes\n"
            f"Destination Code:   {destination}\n"
            f"Time Code:          {timecode}\n"
            f"Rate:               ₱{rate} every {per_minute} minutes\n"
            f"-----------------------------------------\n"
            f"TOTAL CHARGE:       ₱{total:.2f}"
        )
        self.output.insert(tk.END, summary)

    # -------------------- RESET FUNCTION --------------------
    def reset(self):
        self.minutes_var.set("")
        self.dest_var.set("")
        self.time_var.set("")  # clears radio selection
        self.output.delete("1.0", tk.END)

    # -------------------- ABOUT FUNCTION --------------------
    def about(self):
        messagebox.showinfo("About", "Hello I'm your Name")

# RUN APP
root = tk.Tk()
CallChargeApp(root)
root.mainloop()