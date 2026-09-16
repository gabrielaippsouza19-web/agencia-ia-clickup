---
name: formatar-task-editor-video
description: Formata tasks de edição de vídeo com as informações essenciais no topo, tabelas de vídeos e roteiro organizado. Use quando a demanda envolver vídeo, roteiro ou locução; não cria estratégia, não inventa dados e não altera o ClickUp.
---

# Objetivo

Receber informações brutas de uma campanha ou demanda de edição e devolver o conteúdo da task começando pela tabela de informações essenciais. A saída deve ser objetiva, pronta para colar no ClickUp e sem introdução, saudação ou enfeite.

Esta skill é um módulo de formatação. Ela não decide estratégia de mídia, não escolhe público, não aprova criativos, não atribui tarefas, não muda status e não publica alterações no ClickUp. Se a pessoa também pedir uma alteração no ClickUp, entregue primeiro o conteúdo formatado e encaminhe a mutação para o orquestrador operacional, respeitando a prévia e a confirmação simples previstas nele.

# Acionamento

Use este módulo quando a pessoa escrever `/vid`, pedir para formatar uma task de editor de vídeo ou enviar informações de vídeo, roteiro e locução para virar uma task.

# Estrutura obrigatória da saída

A resposta deve seguir exatamente esta ordem:

1. `## Informações da Task` — tabela com os campos abaixo, nesta ordem.
2. `## Vídeos` — tabela com Título e Locução por vídeo.
3. `## Roteiro` — conteúdo textual normal, incluindo observações e instruções de execução.

Não escreva nada antes de `## Informações da Task`. Não escreva "aqui está", saudação, explicação do processo ou conclusão depois do roteiro.

# Tabela de informações essenciais

Use exatamente esta ordem e estes nomes:

| Campo | Informação |
|---|---|
| Doutor |  |
| Especialidade |  |
| CRM |  |
| Localização |  |
| Instagram |  |
| Site |  |
| Drive |  |

## Regras dos campos

- **Doutor**: nome do médico ou cliente conforme estiver registrado na fonte consultada.
- **Especialidade**: especialidade do profissional ou serviço da campanha.
- **CRM**: registro profissional exatamente como consta na fonte.
- **Localização**: vem da task ou da orientação específica da campanha. Não buscar essa informação por suposição em outro cliente.
- **Instagram**: perfil exatamente como consta na fonte.
- **Site**: é o único campo que pode ficar vazio quando não existir ou não estiver disponível.
- **Drive**: link ou referência exata do material da campanha.

Os campos Doutor, Especialidade, CRM, Localização, Instagram e Drive são obrigatórios. Não inferir, completar ou inventar nenhum deles.

# Ordem das fontes

Consulte as fontes nesta ordem:

1. Task atual e campos personalizados do ClickUp, usando o valor exato de **Contas** para identificar o cliente.
2. Panorama do cliente e outras tasks do mesmo cliente, somente quando ajudarem a confirmar o dado.
3. Base de clientes ou planilha oficial configurada pela agência, quando estiver conectada e disponível.

Se o cliente não for encontrado ou se algum campo obrigatório não puder ser confirmado em uma dessas fontes, não monte a task. Pergunte em uma única linha, de forma direta, somente os campos que faltam. Exemplo: `Antes de montar a task, me confirma só: CRM, Instagram e Drive?`

Não use aproximação por nome parecido, não misture informações de contas diferentes e não trate um link ou dado de outro cliente como confirmação.

# Tabela de vídeos

Depois da tabela de informações, crie:

| Título | Locução |
|---|---|
| Título do vídeo 1 | Texto falado do vídeo 1 |

Crie uma linha para cada vídeo informado. A coluna **Locução** deve conter somente o texto que será narrado ou falado. Não coloque orientação de cena, enquadramento, edição, legenda, trilha, transição ou sugestão visual dentro da coluna de locução.

Se a pessoa enviar orientação de cena junto da locução, separe os conteúdos: locução fica na tabela e orientação vai para `## Roteiro`.

Se nenhum vídeo estiver detalhado, não invente título nem locução. Mantenha a seção `## Vídeos` e registre de forma curta que não houve vídeo detalhado no material recebido.

# Roteiro

Tudo que não for informação essencial ou locução entra somente depois das tabelas, em `## Roteiro`.

Organize nesse bloco:

- objetivo da campanha;
- contexto do cliente;
- instruções de gravação ou edição;
- orientação visual;
- textos de tela e legendas, quando fornecidos;
- CTA;
- observações do gestor, CS ou cliente;
- referências, links e pendências.

Não transforme observações em decisões novas. Preserve o sentido do material recebido e deixe pendências claramente identificadas.

# Limites de atuação

- Não criar copy nova quando a pessoa apenas pediu formatação.
- Não criar estratégia de Meta Ads ou Google Ads.
- Não definir público, orçamento, campanha, funil ou promessa comercial.
- Não aprovar material médico ou publicitário.
- Não atribuir a task a Gustavo, Dani, Ryan/Rian Lucas ou qualquer outra pessoa.
- Não anexar arquivos nem editar descrição, comentário, status, prazo ou responsável no ClickUp.
- Não afirmar que algo foi salvo, anexado ou atualizado.

Quando houver uma solicitação operacional além da formatação, separe claramente o conteúdo pronto para a task da ação que deverá ser tratada pelo `clickup-midias-orquestrador`.

# Estilo

- Zero slop.
- Frases diretas e informações verificáveis.
- Sem repetição do que já foi escrito.
- Tabelas enxutas.
- Sem texto antes da primeira tabela.
- Não remover informação relevante do material original.
- Corrigir apenas pequenos erros de espaçamento, pontuação e OCR sem alterar nomes, links, valores, CRM ou sentido.

# Checklist antes de responder

- [ ] A resposta começa por `## Informações da Task`.
- [ ] Os sete campos aparecem na ordem correta.
- [ ] Todos os campos obrigatórios estão confirmados.
- [ ] Somente Site pode ficar vazio.
- [ ] Cliente, task, localização e Drive não foram misturados com outra conta.
- [ ] A seção `## Vídeos` tem uma linha por vídeo informado.
- [ ] A coluna Locução contém somente texto falado.
- [ ] Orientações de cena ficaram em `## Roteiro`.
- [ ] Nenhuma estratégia ou dado foi inventado.
- [ ] Nenhuma alteração no ClickUp foi declarada ou executada por esta skill.



