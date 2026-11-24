# Prática 5 - Serviço de Buzzer Automático com SystemD
Matheus Araujo - 14598171
Edson Neto - 14566780 

Projeto desenvolvido para Raspberry Pi (OS Bookworm) com o objetivo de reproduzir uma escala musical (C4 a B4) automaticamente durante a inicialização do sistema utilizando um serviço SystemD.

## Hardware
- Raspberry Pi
- Buzzer passivo conectado ao pino **GPIO 18** (suporte a PWM) e GND.

## Estrutura dos Arquivos
- `tocar_escala.py`: Script principal em Python 3 utilizando `gpiozero` (`TonalBuzzer`) para tocar a escala de Dó (C4) a Si (B4) em loop.
- `parar_buzzer.py`: Script auxiliar chamado pelo `ExecStop` para garantir o silenciamento do buzzer ao parar o serviço.
- `buzzer.service`: Arquivo de configuração do SystemD.

## Configuração do Serviço (SystemD)
O serviço foi configurado para rodar como `root` com a variável 
`Environment="HOME=/tmp"`, garantindo que a biblioteca `lgpio` tenha permissões para acessar o hardware PWM e criar arquivos temporários durante o boot, além de um atraso inicial de 5 segundos (`ExecStartPre=/bin/sleep 5`) para aguardar a inicialização completa dos pinos GPIO.

### Comandos utilizados na Raspberry Pi
```bash
sudo cp buzzer.service /lib/systemd/system/
sudo systemctl daemon-reload
sudo systemctl enable buzzer.service
sudo systemctl start buzzer.service
```
