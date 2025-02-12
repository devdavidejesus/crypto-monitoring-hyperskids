# Desenvolvido por devdavidejesus
# Data de criação: 12/02/2025
# Descrição: Monitoramento da criptomoeda HYPERSKIDS com alertas de preço e volume via WhatsApp e envio de relatórios por e-mail.

import warnings
from urllib3.exceptions import NotOpenSSLWarning

# Suprimir o aviso NotOpenSSLWarning
warnings.filterwarnings("ignore", category=NotOpenSSLWarning)

import requests
import time
from datetime import datetime, timedelta
from config import (
    TWILIO_ACCOUNT_SID,
    TWILIO_AUTH_TOKEN,
    TWILIO_WHATSAPP_NUMBER,
    YOUR_WHATSAPP_NUMBER,
    EMAIL_ADDRESS,
    EMAIL_PASSWORD,
    EMAIL_RECIPIENT,
    INITIAL_PRICE,
    AMOUNT,
    CRYPTO_ID,
    CRYPTO_SYMBOL,
    VOLUME_THRESHOLD,
    PRICE_CHANGE_THRESHOLD,
    CHECK_INTERVAL,
)
from twilio.rest import Client
import smtplib
from email.mime.text import MIMEText

# Fuso horário de Maceió (UTC-3)
UTC_OFFSET = -3

# Função para enviar e-mail
def send_email(subject, body):
    try:
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = EMAIL_RECIPIENT

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            print("E-mail enviado com sucesso!")
    except Exception as e:
        print(f"Erro ao enviar e-mail: {e}")

# Função para obter dados do CoinGecko
def get_crypto_data():
    url = f"https://api.coingecko.com/api/v3/coins/{CRYPTO_ID}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Erro ao buscar dados do CoinGecko.")
        return None

# Função para calcular lucro ou prejuízo
def calculate_profit_or_loss(current_price):
    total_current_value = current_price * AMOUNT
    total_invested = INITIAL_PRICE * AMOUNT
    profit_loss = total_current_value - total_invested
    return total_current_value, profit_loss

# Função principal
def monitor_hyperskids():
    print("Iniciando monitoramento da HYPERSKIDS...")
    send_email("Início do Monitoramento", "O monitoramento da criptomoeda HYPERSKIDS começou.")

    daily_report = []
    price_history = []  # Armazena os preços para análise de tendência
    volume_history = []  # Armazena os volumes para cálculo da média móvel

    try:
        while True:
            data = get_crypto_data()
            if data:
                current_price = data["market_data"]["current_price"]["brl"]  # Preço em BRL
                market_cap = data["market_data"]["market_cap"]["brl"]  # Market cap em BRL
                volume = data["market_data"]["total_volume"]["brl"]  # Volume em BRL

                total_current_value, profit_loss = calculate_profit_or_loss(current_price)
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                report_entry = (
                    f"{timestamp} - Preço atual: R${current_price:.2f}, "
                    f"Valor total: R${total_current_value:.2f}, "
                    f"Lucro/Prejuízo: R${profit_loss:.2f}"
                )
                daily_report.append(report_entry)
                print(report_entry)

            time.sleep(CHECK_INTERVAL)
    except KeyboardInterrupt:
        send_email("Monitoramento Interrompido", "O monitoramento da criptomoeda HYPERSKIDS foi interrompido.")
        print("Monitoramento interrompido.")

if __name__ == "__main__":
    monitor_hyperskids()