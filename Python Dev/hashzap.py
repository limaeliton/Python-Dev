# framework
# pip install flet

# Título Hashzap
# Botão de Iniciar o chat
#     Poup
#         Bem vindo ao Hashzap
#         Escreva seu nome
#         Entrar no chat
# Chat
#     Eliton entrou no chat
#     Mensagens do usuário
# Campo para enviar mensagem
# Botão de enviar

# 1º import flet as ft
import flet as ft

# 2º def main(pagina)
def main(pagina):
   titulo =  ft.Text("Hashzap")
   
   nome_usuario = ft.TextField(label="Escreva seu nome")
   
   chat = ft.Column()
   
   def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()
   
   pagina.pubsub.subscribe(enviar_mensagem_tunel)
   
   def enviar_mensagem(envento):
      # colocar o nome do usuário na mensagem
       texto_campo_mensagem = f"{nome_usuario.value}: {campo_mensagem.value}"
       pagina.pubsub.send_all(texto_campo_mensagem)
       # limpar o campo_mensagem
       campo_mensagem.value = ""
       pagina.update()
       
   campo_mensagem = ft.TextField(label="Escreva sua mensagem aqui" ,on_submit=enviar_mensagem)
   
   botao_enviar = ft.ElevatedButton("Enviar" ,on_click=enviar_mensagem)
   
   def entrar_chat(envento):
       # fechar o popup
       popup.open = False
       # tirar o botão "Inicar chat" da tela
       pagina.remove(botao_inicar)
       # adicionar o nosso chat
       pagina.add(chat)
       # criar o campo de enviar mensagem
       linha_mensagem = ft.Row(
           [campo_mensagem, botao_enviar]
       )
       pagina.add(linha_mensagem)
       # botão de enviar mensagem
       texto = f"{nome_usuario.value} entrou no chat"
       pagina.pubsub.send_all(texto)
       pagina.update()
    
   popup = ft.AlertDialog(
       open=False, 
       modal=True, 
       title=ft.Text("Bem vindo ao Hashzap"),
       content= nome_usuario,
       actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)]
       )
   
   def inicar_chat(envento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        
   botao_inicar = ft.ElevatedButton("Inicar chat" , on_click=inicar_chat)
   
   
   pagina.add(titulo)
   pagina.add(botao_inicar)
   
   
   
# 3º ft.app(main) Aplicativo
# ft.app(main , view=ft.WEB_BROWSER ) SITE
ft.app(main)