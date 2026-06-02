Aqui está uma versão super básica, limpa e resumida do README, focada apenas no essencial para qualquer pessoa entender e ligar o projeto rapidamente:

Markdown
# 🚪 Controlo de Portas com ESP32

[cite_start]Este projeto usa uma placa ESP32 com **MicroPython** para controlar a abertura e o fecho de 3 portas (Informática, Professores e Almoxarifado) usando servomotores, LEDs e um display OLED[cite: 3].

<p align="center">
  <img src=https://github.com/matheusaribeirodev/Projeto-com-3-servo/blob/main/tw.png
</p>
f

---

## 🔌 Pinos e Ligações

* **Display OLED:** `SDA` -> GPIO 21 | [cite_start]`SCL` -> GPIO 22 [cite: 3]
* **LEDs:** Verde (Abre) -> GPIO 26 | [cite_start]Vermelho (Fecha) -> GPIO 25 [cite: 3]

### Portas e Botões:
1. **💻 Informática:** Servo -> GPIO 18 | Botão Abrir -> GPIO 14 | [cite_start]Botão Fechar -> GPIO 12 [cite: 3]
2. **👥 Professores:** Servo -> GPIO 19 | Botão Abrir -> GPIO 32 | [cite_start]Botão Fechar -> GPIO 0 [cite: 3]
3. **📦 Almoxarifado:** Servo -> GPIO 23 | Botão Abrir -> GPIO 2 | [cite_start]Botão Fechar -> GPIO 33 [cite: 3]

---

## 🕹️ Como Funciona

* [cite_start]**Ao carregar no botão de ABRIR:** O servo gira para **90°**, o LED Verde pisca e o ecrã mostra `"PORTA ABERTA"`[cite: 3].
* [cite_start]**Ao carregar no botão de FECHAR:** O servo gira para **0°**, o LED Vermelho pisca e o ecrã mostra `"PORTA FECHADA"`[cite: 3].

---

## 🚀 Como Testar

1. [cite_start]Abra o simulador no link do [Wokwi](https://wokwi.com/projects/465209512720545793)[cite: 3].
2. Clique no botão de **Play** (Iniciar Simulação).
3. [cite_start]Clique nos botões coloridos para abrir ou fechar as portas de cada sala[cite: 3].

---
[cite_start]🔬 *Projeto desenvolvido por Matheus Augusto Ribeiro.
