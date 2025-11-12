# 📱 App de Troca de Celulares — Arquitetura Serverless na AWS

## 🧠 Visão geral

Este projeto implementa o **backend de um aplicativo de troca de celulares**, utilizando uma **arquitetura 100% serverless** com os principais serviços da AWS.  

A ideia é permitir que usuários **cadastrem anúncios de celulares para troca ou venda**, e que o sistema processe esses anúncios de forma **assíncrona, escalável e automática**, enviando notificações quando o anúncio for publicado com sucesso.

---

## 🏗️ Arquitetura geral




### 🔄 Fluxo resumido

1. O **usuário cria um anúncio** de celular no app.
2. O **API Gateway** recebe a requisição e aciona a **Lambda CreateAd**.
3. A Lambda envia o anúncio para uma **fila SQS**.
4. A **Lambda ProcessQueue** consome mensagens da fila, grava os dados no **DynamoDB** e envia uma notificação via **SNS**.
5. O **SNS NotifyClient** envia uma mensagem de confirmação (e-mail, SMS, push, etc.) para o usuário.

Essa arquitetura é totalmente **escalável, resiliente e de baixo custo**, ideal para aplicativos com grande volume de usuários.

---

## 💡 Motivação e conceito

A proposta é criar uma base sólida para um **aplicativo de trocas de celulares**, no qual os usuários podem:
- Anunciar seus aparelhos disponíveis para troca ou venda;
- Receber notificações quando o anúncio for publicado;
- Garantir que o sistema funcione mesmo em picos de acesso, sem travar.

A arquitetura serverless foi escolhida por:
- Escalar automaticamente conforme a demanda;
- Evitar custos fixos com servidores;
- Garantir confiabilidade e tolerância a falhas;
- Manter o processamento **assíncrono e rápido**.

---

## ☁️ Serviços AWS utilizados

| Serviço | Função |
|----------|--------|
| **API Gateway** | Interface pública do app — recebe os anúncios |
| **Lambda CreateAd** | Processa e envia anúncios para a fila SQS |
| **Amazon SQS** | Fila de mensagens para processamento assíncrono |
| **Lambda ProcessQueue** | Consome a fila, grava no banco e notifica o usuário |
| **Amazon DynamoDB** | Banco NoSQL para armazenar anúncios de celulares |
| **Amazon SNS** | Serviço de notificação — confirma a publicação do anúncio |
