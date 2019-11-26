import argparse
import time


print("""
 ____           _    __ _                                           
|  _ \ ___  ___| |_ / _(_)_  _____ _ __ _   _ _ __  _ __   ___ _ __ 
| |_) / _ \/ __| __| |_| \ \/ / _ \ '__| | | | '_ \| '_ \ / _ \ '__|
|  __/ (_) \__ \ |_|  _| |>  <  __/ |  | |_| | |_) | |_) |  __/ |   
|_|   \___/|___/\__|_| |_/_/\_\___|_|   \__,_| .__/| .__/ \___|_|   
                                             |_|   |_|              
""")

parser = argparse.ArgumentParser()
parser.add_argument('-d', help='Name of your domain', dest='domain_name')
parser.add_argument('-H', help='Name of your hostname', dest='hostname')
args = parser.parse_args()

domain_name = args.domain_name
hostname = args.hostname


text = ("""
# See /usr/share/postfix/main.cf.dist for a commented, more complete version


# Debian specific:  Specifying a file name will cause the first
# line of that file to be used as the name.  The Debian default
# is /etc/mailname.
#myorigin = /etc/mailname

smtpd_banner = $myhostname ESMTP $mail_name (Ubuntu)
biff = no

# appending .domain is the MUA's job.
append_dot_mydomain = no

# Uncomment the next line to generate "delayed mail" warnings
#delay_warning_time = 4h

readme_directory = no

# See http://www.postfix.org/COMPATIBILITY_README.html -- default to 2 on
# fresh installs.
compatibility_level = 2

# TLS parameters
smtpd_tls_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
smtpd_tls_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
smtpd_use_tls=yes
smtpd_tls_session_cache_database = btree:${data_directory}/smtpd_scache
smtp_tls_session_cache_database = btree:${data_directory}/smtp_scache

# See /usr/share/doc/postfix/TLS_README.gz in the postfix-doc package for
# information on enabling SSL in the smtp client.

smtpd_relay_restrictions = permit_mynetworks permit_sasl_authenticated defer_unauth_destination
#myhostname = """+str(hostname)+""" #Default setting for linode is: localhost.members.linode.com
myhostname = """+str(domain_name)+"""
alias_maps = hash:/etc/aliases
alias_database = hash:/etc/aliases
mydestination = mail."""+str(domain_name)+""", localhost, localhost.localdomain, localhost
relayhost = 
mynetworks = 127.0.0.0/8 [::ffff:127.0.0.0]/104 [::1]/128
mailbox_size_limit = 0
recipient_delimiter = +
inet_interfaces = all
inet_protocols = all


# My edits

mime_header_checks = regexp:/etc/postfix/header_checks
header_checks = regexp:/etc/postfix/header_checks

#transport_maps = hash:/etc/postfix/transport 

# SSL Stuff
smtpd_tls_security_level = may
smtp_tls_security_level = may
smtp_tls_loglevel = 1
smtpd_tls_loglevel = 1
""")

if domain_name == None:
    print("Please enter domain name")
elif hostname == None:
    print("Please enter your Jumpbox hostname")
else:
    time.sleep(1)
    print(text)