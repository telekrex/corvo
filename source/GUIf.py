import customtkinter
import tkinter
import os
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("corvo_theme.json")
app = customtkinter.CTk()
app.geometry("1400x900")
app.title("Corvo")
frame = customtkinter.CTkFrame(master=app)
frame.pack(pady=2, padx=2, fill="both", expand=True)

import declare

projects_buttons = []

def open_corvo_file(path):
    print(path)
    os.startfile(path)

def open_location():
    print('')

def optionmenu_callback(choice):
    print("Selected:", choice)

# for project in declare.entries:
#     projects_buttons.append(customtkinter.CTkButton(master=frame, text=project.name, command=lambda path=project.corvo_file_path: open_corvo_file(path)))
#     projects_buttons[-1].pack(pady=8, padx=8)

### DROPDOWN SAMPLE:
dropdown_options = ['all']
dropdown_options = dropdown_options + declare.tags
dropdown = customtkinter.CTkOptionMenu(
    master=app,
    values=dropdown_options,
    command=optionmenu_callback
)
dropdown.pack(padx=20, pady=10)
dropdown.set(dropdown_options[0])  # Set initial selected value


### TABLE SAMPLE:
data = [
    ["Name", "Desc", "Status", 'Actions', 'Thoughts', 'Tags']
]

for entry in declare.entries:
    row = []
    row.append(entry.name)
    row.append(entry.desc)
    row.append(entry.status)
    row.append(entry.actions)
    row.append(entry.thoughts)
    row.append(entry.tags)
    data.append(row)

frame = customtkinter.CTkFrame(frame)
frame.pack(padx=20, pady=20, fill="both", expand=True)

for row_index, row in enumerate(data):
    for col_index, value in enumerate(row):
        cell = customtkinter.CTkLabel(frame, text=value, corner_radius=5, padx=8, pady=4)
        cell.grid(row=row_index, column=col_index, padx=5, pady=5, sticky="nsew")

        # Make columns expand evenly
        frame.grid_columnconfigure(col_index, weight=1)

# Run
app.mainloop()