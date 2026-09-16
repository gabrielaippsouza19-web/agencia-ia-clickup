# Processo universal de criação e delegação de tarefas

Este processo vale para toda a operação: Design, edição/teste de vídeo, IA, automações, CRM, desenvolvimento, mídia paga, CS, Gestor e Analista.

## Informações obrigatórias antes de criar

Antes de criar uma tarefa, localizar ou confirmar:

- cliente e valor exato do campo **Conta**;
- squad no campo **Squad**;
- tipo da demanda;
- tarefa-pai correta, quando a demanda for uma ação de um cliente já existente;
- responsável pela execução;
- resultado esperado;
- prioridade;
- prazo ou regra de vencimento.

Se a prioridade não for informada, não inventar. Perguntar:

> Qual prioridade: Urgente (hoje), Alta (próximo dia útil), Normal (3 dias úteis) ou Baixa (5 dias úteis)?

Se houver uma data explícita, manter essa data e ainda solicitar a prioridade quando ela não tiver sido informada. A data explícita prevalece sobre o cálculo padrão, mas a prioridade continua sendo registrada.

## Matriz global de prioridade e vencimento

| Prioridade do ClickUp | Vencimento padrão |
| --- | --- |
| Urgente | Hoje |
| Alta | Próximo dia útil |
| Normal | Até 3 dias úteis |
| Baixa | Até 5 dias úteis |

Regras:

- prazo explícito de cliente, reunião, lançamento ou campanha prevalece sobre a matriz;
- tarefa atrasada deve ser destacada mesmo que esteja com prioridade Normal ou Baixa;
- comentários, Registro de Atividade e descrição podem justificar elevação da prioridade;
- campanha parada, risco financeiro, reunião no mesmo dia ou bloqueio que impeça a operação podem justificar Urgente;
- a IA deve registrar o motivo quando elevar ou reduzir uma prioridade;
- prioridade e vencimento são campos diferentes e devem ser preenchidos separadamente.

## Roteamento por tipo de demanda

| Demanda | Tarefa ou destino | Responsável de referência |
| --- | --- | --- |
| Criativo estático, flyer, carrossel, formato viral, anúncio visual, LP ou página de vendas | Task de Design/Criativos | Wolf: Gabriel de Almeida; Shark: Gabriel Moura |
| Edição ou teste de vídeo | Task de vídeo | Wolf: Rian Lucas; Shark: Gustavo/Gus; Dani organiza quando necessário |
| IA, automação, CRM ou alteração técnica do Med Scale System | Task de Suporte/IA | Dyego Moreira Fernandes; Gleison em demandas maiores ou pontuais de desenvolvimento |
| Estratégia, cobrança, aprovação, qualidade de lead ou informação do cliente | Panorama do cliente | Subtarefa atribuída ao CS |
| Decisão estratégica de Meta ou Google | Task da plataforma do Gestor | Subtarefa atribuída ao Gestor |
| Execução operacional em Meta ou Google | Task da plataforma do Analista | Subtarefa atribuída ao Analista |
| Analista precisa de informação ou cobrança do cliente | Panorama do cliente | Subtarefa atribuída ao CS |

O squad pertence ao cliente e vem do campo **Squad**. O responsável vem da natureza da demanda e da tabela acima; não usar o nome do squad como substituto do responsável.

## Quando usar subtarefa

Criar subtarefa quando houver uma ação concreta, com dono e prazo, que precise ser acompanhada sem perder o contexto da tarefa-pai.

Exemplos:

- CS precisa de uma decisão do Gestor: subtarefa na task de Meta/Google do Gestor, atribuída ao Gestor;
- Gestor decidiu uma execução: subtarefa na task correspondente do Analista, atribuída ao Analista;
- Gestor ou Analista precisa que o cliente seja cobrado: subtarefa no Panorama, atribuída ao CS;
- Analista precisa de acesso, material ou resposta: subtarefa no Panorama, atribuída ao CS;
- CS recebeu uma informação que exige estratégia: contexto no Panorama e subtarefa para o Gestor.

Uma subtarefa deve ter ação específica, por exemplo: “Solicitar ao cliente a aprovação dos criativos do Plano Anual de Botox”, e não apenas “ver cliente”.

## Fluxo de criação

1. Interpretar a fala e classificar a demanda.
2. Localizar a Conta exata e consultar as tasks abertas, o Panorama e o histórico relevante.
3. Escolher a tarefa-pai ou confirmar que realmente é necessária uma tarefa nova.
4. Identificar o responsável pela execução.
5. Confirmar a prioridade; se faltar, perguntar antes de criar.
6. Calcular o vencimento pela matriz ou usar a data explícita.
7. Apresentar uma prévia com cliente, squad, task-pai, nome, responsável, prioridade, vencimento, descrição e próximo passo.
8. Após confirmação simples, criar a tarefa/subtarefa e registrar o contexto no ClickUp.

Não criar duplicatas. Se a ação já existir, atualizar a task existente, registrar o novo contexto e atribuir a pendência correta.

## Conclusão da tarefa

Quando a pessoa informar que concluiu:

- localizar a task correta pela Conta e pelo squad;
- registrar o que foi feito, onde foi feito e o resultado;
- anexar imagens, PDFs ou arquivos enviados no chat à task correta;
- registrar pendências e próximo passo;
- atualizar status, responsável e vencimento conforme o fluxo da função;
- encaminhar para revisão, aprovação ou publicação quando aplicável.

Toda alteração externa deve passar por prévia e confirmação simples, salvo consulta somente de leitura.



