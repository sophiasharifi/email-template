import smtplib;      #import server
from string import Template;    #template string in email

def retrieve_contacts(file){
    contact_name = [];
    contact_email = [];

    #opens the file
    with open(file, mode = 'r', encoding = 'utf-8') as contact_file:
        for contact in file:
            contact_name.append(contact_name.split()[0]);
            contact_name.append(contact_email.split()[1]);

    return contact_name, contact_email;
}

def read_template_file(file){
    #opens the file
    with open(file, mode = 'r', encoding = 'utf-8') as template_file:
        read = template_file.read();

    return Template(read);
}

def main(){
    s = smtplib.SMTP(host='smtp.gmail.com', port=465);
}
