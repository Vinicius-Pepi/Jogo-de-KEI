from email.policy import default
from subprocess import call


define atendente = Character("Atendente")
define cliente = Character("Cliente")
default notakei = 0

image cliente bravo ="images/EmojiVermelho.png"
image cliente feliz ="images/EmojiAmarelo.png"
image cliente triste ="images/EmojiAzul.png"
image cliente apaixonado ="images/EmojiRosa.png"
image cliente assustado ="images/EmojiRoxo.png"
image cliente desconfiado ="images/EmojiVerde.png"
image fundo ="images/fundo.jpeg"
image atendente ="images/atendente.png"

label start:
    

    scene fundo: 
    show screen hbox_screen
        zoom 2
    atendente "Esse é o fundo"


    show atendente at truecenter:
        zoom 0.5
        yalign 0.98
        xalign 0.02
    with dissolve
    atendente "Esse é o cliente"
    


    atendente "Rodriguem vai se fude"
    return
