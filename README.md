# 🇧🇷 Monitoramento da Criptomoeda HYPERSKIDS

![Python Version](https://img.shields.io/badge/python-3.7%20%7C%203.8%20%7C%203.9-blue)
![License](https://img.shields.io/badge/license-MIT-green)

## Descrição

Monitoramento automatizado da criptomoeda HYPERSKIDS com alertas de preço e volume via WhatsApp e envio de relatórios por e-mail.

## Funcionalidades

- Monitoramento em tempo real do preço em BRL
- Cálculo automático de lucro/prejuízo
- Relatórios via e-mail
- Alertas via WhatsApp
- Tracking de market cap e volume
- Suporte a fuso horário UTC-3 (Maceió)

## Requisitos

- Python 3.7+
- Twilio Account
- Gmail Account
- API CoinGecko

## Configuração

1. Clone o repositório:
```bash
git clone https://github.com/devdavidejesus/crypto-monitoring-hyperskids.git
cd crypto-monitoring-hyperskids
```

2. Configure as variáveis no arquivo config.py:
```python
TWILIO_ACCOUNT_SID = "seu_sid"
TWILIO_AUTH_TOKEN = "seu_token"
TWILIO_WHATSAPP_NUMBER = "seu_numero_twilio"
YOUR_WHATSAPP_NUMBER = "seu_numero_whatsapp"
EMAIL_ADDRESS = "seu_email"
EMAIL_PASSWORD = "sua_senha"
EMAIL_RECIPIENT = "email_destino"
INITIAL_PRICE = valor_inicial
AMOUNT = quantidade
CRYPTO_ID = "hyperskids"
CRYPTO_SYMBOL = "hysk"
```

3. Instale as dependências:
```bash
pip install requests twilio
```

4. Execute o script:
```bash
python monitor_hyperskids.py
```

## Desenvolvido por

Davi de Jesus
- GitHub: [@devdavidejesus](https://github.com/devdavidejesus)
- LinkedIn: [devdavidejesus](https://linkedin.com/in/devdavidejesus)

## Data de Criação

12/02/2025