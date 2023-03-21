from tkinter import *
from tkinter import ttk
import time

# Main Window Here

root = Tk()
root.withdraw()

root_scroll = Toplevel(root)
root_scroll.geometry("1920x1080")
root_scroll.configure(bg="#212121")
root_scroll.title("Car Rent")
root_scroll.resizable(True, True)
the_root_scroll = Canvas(root_scroll, bg="#212121", borderwidth=0, highlightthickness=0)
the_root_scroll.pack(side=TOP, fill=BOTH, expand=1)
my_scrollbar_root = Scrollbar(root_scroll, orient=HORIZONTAL, command=the_root_scroll.xview)
my_scrollbar_root.pack(side=BOTTOM, fill=X)
the_root_scroll.configure(xscrollcommand=my_scrollbar_root.set)
the_root_scroll.bind('<Configure>', lambda e: the_root_scroll.configure(scrollregion=the_root_scroll.bbox("all")))
frame_root_scroll = Frame(the_root_scroll, bg="#212121", borderwidth=0, highlightthickness=0)
the_root_scroll.create_window((0, 0), window=frame_root_scroll, anchor="e")


def for_scroll_root(event):
    the_root_scroll.xview_scroll(int(-1 * (event.delta / 120)), "units")


the_root_scroll.bind_all("<MouseWheel>", for_scroll_root)
frame_root_scroll = Frame(the_root_scroll, bg="#212121", borderwidth=0, highlightthickness=0)
the_root_scroll.create_window((0, 0), window=frame_root_scroll, anchor="nw")

back_ground = PhotoImage(file="background rectangle.png")
Label(frame_root_scroll, image=back_ground, borderwidth=0, bg="#212121").pack()


def button_prices():
    pass


# Entry Box
def entry_box():
    Label_Entry = Label(root_sedan, text=searching_data)
    Label_Entry.place(x=50, y=500)


# Functions for disabling the buttons
def sedan_button():
    root_sedan.destroy()  # close the popup
    button_sedan.config(state='normal')


def suv_button():
    root_suv.destroy()  # close the popup
    button_suv.config(state='normal')


def coupe_button():
    root_coupe.destroy()  # close the popup
    button_coupe.config(state='normal')


def convertible_button():
    root_convertible.destroy()  # close the popup
    button_convertible.config(state='normal')


def sports_button():
    root_sports.destroy()  # close the popup
    button_sports.config(state='normal')


def wagon_button():
    root_wagon.destroy()  # close the popup
    button_wagon.config(state='normal')


def hatchback_button():
    root_hatchback.destroy()  # close the popup
    button_hatchback.config(state='normal')


def minivan_button():
    root_minivan.destroy()  # close the popup
    button_minivan.config(state='normal')


def rent():
    window_rent = Toplevel(root)
    window_rent.geometry("450x350")
    window_rent.configure(bg="#212121")
    window_rent.resizable(False, False)
    window_rent.title("Rent Page")

    def button_day_command():
        root.after(3000, lambda: window_rent.destroy())
        button_day_label.config(text="Thank You for Renting")
        button_day.config(state="disabled")
        button_week.config(state="disabled")
        button_month.config(state="disabled")

    def button_week_command():
        window_rent.after(3000, lambda: window_rent.destroy())
        button_week_label.config(text="Thank You for Renting")
        button_day.config(state="disabled")
        button_month.config(state="disabled")

    def button_month_command():
        window_rent.after(3000, lambda: window_rent.destroy())
        button_month_label.config(text="Thank You for Renting")
        button_week.config(state="disabled")
        button_day.config(state="disabled")

    # Photos
    rent_day = PhotoImage(file="rent_for_day.png")
    rent_week = PhotoImage(file="rent_for_week.png")
    rent_month = PhotoImage(file="rent_for_month.png")

    button_day = Button(window_rent, image=rent_day, borderwidth=0, bg="#212121", activebackground="#212121",
                        cursor="hand2", command=button_day_command)
    button_week = Button(window_rent, image=rent_week, borderwidth=0, bg="#212121", activebackground="#212121",
                         cursor="hand2", command=button_week_command)
    button_month = Button(window_rent, image=rent_month, borderwidth=0, bg="#212121", activebackground="#212121",
                          cursor="hand2", command=button_month_command)

    button_day_label = Label(window_rent, bg="#212121", text="", fg="white", font="Helvetica, 15")
    button_week_label = Label(window_rent, bg="#212121", text="", fg="white", font="Helvetica, 15")
    button_month_label = Label(window_rent, bg="#212121", text="", fg="white", font="Helvetica, 15")

    button_day.image = rent_day
    button_week.image = rent_week
    button_month.image = rent_month

    button_day.grid(row=1, column=1, padx=80, pady=20)
    button_week.grid(row=2, column=1, padx=80, pady=20)
    button_month.grid(row=3, column=1, padx=80, pady=20)

    button_day_label.place(x=133, y=85)
    button_week_label.place(x=133, y=185)
    button_month_label.place(x=133, y=295)


# Functions For Car Buttons
def sedan():
    global root_sedan
    global button_sedan
    root_sedan = Toplevel(root)
    root_sedan.geometry("1920x1080")
    root_sedan.configure(bg="#212121")
    root_sedan.title("Sedan")
    root_sedan.resizable(True, True)
    button_sedan.config(state='disabled')
    root_sedan.protocol("WM_DELETE_WINDOW", sedan_button)
    orange = Frame(root_sedan, width=1920, height=100, bg="#FF6006")
    orange.pack()
    main_frame = Frame(root_sedan)
    main_frame.pack(fill=BOTH, expand=1)
    the_canvas = Canvas(main_frame, bg="#212121", borderwidth=0, highlightthickness=0)
    the_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar = Scrollbar(main_frame, orient=VERTICAL, command=the_canvas.yview)
    my_scrollbar.pack(side=RIGHT, fill=Y)
    the_canvas.configure(yscrollcommand=my_scrollbar.set)
    the_canvas.bind('<Configure>', lambda e: the_canvas.configure(scrollregion=the_canvas.bbox("all")))
    another_frame = Frame(the_canvas, bg="#212121", borderwidth=0, highlightthickness=0)
    the_canvas.create_window((0, 0), window=another_frame, anchor="nw")

    def for_scroll_sedan(event):
        the_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    the_canvas.bind_all("<MouseWheel>", for_scroll_sedan)
    another_frame = Frame(the_canvas, bg="#212121", borderwidth=0, highlightthickness=0)
    the_canvas.create_window((0, 0), window=another_frame, anchor="nw")

    # All the cars images
    audi_a4 = PhotoImage(file="./sedancars/audi.a4.sedan.png")
    cadi_cts = PhotoImage(file="./sedancars/cadillac.CTS.sedan.png")
    ho_ac = PhotoImage(file="./sedancars/honda.accord.sedan.png")
    ho_ci = PhotoImage(file="./sedancars/honda.city.sedan.png")
    hy_el = PhotoImage(file="./sedancars/hyundai.elantra.sedan.png")
    inf_q7 = PhotoImage(file="./sedancars/infiniti.q70.sedan.png")
    ja_xf = PhotoImage(file="./sedancars/jaguar.XF.sedan.png")
    kia_op = PhotoImage(file="./sedancars/kia.optima.sedan.png")
    mas_qua = PhotoImage(file="./sedancars/maserati.quattroporte.sedan.png")
    nis_alt = PhotoImage(file="./sedancars/nissan.altima.sedan.png")
    rol_ph = PhotoImage(file="./sedancars/rolls royce.phantom.sedan.png")
    rol_gh = PhotoImage(file="./sedancars/rollsroyce.ghost.sedan.png")
    tes_ms = PhotoImage(file="./sedancars/tesla.model s.sedan.png")
    toy_cam = PhotoImage(file="./sedancars/toyota.camry.sedan.png")
    toy_cor = PhotoImage(file="./sedancars/toyota.corolla.sedan.png")

    # All the cars labels
    audi_a4_label = Label(another_frame, image=audi_a4, bg="#212121", width=328, height=600)
    cadi_cts_label = Label(another_frame, image=cadi_cts, bg="#212121", width=328, height=600)
    ho_ac_label = Label(another_frame, image=ho_ac, bg="#212121", width=328, height=600)
    ho_ci_label = Label(another_frame, image=ho_ci, bg="#212121", width=328, height=600)
    hy_el_label = Label(another_frame, image=hy_el, bg="#212121", width=328, height=600)
    inf_q7_label = Label(another_frame, image=inf_q7, bg="#212121", width=328, height=600)
    ja_xf_label = Label(another_frame, image=ja_xf, bg="#212121", width=328, height=600)
    kia_op_label = Label(another_frame, image=kia_op, bg="#212121", width=328, height=600)
    mas_qua_label = Label(another_frame, image=mas_qua, bg="#212121", width=328, height=600)
    nis_alt_label = Label(another_frame, image=nis_alt, bg="#212121", width=328, height=600)
    rol_ph_label = Label(another_frame, image=rol_ph, bg="#212121", width=328, height=600)
    rol_gh_label = Label(another_frame, image=rol_gh, bg="#212121", width=328, height=600)
    tes_ms_label = Label(another_frame, image=tes_ms, bg="#212121", width=328, height=600)
    toy_cam_label = Label(another_frame, image=toy_cam, bg="#212121", width=328, height=600)
    toy_cor_label = Label(another_frame, image=toy_cor, bg="#212121", width=328, height=600)

    # All the cars references
    audi_a4_label.image = audi_a4
    cadi_cts_label.image = cadi_cts
    ho_ac_label.image = ho_ac
    ho_ci_label.image = ho_ci
    hy_el_label.image = hy_el
    inf_q7_label.image = inf_q7
    ja_xf_label.image = ja_xf
    kia_op_label.image = kia_op
    mas_qua_label.image = mas_qua
    nis_alt_label.image = nis_alt
    rol_ph_label.image = rol_ph
    rol_gh_label.image = rol_gh
    tes_ms_label.image = tes_ms
    toy_cam_label.image = toy_cam
    toy_cor_label.image = toy_cor

    # All the cars grid
    audi_a4_label.grid(row=2, column=1, padx=60, pady=20)
    cadi_cts_label.grid(row=2, column=2, padx=100, pady=20)
    ho_ac_label.grid(row=2, column=3, padx=60, pady=20)
    ho_ci_label.grid(row=2, column=4, padx=100, pady=20)
    hy_el_label.grid(row=3, column=1, padx=60, pady=20)
    inf_q7_label.grid(row=3, column=2, padx=60, pady=20)
    ja_xf_label.grid(row=3, column=3, padx=60, pady=20)
    kia_op_label.grid(row=3, column=4, padx=60, pady=20)
    mas_qua_label.grid(row=4, column=1, padx=60, pady=20)
    nis_alt_label.grid(row=4, column=2, padx=60, pady=20)
    rol_ph_label.grid(row=4, column=3, padx=60, pady=20)
    rol_gh_label.grid(row=4, column=4, padx=60, pady=20)
    tes_ms_label.grid(row=5, column=1, padx=60, pady=20)
    toy_cam_label.grid(row=5, column=2, padx=60, pady=20)
    toy_cor_label.grid(row=5, column=3, padx=60, pady=20)

    # buttock
    audi_a4 = PhotoImage(file="./allthebuttons/rent.png")
    cadi_cts = PhotoImage(file="./allthebuttons/rent.png")
    ho_ac = PhotoImage(file="./allthebuttons/rent.png")
    ho_ci = PhotoImage(file="./allthebuttons/rent.png")
    hy_el = PhotoImage(file="./allthebuttons/rent.png")
    inf_q7 = PhotoImage(file="./allthebuttons/rent.png")
    ja_xf = PhotoImage(file="./allthebuttons/rent.png")
    kia_op = PhotoImage(file="./allthebuttons/rent.png")
    mas_qua = PhotoImage(file="./allthebuttons/rent.png")
    nis_alt = PhotoImage(file="./allthebuttons/rent.png")
    rol_ph = PhotoImage(file="./allthebuttons/rent.png")
    rol_gh = PhotoImage(file="./allthebuttons/rent.png")
    tes_ms = PhotoImage(file="./allthebuttons/rent.png")
    toy_cam = PhotoImage(file="./allthebuttons/rent.png")
    toy_cor = PhotoImage(file="./allthebuttons/rent.png")

    # butt
    audi_a4_rent = Button(another_frame, image=audi_a4, borderwidth=0, bg="#333232", activebackground="#333232",
                          width=70, height=98, cursor="hand2", command=rent)
    cadi_cts_rent = Button(another_frame, image=cadi_cts, borderwidth=0, bg="#333232", activebackground="#333232",
                           width=70, height=98, cursor="hand2", command=rent)
    ho_ac_rent = Button(another_frame, image=ho_ac, borderwidth=0, bg="#333232", activebackground="#333232", width=70,
                        height=98, cursor="hand2", command=rent)
    ho_ci_rent = Button(another_frame, image=ho_ci, borderwidth=0, bg="#333232", activebackground="#333232", width=70,
                        height=98, cursor="hand2", command=rent)
    hy_el_rent = Button(another_frame, image=hy_el, borderwidth=0, bg="#333232", activebackground="#333232", width=70,
                        height=98, cursor="hand2", command=rent)
    inf_q7_rent = Button(another_frame, image=inf_q7, borderwidth=0, bg="#333232", activebackground="#333232", width=70,
                         height=98, cursor="hand2", command=rent)
    ja_xf_rent = Button(another_frame, image=ja_xf, borderwidth=0, bg="#333232", activebackground="#333232", width=70,
                        height=98, cursor="hand2", command=rent)
    kia_op_rent = Button(another_frame, image=kia_op, borderwidth=0, bg="#333232", activebackground="#333232", width=70,
                         height=98, cursor="hand2", command=rent)
    mas_qua_rent = Button(another_frame, image=mas_qua, borderwidth=0, bg="#333232", activebackground="#333232",
                          width=70, height=98, cursor="hand2", command=rent)
    nis_alt_rent = Button(another_frame, image=nis_alt, borderwidth=0, bg="#333232", activebackground="#333232",
                          width=70, height=98, cursor="hand2", command=rent)
    rol_ph_rent = Button(another_frame, image=rol_ph, borderwidth=0, bg="#333232", activebackground="#333232", width=70,
                         height=98, cursor="hand2", command=rent)
    rol_gh_rent = Button(another_frame, image=rol_gh, borderwidth=0, bg="#333232", activebackground="#333232", width=70,
                         height=98, cursor="hand2", command=rent)
    tes_ms_rent = Button(another_frame, image=tes_ms, borderwidth=0, bg="#333232", activebackground="#333232", width=70,
                         height=98, cursor="hand2", command=rent)
    toy_cam_rent = Button(another_frame, image=toy_cam, borderwidth=0, bg="#333232", activebackground="#333232",
                          width=70, height=98, cursor="hand2", command=rent)
    toy_cor_rent = Button(another_frame, image=toy_cor, borderwidth=0, bg="#333232", activebackground="#333232",
                          width=70, height=98, cursor="hand2", command=rent)

    # refree
    audi_a4_rent.image = audi_a4
    cadi_cts_rent.image = cadi_cts
    ho_ac_rent.image = ho_ac
    ho_ci_rent.image = ho_ci
    hy_el_rent.image = hy_el
    inf_q7_rent.image = inf_q7
    ja_xf_rent.image = ja_xf
    kia_op_rent.image = kia_op
    mas_qua_rent.image = mas_qua
    nis_alt_rent.image = nis_alt
    rol_ph_rent.image = rol_ph
    rol_gh_rent.image = rol_gh
    tes_ms_rent.image = tes_ms
    toy_cam_rent.image = toy_cam
    toy_cor_rent.image = toy_cor

    # greenbutt
    audi_a4_rent.place(x=190, y=470)
    cadi_cts_rent.place(x=685, y=470)
    ho_ac_rent.place(x=1172, y=470)
    ho_ci_rent.place(x=1665, y=470)
    hy_el_rent.place(x=190, y=1115)
    inf_q7_rent.place(x=685, y=1115)
    ja_xf_rent.place(x=1172, y=1115)
    kia_op_rent.place(x=1665, y=1115)
    mas_qua_rent.place(x=190, y=1760)
    nis_alt_rent.place(x=685, y=1760)
    rol_ph_rent.place(x=1172, y=1760)
    rol_gh_rent.place(x=1665, y=1760)
    tes_ms_rent.place(x=190, y=2405)
    toy_cam_rent.place(x=685, y=2405)
    toy_cor_rent.place(x=1172, y=2405)


def suv():
    global root_suv
    global button_suv
    root_suv = Toplevel(root)
    root_suv.geometry("1920x1080")
    root_suv.configure(bg="#212121")
    root_suv.title("SUV")
    root_suv.resizable(True, True)
    button_suv.config(state='disabled')
    root_suv.protocol("WM_DELETE_WINDOW", suv_button)
    orange = Frame(root_suv, width=1920, height=100, bg="#FF6006")
    orange.pack()
    the_canvas_suv = Canvas(root_suv, bg="#212121", borderwidth=0, highlightthickness=0)
    the_canvas_suv.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar_suv = Scrollbar(root_suv, orient=VERTICAL, command=the_canvas_suv.yview)
    my_scrollbar_suv.pack(side=RIGHT, fill=Y)
    the_canvas_suv.configure(yscrollcommand=my_scrollbar_suv.set)
    the_canvas_suv.bind('<Configure>', lambda e: the_canvas_suv.configure(scrollregion=the_canvas_suv.bbox("all")))
    another_frame_suv = Frame(the_canvas_suv, bg="#212121", borderwidth=0, highlightthickness=0)
    the_canvas_suv.create_window((0, 0), window=another_frame_suv, anchor="nw")

    def for_scroll_suv(event):
        the_canvas_suv.yview_scroll(int(-1 * (event.delta / 120)), "units")

    the_canvas_suv.bind_all("<MouseWheel>", for_scroll_suv)
    another_frame_suv = Frame(the_canvas_suv, bg="#212121", borderwidth=0, highlightthickness=0)
    the_canvas_suv.create_window((0, 0), window=another_frame_suv, anchor="nw")

    audi_q8_suv = PhotoImage(file="./suvcars/audi.q8.suv.png")
    bmw_X6_suv = PhotoImage(file="./suvcars/bmw.X6.suv.png")
    cadillac_XT6_suv = PhotoImage(file="./suvcars/cadillac.XT6.suv.png")
    honda_crv_suv = PhotoImage(file="./suvcars/honda.crv.suv.png")
    infiniti_qx80_suv = PhotoImage(file="./suvcars/infiniti.qx80.suv.png")
    infinti_qx30_suv = PhotoImage(file="./suvcars/infinti.qx30.suv.png")
    kia_sportage_suv = PhotoImage(file="./suvcars/kia.sportage.suv.png")
    lamborghini_urus_suv = PhotoImage(file="./suvcars/lamborghini.urus.suv.png")
    landrover_rangerover_suv = PhotoImage(file="./suvcars/landrover.rangerover.suv.png")
    mazda_cx30_suv = PhotoImage(file="./suvcars/mazda.cx30.suv.png")
    mercedes_g63_suv = PhotoImage(file="./suvcars/mercedes.g63.suv.png")
    nissan_patrol_suv = PhotoImage(file="./suvcars/nissan.patrol.suv.png")
    porsche_cayenne_suv = PhotoImage(file="./suvcars/porsche.cayenne.suv.png")
    tesla_modelx_suv = PhotoImage(file="./suvcars/tesla.modelx.suv.png")
    toyota_fortuner_suv = PhotoImage(file="./suvcars/toyota.fortuner.suv.png")
    toyota_landcruiser_suv = PhotoImage(file="./suvcars/toyota.landcruiser.suv.png")
    toyota_pradao_suv = PhotoImage(file="./suvcars/toyota.pradao.suv.png")
    toyota_rav4_suv = PhotoImage(file="./suvcars/toyota.rav4.suv.png")

    audi_q8_suv_label = Label(another_frame_suv, image=audi_q8_suv, bg='#212121', width=328, height=600)
    bmw_X6_suv_label = Label(another_frame_suv, image=bmw_X6_suv, bg='#212121', width=328, height=600)
    cadillac_XT6_suv_label = Label(another_frame_suv, image=cadillac_XT6_suv, bg='#212121', width=328, height=600)
    honda_crv_suv_label = Label(another_frame_suv, image=honda_crv_suv, bg='#212121', width=328, height=600)
    infiniti_qx80_suv_label = Label(another_frame_suv, image=infiniti_qx80_suv, bg='#212121', width=328, height=600)
    infinti_qx30_suv_label = Label(another_frame_suv, image=infinti_qx30_suv, bg='#212121', width=328, height=600)
    kia_sportage_suv_label = Label(another_frame_suv, image=kia_sportage_suv, bg='#212121', width=328, height=600)
    lamborghini_urus_suv_label = Label(another_frame_suv, image=lamborghini_urus_suv, bg='#212121', width=328,
                                       height=600)
    landrover_rangerover_suv_label = Label(another_frame_suv, image=landrover_rangerover_suv, bg='#212121', width=328,
                                           height=600)
    mazda_cx30_suv_label = Label(another_frame_suv, image=mazda_cx30_suv, bg='#212121', width=328, height=600)
    mercedes_g63_suv_label = Label(another_frame_suv, image=mercedes_g63_suv, bg='#212121', width=328, height=600)
    nissan_patrol_suv_label = Label(another_frame_suv, image=nissan_patrol_suv, bg='#212121', width=328, height=600)
    porsche_cayenne_suv_label = Label(another_frame_suv, image=porsche_cayenne_suv, bg='#212121', width=328, height=600)
    tesla_modelx_suv_label = Label(another_frame_suv, image=tesla_modelx_suv, bg='#212121', width=328, height=600)
    toyota_fortuner_suv_label = Label(another_frame_suv, image=toyota_fortuner_suv, bg='#212121', width=328, height=600)
    toyota_landcruiser_suv_label = Label(another_frame_suv, image=toyota_landcruiser_suv, bg='#212121', width=328,
                                         height=600)
    toyota_pradao_suv_label = Label(another_frame_suv, image=toyota_pradao_suv, bg='#212121', width=328, height=600)
    toyota_rav4_suv_label = Label(another_frame_suv, image=toyota_rav4_suv, bg='#212121', width=328, height=600)

    audi_q8_suv_label.image = audi_q8_suv
    bmw_X6_suv_label.image = bmw_X6_suv
    cadillac_XT6_suv_label.image = cadillac_XT6_suv
    honda_crv_suv_label.image = honda_crv_suv
    infiniti_qx80_suv_label.image = infiniti_qx80_suv
    infinti_qx30_suv_label.image = infinti_qx30_suv
    kia_sportage_suv_label.image = kia_sportage_suv
    lamborghini_urus_suv_label.image = lamborghini_urus_suv
    landrover_rangerover_suv_label.image = landrover_rangerover_suv
    mazda_cx30_suv_label.image = mazda_cx30_suv
    mercedes_g63_suv_label.image = mercedes_g63_suv
    nissan_patrol_suv_label.image = nissan_patrol_suv
    porsche_cayenne_suv_label.image = porsche_cayenne_suv
    tesla_modelx_suv_label.image = tesla_modelx_suv
    toyota_fortuner_suv_label.image = toyota_fortuner_suv
    toyota_landcruiser_suv_label.image = toyota_landcruiser_suv
    toyota_pradao_suv_label.image = toyota_pradao_suv
    toyota_rav4_suv_label.image = toyota_rav4_suv

    audi_q8_suv_label.grid(row=2, column=1, padx=60, pady=20)
    bmw_X6_suv_label.grid(row=2, column=2, padx=100, pady=20)
    cadillac_XT6_suv_label.grid(row=2, column=3, padx=60, pady=20)
    honda_crv_suv_label.grid(row=2, column=4, padx=100, pady=20)
    infiniti_qx80_suv_label.grid(row=3, column=1, padx=60, pady=20)
    infinti_qx30_suv_label.grid(row=3, column=2, padx=60, pady=20)
    kia_sportage_suv_label.grid(row=3, column=3, padx=60, pady=20)
    lamborghini_urus_suv_label.grid(row=3, column=4, padx=60, pady=20)
    landrover_rangerover_suv_label.grid(row=4, column=1, padx=60, pady=20)
    mazda_cx30_suv_label.grid(row=4, column=2, padx=60, pady=20)
    mercedes_g63_suv_label.grid(row=4, column=3, padx=60, pady=20)
    nissan_patrol_suv_label.grid(row=4, column=4, padx=60, pady=20)
    porsche_cayenne_suv_label.grid(row=5, column=1, padx=60, pady=20)
    tesla_modelx_suv_label.grid(row=5, column=2, padx=60, pady=20)
    toyota_fortuner_suv_label.grid(row=5, column=3, padx=60, pady=20)
    toyota_landcruiser_suv_label.grid(row=5, column=4, padx=60, pady=20)
    toyota_pradao_suv_label.grid(row=6, column=1, padx=60, pady=20)
    toyota_rav4_suv_label.grid(row=6, column=2, padx=60, pady=20)

    audi_q8_suv_button = PhotoImage(file='./allthebuttons/rent.png')
    bmw_X6_suv_button = PhotoImage(file='./allthebuttons/rent.png')
    cadillac_XT6_suv_button = PhotoImage(file='./allthebuttons/rent.png')
    honda_crv_suv_button = PhotoImage(file='./allthebuttons/rent.png')
    infiniti_qx80_suv_button = PhotoImage(file='./allthebuttons/rent.png')
    infinti_qx30_suv_button = PhotoImage(file='./allthebuttons/rent.png')
    kia_sportage_suv_button = PhotoImage(file='./allthebuttons/rent.png')
    lamborghini_urus_suv_button = PhotoImage(file='./allthebuttons/rent.png')
    landrover_rangerover_suv_button = PhotoImage(file='./allthebuttons/rent.png')
    mazda_cx30_suv_button = PhotoImage(file='./allthebuttons/rent.png')
    mercedes_g63_suv_button = PhotoImage(file='./allthebuttons/rent.png')
    nissan_patrol_suv_button = PhotoImage(file='./allthebuttons/rent.png')
    porsche_cayenne_suv_button = PhotoImage(file='./allthebuttons/rent.png')
    tesla_modelx_suv_button = PhotoImage(file='./allthebuttons/rent.png')
    toyota_fortuner_suv_button = PhotoImage(file='./allthebuttons/rent.png')
    toyota_landcruiser_suv_button = PhotoImage(file='./allthebuttons/rent.png')
    toyota_pradao_suv_button = PhotoImage(file='./allthebuttons/rent.png')
    toyota_rav4_suv_button = PhotoImage(file='./allthebuttons/rent.png')

    audi_q8_suv_rent = Button(another_frame_suv, image=audi_q8_suv_button, borderwidth=0, bg='#333232',
                              activebackground='#333232', width=70, height=98, cursor='hand2', command=rent)
    bmw_X6_suv_rent = Button(another_frame_suv, image=bmw_X6_suv_button, borderwidth=0, bg='#333232',
                             activebackground='#333232', width=70, height=98, cursor='hand2', command=rent)
    cadillac_XT6_suv_rent = Button(another_frame_suv, image=cadillac_XT6_suv_button, borderwidth=0, bg='#333232',
                                   activebackground='#333232', width=70, height=98, cursor='hand2', command=rent)
    honda_crv_suv_rent = Button(another_frame_suv, image=honda_crv_suv_button, borderwidth=0, bg='#333232',
                                activebackground='#333232', width=70, height=98, cursor='hand2', command=rent)
    infiniti_qx80_suv_rent = Button(another_frame_suv, image=infiniti_qx80_suv_button, borderwidth=0, bg='#333232',
                                    activebackground='#333232', width=70, height=98, cursor='hand2', command=rent)
    infinti_qx30_suv_rent = Button(another_frame_suv, image=infinti_qx30_suv_button, borderwidth=0, bg='#333232',
                                   activebackground='#333232', width=70, height=98, cursor='hand2', command=rent)
    kia_sportage_suv_rent = Button(another_frame_suv, image=kia_sportage_suv_button, borderwidth=0, bg='#333232',
                                   activebackground='#333232', width=70, height=98, cursor='hand2', command=rent)
    lamborghini_urus_suv_rent = Button(another_frame_suv, image=lamborghini_urus_suv_button, borderwidth=0,
                                       bg='#333232', activebackground='#333232', width=70, height=98, cursor='hand2',
                                       command=rent)
    landrover_rangerover_suv_rent = Button(another_frame_suv, image=landrover_rangerover_suv_button, borderwidth=0,
                                           bg='#333232', activebackground='#333232', width=70, height=98,
                                           cursor='hand2', command=rent)
    mazda_cx30_suv_rent = Button(another_frame_suv, image=mazda_cx30_suv_button, borderwidth=0, bg='#333232',
                                 activebackground='#333232', width=70, height=98, cursor='hand2', command=rent)
    mercedes_g63_suv_rent = Button(another_frame_suv, image=mercedes_g63_suv_button, borderwidth=0, bg='#333232',
                                   activebackground='#333232', width=70, height=98, cursor='hand2', command=rent)
    nissan_patrol_suv_rent = Button(another_frame_suv, image=nissan_patrol_suv_button, borderwidth=0, bg='#333232',
                                    activebackground='#333232', width=70, height=98, cursor='hand2', command=rent)
    porsche_cayenne_suv_rent = Button(another_frame_suv, image=porsche_cayenne_suv_button, borderwidth=0, bg='#333232',
                                      activebackground='#333232', width=70, height=98, cursor='hand2', command=rent)
    tesla_modelx_suv_rent = Button(another_frame_suv, image=tesla_modelx_suv_button, borderwidth=0, bg='#333232',
                                   activebackground='#333232', width=70, height=98, cursor='hand2', command=rent)
    toyota_fortuner_suv_rent = Button(another_frame_suv, image=toyota_fortuner_suv_button, borderwidth=0, bg='#333232',
                                      activebackground='#333232', width=70, height=98, cursor='hand2', command=rent)
    toyota_landcruiser_suv_rent = Button(another_frame_suv, image=toyota_landcruiser_suv_button, borderwidth=0,
                                         bg='#333232', activebackground='#333232', width=70, height=98, cursor='hand2',
                                         command=rent)
    toyota_pradao_suv_rent = Button(another_frame_suv, image=toyota_pradao_suv_button, borderwidth=0, bg='#333232',
                                    activebackground='#333232', width=70, height=98, cursor='hand2', command=rent)
    toyota_rav4_suv_rent = Button(another_frame_suv, image=toyota_rav4_suv_button, borderwidth=0, bg='#333232',
                                  activebackground='#333232', width=70, height=98, cursor='hand2', command=rent)

    audi_q8_suv_rent.image = audi_q8_suv_button
    bmw_X6_suv_rent.image = bmw_X6_suv_button
    cadillac_XT6_suv_rent.image = cadillac_XT6_suv_button
    honda_crv_suv_rent.image = honda_crv_suv_button
    infiniti_qx80_suv_rent.image = infiniti_qx80_suv_button
    infinti_qx30_suv_rent.image = infinti_qx30_suv_button
    kia_sportage_suv_rent.image = kia_sportage_suv_button
    lamborghini_urus_suv_rent.image = lamborghini_urus_suv_button
    landrover_rangerover_suv_rent.image = landrover_rangerover_suv_button
    mazda_cx30_suv_rent.image = mazda_cx30_suv_button
    mercedes_g63_suv_rent.image = mercedes_g63_suv_button
    nissan_patrol_suv_rent.image = nissan_patrol_suv_button
    porsche_cayenne_suv_rent.image = porsche_cayenne_suv_button
    tesla_modelx_suv_rent.image = tesla_modelx_suv_button
    toyota_fortuner_suv_rent.image = toyota_fortuner_suv_button
    toyota_landcruiser_suv_rent.image = toyota_landcruiser_suv_button
    toyota_pradao_suv_rent.image = toyota_pradao_suv_button
    toyota_rav4_suv_rent.image = toyota_rav4_suv_button

    audi_q8_suv_rent.place(x=190, y=470)
    bmw_X6_suv_rent.place(x=685, y=470)
    cadillac_XT6_suv_rent.place(x=1172, y=470)
    honda_crv_suv_rent.place(x=1665, y=470)
    infiniti_qx80_suv_rent.place(x=190, y=1115)
    infinti_qx30_suv_rent.place(x=685, y=1115)
    kia_sportage_suv_rent.place(x=1172, y=1115)
    lamborghini_urus_suv_rent.place(x=1665, y=1115)
    landrover_rangerover_suv_rent.place(x=190, y=1760)
    mazda_cx30_suv_rent.place(x=685, y=1760)
    mercedes_g63_suv_rent.place(x=1172, y=1760)
    nissan_patrol_suv_rent.place(x=1665, y=1760)
    porsche_cayenne_suv_rent.place(x=190, y=2410)
    tesla_modelx_suv_rent.place(x=685, y=2410)
    toyota_fortuner_suv_rent.place(x=1172, y=2410)
    toyota_landcruiser_suv_rent.place(x=1665, y=2410)
    toyota_pradao_suv_rent.place(x=190, y=3060)
    toyota_rav4_suv_rent.place(x=685, y=3060)


def coupe():
    global root_coupe
    global button_coupe
    root_coupe = Toplevel(root)
    root_coupe.geometry("1920x1080")
    root_coupe.configure(bg="#212121")
    root_coupe.title("Coupe")
    root_coupe.resizable(True, True)
    button_coupe.config(state='disabled')
    root_coupe.protocol("WM_DELETE_WINDOW", coupe_button)
    orange = Frame(root_coupe, width=1920, height=100, bg="#FF6006")
    orange.pack()
    the_canvas_coupe = Canvas(root_coupe, bg="#212121", borderwidth=0, highlightthickness=0)
    the_canvas_coupe.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar_coupe = Scrollbar(root_coupe, orient=VERTICAL, command=the_canvas_coupe.yview)
    my_scrollbar_coupe.pack(side=RIGHT, fill=Y)
    the_canvas_coupe.configure(yscrollcommand=my_scrollbar_coupe.set)
    the_canvas_coupe.bind('<Configure>',
                          lambda e: the_canvas_coupe.configure(scrollregion=the_canvas_coupe.bbox("all")))
    another_frame_coupe = Frame(the_canvas_coupe, bg="#212121", borderwidth=0, highlightthickness=0)
    the_canvas_coupe.create_window((0, 0), window=another_frame_coupe, anchor="nw")

    def for_scroll_coupe(event):
        the_canvas_coupe.yview_scroll(int(-1 * (event.delta / 120)), "units")

    the_canvas_coupe.bind_all("<MouseWheel>", for_scroll_coupe)
    another_frame_coupe = Frame(the_canvas_coupe, bg="#212121", borderwidth=0, highlightthickness=0)
    the_canvas_coupe.create_window((0, 0), window=another_frame_coupe, anchor="nw")

    # All the cars images
    astonmartin_DB11_coupe = PhotoImage(file="./coupecars/astonmartin.DB11.coupe.png")
    astonmartin_vantage_coupe = PhotoImage(file="./coupecars/astonmartin.vantage.coupe.png")
    audi_tt_coupe = PhotoImage(file="./coupecars/audi.tt.coupe.png")
    bentley_continental_coupe = PhotoImage(file="./coupecars/bentley.continental.coupe.png")
    bmw_650i_coupe = PhotoImage(file="./coupecars/bmw.650i.coupe.png")
    bmw_i8_coupe = PhotoImage(file="./coupecars/bmw.i8.coupe.png")
    cadillac_ats_v_coupe = PhotoImage(file="./coupecars/cadillac.ats-v.coupe.png")
    chevrolet_camaro_coupe = PhotoImage(file="./coupecars/chevrolet.camaro.coupe.png")
    dodge_challenger_coupe = PhotoImage(file="./coupecars/dodge.challenger.coupe.png")
    ford_mustang_coupe = PhotoImage(file="./coupecars/ford.mustang.coupe.png")
    jaguar_f_type_coupe = PhotoImage(file="./coupecars/jaguar.f-type.coupe.png")
    lotus_evora_coupe = PhotoImage(file="./coupecars/lotus.evora.coupe.png")
    maserati_granturismo_coupe = PhotoImage(file="./coupecars/maserati.granturismo.coupe.png")
    McLaren_720s_coupe = PhotoImage(file="./coupecars/McLaren.720s.coupe.png")
    mercedes_amg_gt_coupe = PhotoImage(file="./coupecars/mercedes.amg-gt.coupe.png")
    mercedes_c43_coupe = PhotoImage(file="./coupecars/mercedes.c43.coupe.png")
    nissan_370z_coupe = PhotoImage(file="./coupecars/nissan.370z.coupe.png")
    subaru_brz_coupe = PhotoImage(file="./coupecars/subaru.brz.coupe.png")
    toyota_86_coupe = PhotoImage(file="./coupecars/toyota.86.coupe.png")
    toyota_supra_coupe = PhotoImage(file="./coupecars/toyota.supra.coupe.png")

    # All the cars labels
    astonmartin_DB11_coupe_label = Label(another_frame_coupe, image=astonmartin_DB11_coupe, bg='#212121', width=328,
                                         height=600)
    astonmartin_vantage_coupe_label = Label(another_frame_coupe, image=astonmartin_vantage_coupe, bg='#212121',
                                            width=328, height=600)
    audi_tt_coupe_label = Label(another_frame_coupe, image=audi_tt_coupe, bg='#212121', width=328, height=600)
    bentley_continental_coupe_label = Label(another_frame_coupe, image=bentley_continental_coupe, bg='#212121',
                                            width=328, height=600)
    bmw_650i_coupe_label = Label(another_frame_coupe, image=bmw_650i_coupe, bg='#212121', width=328, height=600)
    bmw_i8_coupe_label = Label(another_frame_coupe, image=bmw_i8_coupe, bg='#212121', width=328, height=600)
    cadillac_ats_v_coupe_label = Label(another_frame_coupe, image=cadillac_ats_v_coupe, bg='#212121', width=328,
                                       height=600)
    chevrolet_camaro_coupe_label = Label(another_frame_coupe, image=chevrolet_camaro_coupe, bg='#212121', width=328,
                                         height=600)
    dodge_challenger_coupe_label = Label(another_frame_coupe, image=dodge_challenger_coupe, bg='#212121', width=328,
                                         height=600)
    ford_mustang_coupe_label = Label(another_frame_coupe, image=ford_mustang_coupe, bg='#212121', width=328, height=600)
    jaguar_f_type_coupe_label = Label(another_frame_coupe, image=jaguar_f_type_coupe, bg='#212121', width=328,
                                      height=600)
    lotus_evora_coupe_label = Label(another_frame_coupe, image=lotus_evora_coupe, bg='#212121', width=328, height=600)
    maserati_granturismo_coupe_label = Label(another_frame_coupe, image=maserati_granturismo_coupe, bg='#212121',
                                             width=328, height=600)
    McLaren_720s_coupe_label = Label(another_frame_coupe, image=McLaren_720s_coupe, bg='#212121', width=328, height=600)
    mercedes_amg_gt_coupe_label = Label(another_frame_coupe, image=mercedes_amg_gt_coupe, bg='#212121', width=328,
                                        height=600)
    mercedes_c43_coupe_label = Label(another_frame_coupe, image=mercedes_c43_coupe, bg='#212121', width=328, height=600)
    nissan_370z_coupe_label = Label(another_frame_coupe, image=nissan_370z_coupe, bg='#212121', width=328, height=600)
    subaru_brz_coupe_label = Label(another_frame_coupe, image=subaru_brz_coupe, bg='#212121', width=328, height=600)
    toyota_86_coupe_label = Label(another_frame_coupe, image=toyota_86_coupe, bg='#212121', width=328, height=600)
    toyota_supra_coupe_label = Label(another_frame_coupe, image=toyota_supra_coupe, bg='#212121', width=328, height=600)

    # All the cars referenced
    astonmartin_DB11_coupe_label.image = astonmartin_DB11_coupe
    astonmartin_vantage_coupe_label.image = astonmartin_vantage_coupe
    audi_tt_coupe_label.image = audi_tt_coupe
    bentley_continental_coupe_label.image = bentley_continental_coupe
    bmw_650i_coupe_label.image = bmw_650i_coupe
    bmw_i8_coupe_label.image = bmw_i8_coupe
    cadillac_ats_v_coupe_label.image = cadillac_ats_v_coupe
    chevrolet_camaro_coupe_label.image = chevrolet_camaro_coupe
    dodge_challenger_coupe_label.image = dodge_challenger_coupe
    ford_mustang_coupe_label.image = ford_mustang_coupe
    jaguar_f_type_coupe_label.image = jaguar_f_type_coupe
    lotus_evora_coupe_label.image = lotus_evora_coupe
    maserati_granturismo_coupe_label.image = maserati_granturismo_coupe
    McLaren_720s_coupe_label.image = McLaren_720s_coupe
    mercedes_amg_gt_coupe_label.image = mercedes_amg_gt_coupe
    mercedes_c43_coupe_label.image = mercedes_c43_coupe
    nissan_370z_coupe_label.image = nissan_370z_coupe
    subaru_brz_coupe_label.image = subaru_brz_coupe
    toyota_86_coupe_label.image = toyota_86_coupe
    toyota_supra_coupe_label.image = toyota_supra_coupe

    # All the cars grid
    astonmartin_DB11_coupe_label.grid(row=2, column=1, padx=60, pady=20)
    astonmartin_vantage_coupe_label.grid(row=2, column=2, padx=100, pady=20)
    audi_tt_coupe_label.grid(row=2, column=3, padx=60, pady=20)
    bentley_continental_coupe_label.grid(row=2, column=4, padx=100, pady=20)
    bmw_650i_coupe_label.grid(row=3, column=1, padx=60, pady=20)
    bmw_i8_coupe_label.grid(row=3, column=2, padx=60, pady=20)
    cadillac_ats_v_coupe_label.grid(row=3, column=3, padx=60, pady=20)
    chevrolet_camaro_coupe_label.grid(row=3, column=4, padx=60, pady=20)
    dodge_challenger_coupe_label.grid(row=4, column=1, padx=60, pady=20)
    ford_mustang_coupe_label.grid(row=4, column=2, padx=60, pady=20)
    jaguar_f_type_coupe_label.grid(row=4, column=3, padx=60, pady=20)
    lotus_evora_coupe_label.grid(row=4, column=4, padx=60, pady=20)
    maserati_granturismo_coupe_label.grid(row=5, column=1, padx=60, pady=20)
    McLaren_720s_coupe_label.grid(row=5, column=2, padx=60, pady=20)
    mercedes_amg_gt_coupe_label.grid(row=5, column=3, padx=60, pady=20)
    mercedes_c43_coupe_label.grid(row=5, column=4, padx=60, pady=20)
    nissan_370z_coupe_label.grid(row=6, column=1, padx=60, pady=20)
    subaru_brz_coupe_label.grid(row=6, column=2, padx=60, pady=20)
    toyota_86_coupe_label.grid(row=6, column=3, padx=60, pady=20)
    toyota_supra_coupe_label.grid(row=6, column=4, padx=60, pady=20)

    # All the button images
    astonmartin_DB11_coupe_button = PhotoImage(file='./allthebuttons/rent.png')
    astonmartin_vantage_coupe_button = PhotoImage(file='./allthebuttons/rent.png')
    audi_tt_coupe_button = PhotoImage(file='./allthebuttons/rent.png')
    bentley_continental_coupe_button = PhotoImage(file='./allthebuttons/rent.png')
    bmw_650i_coupe_button = PhotoImage(file='./allthebuttons/rent.png')
    bmw_i8_coupe_button = PhotoImage(file='./allthebuttons/rent.png')
    cadillac_ats_v_coupe_button = PhotoImage(file='./allthebuttons/rent.png')
    chevrolet_camaro_coupe_button = PhotoImage(file='./allthebuttons/rent.png')
    dodge_challenger_coupe_button = PhotoImage(file='./allthebuttons/rent.png')
    ford_mustang_coupe_button = PhotoImage(file='./allthebuttons/rent.png')
    jaguar_f_type_coupe_button = PhotoImage(file='./allthebuttons/rent.png')
    lotus_evora_coupe_button = PhotoImage(file='./allthebuttons/rent.png')
    maserati_granturismo_coupe_button = PhotoImage(file='./allthebuttons/rent.png')
    McLaren_720s_coupe_button = PhotoImage(file='./allthebuttons/rent.png')
    mercedes_amg_gt_coupe_button = PhotoImage(file='./allthebuttons/rent.png')
    mercedes_c43_coupe_button = PhotoImage(file='./allthebuttons/rent.png')
    nissan_370z_coupe_button = PhotoImage(file='./allthebuttons/rent.png')
    subaru_brz_coupe_button = PhotoImage(file='./allthebuttons/rent.png')
    toyota_86_coupe_button = PhotoImage(file='./allthebuttons/rent.png')
    toyota_supra_coupe_button = PhotoImage(file='./allthebuttons/rent.png')

    # All the buttons
    astonmartin_DB11_coupe_rent = Button(another_frame_coupe, image=astonmartin_DB11_coupe_button, borderwidth=0,
                                         bg='#333232', activebackground='#333232', width=70, height=98, cursor='hand2',
                                         command=rent)
    astonmartin_vantage_coupe_rent = Button(another_frame_coupe, image=astonmartin_vantage_coupe_button, borderwidth=0,
                                            bg='#333232', activebackground='#333232', width=70, height=98,
                                            cursor='hand2', command=rent)
    audi_tt_coupe_rent = Button(another_frame_coupe, image=audi_tt_coupe_button, borderwidth=0, bg='#333232',
                                activebackground='#333232', width=70, height=98, cursor='hand2', command=rent)
    bentley_continental_coupe_rent = Button(another_frame_coupe, image=bentley_continental_coupe_button, borderwidth=0,
                                            bg='#333232', activebackground='#333232', width=70, height=98,
                                            cursor='hand2', command=rent)
    bmw_650i_coupe_rent = Button(another_frame_coupe, image=bmw_650i_coupe_button, borderwidth=0, bg='#333232',
                                 activebackground='#333232', width=70, height=98, cursor='hand2', command=rent)
    bmw_i8_coupe_rent = Button(another_frame_coupe, image=bmw_i8_coupe_button, borderwidth=0, bg='#333232',
                               activebackground='#333232', width=70, height=98, cursor='hand2', command=rent)
    cadillac_ats_v_coupe_rent = Button(another_frame_coupe, image=cadillac_ats_v_coupe_button, borderwidth=0,
                                       bg='#333232', activebackground='#333232', width=70, height=98, cursor='hand2',
                                       command=rent)
    chevrolet_camaro_coupe_rent = Button(another_frame_coupe, image=chevrolet_camaro_coupe_button, borderwidth=0,
                                         bg='#333232', activebackground='#333232', width=70, height=98, cursor='hand2',
                                         command=rent)
    dodge_challenger_coupe_rent = Button(another_frame_coupe, image=dodge_challenger_coupe_button, borderwidth=0,
                                         bg='#333232', activebackground='#333232', width=70, height=98, cursor='hand2',
                                         command=rent)
    ford_mustang_coupe_rent = Button(another_frame_coupe, image=ford_mustang_coupe_button, borderwidth=0, bg='#333232',
                                     activebackground='#333232', width=70, height=98, cursor='hand2', command=rent)
    jaguar_f_type_coupe_rent = Button(another_frame_coupe, image=jaguar_f_type_coupe_button, borderwidth=0,
                                      bg='#333232', activebackground='#333232', width=70, height=98, cursor='hand2',
                                      command=rent)
    lotus_evora_coupe_rent = Button(another_frame_coupe, image=lotus_evora_coupe_button, borderwidth=0, bg='#333232',
                                    activebackground='#333232', width=70, height=98, cursor='hand2', command=rent)
    maserati_granturismo_coupe_rent = Button(another_frame_coupe, image=maserati_granturismo_coupe_button,
                                             borderwidth=0, bg='#333232', activebackground='#333232', width=70,
                                             height=98, cursor='hand2', command=rent)
    McLaren_720s_coupe_rent = Button(another_frame_coupe, image=McLaren_720s_coupe_button, borderwidth=0, bg='#333232',
                                     activebackground='#333232', width=70, height=98, cursor='hand2', command=rent)
    mercedes_amg_gt_coupe_rent = Button(another_frame_coupe, image=mercedes_amg_gt_coupe_button, borderwidth=0,
                                        bg='#333232', activebackground='#333232', width=70, height=98, cursor='hand2',
                                        command=rent)
    mercedes_c43_coupe_rent = Button(another_frame_coupe, image=mercedes_c43_coupe_button, borderwidth=0, bg='#333232',
                                     activebackground='#333232', width=70, height=98, cursor='hand2', command=rent)
    nissan_370z_coupe_rent = Button(another_frame_coupe, image=nissan_370z_coupe_button, borderwidth=0, bg='#333232',
                                    activebackground='#333232', width=70, height=98, cursor='hand2', command=rent)
    subaru_brz_coupe_rent = Button(another_frame_coupe, image=subaru_brz_coupe_button, borderwidth=0, bg='#333232',
                                   activebackground='#333232', width=70, height=98, cursor='hand2', command=rent)
    toyota_86_coupe_rent = Button(another_frame_coupe, image=toyota_86_coupe_button, borderwidth=0, bg='#333232',
                                  activebackground='#333232', width=70, height=98, cursor='hand2', command=rent)
    toyota_supra_coupe_rent = Button(another_frame_coupe, image=toyota_supra_coupe_button, borderwidth=0, bg='#333232',
                                     activebackground='#333232', width=70, height=98, cursor='hand2', command=rent)

    # All the buttons referenced
    astonmartin_DB11_coupe_rent.image = astonmartin_DB11_coupe_button
    astonmartin_vantage_coupe_rent.image = astonmartin_vantage_coupe_button
    audi_tt_coupe_rent.image = audi_tt_coupe_button
    bentley_continental_coupe_rent.image = bentley_continental_coupe_button
    bmw_650i_coupe_rent.image = bmw_650i_coupe_button
    bmw_i8_coupe_rent.image = bmw_i8_coupe_button
    cadillac_ats_v_coupe_rent.image = cadillac_ats_v_coupe_button
    chevrolet_camaro_coupe_rent.image = chevrolet_camaro_coupe_button
    dodge_challenger_coupe_rent.image = dodge_challenger_coupe_button
    ford_mustang_coupe_rent.image = ford_mustang_coupe_button
    jaguar_f_type_coupe_rent.image = jaguar_f_type_coupe_button
    lotus_evora_coupe_rent.image = lotus_evora_coupe_button
    maserati_granturismo_coupe_rent.image = maserati_granturismo_coupe_button
    McLaren_720s_coupe_rent.image = McLaren_720s_coupe_button
    mercedes_amg_gt_coupe_rent.image = mercedes_amg_gt_coupe_button
    mercedes_c43_coupe_rent.image = mercedes_c43_coupe_button
    nissan_370z_coupe_rent.image = nissan_370z_coupe_button
    subaru_brz_coupe_rent.image = subaru_brz_coupe_button
    toyota_86_coupe_rent.image = toyota_86_coupe_button
    toyota_supra_coupe_rent.image = toyota_supra_coupe_button

    # All the buttons placed
    astonmartin_DB11_coupe_rent.place(x=190, y=470)
    astonmartin_vantage_coupe_rent.place(x=685, y=470)
    audi_tt_coupe_rent.place(x=1172, y=470)
    bentley_continental_coupe_rent.place(x=1665, y=470)
    bmw_650i_coupe_rent.place(x=190, y=1115)
    bmw_i8_coupe_rent.place(x=685, y=1115)
    cadillac_ats_v_coupe_rent.place(x=1172, y=1115)
    chevrolet_camaro_coupe_rent.place(x=1665, y=1115)
    dodge_challenger_coupe_rent.place(x=190, y=1760)
    ford_mustang_coupe_rent.place(x=685, y=1760)
    jaguar_f_type_coupe_rent.place(x=1172, y=1760)
    lotus_evora_coupe_rent.place(x=1665, y=1760)
    maserati_granturismo_coupe_rent.place(x=190, y=2410)
    McLaren_720s_coupe_rent.place(x=685, y=2410)
    mercedes_amg_gt_coupe_rent.place(x=1172, y=2410)
    mercedes_c43_coupe_rent.place(x=1665, y=2410)
    nissan_370z_coupe_rent.place(x=190, y=3060)
    subaru_brz_coupe_rent.place(x=685, y=3060)
    toyota_86_coupe_rent.place(x=1172, y=3060)
    toyota_supra_coupe_rent.place(x=1665, y=3060)


def convertible():
    global root_convertible
    global button_convertible
    root_convertible = Toplevel(root)
    root_convertible.geometry("1920x1080")
    root_convertible.configure(bg="#212121")
    root_convertible.title("Convertible")
    root_convertible.resizable(True, True)
    button_convertible.config(state='disabled')
    root_convertible.protocol("WM_DELETE_WINDOW", convertible_button)
    orange = Frame(root_convertible, width=1920, height=100, bg="#FF6006")
    orange.pack()
    the_canvas_convertible = Canvas(root_convertible, bg="#212121", borderwidth=0, highlightthickness=0)
    the_canvas_convertible.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar_convertible = Scrollbar(root_convertible, orient=VERTICAL, command=the_canvas_convertible.yview)
    my_scrollbar_convertible.pack(side=RIGHT, fill=Y)
    the_canvas_convertible.configure(yscrollcommand=my_scrollbar_convertible.set)
    the_canvas_convertible.bind('<Configure>', lambda e: the_canvas_convertible.configure(
        scrollregion=the_canvas_convertible.bbox("all")))
    another_frame_convertible = Frame(the_canvas_convertible, bg="#212121", borderwidth=0, highlightthickness=0)
    the_canvas_convertible.create_window((0, 0), window=another_frame_convertible, anchor="nw")

    def for_scroll_convertible(event):
        the_canvas_convertible.yview_scroll(int(-1 * (event.delta / 120)), "units")

    the_canvas_convertible.bind_all("<MouseWheel>", for_scroll_convertible)
    the_canvas_convertible.create_window((0, 0), window=another_frame_convertible, anchor="nw")

    audi_r8_converible = PhotoImage(file="./convertiblecars/audi.r8.converible.png")
    bmw_z4_convertible = PhotoImage(file="./convertiblecars/bmw.z4.convertible.png")
    chevrolet_corvette_convertible = PhotoImage(file="./convertiblecars/chevrolet.corvette.convertible.png")
    ferrari_458_convertible = PhotoImage(file="./convertiblecars/ferrari.458.convertible.png")
    ferrari_california_convertible = PhotoImage(file="./convertiblecars/ferrari.california.convertible.png")
    ferrari_f50_convertible = PhotoImage(file="./convertiblecars/ferrari.f50.convertible.png")
    lotus_exige_convertible = PhotoImage(file="./convertiblecars/lotus.exige.convertible.png")
    mazda_MX_5_convertible = PhotoImage(file="./convertiblecars/mazda.MX-5.convertible.png")
    McLaren_650s_convertible = PhotoImage(file="./convertiblecars/McLaren.650s.convertible.png")
    porsche_718_convertible = PhotoImage(file="./convertiblecars/porsche.718.convertible.png")

    audi_r8_converible_label = Label(another_frame_convertible, image=audi_r8_converible, bg='#212121', width=328,
                                     height=600)
    bmw_z4_convertible_label = Label(another_frame_convertible, image=bmw_z4_convertible, bg='#212121', width=328,
                                     height=600)
    chevrolet_corvette_convertible_label = Label(another_frame_convertible, image=chevrolet_corvette_convertible,
                                                 bg='#212121', width=328, height=600)
    ferrari_458_convertible_label = Label(another_frame_convertible, image=ferrari_458_convertible, bg='#212121',
                                          width=328, height=600)
    ferrari_california_convertible_label = Label(another_frame_convertible, image=ferrari_california_convertible,
                                                 bg='#212121', width=328, height=600)
    ferrari_f50_convertible_label = Label(another_frame_convertible, image=ferrari_f50_convertible, bg='#212121',
                                          width=328, height=600)
    lotus_exige_convertible_label = Label(another_frame_convertible, image=lotus_exige_convertible, bg='#212121',
                                          width=328, height=600)
    mazda_MX_5_convertible_label = Label(another_frame_convertible, image=mazda_MX_5_convertible, bg='#212121',
                                         width=328, height=600)
    McLaren_650s_convertible_label = Label(another_frame_convertible, image=McLaren_650s_convertible, bg='#212121',
                                           width=328, height=600)
    porsche_718_convertible_label = Label(another_frame_convertible, image=porsche_718_convertible, bg='#212121',
                                          width=328, height=600)

    audi_r8_converible_label.image = audi_r8_converible
    bmw_z4_convertible_label.image = bmw_z4_convertible
    chevrolet_corvette_convertible_label.image = chevrolet_corvette_convertible
    ferrari_458_convertible_label.image = ferrari_458_convertible
    ferrari_california_convertible_label.image = ferrari_california_convertible
    ferrari_f50_convertible_label.image = ferrari_f50_convertible
    lotus_exige_convertible_label.image = lotus_exige_convertible
    mazda_MX_5_convertible_label.image = mazda_MX_5_convertible
    McLaren_650s_convertible_label.image = McLaren_650s_convertible
    porsche_718_convertible_label.image = porsche_718_convertible

    audi_r8_converible_label.grid(row=2, column=1, padx=60, pady=20)
    bmw_z4_convertible_label.grid(row=2, column=2, padx=100, pady=20)
    chevrolet_corvette_convertible_label.grid(row=2, column=3, padx=60, pady=20)
    ferrari_458_convertible_label.grid(row=2, column=4, padx=100, pady=20)
    ferrari_california_convertible_label.grid(row=3, column=1, padx=60, pady=20)
    ferrari_f50_convertible_label.grid(row=3, column=2, padx=60, pady=20)
    lotus_exige_convertible_label.grid(row=3, column=3, padx=60, pady=20)
    mazda_MX_5_convertible_label.grid(row=3, column=4, padx=60, pady=20)
    McLaren_650s_convertible_label.grid(row=4, column=1, padx=60, pady=20)
    porsche_718_convertible_label.grid(row=4, column=2, padx=60, pady=20)

    audi_r8_converible_button = PhotoImage(file='./allthebuttons/rent.png')
    bmw_z4_convertible_button = PhotoImage(file='./allthebuttons/rent.png')
    chevrolet_corvette_convertible_button = PhotoImage(file='./allthebuttons/rent.png')
    ferrari_458_convertible_button = PhotoImage(file='./allthebuttons/rent.png')
    ferrari_california_convertible_button = PhotoImage(file='./allthebuttons/rent.png')
    ferrari_f50_convertible_button = PhotoImage(file='./allthebuttons/rent.png')
    lotus_exige_convertible_button = PhotoImage(file='./allthebuttons/rent.png')
    mazda_MX_5_convertible_button = PhotoImage(file='./allthebuttons/rent.png')
    McLaren_650s_convertible_button = PhotoImage(file='./allthebuttons/rent.png')
    porsche_718_convertible_button = PhotoImage(file='./allthebuttons/rent.png')

    audi_r8_converible_rent = Button(another_frame_convertible, image=audi_r8_converible_button, borderwidth=0,
                                     bg='#333232', activebackground='#333232', width=70, height=98, cursor='hand2',
                                     command=rent)
    bmw_z4_convertible_rent = Button(another_frame_convertible, image=bmw_z4_convertible_button, borderwidth=0,
                                     bg='#333232', activebackground='#333232', width=70, height=98, cursor='hand2',
                                     command=rent)
    chevrolet_corvette_convertible_rent = Button(another_frame_convertible, image=chevrolet_corvette_convertible_button,
                                                 borderwidth=0, bg='#333232', activebackground='#333232', width=70,
                                                 height=98, cursor='hand2', command=rent)
    ferrari_458_convertible_rent = Button(another_frame_convertible, image=ferrari_458_convertible_button,
                                          borderwidth=0, bg='#333232', activebackground='#333232', width=70, height=98,
                                          cursor='hand2', command=rent)
    ferrari_california_convertible_rent = Button(another_frame_convertible, image=ferrari_california_convertible_button,
                                                 borderwidth=0, bg='#333232', activebackground='#333232', width=70,
                                                 height=98, cursor='hand2', command=rent)
    ferrari_f50_convertible_rent = Button(another_frame_convertible, image=ferrari_f50_convertible_button,
                                          borderwidth=0, bg='#333232', activebackground='#333232', width=70, height=98,
                                          cursor='hand2', command=rent)
    lotus_exige_convertible_rent = Button(another_frame_convertible, image=lotus_exige_convertible_button,
                                          borderwidth=0, bg='#333232', activebackground='#333232', width=70, height=98,
                                          cursor='hand2', command=rent)
    mazda_MX_5_convertible_rent = Button(another_frame_convertible, image=mazda_MX_5_convertible_button, borderwidth=0,
                                         bg='#333232', activebackground='#333232', width=70, height=98, cursor='hand2',
                                         command=rent)
    McLaren_650s_convertible_rent = Button(another_frame_convertible, image=McLaren_650s_convertible_button,
                                           borderwidth=0, bg='#333232', activebackground='#333232', width=70, height=98,
                                           cursor='hand2', command=rent)
    porsche_718_convertible_rent = Button(another_frame_convertible, image=porsche_718_convertible_button,
                                          borderwidth=0, bg='#333232', activebackground='#333232', width=70, height=98,
                                          cursor='hand2', command=rent)

    audi_r8_converible_rent.image = audi_r8_converible_button
    bmw_z4_convertible_rent.image = bmw_z4_convertible_button
    chevrolet_corvette_convertible_rent.image = chevrolet_corvette_convertible_button
    ferrari_458_convertible_rent.image = ferrari_458_convertible_button
    ferrari_california_convertible_rent.image = ferrari_california_convertible_button
    ferrari_f50_convertible_rent.image = ferrari_f50_convertible_button
    lotus_exige_convertible_rent.image = lotus_exige_convertible_button
    mazda_MX_5_convertible_rent.image = mazda_MX_5_convertible_button
    McLaren_650s_convertible_rent.image = McLaren_650s_convertible_button
    porsche_718_convertible_rent.image = porsche_718_convertible_button

    audi_r8_converible_rent.place(x=190, y=470)
    bmw_z4_convertible_rent.place(x=685, y=470)
    chevrolet_corvette_convertible_rent.place(x=1172, y=470)
    ferrari_458_convertible_rent.place(x=1665, y=470)
    ferrari_california_convertible_rent.place(x=190, y=1115)
    ferrari_f50_convertible_rent.place(x=685, y=1115)
    lotus_exige_convertible_rent.place(x=1172, y=1115)
    mazda_MX_5_convertible_rent.place(x=1665, y=1115)
    McLaren_650s_convertible_rent.place(x=190, y=1760)
    porsche_718_convertible_rent.place(x=685, y=1760)


def sports():
    global root_sports
    global button_sports
    root_sports = Toplevel(root)
    root_sports.geometry("1920x1080")
    root_sports.configure(bg="#212121")
    root_sports.title("Sports")
    root_sports.resizable(True, True)
    button_sports.config(state='disabled')
    root_sports.protocol("WM_DELETE_WINDOW", sports_button)
    orange = Frame(root_sports, width=1920, height=100, bg="#FF6006")
    orange.pack()

    the_canvas_sports = Canvas(root_sports, bg="#212121", borderwidth=0, highlightthickness=0)
    the_canvas_sports.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar_sports = Scrollbar(root_sports, orient=VERTICAL, command=the_canvas_sports.yview)
    my_scrollbar_sports.pack(side=RIGHT, fill=Y)
    the_canvas_sports.configure(yscrollcommand=my_scrollbar_sports.set)
    the_canvas_sports.bind('<Configure>',
                           lambda e: the_canvas_sports.configure(scrollregion=the_canvas_sports.bbox("all")))
    another_frame_sports = Frame(the_canvas_sports, bg="#212121", borderwidth=0, highlightthickness=0, )
    the_canvas_sports.create_window((0, 0), window=another_frame_sports, anchor="nw")

    def for_scroll_sports(event):
        the_canvas_sports.yview_scroll(int(-1 * (event.delta / 120)), "units")

    the_canvas_sports.bind_all("<MouseWheel>", for_scroll_sports)
    another_frame_sports = Frame(the_canvas_sports, bg="#212121", borderwidth=0, highlightthickness=0)
    the_canvas_sports.create_window((0, 0), window=another_frame_sports, anchor="nw")

    # All the cars photos
    lamborghini_murcielago_sports = PhotoImage(file="./sportscars/lamborghini.murcielago.sports.png")
    lamborghini_huracan_sports = PhotoImage(file="./sportscars/lamborghini.huracan.sports.png")
    nissan_gtr = PhotoImage(file="./sportscars/nissan_gt-r_sports.png")
    honda_nsx = PhotoImage(file="./sportscars/honda.NS-X.sports.png")
    ford_gt = PhotoImage(file="./sportscars/ford.GT.sports.png")
    buggati_veyron = PhotoImage(file="./sportscars/bugatti.veyron.sports.png")
    dodge_charger = PhotoImage(file="./sportscars/dodge.charger hellcat.sports.png")
    agera = PhotoImage(file="./sportscars/koenigsegg.agera rs.sports.png")
    porsche_sports = PhotoImage(file="./sportscars/porsche.918 spyder.sports.png")
    laferrari = PhotoImage(file="./sportscars/ferrari.laFerrari.sports.png")
    aventador = PhotoImage(file="./sportscars/lamborghini.aventador.sports.png")
    enzo = PhotoImage(file="./sportscars/ferrari.enzo.sports.png")

    # All the cars labels
    lamborghini_murcielago_sports_label = Label(another_frame_sports, image=lamborghini_murcielago_sports, bg="#212121",
                                                width=328, height=600)
    lamborghini_huracan_sports_label = Label(another_frame_sports, image=lamborghini_huracan_sports, bg="#212121",
                                             width=328, height=600)
    nissan_gtr_sports_label = Label(another_frame_sports, image=nissan_gtr, bg="#212121", width=328, height=600)
    honda_nsx_label = Label(another_frame_sports, image=honda_nsx, bg="#212121", width=328, height=600)
    ford_gt_label = Label(another_frame_sports, image=ford_gt, bg="#212121", width=328, height=600)
    buggati_veyron_label = Label(another_frame_sports, image=buggati_veyron, bg="#212121", width=328, height=600)
    dodge_charger_label = Label(another_frame_sports, image=dodge_charger, bg="#212121", width=328, height=600)
    agera_label = Label(another_frame_sports, image=agera, bg="#212121", width=328, height=600)
    porsche_sports_label = Label(another_frame_sports, image=porsche_sports, bg="#212121", width=328, height=600)
    laferrari_label = Label(another_frame_sports, image=laferrari, bg="#212121", width=328, height=600)
    aventador_label = Label(another_frame_sports, image=aventador, bg="#212121", width=328, height=600)
    enzo_label = Label(another_frame_sports, image=enzo, bg="#212121", width=328, height=600)

    # All the cars references
    lamborghini_murcielago_sports_label.image = lamborghini_murcielago_sports
    lamborghini_huracan_sports_label.image = lamborghini_huracan_sports
    nissan_gtr_sports_label.image = nissan_gtr
    honda_nsx_label.image = honda_nsx
    ford_gt_label.image = ford_gt
    buggati_veyron_label.image = buggati_veyron
    dodge_charger_label.image = dodge_charger
    agera_label.image = agera
    porsche_sports_label.image = porsche_sports
    laferrari_label.image = laferrari
    aventador_label.image = aventador
    enzo_label.image = enzo

    # All the cars grid
    lamborghini_murcielago_sports_label.grid(row=2, column=1, padx=60, pady=20)
    lamborghini_huracan_sports_label.grid(row=2, column=2, padx=100, pady=20)
    nissan_gtr_sports_label.grid(row=2, column=3, padx=60, pady=20)
    honda_nsx_label.grid(row=2, column=4, padx=100, pady=20)
    ford_gt_label.grid(row=3, column=1, padx=60, pady=20)
    buggati_veyron_label.grid(row=3, column=2, padx=60, pady=20)
    dodge_charger_label.grid(row=3, column=3, padx=60, pady=20)
    agera_label.grid(row=3, column=4, padx=60, pady=20)
    porsche_sports_label.grid(row=4, column=1, padx=60, pady=20)
    laferrari_label.grid(row=4, column=2, padx=60, pady=20)
    aventador_label.grid(row=4, column=3, padx=60, pady=20)
    enzo_label.grid(row=4, column=4, padx=60, pady=20)

    # Images for button
    lambo_murc = PhotoImage(file="./allthebuttons/rent.png")
    lambo_huracan = PhotoImage(file="./allthebuttons/rent.png")
    niss_gtr = PhotoImage(file="./allthebuttons/rent.png")
    hond_nsx = PhotoImage(file="./allthebuttons/rent.png")
    ford_gt_button = PhotoImage(file="./allthebuttons/rent.png")
    buggati_veyron_button = PhotoImage(file="./allthebuttons/rent.png")
    dodge_charger_button = PhotoImage(file="./allthebuttons/rent.png")
    agera_button = PhotoImage(file="./allthebuttons/rent.png")
    porsche_sports_button = PhotoImage(file="./allthebuttons/rent.png")
    laferrari_button = PhotoImage(file="./allthebuttons/rent.png")
    aventador_button = PhotoImage(file="./allthebuttons/rent.png")
    enzo_button = PhotoImage(file="./allthebuttons/rent.png")

    # Actual Buttons with Image
    lambo_murc_rent = Button(another_frame_sports, image=lambo_murc, borderwidth=0, bg="#333232",
                             activebackground="#333232", width=70, height=98, cursor="hand2", command=rent)
    lambo_huracan_rent = Button(another_frame_sports, image=lambo_huracan, borderwidth=0, bg="#333232",
                                activebackground="#333232", width=70, height=98, cursor="hand2", command=rent)
    niss_gtr_rent = Button(another_frame_sports, image=niss_gtr, borderwidth=0, bg="#333232",
                           activebackground="#333232", width=70, height=98, cursor="hand2", command=rent)
    hond_nsx_rent = Button(another_frame_sports, image=hond_nsx, borderwidth=0, bg="#333232",
                           activebackground="#333232", width=70, height=98, cursor="hand2", command=rent)
    ford_gt_rent = Button(another_frame_sports, image=ford_gt_button, borderwidth=0, bg="#333232",
                          activebackground="#333232", width=70, height=98, cursor="hand2", command=rent)
    veyron_rent = Button(another_frame_sports, image=buggati_veyron_button, borderwidth=0, bg="#333232",
                         activebackground="#333232", width=70, height=98, cursor="hand2", command=rent)
    charger_rent = Button(another_frame_sports, image=dodge_charger_button, borderwidth=0, bg="#333232",
                          activebackground="#333232", width=70, height=98, cursor="hand2", command=rent)
    agera_rent = Button(another_frame_sports, image=agera_button, borderwidth=0, bg="#333232",
                        activebackground="#333232", width=70, height=98, cursor="hand2", command=rent)
    porsche_rent = Button(another_frame_sports, image=porsche_sports_button, borderwidth=0, bg="#333232",
                          activebackground="#333232", width=70, height=98, cursor="hand2", command=rent)
    laferrari_rent = Button(another_frame_sports, image=laferrari_button, borderwidth=0, bg="#333232",
                            activebackground="#333232", width=70, height=98, cursor="hand2", command=rent)
    aventador_rent = Button(another_frame_sports, image=aventador_button, borderwidth=0, bg="#333232",
                            activebackground="#333232", width=70, height=98, cursor="hand2", command=rent)
    enzo_rent = Button(another_frame_sports, image=enzo_button, borderwidth=0, bg="#333232", activebackground="#333232",
                       width=70, height=98, cursor="hand2", command=rent)

    # Buttons referenced
    lambo_murc_rent.image = lambo_murc
    lambo_huracan_rent.image = lambo_huracan
    niss_gtr_rent.image = niss_gtr
    hond_nsx_rent.image = hond_nsx
    ford_gt_rent.image = ford_gt_button
    veyron_rent.image = buggati_veyron_button
    charger_rent.image = dodge_charger_button
    agera_rent.image = agera_button
    porsche_rent.image = porsche_sports_button
    laferrari_rent.image = laferrari_button
    aventador_rent.image = aventador_button
    enzo_rent.image = enzo_button

    # Buttons grid
    lambo_murc_rent.place(x=190, y=470)
    lambo_huracan_rent.place(x=685, y=470)
    niss_gtr_rent.place(x=1172, y=470)
    hond_nsx_rent.place(x=1665, y=470)
    ford_gt_rent.place(x=190, y=1115)
    veyron_rent.place(x=685, y=1115)
    charger_rent.place(x=1172, y=1115)
    agera_rent.place(x=1665, y=1115)
    porsche_rent.place(x=190, y=1760)
    laferrari_rent.place(x=685, y=1760)
    aventador_rent.place(x=1172, y=1760)
    enzo_rent.place(x=1665, y=1760)


def wagon():
    global root_wagon
    global button_wagon
    root_wagon = Toplevel(root)
    root_wagon.geometry("1920x1080")
    root_wagon.configure(bg="#212121")
    root_wagon.title("Wagon")
    root_wagon.resizable(True, True)
    button_wagon.config(state='disabled')
    root_wagon.protocol("WM_DELETE_WINDOW", wagon_button)
    orange = Frame(root_wagon, width=1920, height=100, bg="#FF6006")
    orange.pack()
    the_canvas_wagon = Canvas(root_wagon, bg="#212121", borderwidth=0, highlightthickness=0)
    the_canvas_wagon.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar_wagon = Scrollbar(root_wagon, orient=VERTICAL, command=the_canvas_wagon.yview)
    my_scrollbar_wagon.pack(side=RIGHT, fill=Y)
    the_canvas_wagon.configure(yscrollcommand=my_scrollbar_wagon.set)
    the_canvas_wagon.bind('<Configure>',
                          lambda e: the_canvas_wagon.configure(scrollregion=the_canvas_wagon.bbox("all")))
    another_frame_wagon = Frame(the_canvas_wagon, bg="#212121", borderwidth=0, highlightthickness=0)
    the_canvas_wagon.create_window((0, 0), window=another_frame_wagon, anchor="nw")

    def for_scroll_wagon(event):
        the_canvas_wagon.yview_scroll(int(-1 * (event.delta / 120)), "units")

    the_canvas_wagon.bind_all("<MouseWheel>", for_scroll_wagon)
    another_frame_wagon = Frame(the_canvas_wagon, bg="#212121", borderwidth=0, highlightthickness=0)
    the_canvas_wagon.create_window((0, 0), window=another_frame_wagon, anchor="nw")

    # All the cars photos
    audi_rs4 = PhotoImage(file="./wagoncars/audi.RS4.wagon.png")
    porsce = PhotoImage(file="./wagoncars/porsche.panamera.wagon.png")

    wagon_list = [audi_rs4, porsce]

    for i in wagon_list:
        row = 2
        column_wagon = wagon_list.index(i)
        Label(another_frame_wagon, image=i, bg="#212121", width=328, height=600).grid(row=row, column=column_wagon, padx=70, pady=20)
        i.image = i

    # Button images
    audi_rs4_pic = PhotoImage(file="./allthebuttons/rent.png")
    porsche_pic = PhotoImage(file="./allthebuttons/rent.png")

    # Buttons
    audi_rs4_rent = Button(root_wagon, image=audi_rs4_pic, borderwidth=0, bg="#333232", activebackground="#333232",
                           width=70, height=98, cursor="hand2", command=rent)
    porsche_rent = Button(root_wagon, image=porsche_pic, borderwidth=0, bg="#333232", activebackground="#333232",
                          width=70, height=98, cursor="hand2", command=rent)

    # Referenced
    audi_rs4_rent.image = audi_rs4_pic
    porsche_rent.image = porsche_pic

    # Placed
    audi_rs4_rent.place(x=190, y=570)
    porsche_rent.place(x=670, y=570)


def hatchback():
    global root_hatchback, column
    global button_hatchback
    root_hatchback = Toplevel(root)
    root_hatchback.geometry("1920x1080")
    root_hatchback.configure(bg="#212121")
    root_hatchback.title("Hatchback")
    root_hatchback.resizable(True, True)
    button_hatchback.config(state='disabled')
    root_hatchback.protocol("WM_DELETE_WINDOW", hatchback_button)
    orange = Frame(root_hatchback, width=1920, height=100, bg="#FF6006")
    orange.pack()
    the_canvas_hatchback = Canvas(root_hatchback, bg="#212121", borderwidth=0, highlightthickness=0)
    the_canvas_hatchback.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar_hatchback = Scrollbar(root_hatchback, orient=VERTICAL, command=the_canvas_hatchback.yview)
    my_scrollbar_hatchback.pack(side=RIGHT, fill=Y)
    the_canvas_hatchback.configure(yscrollcommand=my_scrollbar_hatchback.set)
    the_canvas_hatchback.bind('<Configure>',
                              lambda e: the_canvas_hatchback.configure(scrollregion=the_canvas_hatchback.bbox("all")))
    another_frame_hatchback = Frame(the_canvas_hatchback, bg="#212121", borderwidth=0, highlightthickness=0)
    the_canvas_hatchback.create_window((0, 0), window=another_frame_hatchback, anchor="nw")

    def for_scroll_hatchback(event):
        the_canvas_hatchback.yview_scroll(int(-1 * (event.delta / 120)), "units")

    the_canvas_hatchback.bind_all("<MouseWheel>", for_scroll_hatchback)
    another_frame_hatchback = Frame(the_canvas_hatchback, bg="#212121", borderwidth=0, highlightthickness=0)
    the_canvas_hatchback.create_window((0, 0), window=another_frame_hatchback, anchor="nw")

    ford_focus_hatchback = PhotoImage(file="./hatchbackcars/ford.focus.hatchback.png")
    honda_civic_hatchback = PhotoImage(file="./hatchbackcars/honda.civic.hatchback.png")
    hyundai_veloster_hatchback = PhotoImage(file="./hatchbackcars/hyundai.veloster.hatchback.png")
    kia_picanto_hatchback = PhotoImage(file="./hatchbackcars/kia.picanto.hatchback.png")
    nissan_tiida_hatchback = PhotoImage(file="./hatchbackcars/nissan.tiida.hatchback.png")
    subaru_impreza_hatchback = PhotoImage(file="./hatchbackcars/subaru.impreza.hatchback.png")
    toyota_yaris_hatchback = PhotoImage(file="./hatchbackcars/toyota.yaris.hatchback.png")

    ford_focus_hatchback_label = Label(another_frame_hatchback, image=ford_focus_hatchback, bg="#212121", width=328, height=600)
    honda_civic_hatchback_label = Label(another_frame_hatchback, image=honda_civic_hatchback, bg="#212121", width=328, height=600)
    hyundai_veloster_hatchback_label = Label(another_frame_hatchback, image=hyundai_veloster_hatchback, bg="#212121", width=328, height=600)
    kia_picanto_hatchback_label = Label(another_frame_hatchback, image=kia_picanto_hatchback, bg="#212121", width=328, height=600)
    nissan_tiida_hatchback_label = Label(another_frame_hatchback, image=nissan_tiida_hatchback, bg="#212121", width=328, height=600)
    subaru_impreza_hatchback_label = Label(another_frame_hatchback, image=subaru_impreza_hatchback, bg="#212121", width=328, height=600)
    toyota_yaris_hatchback_label = Label(another_frame_hatchback, image=toyota_yaris_hatchback, bg="#212121", width=328, height=600)


    # All the cars references
    ford_focus_hatchback_label.image = ford_focus_hatchback
    honda_civic_hatchback_label.image = honda_civic_hatchback
    hyundai_veloster_hatchback_label.image = hyundai_veloster_hatchback
    kia_picanto_hatchback_label.image = kia_picanto_hatchback
    nissan_tiida_hatchback_label.image = nissan_tiida_hatchback
    subaru_impreza_hatchback_label.image = subaru_impreza_hatchback
    toyota_yaris_hatchback_label.image = toyota_yaris_hatchback

    # All the cars grid
    ford_focus_hatchback_label.grid(row=2, column=1, padx=60, pady=20)
    honda_civic_hatchback_label.grid(row=2, column=2, padx=100, pady=20)
    hyundai_veloster_hatchback_label.grid(row=2, column=3, padx=60, pady=20)
    kia_picanto_hatchback_label.grid(row=2, column=4, padx=100, pady=20)
    nissan_tiida_hatchback_label.grid(row=3, column=1, padx=60, pady=20)
    subaru_impreza_hatchback_label.grid(row=3, column=2, padx=60, pady=20)
    toyota_yaris_hatchback_label.grid(row=3, column=3, padx=60, pady=20)


    ford_focus_hatchback_button = PhotoImage(file='./allthebuttons/rent.png')
    honda_civic_hatchback_button = PhotoImage(file='./allthebuttons/rent.png')
    hyundai_veloster_hatchback_button = PhotoImage(file='./allthebuttons/rent.png')
    kia_picanto_hatchback_button = PhotoImage(file='./allthebuttons/rent.png')
    nissan_tiida_hatchback_button = PhotoImage(file='./allthebuttons/rent.png')
    subaru_impreza_hatchback_button = PhotoImage(file='./allthebuttons/rent.png')
    toyota_yaris_hatchback_button = PhotoImage(file='./allthebuttons/rent.png')

    ford_focus_hatchback_rent = Button(another_frame_hatchback, image=ford_focus_hatchback_button, borderwidth=0,
                                       bg='#333232', activebackground='#333232', width=70, height=98, cursor='hand2',
                                       command=rent)
    honda_civic_hatchback_rent = Button(another_frame_hatchback, image=honda_civic_hatchback_button, borderwidth=0,
                                        bg='#333232', activebackground='#333232', width=70, height=98, cursor='hand2',
                                        command=rent)
    hyundai_veloster_hatchback_rent = Button(another_frame_hatchback, image=hyundai_veloster_hatchback_button,
                                             borderwidth=0, bg='#333232', activebackground='#333232', width=70,
                                             height=98, cursor='hand2', command=rent)
    kia_picanto_hatchback_rent = Button(another_frame_hatchback, image=kia_picanto_hatchback_button, borderwidth=0,
                                        bg='#333232', activebackground='#333232', width=70, height=98, cursor='hand2',
                                        command=rent)
    nissan_tiida_hatchback_rent = Button(another_frame_hatchback, image=nissan_tiida_hatchback_button, borderwidth=0,
                                         bg='#333232', activebackground='#333232', width=70, height=98, cursor='hand2',
                                         command=rent)
    subaru_impreza_hatchback_rent = Button(another_frame_hatchback, image=subaru_impreza_hatchback_button,
                                           borderwidth=0, bg='#333232', activebackground='#333232', width=70, height=98,
                                           cursor='hand2', command=rent)
    toyota_yaris_hatchback_rent = Button(another_frame_hatchback, image=toyota_yaris_hatchback_button, borderwidth=0,
                                         bg='#333232', activebackground='#333232', width=70, height=98, cursor='hand2',
                                         command=rent)

    ford_focus_hatchback_rent.image = ford_focus_hatchback_button
    honda_civic_hatchback_rent.image = honda_civic_hatchback_button
    hyundai_veloster_hatchback_rent.image = hyundai_veloster_hatchback_button
    kia_picanto_hatchback_rent.image = kia_picanto_hatchback_button
    nissan_tiida_hatchback_rent.image = nissan_tiida_hatchback_button
    subaru_impreza_hatchback_rent.image = subaru_impreza_hatchback_button
    toyota_yaris_hatchback_rent.image = toyota_yaris_hatchback_button

    ford_focus_hatchback_rent.place(x=190, y=470)
    honda_civic_hatchback_rent.place(x=685, y=470)
    hyundai_veloster_hatchback_rent.place(x=1172, y=470)
    kia_picanto_hatchback_rent.place(x=1665, y=470)
    nissan_tiida_hatchback_rent.place(x=190, y=1115)
    subaru_impreza_hatchback_rent.place(x=685, y=1115)
    toyota_yaris_hatchback_rent.place(x=1172, y=1115)


def minivan():
    global root_minivan
    global button_minivan
    root_minivan = Toplevel(root)
    root_minivan.geometry("1920x1080")
    root_minivan.configure(bg="#212121")
    root_minivan.title("Minivan")
    root_minivan.resizable(True, True)
    button_minivan.config(state='disabled')
    root_minivan.protocol("WM_DELETE_WINDOW", minivan_button)
    orange = Frame(root_minivan, width=1920, height=100, bg="#FF6006")
    orange.pack()
    the_canvas_minivan = Canvas(root_minivan, bg="#212121", borderwidth=0, highlightthickness=0)
    the_canvas_minivan.pack(side=LEFT, fill=BOTH, expand=1)
    my_scrollbar_minivan = Scrollbar(root_minivan, orient=VERTICAL, command=the_canvas_minivan.yview)
    my_scrollbar_minivan.pack(side=RIGHT, fill=Y)
    the_canvas_minivan.configure(yscrollcommand=my_scrollbar_minivan.set)
    the_canvas_minivan.bind('<Configure>',
                            lambda e: the_canvas_minivan.configure(scrollregion=the_canvas_minivan.bbox("all")))
    another_frame_minivan = Frame(the_canvas_minivan, bg="#212121", borderwidth=0, highlightthickness=0)
    the_canvas_minivan.create_window((0, 0), window=another_frame_minivan, anchor="nw")

    def for_scroll_minivan(event):
        the_canvas_minivan.yview_scroll(int(-1 * (event.delta / 120)), "units")

    the_canvas_minivan.bind_all("<MouseWheel>", for_scroll_minivan)
    another_frame_minivan = Frame(the_canvas_minivan, bg="#212121", borderwidth=0, highlightthickness=0)
    the_canvas_minivan.create_window((0, 0), window=another_frame_minivan, anchor="nw")

    # All the cars photos
    hyundai_imax = PhotoImage(file="./minivancars/hyundai.iMax.minivan.png")
    kia_carnival = PhotoImage(file="./minivancars/kia.carnival.minivan.png")
    v250 = PhotoImage(file="./minivancars/mercedes.V250.minivan.png")
    toyota_tarago = PhotoImage(file="./minivancars/toyota.tarago.minivan.png")

    # All the cars labels
    minivan_list = [hyundai_imax, kia_carnival, v250, toyota_tarago]

    for i in minivan_list:
        row = 2
        column_minivan = minivan_list.index(i)
        Label(another_frame_minivan, image=i, bg="#212121", width=328, height=600).grid(row=row, column=column_minivan, padx=70, pady=20)
        i.image = i

    # Images for button
    hyundai_button = PhotoImage(file="./allthebuttons/rent.png")
    kia_button = PhotoImage(file="./allthebuttons/rent.png")
    v250_button = PhotoImage(file="./allthebuttons/rent.png")
    toyota_button = PhotoImage(file="./allthebuttons/rent.png")

    # Actual Buttons with Image
    hyundai_rent = Button(another_frame_minivan, image=hyundai_button, borderwidth=0, bg="#333232",
                          activebackground="#333232", width=70, height=98, cursor="hand2", command=rent)
    kia_rent = Button(another_frame_minivan, image=kia_button, borderwidth=0, bg="#333232", activebackground="#333232",
                      width=70, height=98, cursor="hand2", command=rent)
    v250_rent = Button(another_frame_minivan, image=v250_button, borderwidth=0, bg="#333232",
                       activebackground="#333232", width=70, height=98, cursor="hand2", command=rent)
    toyota_rent = Button(another_frame_minivan, image=toyota_button, borderwidth=0, bg="#333232",
                         activebackground="#333232", width=70, height=98, cursor="hand2", command=rent)

    # Buttons referenced
    hyundai_rent.image = hyundai_button
    kia_rent.image = kia_button
    v250_rent.image = v250_button
    toyota_rent.image = toyota_button

    # Buttons grid
    hyundai_rent.place(x=200, y=470)
    kia_rent.place(x=670, y=470)
    v250_rent.place(x=1150, y=470)
    toyota_rent.place(x=1620, y=470)


# Credits
def clickedme():
    label_for_names = Label(frame_root_scroll, text="", font="Helvetica, 20")
    label_for_names2 = Label(frame_root_scroll, text="", font="Helvetica, 20")
    label_for_names3 = Label(frame_root_scroll, text="", font="Helvetica, 20")

    label_for_names.place(x=915, y=910)
    label_for_names2.place(x=1100, y=995)
    label_for_names3.place(x=750, y=995)

    label_for_names.config(text="Aakash", font="Helvetica, 20", bg="#212121", fg="white")
    label_for_names2.config(text="Patson", font="Helvetica, 20", bg="#212121", fg="white")
    label_for_names3.config(text="Vivek", font="Helvetica, 20", bg="#212121", fg="white")


# Variables For The Photos
sedan_car = PhotoImage(file="sedan.png")
suv_car = PhotoImage(file="suv.png")
coupe_car = PhotoImage(file="coupe.png")
convertible_car = PhotoImage(file="convertible.png")
sports_car = PhotoImage(file="sports.png")
wagon_car = PhotoImage(file="wagon.png")
hatchback_car = PhotoImage(file="hatchback.png")
minivan_car = PhotoImage(file="minivan.png")
search_button = PhotoImage(file="search.png")
image_button = PhotoImage(file="credits.png")

# Styles For The Buttons
button_sedan = Button(frame_root_scroll, image=sedan_car, bg="#212121", borderwidth=0, command=sedan,
                      activebackground="#212121", cursor="hand2")
button_suv = Button(frame_root_scroll, image=suv_car, bg="#212121", borderwidth=0, command=suv,
                    activebackground="#212121", cursor="hand2")
button_coupe = Button(frame_root_scroll, image=coupe_car, bg="#212121", borderwidth=0, command=coupe,
                      activebackground="#212121", cursor="hand2")
button_minivan = Button(frame_root_scroll, image=minivan_car, bg="#212121", borderwidth=0, command=minivan,
                        activebackground="#212121", cursor="hand2")
button_convertible = Button(frame_root_scroll, image=convertible_car, bg="#212121", borderwidth=0, command=convertible,
                            activebackground="#212121", cursor="hand2")
button_sports = Button(frame_root_scroll, image=sports_car, bg="#212121", borderwidth=0, command=sports,
                       activebackground="#212121", cursor="hand2")
button_wagon = Button(frame_root_scroll, image=wagon_car, bg="#212121", borderwidth=0, command=wagon,
                      activebackground="#212121", cursor="hand2")
button_hatchback = Button(frame_root_scroll, image=hatchback_car, bg="#212121", borderwidth=0, command=hatchback,
                          activebackground="#212121", cursor="hand2")
button_for_credits = Button(frame_root_scroll, text="Click Me", command=clickedme, image=image_button, borderwidth=0,
                            bg="#212121", activebackground="#212121", cursor="hand2")

# Button Positions
button_sedan.place(x=20, y=300)
button_suv.place(x=995, y=300)
button_coupe.place(x=1480, y=300)
button_minivan.place(x=510, y=300)
button_sports.place(x=20, y=650)
button_wagon.place(x=995, y=650)
button_convertible.place(x=1480, y=650)
button_hatchback.place(x=510, y=650)
button_for_credits.place(x=866, y=960)

# Labels With Pics For Signification
navigation_bar = PhotoImage(file="nav bar.png")
assort_price = PhotoImage(file="assortprice.png")
search_bar = PhotoImage(file="search box.png")

# Using Label
label_nav = Label(frame_root_scroll, image=navigation_bar, borderwidth=0, bg="#212121", height=100).place(x=685, y=178)


# Search Button Functions :
def button_check(*args):
    astonmartin_DB11_coupe = PhotoImage(file='./allthecars/astonmartin.DB11.coupe.png')
    astonmartin_vantage_coupe = PhotoImage(file='./allthecars/astonmartin.vantage.coupe.png')
    audi_a3_hatchback = PhotoImage(file='./allthecars/audi.a3.hatchback.png')
    audi_a4_sedan = PhotoImage(file='./allthecars/audi.a4.sedan.png')
    audi_q8_suv = PhotoImage(file='./allthecars/audi.q8.suv.png')
    audi_r8_converible = PhotoImage(file='./allthecars/audi.r8.converible.png')
    audi_RS4_wagon = PhotoImage(file='./allthecars/audi.RS4.wagon.png')
    audi_tt_coupe = PhotoImage(file='./allthecars/audi.tt.coupe.png')
    bentley_continental_coupe = PhotoImage(file='./allthecars/bentley.continental.coupe.png')
    bmw_650i_coupe = PhotoImage(file='./allthecars/bmw.650i.coupe.png')
    bmw_i8_coupe = PhotoImage(file='./allthecars/bmw.i8.coupe.png')
    bmw_X6_suv = PhotoImage(file='./allthecars/bmw.X6.suv.png')
    bmw_z4_convertible = PhotoImage(file='./allthecars/bmw.z4.convertible.png')
    bugatti_veyron_sports = PhotoImage(file='./allthecars/bugatti.veyron.sports.png')
    cadillac_atsv_coupe = PhotoImage(file='./allthecars/cadillac.atsv.coupe.png')
    cadillac_CTS_sedan = PhotoImage(file='./allthecars/cadillac.CTS.sedan.png')
    cadillac_XT6_suv = PhotoImage(file='./allthecars/cadillac.XT6.suv.png')
    chevrolet_camaro_coupe = PhotoImage(file='./allthecars/chevrolet.camaro.coupe.png')
    chevrolet_corvette_convertible = PhotoImage(file='./allthecars/chevrolet.corvette.convertible.png')
    dodge_challenger_coupe = PhotoImage(file='./allthecars/dodge.challenger.coupe.png')
    dodge_charger_hellcat_sports = PhotoImage(file='./allthecars/dodge.charger hellcat.sports.png')
    ferrari_458_convertible = PhotoImage(file='./allthecars/ferrari.458.convertible.png')
    ferrari_california_convertible = PhotoImage(file='./allthecars/ferrari.california.convertible.png')
    ferrari_enzo_sports = PhotoImage(file='./allthecars/ferrari.enzo.sports.png')
    ferrari_f50_convertible = PhotoImage(file='./allthecars/ferrari.f50.convertible.png')
    ferrari_laFerrari_sports = PhotoImage(file='./allthecars/ferrari.laFerrari.sports.png')
    ford_focus_hatchback = PhotoImage(file='./allthecars/ford.focus.hatchback.png')
    ford_GT_sports = PhotoImage(file='./allthecars/ford.GT.sports.png')
    ford_mustang_coupe = PhotoImage(file='./allthecars/ford.mustang.coupe.png')
    honda_accord_sedan = PhotoImage(file='./allthecars/honda.accord.sedan.png')
    honda_city_sedan = PhotoImage(file='./allthecars/honda.city.sedan.png')
    honda_civic_hatchback = PhotoImage(file='./allthecars/honda.civic.hatchback.png')
    honda_crv_suv = PhotoImage(file='./allthecars/honda.cr-v.suv.png')
    honda_NSX_sports = PhotoImage(file='./allthecars/honda.NS-X.sports.png')
    hyundai_elantra_sedan = PhotoImage(file='./allthecars/hyundai.elantra.sedan.png')
    hyundai_iMax_minivan = PhotoImage(file='./allthecars/hyundai.iMax.minivan.png')
    hyundai_veloster_hatchback = PhotoImage(file='./allthecars/hyundai.veloster.hatchback.png')
    infiniti_q70_sedan = PhotoImage(file='./allthecars/infiniti.q70.sedan.png')
    infiniti_qx30_suv = PhotoImage(file='./allthecars/infiniti.qx30.suv.png')
    infiniti_qx80_suv = PhotoImage(file='./allthecars/infiniti.qx80.suv.png')
    jaguar_ftype_coupe = PhotoImage(file='./allthecars/jaguar.f-type.coupe.png')
    jaguar_XF_sedan = PhotoImage(file='./allthecars/jaguar.XF.sedan.png')
    kia_carnival_minivan = PhotoImage(file='./allthecars/kia.carnival.minivan.png')
    kia_optima_sedan = PhotoImage(file='./allthecars/kia.optima.sedan.png')
    kia_picanto_hatchback = PhotoImage(file='./allthecars/kia.picanto.hatchback.png')
    kia_sportage_suv = PhotoImage(file='./allthecars/kia.sportage.suv.png')
    koenigsegg_agerars_sports = PhotoImage(file='./allthecars/koenigsegg.agera rs.sports.png')
    lamborghini_aventador_sports = PhotoImage(file='./allthecars/lamborghini.aventador.sports.png')
    lamborghini_huracan_sports = PhotoImage(file='./allthecars/lamborghini.huracan.sports.png')
    lamborghini_murcielago_sports = PhotoImage(file='./allthecars/lamborghini.murcielago.sports.png')
    lamborghini_urus_suv = PhotoImage(file='./allthecars/lamborghini.urus.suv.png')
    landrover_rangerover_suv = PhotoImage(file='./allthecars/landrover.range rover.suv.png')
    lotus_evora_coupe = PhotoImage(file='./allthecars/lotus.evora.coupe.png')
    lotus_exige_convertible = PhotoImage(file='./allthecars/lotus.exige.convertible.png')
    maserati_granturismo_coupe = PhotoImage(file='./allthecars/maserati.granturismo.coupe.png')
    maserati_quattroporte_sedan = PhotoImage(file='./allthecars/maserati.quattroporte.sedan.png')
    mazda_cx30_suv = PhotoImage(file='./allthecars/mazda.cx30.suv.png')
    mazda_MX5_convertible = PhotoImage(file='./allthecars/mazda.MX-5.convertible.png')
    McLaren_650s_convertible = PhotoImage(file='./allthecars/McLaren.650s.convertible.png')
    McLaren_720s_coupe = PhotoImage(file='./allthecars/McLaren.720s.coupe.png')
    mercedes_amggt_coupe = PhotoImage(file='./allthecars/mercedes.amggt.coupe.png')
    mercedes_c43_coupe = PhotoImage(file='./allthecars/mercedes.c43.coupe.png')
    mercedes_g63_suv = PhotoImage(file='./allthecars/mercedes.g63.suv.png')
    mercedes_V250_minivan = PhotoImage(file='./allthecars/mercedes.V250.minivan.png')
    nissan_370z_coupe = PhotoImage(file='./allthecars/nissan.370z.coupe.png')
    nissan_altima_sedan = PhotoImage(file='./allthecars/nissan.altima.sedan.png')
    nissan_gtr_sports = PhotoImage(file='./allthecars/nissan.gt-r.sports.png')
    nissan_patrol_suv = PhotoImage(file='./allthecars/nissan.patrol.suv.png')
    nissan_tiida_hatchback = PhotoImage(file='./allthecars/nissan.tiida.hatchback.png')
    porsche_718_convertible = PhotoImage(file='./allthecars/porsche.718.convertible.png')
    porsche_918_spyder_sports = PhotoImage(file='./allthecars/porsche.918 spyder.sports.png')
    porsche_cayenne_suv = PhotoImage(file='./allthecars/porsche.cayenne.suv.png')
    porsche_panamera_wagon = PhotoImage(file='./allthecars/porsche.panamera.wagon.png')
    rollsroyce_ghost_sedan = PhotoImage(file='./allthecars/rollsroyce.ghost.sedan.png')
    rollsroyce_phantom_sedan = PhotoImage(file='./allthecars/rollsroyce.phantom.sedan.png')
    subaru_brz_coupe = PhotoImage(file='./allthecars/subaru.brz.coupe.png')
    subaru_impreza_hatchback = PhotoImage(file='./allthecars/subaru.impreza.hatchback.png')
    tesla_models_sedan = PhotoImage(file='./allthecars/tesla.model s.sedan.png')
    tesla_modelx_suv = PhotoImage(file='./allthecars/tesla.model x.suv.png')
    toyota_86_coupe = PhotoImage(file='./allthecars/toyota.86.coupe.png')
    toyota_camry_sedan = PhotoImage(file='./allthecars/toyota.camry.sedan.png')
    toyota_corolla_sedan = PhotoImage(file='./allthecars/toyota.corolla.sedan.png')
    toyota_fortuner_suv = PhotoImage(file='./allthecars/toyota.fortuner.suv.png')
    toyota_landcruiser_suv = PhotoImage(file='./allthecars/toyota.land cruiser.suv.png')
    toyota_pradao_suv = PhotoImage(file='./allthecars/toyota.pradao.suv.png')
    toyota_rav4_suv = PhotoImage(file='./allthecars/toyota.rav4.suv.png')
    toyota_supra_coupe = PhotoImage(file='./allthecars/toyota.supra.coupe.png')
    toyota_tarago_minivan = PhotoImage(file='./allthecars/toyota.tarago.minivan.png')
    toyota_yaris_hatchback = PhotoImage(file='./allthecars/toyota.yaris.hatchback.png')

    cars = {"aston martin": (astonmartin_DB11_coupe, astonmartin_vantage_coupe),
            "audi": (audi_a3_hatchback, audi_a4_sedan, audi_q8_suv, audi_r8_converible, audi_RS4_wagon, audi_tt_coupe),
            "bentley": bentley_continental_coupe,
            "bmw": (bmw_650i_coupe, bmw_i8_coupe, bmw_X6_suv, bmw_z4_convertible),
            "buggati": bugatti_veyron_sports,
            "cadillac": (cadillac_atsv_coupe, cadillac_CTS_sedan, cadillac_XT6_suv),
            "chevrolet": (chevrolet_camaro_coupe, chevrolet_corvette_convertible),
            "dodge": (dodge_challenger_coupe, dodge_charger_hellcat_sports),
            "ferrari": (ferrari_458_convertible, ferrari_california_convertible, ferrari_enzo_sports,
                        ferrari_f50_convertible, ferrari_laFerrari_sports),
            "ford": (ford_focus_hatchback, ford_GT_sports, ford_mustang_coupe),
            "honda": (honda_accord_sedan, honda_city_sedan, honda_civic_hatchback, honda_crv_suv, honda_NSX_sports),
            "hyundai": (hyundai_elantra_sedan, hyundai_iMax_minivan, hyundai_veloster_hatchback),
            "infiniti": (infiniti_q70_sedan, infiniti_qx30_suv, infiniti_qx80_suv),
            "jaguar": (jaguar_ftype_coupe, jaguar_XF_sedan),
            "kia": (kia_carnival_minivan, kia_optima_sedan, kia_picanto_hatchback, kia_sportage_suv),
            "koenigsegg": koenigsegg_agerars_sports,
            "lamborghini": (lamborghini_aventador_sports, lamborghini_huracan_sports, lamborghini_murcielago_sports,
                            lamborghini_urus_suv),
            "landrover": landrover_rangerover_suv,
            "lotus": (lotus_evora_coupe, lotus_exige_convertible),
            "maserati": (maserati_granturismo_coupe, maserati_quattroporte_sedan),
            "mazda": (mazda_cx30_suv, mazda_MX5_convertible),
            "mcLaren": (McLaren_650s_convertible, McLaren_720s_coupe),
            "mercedes": (mercedes_amggt_coupe, mercedes_c43_coupe, mercedes_g63_suv, mercedes_V250_minivan),
            "nissan": (nissan_370z_coupe, nissan_altima_sedan, nissan_gtr_sports, nissan_patrol_suv,
                       nissan_tiida_hatchback),
            "porsche": (porsche_718_convertible, porsche_918_spyder_sports, porsche_cayenne_suv,
                        porsche_panamera_wagon),
            "rollsroyce": (rollsroyce_ghost_sedan, rollsroyce_phantom_sedan),
            "subaru": (subaru_brz_coupe, subaru_impreza_hatchback),
            "tesla": (tesla_models_sedan, tesla_modelx_suv),
            "toyota": (toyota_86_coupe, toyota_camry_sedan, toyota_corolla_sedan, toyota_fortuner_suv,
                       toyota_landcruiser_suv, toyota_pradao_suv, toyota_rav4_suv, toyota_supra_coupe,
                       toyota_tarago_minivan, toyota_yaris_hatchback),
            }

    if search_str.get().lower().rstrip(" ") in cars.keys():
        global search_window
        search_window = Toplevel(root)
        search_window.title("Search")
        search_window.geometry("1366x700")
        search_window.configure(bg="#212121")
        search_window.resizable(False, False)
        the_canvas_search = Canvas(search_window, bg="#212121", borderwidth=0, highlightthickness=0)
        the_canvas_search.pack(side=TOP, fill=BOTH, expand=1)
        my_scrollbar_search = Scrollbar(search_window, orient=HORIZONTAL, command=the_canvas_search.xview)
        my_scrollbar_search.pack(side=BOTTOM, fill=X)
        the_canvas_search.configure(xscrollcommand=my_scrollbar_search.set)
        the_canvas_search.bind('<Configure>',
                               lambda e: the_canvas_search.configure(scrollregion=the_canvas_search.bbox("all")))
        another_frame_search = Frame(the_canvas_search, bg="#212121", borderwidth=0, highlightthickness=0)
        the_canvas_search.create_window((0, 0), window=another_frame_search, anchor="e")

        def rent_search():
            window_rent_search = Toplevel(root)
            window_rent_search.geometry("450x350")
            window_rent_search.configure(bg="#212121")
            window_rent_search.resizable(False, False)
            window_rent_search.title("Renting")

            def button_day_command():
                root.after(3000, lambda: root.destroy())
                button_day_label.config(text="Thank You for Renting")
                button_week.config(state="disabled")
                button_month.config(state="disabled")

            def button_week_command():
                window_rent_search.after(3000, lambda: window_rent_search.destroy())
                button_week_label.config(text="Thank You for Renting")
                button_day.config(state="disabled")
                button_month.config(state="disabled")

            def button_month_command():
                window_rent_search.after(3000, lambda: window_rent_search.destroy())
                button_month_label.config(text="Thank You for Renting")
                button_day.config(state="disabled")
                button_week.config(state="disabled")

            # Photos
            rent_day = PhotoImage(file="rent_for_day.png")
            rent_week = PhotoImage(file="rent_for_week.png")
            rent_month = PhotoImage(file="rent_for_month.png")

            button_day = Button(window_rent_search, image=rent_day, borderwidth=0, bg="#212121",
                                activebackground="#212121",
                                cursor="hand2", command=button_day_command)
            button_week = Button(window_rent_search, image=rent_week, borderwidth=0, bg="#212121",
                                 activebackground="#212121",
                                 cursor="hand2", command=button_week_command)
            button_month = Button(window_rent_search, image=rent_month, borderwidth=0, bg="#212121",
                                  activebackground="#212121",
                                  cursor="hand2", command=button_month_command)

            button_day_label = Label(window_rent_search, bg="#212121", text="", fg="white", font="Helvetica, 15")
            button_week_label = Label(window_rent_search, bg="#212121", text="", fg="white", font="Helvetica, 15")
            button_month_label = Label(window_rent_search, bg="#212121", text="", fg="white", font="Helvetica, 15")

            button_day.image = rent_day
            button_week.image = rent_week
            button_month.image = rent_month

            button_day.grid(row=1, column=1, padx=80, pady=20)
            button_week.grid(row=2, column=1, padx=80, pady=20)
            button_month.grid(row=3, column=1, padx=80, pady=20)

            button_day_label.place(x=133, y=85)
            button_week_label.place(x=133, y=185)
            button_month_label.place(x=133, y=295)

        for i in cars.items():
            if search_str.get().lower() in i:
                for j in cars.get(search_str.get().lower()):
                    row = 2
                    column_search = cars.get(search_str.get().lower()).index(j)
                    Button(another_frame_search, image=j, bg="#212121", width=328, height=600,
                           activebackground="#212121", borderwidth=0, cursor="hand2", command=rent_search,
                           state="normal").grid(row=row, column=column_search, padx=50, pady=40, sticky="E")
                    j.image = j

    elif search_str.get().lower().rstrip(" ") not in cars.keys():
        not_found = Toplevel(root)
        not_found.title("Error Page")
        not_found_page = PhotoImage(file="notfound.png")
        not_found_page.image = not_found_page
        Label(not_found, image=not_found_page).pack()
        not_found.geometry("1920x1080")
        not_found.after(5000, lambda: not_found.destroy())
    search_input.delete(first=0, last=22)


# Canvas for entry
canvas_entry = Canvas(frame_root_scroll, width=100, height=50, bg="#292929", borderwidth=0, highlightthickness=0)
label_search = Label(canvas_entry, image=search_bar, borderwidth=0, bg="#292929")
canvas_entry.place(x=740, y=200)
label_search.pack()
button_search = Button(frame_root_scroll, image=search_button, bg="#292929", borderwidth=0, command=button_check,
                       activebackground="#292929", cursor="hand2", width=42, height=45)
button_search.place(x=1180, y=199)

# Search Box
search_str = StringVar()
search_input = Entry(canvas_entry, width=24, bg="#2F2F2F", font="Helvetica, 20", textvariable=search_str, borderwidth=0,
                     highlightcolor="red", fg="#C6C6C6", insertbackground="#FF6006", cursor="cross")
search_input.bind("<Return>", button_check)
search_input.insert(0, "Search by brand")


def deleting_insert(event):
    search_input.delete(0, "end")
    return None


search_input.bind("<Button-1>", deleting_insert)
search_input.place(x=17, y=8)

root.mainloop()
