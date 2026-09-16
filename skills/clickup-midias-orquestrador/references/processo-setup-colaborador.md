# Setup inicial de cada colaborador

## Objetivo

Cada colaborador deve ter seu próprio chat de IA conectado ao mesmo ClickUp e orientado pelo mesmo orquestrador. A IA não deve usar uma lista local como fonte atual de clientes, squads ou tarefas; ela consulta o ClickUp em tempo real.

O setup é feito uma vez por conta/chat e repetido quando a pessoa trocar de conta, workspace ou ambiente de IA.

## O que cada colaborador precisa

- conta individual no ClickUp com acesso ao workspace correto;
- conta no Codex, ChatGPT ou outra IA aprovada pela agência;
- conexão/app/MCP do ClickUp disponível e autorizado;
- skill `clickup-midias-orquestrador` instalada ou disponibilizada no ambiente;
- nome, função e squad da pessoa informados no primeiro uso.

Instalar uma skill não substitui conectar e autorizar o ClickUp. A conexão do app e as permissões da conta continuam sendo necessárias.

## Roteiro de implementação

1. O colaborador informa nome, função, squad e escopo de atuação.
2. Conecta o ClickUp no ambiente de IA usando a própria conta autorizada.
3. Instala ou seleciona a skill `clickup-midias-orquestrador`.
4. Cola o prompt de inicialização abaixo.
5. Faz três consultas de leitura para validar workspace, cliente e tarefas.
6. Confere se a IA identificou Conta, Squad e responsáveis sem inventar dados.
7. Testa uma prévia de escrita sem executar.
8. Depois da validação, passa a usar o chat para consultas e atualizações com confirmação simples.

## Prompt de inicialização

```text
Você é meu assistente operacional da agência.

Minha identidade:
- Nome: [NOME]
- Função: [FUNÇÃO]
- Squad: [WOLF, SHARK, KRAKEN ou LION]

Use o ClickUp como fonte única e atualizada para clientes, Conta, Squad, tarefas, responsáveis, prazos, comentários, anexos e histórico. Consulte primeiro o ClickUp; não invente nem use memória local para afirmar o estado atual.

Quando eu pedir uma consulta, apenas leia e responda com os links das tasks relevantes.

Quando eu pedir uma criação ou atualização, localize a Conta exata, a task-pai e o responsável. Se faltar prioridade, pergunte antes de criar. Calcule o vencimento pela matriz: Urgente hoje, Alta no próximo dia útil, Normal em três dias úteis e Baixa em cinco dias úteis.

Antes de qualquer escrita, mostre uma prévia curta com task, cliente, Squad, responsável, prioridade, vencimento, comentário e próximo passo. Só execute depois da minha confirmação simples.

Registre tudo que for operacional no ClickUp. Anexe imagens, PDFs e arquivos à task correta. Não misture clientes por nome parecido e não trate task arquivada como prova de que o cliente saiu.

Ao iniciar, confirme apenas: “Setup recebido. Vou consultar o ClickUp como fonte oficial e respeitar seu escopo de função.”
```

## Testes de validação

Sem alterar nada, o colaborador deve pedir:

- “Liste minhas tarefas atrasadas e as que vencem hoje.”
- “Localize o Panorama e as tasks principais da Conta [cliente].”
- “Mostre meu Squad, meu papel e quais responsáveis aparecem nas tasks desse cliente.”

O teste está aprovado quando a IA:

- encontra o workspace correto;
- usa a Conta exata;
- identifica o Squad pelo campo do ClickUp;
- respeita o papel do colaborador;
- diferencia task aberta, concluída e arquivada;
- não cria, edita, comenta, atribui ou anexa nada sem prévia e confirmação.

## Regra para outras IAs

Se a ferramenta escolhida não tiver conexão funcional com o ClickUp, ela pode ajudar a redigir ou organizar uma prévia, mas não pode ser considerada fonte de verdade nem afirmar que atualizou tarefas. Para sincronização em tempo real, é necessário que a ferramenta tenha o app/MCP do ClickUp autorizado.



