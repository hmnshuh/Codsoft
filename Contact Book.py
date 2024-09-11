import tkinter as tk
from tkinter import messagebox, simpledialog, Scrollbar, Listbox

# Function to handle adding a new contact
def add_contact():
    name = simpledialog.askstring("Add Contact", "Enter Name:")
    if not name:
        return
    
    phone = simpledialog.askstring("Add Contact", "Enter Phone Number:")
    if not phone:
        return
    
    email = simpledialog.askstring("Add Contact", "Enter Email:")
    address = simpledialog.askstring("Add Contact", "Enter Address:")
    
    contacts.append({'name': name, 'phone': phone, 'email': email, 'address': address})
    update_contact_list()

# Function to update the contact list display
def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['name']}: {contact['phone']}")

# Function to handle searching for a contact
def search_contact():
    query = simpledialog.askstring("Search Contact", "Enter Name or Phone Number:")
    if not query:
        return
    
    found_contacts = []
    for contact in contacts:
        if query.lower() in contact['name'].lower() or query in contact['phone']:
            found_contacts.append(contact)
    
    if found_contacts:
        messagebox.showinfo("Search Results", "\n".join([f"{contact['name']}: {contact['phone']}" for contact in found_contacts]))
    else:
        messagebox.showinfo("Search Results", "No contacts found.")

# Function to handle updating a contact
def update_contact():
    selected_index = contact_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("Update Contact", "Select a contact to update.")
        return
    
    contact = contacts[selected_index[0]]
    new_phone = simpledialog.askstring("Update Contact", f"Update Phone Number for {contact['name']}:")
    if new_phone:
        contact['phone'] = new_phone
        update_contact_list()

# Function to handle deleting a contact
def delete_contact():
    selected_index = contact_listbox.curselection()
    if not selected_index:
        messagebox.showwarning("Delete Contact", "Select a contact to delete.")
        return
    
    confirmed = messagebox.askyesno("Delete Contact", "Are you sure you want to delete this contact?")
    if confirmed:
        del contacts[selected_index[0]]
        update_contact_list()

# Setting up the main window
root = tk.Tk()
root.title("Contact Book")
root.geometry("600x400")

# List to store contacts
contacts = []

# Creating widgets
frame_left = tk.Frame(root)
frame_right = tk.Frame(root)

add_button = tk.Button(frame_left, text="Add Contact", command=add_contact)
search_button = tk.Button(frame_left, text="Search Contact", command=search_contact)
update_button = tk.Button(frame_left, text="Update Contact", command=update_contact)
delete_button = tk.Button(frame_left, text="Delete Contact", command=delete_contact)

contact_list_label = tk.Label(frame_right, text="Contact List", font=("Arial", 14))
scrollbar = Scrollbar(frame_right)
contact_listbox = Listbox(frame_right, width=40, yscrollcommand=scrollbar.set, font=("Arial", 12))

# Packing widgets
frame_left.pack(side=tk.LEFT, padx=20, pady=20)
frame_right.pack(side=tk.LEFT, padx=20, pady=20)

add_button.pack(pady=10)
search_button.pack(pady=10)
update_button.pack(pady=10)
delete_button.pack(pady=10)

contact_list_label.pack(pady=10)
contact_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar.config(command=contact_listbox.yview)

# Running the main event loop
root.mainloop()
