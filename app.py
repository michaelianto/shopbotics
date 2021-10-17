from tkinter import *
from chat import get_response, bot_name
import json

BG_COLOR = "#393e46"
BG_GRAY = "#02475e"
TEXT_COLOR = "#ffde7d"

FONT = "Helvetica 14"
FONT_BOLD = "Helvetica 13 bold"

class ChatApplication:
    
    def __init__(self):
        self.window = Tk()
        self._setup_main_window()
        
    def run(self):
        self.window.mainloop()
        
    def _setup_main_window(self):
        self.window.title("Chat")
        self.window.resizable(width=False, height=False)
        self.window.configure(width=900, height=550, bg=BG_COLOR)
        
        # head label
        head_label = Label(self.window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="SHOPBOTICS Demo App", font=FONT_BOLD, pady=10)
        head_label.place(relwidth=1)
        
        # tiny divider
        line = Label(self.window, width=450, bg=BG_GRAY)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        
        # text widget
        self.text_widget = Text(self.window, width=20, height=2, bg=BG_COLOR, fg=TEXT_COLOR,
                                font=FONT, padx=5, pady=5)
        self.text_widget.place(relheight=0.745, relwidth=1, rely=0.08)
        self.text_widget.configure(cursor="arrow", state=DISABLED)
        
        # scroll bar
        scrollbar = Scrollbar(self.text_widget)
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.text_widget.yview)
        
        # bottom label
        bottom_label = Label(self.window, bg=BG_GRAY, height=80)
        bottom_label.place(relwidth=1, rely=0.825)
        
        # message entry box
        self.msg_entry = Entry(bottom_label, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT)
        self.msg_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.msg_entry.focus()
        self.msg_entry.bind("<Return>", self._on_enter_pressed)
        
        # send button
        send_button = Button(bottom_label, text="Send", font=FONT_BOLD, width=20, bg=BG_GRAY, fg=TEXT_COLOR,
                             command=lambda: self._on_enter_pressed(None))
        send_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.11)

        # setting button
        setting_button = Button(bottom_label, text="Setting", font=FONT_BOLD, width=20, bg=BG_GRAY, fg=TEXT_COLOR,
                             command=lambda: self._on_setting_pressed(None))
        setting_button.place(relx=0.89, rely=0.008, relheight=0.06, relwidth=0.11)

    def _on_setting_pressed(self, event):
        self.setting_window = Tk()
        self.setting_window.title("Answer Setting")
        self.setting_window.resizable(width=False, height=False)
        self.setting_window.configure(width=900, height=550, bg=BG_COLOR)

        head_label = Label(self.setting_window, bg=BG_COLOR, fg=TEXT_COLOR,
                           text="SHOPBOTICS Answer Setting", font=FONT_BOLD, pady=10)
        head_label.pack()
        with open('intents.json', 'r') as f:
            intents = json.load(f)

        all_words = []
        tags = []
        all_pattern = {}
        for intent in intents['intents']:
            tag = intent['tag']
            # add to tag list
            tags.append(tag)

        scrollbar = Scrollbar(self.setting_window)
        scrollbar.pack(side=RIGHT, fill=Y)

        # # curr label
        curr_label = Label(self.setting_window, bg=BG_GRAY, width=80, height=1)
        curr_label.pack()

        tag_button = []

        def show_response_page(idx):
            self.response_window = Tk()
            self.response_window.title("Edit Response")
            self.response_window.resizable(width=False, height=False)
            self.response_window.configure(width=900, height=550, bg=BG_COLOR)

            head_label = Label(self.response_window, bg=BG_COLOR, fg=TEXT_COLOR,
                               text="Edit Bot Response\nSeperate Response with '-'", font=FONT_BOLD, pady=10)
            head_label.place(relwidth=1)

            def update_json(x=None, idx=None):
                response = resp_entry.get()
                print(response.split("-"))
                curr_intent = intents['intents']
                print(curr_intent[idx])
                curr_intent = curr_intent[idx]
                print(curr_intent['responses'])
                intents['intents'][idx]['responses'] = response.split("-")
                print(intents['intents'][idx]['responses'])

                json_object = json.dumps(intents, indent=4)

                with open("intents.json", "w") as outfile:
                    outfile.write(json_object)

            bottom_label = Label(self.response_window, bg=BG_GRAY, height=80)
            bottom_label.place(relwidth=1, rely=0.825)


            resp_entry = Entry(bottom_label, bg=BG_COLOR, fg=TEXT_COLOR, font=FONT)
            resp_entry.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
            resp_entry.focus()
            resp_entry.bind("<Return>", update_json)

            # send button
            update_button = Button(bottom_label, text="Update", font=FONT_BOLD, width=20, bg=BG_GRAY,fg=TEXT_COLOR,
                                 command=lambda: update_json(idx=idx))
            update_button.place(relx=0.77, rely=0.008, relheight=0.06, relwidth=0.23)

        salam_button = Button(curr_label, text="1: Salam", font=FONT_BOLD, fg=TEXT_COLOR,width=80,height=1, bg=BG_GRAY, command=lambda: show_response_page(0))
        salam_button.pack()
        terimakasih_button = Button(curr_label, text="2: Terimakasih", font=FONT_BOLD, fg=TEXT_COLOR,width=80, height=1, bg=BG_GRAY,command=lambda: show_response_page(1))
        terimakasih_button.pack()
        jam_button = Button(curr_label, text="3: Jam Operasional", font=FONT_BOLD, fg=TEXT_COLOR,width=80, height=1, bg=BG_GRAY, command=lambda: show_response_page(2))
        jam_button.pack()
        lokasi_button = Button(curr_label, text="4: Lokasi", font=FONT_BOLD, fg=TEXT_COLOR,width=80, height=1, bg=BG_GRAY,
                                      command=lambda: show_response_page(3))
        lokasi_button.pack()
        pembayaran_button = Button(curr_label, text="5: Pembayaran", font=FONT_BOLD, fg=TEXT_COLOR,width=80, height=1, bg=BG_GRAY,
                                    command=lambda: show_response_page(4))
        pembayaran_button.pack()
        servis_button = Button(curr_label, text="6: Layanan", font=FONT_BOLD, fg=TEXT_COLOR,width=80, height=1, bg=BG_GRAY,
                                      command=lambda: show_response_page(5))
        servis_button.pack()

    def _on_enter_pressed(self, event):
        msg = self.msg_entry.get()
        self._insert_message(msg, "You")
        
    def _insert_message(self, msg, sender):
        if not msg:
            return
        
        self.msg_entry.delete(0, END)
        msg1 = f"{sender}: {msg}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg1)
        self.text_widget.configure(state=DISABLED)
        
        msg2 = f"{bot_name}: {get_response(msg)}\n\n"
        self.text_widget.configure(state=NORMAL)
        self.text_widget.insert(END, msg2)
        self.text_widget.configure(state=DISABLED)
        
        self.text_widget.see(END)
             
        
if __name__ == "__main__":
    app = ChatApplication()
    app.run()