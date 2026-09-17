---
name: arte
description: Formata tasks de design com as tabelas de Cliente e Copy no topo, usando o ClickUp como fonte única e perguntando quando faltar informação obrigatória.
metadata:
  short-description: Formata briefing de arte para o designer
---

# Objetivo

Receba as informações da campanha e devolva a task do designer começando pelas duas tabelas obrigatórias, sem introdução ou enfeite. Todo o restante — observações, formato, referências e orientações — vem depois das tabelas.

# Fonte de dados

- O ClickUp é a fonte única para cliente, localização, Instagram, Drive e demais dados.
- Leia diretamente a task ou o caminho indicado pelo usuário no ClickUp.
- Se um campo necessário não estiver na task, pergunte; não busque em planilhas ou outros lugares, não duplique dados e não infira.

# Estrutura obrigatória da resposta

1. `## Cliente` — tabela com Nome, Localização, Instagram, Site e Drive, nesta ordem.
2. `## Copy` — tabela com Headline, Sub-headline, Parágrafo e CTA, nesta ordem.
3. Só depois das tabelas: observações, formato, referências e demais orientações.

Nada pode vir antes de `## Cliente`.

# Campos obrigatórios

| Tabela | Campo | Obrigatório |
| --- | --- | --- |
| Cliente | Nome | sim |
| Cliente | Localização | sim; cidade + estado (sigla), usada para o pino no mapa |
| Cliente | Instagram | sim |
| Cliente | Site | não; deixar vazio se não existir |
| Cliente | Drive | sim |
| Copy | Headline | sim |
| Copy | Sub-headline | sim |
| Copy | Parágrafo | não; deixar vazio se não houver |
| Copy | CTA | sim |

Se faltar qualquer campo obrigatório, não monte a task. Pergunte em uma linha, listando somente o que falta: `Antes de montar a task, me confirma só: [campos]?`.

# Regras da copy

- A copy pode vir pronta ou como ideia principal.
- O Gestor precisa fornecer pelo menos a estratégia, o que será trabalhado e a vertente do criativo. Se isso não estiver disponível, pergunte antes de ajustar a copy.
- Você pode corrigir português e melhorar a frase sem alterar a estratégia.
- Headline e Sub-headline devem ser curtas, claras e completas; não corte preposições ou palavras apenas para reduzir o tamanho.
- Não invente oferta, preço, promessa, especialidade, localização ou informação médica.

# Regras para o designer

- O Gestor fornece estratégia, copy e briefing; o designer executa a parte visual.
- Informe formato, dimensões, canal, referências e materiais somente quando constarem na task ou forem fornecidos pelo usuário.
- Não substitua a aprovação do Gestor, do CS ou do cliente.
- O conteúdo enviado ao ClickUp deve manter o briefing organizado e permitir que outra pessoa execute sem precisar interpretar o que faltou.

# Regra de consulta ao repositório

Este repositório é a fonte oficial das regras do processo. Ao iniciar uma conversa, e sempre que houver dúvida sobre o formato ou uma possível atualização, consulte a versão mais recente deste arquivo no GitHub antes de montar ou alterar uma task:

https://github.com/gabrielaippsouza19-web/agencia-ia-clickup

Se o GitHub estiver indisponível, informe que está usando a cópia local e não trate uma instrução antiga como regra nova sem confirmação.

# Checklist

- [ ] A resposta começa com `## Cliente`.
- [ ] As tabelas Cliente e Copy aparecem nessa ordem.
- [ ] Todos os campos obrigatórios estão preenchidos ou foram solicitados.
- [ ] Site e Parágrafo são os únicos campos que podem ficar vazios.
- [ ] Estratégia/vertente foi confirmada quando a copy veio apenas como ideia.
- [ ] Português foi revisado sem alterar o sentido.
- [ ] Observações e referências aparecem somente depois das tabelas.

