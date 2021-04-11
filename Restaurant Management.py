import tkinter as tk 
from tkinter import *
from tkinter import ttk 
from tkinter import messagebox as msg 
import time
import shutil
import os
import re
import requests
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#====================Functions====================

def tiffen_search_ftn():
    tiffen_search_result["state"]="normal"
    tiffen_search_result.delete("0","end")
    tiffen_search_result["state"]="disabled"
    search_elements_tiffen=0
    tiffen_search_entry_ftn=tiffen_search_entry.get()

    if tiffen_search_entry_ftn=="":
        msg.showerror("Error","Please Enter Any Name Of The Food To Search")
    else:
        for tiffen_search_entry_ftn_ele in range(len(tiffen_items)):
            if tiffen_search_entry_ftn in tiffen_items[tiffen_search_entry_ftn_ele] or tiffen_search_entry_ftn.lower() in tiffen_items[tiffen_search_entry_ftn_ele][1].lower():
                if search_elements_tiffen==0:
                    tiffen_search_result["state"]="normal"
                    tiffen_search_result.insert("0",tiffen_search_entry_ftn_ele)
                    search_elements_tiffen+=1
                    tiffen_search_result["state"]="disabled"
                else:
                    tiffen_search_result["state"]="normal"
                    tiffen_search_result.insert("end",","+str(tiffen_search_entry_ftn_ele))
                    tiffen_search_result["state"]="disabled"

            


def icecream_juice_shake_search_ftn():
    icecream_juice_shake_search_result["state"]="normal"
    icecream_juice_shake_search_result.delete("0","end")
    icecream_juice_shake_search_result["state"]="disabled"
    search_elements_icecream_juice_shake=0
    icecream_juice_shake_search_entry_ftn=icecream_juice_shake_search_entry.get()

    if icecream_juice_shake_search_entry_ftn=="":
        msg.showerror("Error","Please Enter Any Name Of The Food To Search")
    else:
        for icecream_juice_shake_search_entry_ftn_ele in range(len(icecream_juice_shake_items)):
            if icecream_juice_shake_search_entry_ftn in icecream_juice_shake_items[icecream_juice_shake_search_entry_ftn_ele] or icecream_juice_shake_search_entry_ftn.lower() in icecream_juice_shake_items[icecream_juice_shake_search_entry_ftn_ele][1].lower():
                if search_elements_icecream_juice_shake==0:
                    icecream_juice_shake_search_result["state"]="normal"
                    icecream_juice_shake_search_result.insert("0",icecream_juice_shake_search_entry_ftn_ele)
                    search_elements_icecream_juice_shake+=1
                    icecream_juice_shake_search_result["state"]="disabled"
                else:
                    icecream_juice_shake_search_result["state"]="normal"
                    icecream_juice_shake_search_result.insert("end",","+str(icecream_juice_shake_search_entry_ftn_ele))
                    icecream_juice_shake_search_result["state"]="disabled"

def bill_no_setting_ftn():
    path="Bills"
    try:
        total_bills=os.listdir(path)
    except FileNotFoundError:
            os.makedirs("Bills") 
            
            
    total_bills=os.listdir(path)
    total_bills_number=len(total_bills)
    if total_bills_number!=0:
        new_bill_number=total_bills_number+1
        bill_no_entry["state"]="normal"
        bill_no_entry.insert(0,new_bill_number)
        bill_no.set(new_bill_number)
        bill_no_entry["state"]="disabled"
    else:
        new_bill_number=1
        bill_no_entry["state"]="normal"
        bill_no_entry.insert(0,new_bill_number)
        bill_no.set(new_bill_number)
        bill_no_entry["state"]="disabled"

def bill_saving_ftn():
    global bill_items
    global bill_items_number
    total_gst=0
    total_amount=0
    
    bill_no_setting_ftn()

    with open("Bills\\"+bill_no.get()+".txt","w") as bill:
                bill.write("Heman's Restaurant (Pure Veg)".center(80," "))
                bill.write("\n")
                bill.write("Address : 9/1,5/1 Rajavathani Street,".center(80," "))
                bill.write("\n")
                bill.write("          Shevapet, Salem-###### (TN)".center(80," "))
                bill.write("\n")
                bill.write("Mobile : 6374###4##".center(80," "))
                bill.write("\n")
                bill.write("Email : hemanth#########@gmail.com".center(80," "))
                bill.write("\n")
                bill.write("\n")
                gst_number="GST Number : "+gstin_entry_lbl.get()
                bill_number="               Bill Number : "+bill_no.get()
                bill.write(gst_number.center(40," "))
                bill.write(bill_number.center(35," "))
                bill.write("\n")
                bill.write("=====================================Recipt=====================================")
                bill.write("\n")
                bill.write("{:<4}{:<5}{:25}{:<5}{:<17}{:<5}{:<14}{:<6}".format("Se.","Code","Item".center(24," "),"Cost","Quan.".center(16," "),"CGST","SGST".center(13," "),"Total"))
                bill.write("\n")
                

                for bill_items_printing in range(len(bill_items)):
                    bill.write("{:<4}{:<5}{:25}{:<5}{:<17}{:<5}{:<14}{:<6}".format(str(bill_items[bill_items_printing][0]).center(3," "),bill_items[bill_items_printing][1].center(4," "),str(bill_items[bill_items_printing][2]).center(24," "),str(bill_items[bill_items_printing][3]).center(4," "),str(bill_items[bill_items_printing][4]).center(16," "),str(bill_items[bill_items_printing][5]),str(bill_items[bill_items_printing][6]).center(13," "),str(bill_items[bill_items_printing][7]).center(5," ")))
                    total_gst+=bill_items[bill_items_printing][5]
                    total_amount+=bill_items[bill_items_printing][7]
                    bill.write("\n")
                bill.write("================================================================================\n")
                bill.write("{:<4}{:<5}{:25}{:<5}{:<16}{:<5} {:<14}{:<6}".format("","","","","",str(round(total_gst,2)),str(round(total_gst,2)).center(13," "),str(total_amount).center(5," ")))
                bill.write("\n\n")
                bill.write("{:<4}{:<5}{:25}{:<5}{:<10}{}{:<6}".format("","","","","","Total Amount(Without GST) =",str(total_amount)))
                bill.write("\n")
                bill.write("{:<4}{:<5}{:25}{:<5}{:<10}{:<26}{}{:<6}".format("","","","","","Total GST ("+str(round(total_gst,2))+" + "+str(round(total_gst,2))+") ","=",int(round(total_gst+total_gst,2))))
                bill.write("\n")
                bill.write("{:<4}{:<5}{:25}{:<5}{:<16}{:<7}{:<14}{:<6}".format("","","","","","","Total Amount =",int(total_amount+round(total_gst,2)+round(total_gst,2))))
                bill.write("\n\n               *****Thanks For Visiting Have A Nice Time*****               ")

    


def bill_adding_ftn():
    global bill_items_number
    global bill_items

    items_number=len(bill_items)
    items_number-=1

    if bill_items_number%2!=0:
            bill_tree.insert("","end",tags="bg_color1",values=bill_items[items_number])
            bill_items_number+=1
    else:
            bill_tree.insert("","end",tags="bg_color2",values=bill_items[items_number])
            bill_items_number+=1




def tiffen_bill_adding_ftn():
    global bill_items_number
    global bill_items

    tiffen_item_entry_ftn=tiffen_item_entry.get()
    tiffen_item_quantity_ftn=tiffen_item_quantity.get()
    tax_ftn=tax_entry.get().split("%")

    if tiffen_item_entry_ftn!="":

        if tiffen_item_quantity_ftn=="":
            msg.showinfo("Information","The Quantity Column Is Empty So It Is Considered As 1")
            tiffen_item_quantity_ftn=1

        tiffen_bill_item_serial=str(bill_items_number)
        tiffen_bill_item_code="T"+tiffen_item_entry_ftn
        tiffen_bill_item_name=tiffen_items[int(tiffen_item_entry_ftn)][1]
        tiffen_bill_item_price=tiffen_items[int(tiffen_item_entry_ftn)][2]
        tiffen_bill_item_quantity=int(tiffen_item_quantity_ftn)
        tiffen_bill_item_sgst_not_rounded=(((tiffen_bill_item_price*int(tax_ftn[0]))/100)*tiffen_bill_item_quantity)
        tiffen_bill_item_sgst=round(tiffen_bill_item_sgst_not_rounded,2)
        tiffen_bill_item_cgst=tiffen_bill_item_sgst
        tiffen_bill_item_total=tiffen_bill_item_price*tiffen_bill_item_quantity

        item=(tiffen_bill_item_serial,tiffen_bill_item_code,tiffen_bill_item_name,tiffen_bill_item_price,tiffen_bill_item_quantity,tiffen_bill_item_sgst,tiffen_bill_item_cgst,tiffen_bill_item_total)
        
        bill_items+=[(item)]

        bill_adding_ftn()

    else:
        msg.showerror("Error","Please Enter The Tiffen Item Serial To Add Into The Bill")

    tiffen_item_entry.set("")
    tiffen_item_quantity.set("")


def ijs_bill_adding_ftn():
    global bill_items_number
    global bill_items

    ijs_item_entry_ftn=icecream_juice_shake_item_entry.get()
    ijs_item_quantity_ftn=icecream_juice_shake_item_quantity.get()
    tax_ftn=tax_entry.get().split("%")

    if ijs_item_entry_ftn!="":

        if ijs_item_quantity_ftn=="":
            msg.showinfo("Information","The Quantity Column Is Empty So It Is Considered As 1")
            ijs_item_quantity_ftn=1

        ijs_bill_item_serial=str(bill_items_number)
        ijs_bill_item_code="S"+str(ijs_item_entry_ftn)
        ijs_bill_item_name=icecream_juice_shake_items[int(ijs_item_entry_ftn)][1]
        ijs_bill_item_price=icecream_juice_shake_items[int(ijs_item_entry_ftn)][2]
        ijs_bill_item_quantity=int(ijs_item_quantity_ftn)
        ijs_bill_item_sgst_not_rounded=(((ijs_bill_item_price*int(tax_ftn[0]))/100)*ijs_bill_item_quantity)
        ijs_bill_item_sgst=round(ijs_bill_item_sgst_not_rounded,2)
        ijs_bill_item_cgst=ijs_bill_item_sgst
        ijs_bill_item_total=ijs_bill_item_price*ijs_bill_item_quantity
        
        item=(ijs_bill_item_serial,ijs_bill_item_code,ijs_bill_item_name,ijs_bill_item_price,ijs_bill_item_quantity,ijs_bill_item_sgst,ijs_bill_item_cgst,ijs_bill_item_total)

        bill_items+=[(item)]

        bill_adding_ftn()


    else:
        msg.showerror("Error","Please Enter The Ice Cream, Juice, Shake Item Serial To Add Into The Bill")

    icecream_juice_shake_item_entry.set("")
    icecream_juice_shake_item_quantity.set("")


def on_click_bill_tree(*kwargs):
    global bill_items
    global bill_items_number

    
    ch=msg.askyesnocancel("Information","Click Yes To Update\nClick No To Delete\nOtherwise Click Cancel ")

    if ch==True:
        cursor=bill_tree.focus()
        contents=bill_tree.item(cursor)
        row_contents=contents["values"]
        
        if row_contents=="":
            pass
        else:

            if "T" in row_contents[1]:
                tiffen_add_btn["state"]="disabled"
                tiffen_update_btn["state"]="normal"
                icecream_juice_shake_add_btn["state"]="disabled"
                serial_matching=re.match(r"([A-Z]+)([0-9]+)",row_contents[1])
                if serial_matching:
                    serial_adding=serial_matching.group()
                tiffen_item_entry.set(serial_adding[1])
                tiffen_item_quantity.set(row_contents[4])

            elif "S" in row_contents[1]:
                icecream_juice_shake_add_btn["state"]="disabled"
                icecream_juice_shake_update_btn["state"]="normal"
                tiffen_add_btn["state"]="diabled"
                main_screen["background"]="light grey"
                tiffen_frame["background"]="light grey"
                tiffen_billing["background"]="light grey"
                tiffen_items_search_lbl["background"]="light grey"
                tiffen_item_quantity_lbl["background"]="light grey"
                tiffen_item_lbl["background"]="light grey"
                serial_matching=re.match(r"([A-Z]+)([0-9]+)",row_contents[1])
                if serial_matching:
                    serial_adding=serial_matching.group()
                    icecream_juice_shake_item_entry.set(serial_adding[1])
                    icecream_juice_shake_item_quantity.set(row_contents[4])
                
    if ch==False:
        delete_row=bill_tree.selection()
        ch_delete_confirmation=msg.askyesno("Warning","Are You Sure You Want To delete The Selected Item")
        if ch_delete_confirmation==True:

            cursor=bill_tree.focus()
            contents=bill_tree.item(cursor)
            row_contents=contents["values"]

            bill_items_number-=1
            del bill_items[row_contents[0]-1]

            bill_tree.delete(delete_row)


def tiffen_update_ftn():
    cursor=bill_tree.focus()
    contents=bill_tree.item(cursor)
    row_contents=contents["values"]

    bill_tree.delete((row_contents[0])-1)
   
def clear_all_ftn():
    global bill_items
    global bill_items_number
    global presence

    bill_items_number=1
    bill_items=[]
    presence=0
    mobile_number_bill.set("")
    mail_bill.set("")
    bill_no_setting_ftn()

    row=bill_tree.get_children()
    if row!=():
        for row_item in row:
            bill_tree.delete(row_item)


def print_ftn(*args):
    global presence
    print_user_choice=msg.askyesno("Confirmation","Are You Sure You Want To Take Print?")
    if bill_items_number!=1:
        if print_user_choice==True:
            if presence==0:
                bill_saving_ftn()
                presence+=1
            filename_print="Bills\\"+bill_no.get()+".txt"
            os.startfile(filename_print,"print")
            msg.showinfo("Information","The Bill Has Been Successfully Printrd")
            
    else:
        msg.showwarning("Warning","Please Add Items To The Bill")


def sms_ftn(*args):
    global presence

    mobile_number_bill_ftn=mobile_number_bill.get()

    if mobile_number_bill_ftn=="":
        msg.showerror("Error","Please Enter The Mobile Number To Proceed")
    else:
        user_sms_choice=msg.askyesno("Confirmation","Are You Sure You Want To Send SMS To : "+mobile_number_bill_ftn+" ?")
        if bill_items_number!=1:
            if user_sms_choice==True:
                total_gst_sms=0
                total_amount_sms=0
                if presence==0:
                    bill_saving_ftn()
                    presence+=1
                for bill_item_sms in range(len(bill_items)):
                    total_gst_sms+=bill_items[bill_item_sms][5]
                    total_amount_sms+=bill_items[bill_item_sms][7]
                sms_bill="""
                Heman's Restaurent(Pure Veg)
        Bill Amount (Without GST) ={}
        Total GST ({}+{}) ={}
        Total Bill Amount ={}

            Thanks For Visiting""".format(total_amount_sms,round(total_gst_sms,2),round(total_gst_sms,2),int(round(total_gst_sms,2)+round(total_gst_sms,2)),int(total_amount_sms+round(total_gst_sms,2)+round(total_gst_sms,2)))

 
        
                def sms_sending_ftn():
                    url="https://www.fast2sms.com/dev/bulk"
                    params={
                        "authorization":"#Paste Your API Key",            #Paste Your Generated API key here if no generate it from fast2sms site.
                        "sender_id":"FSTSMS",
                        "message":sms_bill,
                        "language":"english",
                        "route":"p",
                        "numbers":mobile_number_bill_ftn
                    }

                    try:
                        response=requests.get(url,params=params)
                        result=response.json()
                        bill_saving_ftn()
                        msg.showinfo("Information","The Message Has Been Successfully Sent!!!")
                        
                    except:
                        msg.showerror("Error","An Error Occured\nCheck Your Internet Connection")


                variable_progress=sms_sending_ftn()
        else:
            msg.showwarning("Warning","Please Add Items To The Bill And Proceed")

def mail_ftn(*args):
    global presence
    mail_bill_ftn=mail_bill.get()

    if mail_bill_ftn=="":
        msg.showerror("Error","Please Enter The Mail Address And Proceed")
    else:
        mail_user_choice=msg.askyesno("Confirmation","Are You Sure You Want To Mail To : "+mail_bill_ftn+" ?")
        if bill_items_number!=1:
            if mail_user_choice==True:
                if presence==0:
                    bill_saving_ftn()
                    presence+=1
                email="#Mail_I'd"                       #Paste Your Mail I'd here
                password="#Password"                    #Paste your Password here (before turn on less secure app in your mail settings)

                email_message=MIMEMultipart()
                email_message["From"]=email
                email_message["To"]=mail_bill_ftn
                email_message["Subject"]="Heman's Restaurant(pure veg)"
                content_body="The Bill Is Attached With This Mail"

                email_message.attach(MIMEText(content_body,"plain"))
                email_text=email_message.as_string()
                attachment_file="Bills\\"+bill_no.get()+".txt"
                attachment=open(attachment_file,"r")

                part=MIMEBase("application","octet-stream")
                part.set_payload((attachment).read())
        
                part.add_header("Content-Disposition","attachment",filename="Your Bill.docx")

                email_message.attach(part)
                email_text=email_message.as_string()
            
                server=smtplib.SMTP("smtp.gmail.com",587)
                server.starttls()
                server.login(email,password)

                    
                server.sendmail(email,mail_bill_ftn,email_text)
                server.quit()

                msg.showinfo("Done","The Mail Has Been Successfully Sent!!!")
                
        else:
            msg.showwarning("Warning","Please Add Items To The Bill And Proceed")
def psm_ftn():
    if bill_items_number!=1:
        if mobile_number_bill.get()=="":
            if mail_bill.get=="":
                print_ftn()
                sms_ftn()
                mail_ftn()
            else:
                msg.showwarning("Warning","Please Enter The Mail Address")
        else:
            msg.showwarning("Warning","Please Enter The Mobile Number")
    else:
        msg.showwarning("Warning","Please Add The Items To The Bill and Proceed")



        
#====================Items===================

bill_items_number=1
bill_items=[]
presence=0

tiffen_items=[("Item","Cost"),(1,"Small Idly",3),(2,"Idly",10),(3,"Kuzi Paniyarm",8),(4,"Dosa",10),(5,"Plain Dosa",20),
(6,"Paper Dosa",35),(7,"Uthapam",30),(8,"Ghee Roast",30),(9,"Mushroom Dosa",55),(10,"Cauliflower Dosa",55),(11,"Onion Dosa",50),
(12,"Chappathi",15),(13,"Poori",15),(14,"Soola Poori",25),(15,"Paroota",20),(16,"Kothu Paroota",70),(17,"Califlower Manchooriyan",70),
(18,"Mushroom Manchooriyan",70),(19,"Idiyapam",10),(20,"Pongal",50)]

icecream_juice_shake_items=[("Item","Cost"),(1,"Vanilla Ice Cream",35),(2,"Chocolate Ice Cream",40),(3,"Mango Ice Cream",55),(4,"Pineapple Ice Cream",55),
(5,"Strawberry Ice Cream",55),(6,"Orange Ice Cream",55),(7,"Pistachio Ice Cream",45),(8,"Watermelon Ice Cream",55),
(9,"Watermellon Juice",50),(10,"Pomegranate Juice",50),(11,"Blueberry Juice",50),(12,"Grape Fruit Juice",50),
(13,"Cranberry Juice",50),(14,"Orange Juice",50),(15,"Apple Juice",50),(16,"Kiwi Juice",50),(17,"Milk Shake",80),
(18,"Chocolate Milk Shake",80),(19,"Salted Carmel Milk Shake",80),(20,"Peanut Butter Milk Shake",80)]





#====================Starting====================

main_screen=tk.Tk()
main_screen.title("Restaurant Billing Management")
main_screen.geometry("1350x700+0+0")
main_screen.config(background="violet")

heading=tk.Label(text="Heman's Restaurant Billing Management",foreground="dark blue",background="#FFFF99",font=("jokerman",24,"bold")).grid(row=0,column=1,sticky="N"+"W"+"E"+"S")

#====================Tiffen Frame===================

tiffen_frame=tk.LabelFrame(main_screen,text="Tiffen",background="violet",foreground="dark green",font=("chiller",30,"bold"),border=6)
tiffen_frame.grid(row=2,column=0,padx=3)

#====================Tiffen Tree View====================

tiffen_table=ttk.Treeview(tiffen_frame,columns=("serial","item name","cost per item"),height=20)

tiffen_table.heading("serial",text="Serial")
tiffen_table.heading("item name",text="Item Name")
tiffen_table.heading("cost per item",text="Cost Per Item (Rs)")

tiffen_table["show"]="headings"
tiffen_table.column("serial",width=47)
tiffen_table.column("item name",width=160)
tiffen_table.column("cost per item",width=108)

#====================Tiffen Data Inserting====================

for tiffen_items_inserting in range(len(tiffen_items)):
    if tiffen_items_inserting==0:
        pass
    else:
        tiffen_items_loop=list(tiffen_items[tiffen_items_inserting])
        tiffen_table.insert("","end",values=tiffen_items_loop)

tiffen_table.pack(expand=1,fill="both")

#====================Ice Cream, Juice and Shake Frame====================

icecream_juice_shake_frame=tk.LabelFrame(main_screen,text="Ice Cream\Juice\Shake",background="violet",foreground="dark green",font=("chiller",28,"bold"),border=6)
icecream_juice_shake_frame.grid(row=2,column=2)

#====================Ice Cream, Juice And Shake TreeView====================

icecream_juice_shake_table=ttk.Treeview(icecream_juice_shake_frame,column=("serial","item name","cost per item"),height=20)

icecream_juice_shake_table.heading("serial",text="Serial")
icecream_juice_shake_table.heading("item name",text="Item Name")
icecream_juice_shake_table.heading("cost per item",text="Cost Per Item (Rs)")

icecream_juice_shake_table["show"]="headings"
icecream_juice_shake_table.column("serial",width=47)
icecream_juice_shake_table.column("item name",width=160)
icecream_juice_shake_table.column("cost per item",width=108)

#====================Ice Cream, Juice And Shake data Inserting====================

for icecream_juice_shake_inserting in range(len(icecream_juice_shake_items)):
    if icecream_juice_shake_inserting==0:
        pass
    else:
        icecream_juice_shake_items_loop=list(icecream_juice_shake_items[icecream_juice_shake_inserting])
        icecream_juice_shake_table.insert("","end",values=icecream_juice_shake_items_loop)

icecream_juice_shake_table.pack(expand=1,fill="both")


#===================Tiffen Billing Frame===================

tiffen_billing=tk.LabelFrame(main_screen,text="Tiffin Billing",foreground="yellow",background="violet",font=("consolas",17,"bold"))
tiffen_billing.grid(row=1,column=0)

#===================Tiffen Billing And Its Components===================

tiffen_search_entry=tk.StringVar()
tiffen_items_search_lbl=tk.Label(tiffen_billing,text="Search:",foreground="black",background="violet",font=("arial",15))
tiffen_items_search_lbl.grid(row=0,column=0)
tiffen_search_entry_lbl=ttk.Entry(tiffen_billing,textvariable=tiffen_search_entry,width=15,font=("arialblack",13))
tiffen_search_entry_lbl.grid(row=0,column=1)

tiffen_search_result=ttk.Entry(tiffen_billing,width=10,state=DISABLED,font=(15))#-----Tiffen Search Result-----
tiffen_search_result.grid(row=0,column=2,padx=3)

tiffen_search_btn=ttk.Button(tiffen_billing,text="Search",command=tiffen_search_ftn).grid(row=1,column=1)


#-----Tiffen Item Serial-----

tiffen_item_entry=tk.StringVar()
tiffen_item_lbl=tk.Label(tiffen_billing,text="Serial To Add:",foreground="blue",background="violet",font=("arialblack",15))
tiffen_item_lbl.grid(row=2,column=0,columnspan=2,sticky="E")

tiffen_item_entry_lbl=ttk.Entry(tiffen_billing,textvariable=tiffen_item_entry,font=(18),width=8).grid(row=2,column=2,sticky="W")

#-----Tiffen Item Quantity-----

tiffen_item_quantity=tk.StringVar()
tiffen_item_quantity_lbl=tk.Label(tiffen_billing,text="Number Of Quantity:",foreground="blue",background="violet",font=("arialblack",15))
tiffen_item_quantity_lbl.grid(row=3,column=0,columnspan=2,sticky="E")

tiffen_item_quantity_entry=ttk.Entry(tiffen_billing,textvariable=tiffen_item_quantity,font=(18),width=8)
tiffen_item_quantity_entry.grid(row=3,column=2,sticky="W")

tiffen_add_btn=ttk.Button(tiffen_billing,text="Add",command=tiffen_bill_adding_ftn)
tiffen_add_btn.grid(row=5,column=2)

tiffen_update_btn=ttk.Button(tiffen_billing,text="Update",command=tiffen_update_ftn)
tiffen_update_btn.grid(row=5,column=0,columnspan=2)
tiffen_update_btn["state"]="disabled"

#====================Ice Cream Juice And Shake Billing Frame===================

icecream_juice_shake_billing_frame=tk.LabelFrame(main_screen,text="Ice\Juice\Shake Billing",background="violet",foreground="yellow",font=("consolas",17,"bold"))
icecream_juice_shake_billing_frame.grid(row=1,column=2)

#====================Ice Cream Juice And Shake Billing And Its Components===================

icecream_juice_shake_search_entry=tk.StringVar()
icecream_juice_shake_search_lbl=tk.Label(icecream_juice_shake_billing_frame,text="Search:",foreground="black",background="violet",font=("arial",15)).grid(row=0,column=0)
icecream_juice_shake_search_entry_lbl=tk.Entry(icecream_juice_shake_billing_frame,textvariable=icecream_juice_shake_search_entry,width=15,font=("arialblack",13))
icecream_juice_shake_search_entry_lbl.grid(row=0,column=1)

#-----SearchResult-----

icecream_juice_shake_search_result=tk.Entry(icecream_juice_shake_billing_frame,state="disabled",font=(13),width=10)
icecream_juice_shake_search_result.grid(row=0,column=2,padx=5)

icecream_juice_shake_search_btn=ttk.Button(icecream_juice_shake_billing_frame,text="Search",command=icecream_juice_shake_search_ftn).grid(row=1,column=1)

#-----Ice Cream Juice Shake Item Serial-----

icecream_juice_shake_item_entry=tk.StringVar()
icecream_juice_shake_item_lbl=tk.Label(icecream_juice_shake_billing_frame,text="Serial To Add:",foreground="blue",background="violet",font=("arialblack",15)).grid(row=2,column=0,columnspan=2,sticky="E")

icecream_juice_shake_item_entry_lbl=ttk.Entry(icecream_juice_shake_billing_frame,textvariable=icecream_juice_shake_item_entry,font=(18),width=8)
icecream_juice_shake_item_entry_lbl.grid(row=2,column=2,sticky="W")

#-----Ice Cream Juice Shake Item Quantity-----

icecream_juice_shake_item_quantity=tk.StringVar()
icecream_juice_shake_item_quantity_lbl=tk.Label(icecream_juice_shake_billing_frame,text="Number Of Quantity:",foreground="blue",background="violet",font=("arialblack",15)).grid(row=3,column=0,columnspan=2,sticky="E")

icecream_juice_shake_item_quantity_entry=ttk.Entry(icecream_juice_shake_billing_frame,textvariable=icecream_juice_shake_item_quantity,font=(18),width=8)
icecream_juice_shake_item_quantity_entry.grid(row=3,column=2,sticky="W")

icecream_juice_shake_add_btn=ttk.Button(icecream_juice_shake_billing_frame,text="Add",command=ijs_bill_adding_ftn)
icecream_juice_shake_add_btn.grid(row=5,column=2)

icecream_juice_shake_update_btn=ttk.Button(icecream_juice_shake_billing_frame,text="Update")
icecream_juice_shake_update_btn.grid(row=5,column=0,columnspan=2)
icecream_juice_shake_update_btn["state"]="disabled"

#====================Bill Frame======================
bill_frame=tk.LabelFrame(main_screen,text="Bill & Its Settings",foreground="lime",background="violet",font=("courier",20,"bold"),border=9)
bill_frame.grid(row=1,column=1,rowspan=2)

#====================Bill Components=====================

#-----Tax Settings-----

tax_entry=tk.StringVar()
tax_lbl=tk.Label(bill_frame,text="Tax : ",background="violet",font=("kokila",20)).grid(row=0,column=0)
tax_combo_lbl=ttk.Combobox(bill_frame,textvariable=tax_entry,width=8,font=(15))
tax_combo_lbl["values"]=["5%","12%","18%"]
tax_combo_lbl.set("18%")
tax_combo_lbl.grid(row=0,column=1)


gstin_number_lbl=tk.Label(bill_frame,text="GSTIN Number : ",background="violet",font=("kokila",20)).grid(row=0,column=2)
gstin_entry_lbl=tk.Entry(bill_frame,font=(15),width=15)
gstin_entry_lbl.insert("end","GST123456789#####")
gstin_entry_lbl.grid(row=0,column=3)
gstin_entry_lbl["state"]="disabled"

bill_no=tk.StringVar()
bill_no_lbl=tk.Label(bill_frame,text="Bill No. :",background="violet",font=("kokila",20)).grid(row=0,column=4)
bill_no_entry=tk.Entry(bill_frame,textvariable=bill_no,width=7,font=(15),state="disabled")
bill_no_entry.grid(row=0,column=5)

#-----Bill Treeview-----

bill_tree_style=ttk.Style()
bill_tree_style.configure("mystyle.Treeview",highlightthickness=0,border=0,font=("gorgia",15))
bill_tree_style.configure("mystyle.Treeview.Heading",font=("arial",16,"underline"),background="green")

bill_tree=ttk.Treeview(bill_frame,columns=("serial","item_code","item_name","price","quantity","sgst","cgst","total"),height=21,style="mystyle.Treeview")

bill_tree.heading("serial",text="Se.")
bill_tree.heading("item_code",text="Code")
bill_tree.heading("item_name",text="Item Name")
bill_tree.heading("price",text="Price")
bill_tree.heading("quantity",text="Quantity")
bill_tree.heading("sgst",text="SGST")
bill_tree.heading("cgst",text="CGST")
bill_tree.heading("total",text="Total")

bill_tree["show"]="headings"
bill_tree.column("serial",width=35,anchor="center")
bill_tree.column("item_code",width=60,anchor="center")
bill_tree.column("item_name",width=190,anchor="center")
bill_tree.column("price",width=65,anchor="center")
bill_tree.column("quantity",width=90,anchor="center")
bill_tree.column("sgst",width=70,anchor="center")
bill_tree.column("cgst",width=70,anchor="center")
bill_tree.column("total",width=70,anchor="center")

bill_tree.tag_configure("bg_color1",background="misty rose")
bill_tree.tag_configure("bg_color2",background="aqua")
bill_tree.bind("<ButtonRelease-1>",on_click_bill_tree)

bill_tree.grid(row=1,column=0,columnspan=6)

bill_options_frame=tk.LabelFrame(bill_frame,text="Options",background="violet",foreground="black",font=(15))
bill_options_frame.grid(row=2,column=0,columnspan=6)

print_btn=tk.Button(bill_options_frame,text="Print",font=("arial",16,"bold"),bd=5,background="yellow",foreground="black",command=print_ftn).grid(row=0,column=0,padx=5)

save_btn=tk.Button(bill_options_frame,text="Save",font=("arial",16,"bold"),bd=5,background="yellow",foreground="black",command=bill_saving_ftn).grid(row=0,column=1,padx=5)

clear_all_btn=tk.Button(bill_options_frame,text="Clear All",bd=5,background="black",foreground="yellow",font=("arial",16,"bold"),command=clear_all_ftn).grid(row=0,column=2,padx=5)

exit_btn=tk.Button(bill_options_frame,text="Exit",bd=5,foreground="yellow",background="black",font=("arial",16,"bold")).grid(row=0,column=3,padx=5)

sms_btn=tk.Button(bill_options_frame,text="SMS To",bd=5,background="dark blue",foreground="white",font=("arial",16,"bold"),command=sms_ftn).grid(row=0,column=4,padx=5)

mail_btn=tk.Button(bill_options_frame,text="Mail To",bd=5,background="dark blue",foreground="white",font=("arial",16,"bold"),command=mail_ftn).grid(row=0,column=5,padx=5)

psm_btn=tk.Button(bill_options_frame,text="PSM",bd=5,background="aqua",foreground="red",font=("arial",16,"bold"),command=psm_ftn).grid(row=0,column=6,padx=5)

bill_personal_frame=tk.Frame(bill_options_frame)
bill_personal_frame.grid(row=1,columnspan=7,column=0,pady=5)

mobile_number_bill=tk.StringVar()
mobile_number_bill_lbl=tk.Label(bill_personal_frame,text="Mobile :",font=("arial",16,"bold"),foreground="black",background="violet").grid(row=0,column=0,sticky="W")
mobile_number_bill_entry=tk.Entry(bill_personal_frame,textvariable=mobile_number_bill,font=(18)).grid(row=0,column=1,sticky="W",padx=5)

mail_bill=tk.StringVar()
mail_bill_lbl=tk.Label(bill_personal_frame,text="Mail :",font=("arial",16,"bold"),foreground="black",background="violet").grid(row=0,column=2,padx=5,sticky="E")
mail_bill_entry=tk.Entry(bill_personal_frame,textvariable=mail_bill,font=(18),width=30).grid(row=0,column=3,sticky="E")

bill_no_setting_ftn()




main_screen.mainloop()
