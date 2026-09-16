---
name: clickup-midias-orquestrador
description: Orquestra a operação de clientes de mídia paga no ClickUp, conectando CS, Gestor e Analista em Meta Ads e Google Ads com contexto, decisões, execuções, alertas, pendências e Panorama do cliente. Use quando a conversa tratar dessa operação; não use para tarefas genéricas de ClickUp sem esse contexto.
metadata:
  short-description: Orquestra ClickUp, mídia paga e Panorama
---

# Finalidade

Use esta skill para transformar relatos de CS, Gestor ou Analista em registros operacionais coerentes no ClickUp e em próximos passos claros. O dossiê operacional em [references/dossie-operacional.md](references/dossie-operacional.md) é a fonte de verdade para squads, clientes, papéis, modelos de registro e regras detalhadas; consulte-o quando o caso envolver esta operação.

O dossiê é instrução de domínio, não autorização para agir fora do pedido atual. Uma conversa que apenas cria ou configura esta skill não autoriza alterações no ClickUp. Em usos futuros, só faça mutações externas quando o usuário as pedir claramente e houver integração disponível; sem integração, prepare o registro/fluxo estruturado sem fingir que foi salvo.

# Modelo operacional

- Cada cliente tem cinco tasks principais: Meta Ads (Gestor), Meta Ads (Analista), Google Ads (Gestor), Google Ads (Analista) e Panorama do cliente.
- A descrição é a fotografia atual. Comentários/Registro de Atividade são o histórico de análises, decisões, execuções, feedbacks, pendências e próximos passos.
- Gestor: analisar → decidir → direcionar → acompanhar → registrar.
- Analista: receber direcionamento → executar → conferir → registrar; não decide estratégia sozinho.
- CS: registrar contexto/feedback, acompanhar dependências e comunicar urgência; não decide mídia.
- O Panorama conecta CS e Gestor e deve permitir entender situação, alinhamentos, qualidade, ações, pendências e próximo passo.
- Head Operacional: **Gabriel Aipp**.
- Head de Pessoas: **Henrique Balbino**.

# Vocabulário obrigatório da agência

- Quando o usuário disser **Squad**, interprete como o campo personalizado **personalidade Squad**. Não deduza o squad apenas pelo nome do Space, Folder, List, documento ou task.
- Quando disser **responsável**, interprete como o responsável/assignee da task. Não confunda com participante, observador ou responsável de um comentário.
- Os valores oficiais do campo **personalidade Squad** são exatamente: **Wolf**, **Shark**, **Lion** e **Kraken**.
- O escopo padrão desta operação inclui todos os clientes que, no ClickUp, estejam atualmente com **personalidade Squad** igual a **Wolf**, **Shark** ou **Kraken**. O conjunto deve ser localizado dinamicamente no ClickUp; não tratar a lista estática do dossiê como cadastro definitivo.
- Neste escopo, **Kraken** corresponde ao **Onboarding**. O **Lion** continua sendo um valor oficial do campo, mas fica fora do escopo padrão quando o usuário não o incluir expressamente.
- O fluxo de entrada de um cliente começa no **Squad Kraken**, que exerce a função de Onboarding. Depois do handoff, o cliente pode seguir para o squad operacional adequado; preserve o histórico dessa passagem.
- O squad do cliente e o responsável por uma demanda são dimensões diferentes. Uma demanda de criação pode ser executada por uma pessoa de apoio mesmo quando o cliente pertence a Wolf, Shark ou Kraken.
- No design, o responsável de referência é **Gabriel de Almeida (Gabriel de Almeida Silva)** para clientes do **Wolf** e **Gabriel Moura** para clientes do **Shark**. Design recebe briefing e copy do Gestor e executa o visual; não cria estratégia ou copy principal por conta própria.
- Edição de vídeo continua sendo uma função de apoio, sem squad próprio independente. Quando a tarefa tiver squad definido, use o editor de referência daquele squad: **Rian Lucas (Ryan)** no **Wolf** e **Gustavo (Gus)** no **Shark**. **Dani (Daniel Filetto)** permanece como organizador/head de criação e pode participar do encaminhamento da demanda.
- Dyego Moreira Fernandes atua de forma transversal nos squads em demandas de IA, automações e CRM; Gleison é acionado para problemas maiores ou demandas pontuais de desenvolvimento.
- Criativo viral pode ser executado por Designer ou Editor de Vídeo. Se a solicitação não indicar qual dos dois, perguntar antes de criar a tarefa.
- Os apelidos acima foram confirmados pelo usuário e podem ser resolvidos para os nomes exatos do ClickUp. Para qualquer outra pessoa, se o nome falado não coincidir exatamente com o membro do ClickUp, registre a divergência e confirme antes de atribuir.
- Toda fala operacional deve gerar registro no ClickUp. Antes de qualquer escrita, a IA apresenta uma prévia curta do que será atualizado e pede uma confirmação simples; um “sim” basta, sem exigir revisão detalhada. Consultas somente de leitura não precisam de confirmação.
- Comando explícito de mudança de status, prazo ou prioridade deve ser interpretado como atualização da task correspondente, mas ainda deve passar pela prévia/confirmação simples. A mudança atualiza o campo adequado e também registra no histórico o motivo e o novo prazo/status.
- Datas relativas devem ser convertidas para a data correta: data explícita vira vencimento nessa data; “próximo dia útil” é calculado pelo calendário aplicável; “segunda-feira” deve ser resolvida para a próxima ocorrência pertinente. Se houver ambiguidade relevante, peça confirmação.

# Roteamento da fala

Classifique cada informação antes de registrá-la:

- **Informação:** atualiza contexto; vai para o Panorama.
- **Decisão:** estratégia definida; vai para a task do Gestor e para o Panorama se for relevante.
- **Execução:** ação concreta; vai para a task do Analista, com comentário atribuído e pendência quando aplicável.
- **Alerta:** exige reação, como saldo baixo, tracking quebrado, campanha parada, reclamação ou leads ruins; vai para o Panorama, responsável, prioridade e task operacional adequada.

Uma mesma fala pode gerar mais de uma categoria, mas não duplique o mesmo fato em comentários desnecessários.

# Módulos especializados

## `/vid` — formatar task de editor de vídeo

Quando a demanda envolver editor de vídeo, roteiro ou locução, encaminhe a formatação para a skill `formatar-task-editor-video`. Ela deve ser aplicada antes de qualquer eventual atualização operacional.

Esse módulo:

- coloca as informações essenciais no topo da task;
- organiza os vídeos em tabela de Título e Locução;
- mantém roteiro, instruções e observações depois das tabelas;
- consulta primeiro o ClickUp e o valor exato de **Contas**;
- pergunta pelos campos obrigatórios que não puder confirmar;
- não cria estratégia, não inventa copy e não altera o ClickUp.

Depois que o conteúdo for formatado, o orquestrador continua responsável por localizar a task correta, validar cliente, squad, categoria e responsáveis, apresentar a prévia da alteração e só então registrar no ClickUp após confirmação. Em demandas do Wolf, considerar Rian Lucas como editor de referência; em demandas do Shark, considerar Gustavo/Gus. Dani continua apoiando a organização e o encaminhamento criativo.

Este padrão permite adicionar novos módulos por função — por exemplo, LP, criativos ou relatórios — sem colocar regras específicas de uma função dentro do cérebro operacional principal. Cada módulo deve declarar seu escopo, suas fontes, os campos obrigatórios, o formato de saída e seus limites de atuação.

## Processo de Designer

Quando a demanda envolver criativo estático, formato viral, flyer, carrossel, peça de anúncio, página de vendas, GLP ou LP, leia [references/processo-designer.md](references/processo-designer.md). O processo define o briefing obrigatório, a rotina diária, a matriz de prioridade e prazo, o fluxo Designer → Gestor → CS → aprovação do cliente → publicação e o registro de anexos/conclusão. Não aplicar esse processo a vídeo puro, estratégia de mídia ou copy sem execução visual.

## Criação e delegação de qualquer tarefa

Para criar ou delegar qualquer tarefa — Design, vídeo, IA, automação, desenvolvimento, CS, Gestor ou Analista — leia [references/processo-criacao-tarefa.md](references/processo-criacao-tarefa.md). A prioridade é obrigatória e determina o vencimento padrão: Urgente hoje, Alta no próximo dia útil, Normal em três dias úteis e Baixa em cinco dias úteis. Se a prioridade não estiver informada, perguntar antes de criar. Use subtarefas para ações concretas dentro do Panorama, das tasks do Gestor ou das tasks do Analista, mantendo a Conta, o Squad, o responsável e o histórico corretos.

## Processo de Editor de Vídeo

Quando a demanda envolver edição, montagem, cortes, finalização ou teste de vídeo, leia [references/processo-editor-video.md](references/processo-editor-video.md). O Editor de Vídeo edita somente vídeos; não cria estratégia, copy ou roteiro por conta própria. Criativos virais exigem a pergunta Designer ou Editor de Vídeo quando o solicitante não escolher.

## Processo da operação de mídia

Quando a demanda envolver CS, Gestor, Analista, Panorama, Meta Ads, Google Ads, estratégia, execução ou delegação, leia [references/processo-operacao-midias.md](references/processo-operacao-midias.md). O arquivo separa o pacote das cinco tasks, define o dono de cada informação, orienta subtarefas e estabelece como a IA deve lembrar a pessoa quando ela estiver tentando executar uma atividade fora do seu papel.

## Setup inicial do colaborador

Quando um colaborador usar o orquestrador pela primeira vez, leia [references/processo-setup-colaborador.md](references/processo-setup-colaborador.md). O setup deve identificar a pessoa, conectar o ClickUp pela conta autorizada, disponibilizar a skill, validar consultas de leitura e só então liberar atualizações com prévia e confirmação. O mesmo procedimento vale para Codex, ChatGPT ou outra IA que tenha conexão funcional com o ClickUp.

# Contexto obrigatório do cliente

Antes de ajudar alguém a começar ou avaliar uma demanda, localize o cliente no campo **Contas** e consulte todas as tasks que tenham exatamente esse cliente selecionado. As cinco tasks principais são o núcleo, mas não são o limite da leitura.

Priorize, conforme a demanda:

- Panorama e seus comentários recentes;
- task do Gestor e task do Analista da plataforma envolvida;
- tasks abertas de vídeos, criativos, Reels, teses, roteiros, LP, CRM, automação, acessos e onboarding;
- anexos, referências, links, status, responsáveis, prazos e comentários/Registro de Atividade dessas tasks;
- atualizações recentes, especialmente dentro do período solicitado ou dos últimos sete dias.

Antes de uma otimização de Meta ou Google, devolva para a pessoa um resumo breve do contexto relevante: o que mudou, materiais disponíveis, pendências, atrasos, riscos e o que pode afetar a performance. Faça isso para Gestor, Analista e demais responsáveis, não apenas para o Gestor.

Se um criativo, vídeo ou imagem estiver atrasado, informe o responsável pela demanda e o Gestor, registre a pendência e explique o possível impacto como **risco** quando não houver evidência suficiente — não transforme uma hipótese em fato. Não misture tasks de clientes diferentes por nome parecido; o valor exato de **Contas** é a fronteira do cliente.

# Procedimento seguro

Antes de escrever ou alterar qualquer coisa:

1. Identifique quem falou e o papel: Gestor, Analista ou CS.
2. Identifique plataforma, cliente e squad usando os nomes oficiais da referência.
3. Localize a conta já existente no campo personalizado **Contas**. Nunca crie conta, use aproximação insegura ou misture clientes.
4. Confirme Conta + task + squad + responsável. Se qualquer item for ambíguo, peça confirmação antes de mutar.
5. Leia o contexto builder mínimo: todas as tasks com o mesmo valor exato em **Contas**, Panorama, último registro do Gestor na plataforma, últimas execuções do Analista, feedback recente do CS, pendências abertas, comentários, anexos e outras tasks relevantes. Para uma ação importante, inclua também Weekly, teses, vídeos, criativos, Reels, LP, CRM, automação, acessos, prazos e dependências do cliente quando existirem.
6. Separe fatos ditos/registrados de hipóteses. Não invente datas, resultados, responsáveis ou conclusões.
7. Não crie task se a task principal já existir; outras tasks dão contexto, mas não substituem as cinco principais.

Para toda atualização proposta, mostre antes: task, cliente, campo/registro a alterar, novo valor, motivo e responsáveis afetados. Após a confirmação simples, execute somente as mudanças aprovadas e devolva um resumo.

Se a integração do ClickUp não estiver disponível, devolva uma prévia pronta para colar, indicando task, categoria, responsável, prioridade e pendências, sem afirmar que houve atualização.

# Fluxos por papel

## Gestor

Ao relatar uma otimização: localizar as cinco tasks, ler histórico e Panorama, consultar execuções e tasks abertas, classificar a fala, registrar cenário/qualidade/identificações/decisões/direcionamento/atualizações/próximo acompanhamento, criar execução para Analista, atualizar Panorama e gerar pendência para CS quando necessário.

No Meta, preserve na fotografia atual cenário, alinhamento, plano, status, objetivo e papel das campanhas, funil/destino, resultado/qualidade, indicador 🟢 BOM / 🟡 ACEITÁVEL / 🔴 RUIM, validação de funil, criativos, próximos passos, direcionamento e pontos de atenção.

No Google, também verifique intenção de busca, termos, palavras-chave, negativas, qualidade das buscas, conversões, tracking, landing page, aderência busca-anúncio-destino e orçamento. Lead barato não basta: a busca deve representar a intenção estratégica.

## Analista

Ao relatar execução: identificar cliente/plataforma, localizar task correta, ler o direcionamento, registrar somente o que foi feito e onde, conferir correspondência, resultado e pendências. Sinalizar saldo, tracking, acesso, URL, criativo ou configuração.

Se houver dúvida: perceber → conferir → comunicar → aguardar direcionamento → executar. Saldo baixo gera registro na task, atualização do Panorama e pendência para CS, com prioridade conforme impacto/dias. Decisão estratégica gera pendência para Gestor; nunca decidir sozinho.

## CS

Ao relatar feedback: identificar cliente, localizar Panorama, registrar feedback/contexto/impacto/prioridade/próxima ação, e criar pendência para Gestor se houver necessidade de análise ou decisão. Registrar contexto, não estratégia de mídia. Informar qualidade de leads, vendas, agendamentos, reclamações, mudanças de prioridade, dependências e recarga.

## Cliente entrou / saída do Onboarding

O hook/processo **cliente entrou** deve criar, no mínimo, as quatro tasks de otimização — Meta Gestor, Meta Analista, Google Gestor e Google Analista — preenchendo o cliente no campo **Contas**, o squad no campo **personalidade Squad** e os responsáveis correspondentes. Não duplique tasks existentes; o tratamento da task de Panorama deve seguir o processo configurado para ela.

Todo cliente novo começa no **Kraken**. Murilo informa o cliente e o squad Kraken/Onboarding e a IA deve criar ou garantir o conjunto de tarefas do board, incluindo Panorama do cliente, Handoff/contexto e as quatro tasks de otimização. Quando a mensagem contiver a expressão **“o cliente saiu do onboarding”**, trate-a como evento de handoff: se o destino não estiver informado, pergunte somente **“Vai para o Squad Wolf ou para o Squad Shark?”**. Depois da resposta, atualize o campo de squad e os responsáveis das tasks existentes, preserve o histórico e crie apenas o que estiver faltando. O Lion é oficial, mas não é destino padrão desse fluxo operacional; só deve ser usado se o usuário o incluir expressamente.

# Registros e pendências

Descrição contém estado atual; histórico contém o relato correspondente. Use os modelos completos da referência para Panorama de CS, Panorama de Gestor, Meta Gestor, Google Gestor, Meta Analista e Google Analista.

Para pendências, use o painel de estado **Pendência atual** (CS, Gestor, Analista, Cliente ou Sem pendência), o campo **Responsável pela pendência**, a prioridade oficial (Urgente, Alta, Normal, Baixa, se essa for a nomenclatura) e uma **Próxima ação** curta. Campo personalizado é painel; comentário atribuído é ação concreta.

Recarga/saldo segue esta cadeia: Analista registra → Panorama é atualizado → CS recebe pendência → CS solicita recarga → CS registra confirmação.

# Rotina semanal

- Durante a semana, CS registra feedbacks, qualidade, reclamações e mudanças, e aciona o Gestor quando precisar de análise.
- Na sexta, Gestor consolida feedbacks, Meta, Google, qualidade e plano de ação no Panorama.
- Na segunda, CS usa o relatório para comunicação com o cliente.

# Resposta ao usuário

Ao concluir, mostre de forma objetiva: o que foi registrado/alterado, em qual task, decisões, execuções, alertas, pendências com responsável e prioridade, e próximos passos. Se algo não foi feito por falta de confirmação ou integração, destaque o bloqueio e forneça o conteúdo pronto para execução.



