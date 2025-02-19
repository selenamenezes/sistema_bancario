# Sistema Bancário V2

Este projeto é uma simulação de um sistema bancário simples desenvolvido em Python. Ele oferece funcionalidades básicas de cadastro de usuários, criação de contas bancárias, depósitos, saques, exibição de extratos e listagem de contas.

## Funcionalidades

### 1. Cadastro de Usuário
A função `criar_usuario` permite cadastrar novos usuários no sistema. O endereço do usuário é formatado pela função `end_formatado`. Cada usuário é identificado pelo seu CPF, e não é possível cadastrar dois usuários com o mesmo CPF.

### 2. Criação de Conta
A função `criar_conta` permite criar uma nova conta bancária para um usuário previamente cadastrado. Cada conta é associada a um CPF de um usuário existente.

### 3. Depósito
A função `depositar` permite realizar depósitos na conta bancária. Apenas valores maiores ou iguais a 1 são aceitos.

### 4. Saque
A função `sacar` permite realizar saques na conta bancária. Existem algumas regras para a realização de saques:
- O valor do saque não pode ser maior que o saldo disponível.
- O valor do saque deve ser maior ou igual a 1.
- O valor do saque não pode exceder o limite de saque definido.
- Existe um limite diário para o número de saques.

### 5. Extrato
A função `exibir_extrato` exibe o extrato da conta, incluindo todos os depósitos e saques realizados, bem como o saldo atual.

### 6. Listagem de Contas
A função `listar_contas` exibe todas as contas bancárias cadastradas no sistema, juntamente com os detalhes do titular da conta.

### Menu
A função `main` é responsável por exibir o menu de operações e gerenciar a interação do usuário com o sistema. As opções do menu incluem:
- [1] Novo usuário
- [2] Nova conta
- [3] Depositar
- [4] Sacar
- [5] Extrato
- [6] Listar contas
- [0] Sair