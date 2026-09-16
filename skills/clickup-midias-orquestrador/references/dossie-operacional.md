# Dossiê operacional — ClickUp + Meta Ads + Google Ads + Panorama do cliente

Este arquivo é a referência detalhada da skill `clickup-midias-orquestrador`. Ele consolida regras, papéis, estruturas de tasks, squads, clientes e arquitetura de automação da operação. Use-o como base oficial em conversas sobre esta operação.

## 1. Estrutura por cliente

Cada cliente possui cinco tasks principais:

1. Otimização no Meta Ads (Gestor)
2. Otimização no Meta Ads (Analista)
3. Otimização no Google Ads (Gestor)
4. Otimização no Google Ads (Analista)
5. Panorama do cliente

Princípio:

- Gestor analisa, decide, direciona, acompanha e registra.
- Analista recebe direcionamento, executa, confere e registra.
- CS registra contexto e feedback do cliente, acompanha pendências e utiliza o Panorama.
- A IA conecta as tasks e evita atualização manual repetida.

O detalhamento de criação, prioridade, subtarefas e delegação está em [references/processo-criacao-tarefa.md](processo-criacao-tarefa.md). O detalhamento da operação entre CS, Gestor e Analista está em [references/processo-operacao-midias.md](processo-operacao-midias.md).

## 2A. Liderança e método

- Head Operacional: **Gabriel Aipp**.
- Head de Pessoas: **Henrique Balbino**.
- A metodologia por tipo de cliente ainda está em construção. Não inventar nomes finais, categorias ou regras metodológicas; usar apenas as definições que forem posteriormente confirmadas.

## 2. Regra de informação

**Descrição = fotografia atual.**

**Registro de Atividade = histórico.**

A descrição contém apenas o estado atual e o que continua válido. Comentários/Registro de Atividade guardam análises, decisões, execuções, feedbacks, pendências e próximos passos.

## 3. Papéis

### Gestor

Fluxo: **ANALISAR → DECIDIR → DIRECIONAR → ACOMPANHAR → REGISTRAR**

Responsabilidades:

- analisar conta e estratégia;
- interpretar resultado e qualidade;
- validar funil, tracking e coerência;
- decidir estratégia;
- definir próximos passos;
- direcionar Analista;
- acompanhar execução;
- atualizar contexto relevante para CS/Panorama.

### Analista

Fluxo: **DIRECIONAMENTO → EXECUÇÃO → CONFERÊNCIA → REGISTRO**

Regra principal: **O Gestor define. O Analista executa.**

O Analista:

- executa exatamente o direcionamento;
- confere campanha, grupo, anúncio, palavra-chave ou configuração;
- identifica erros e divergências;
- comunica falta de informação;
- não toma decisão estratégica sozinho;
- registra execução;
- gera alerta de saldo, tracking, acesso ou erro operacional quando necessário.

Se houver dúvida: **Perceber → Conferir → Comunicar → Aguardar direcionamento → Executar.**

### CS

O CS:

- registra feedback do cliente;
- informa qualidade dos leads, vendas, agendamentos, reclamações e mudanças de prioridade;
- acompanha dependências do cliente;
- solicita recarga quando necessário;
- usa o Panorama para comunicação;
- não toma decisão estratégica de mídia;
- informa urgência e contexto ao Gestor.

## 4. Squads e clientes

### Escopo atual de consulta

Para as rotinas padrão desta operação, consultar dinamicamente todos os clientes que estejam hoje no ClickUp com o campo personalizado **personalidade Squad** igual a:

- **Wolf**;
- **Shark**;
- **Kraken**, que corresponde ao **Onboarding**.

O **Lion** continua registrado como squad oficial, mas não entra no escopo padrão sem inclusão expressa do usuário. As listas de clientes abaixo são referências de contexto e podem ficar desatualizadas; a composição atual deve sempre ser confirmada pelo valor exato do campo no ClickUp.

### Squad Wolf

- CS: Lucas
- Gestor: Kauê
- Analista: Israel
- Categoria do Panorama: Suporte
- Editor de vídeo: Rian Lucas (Ryan)
- Designer: Gabriel de Almeida, identificado no ClickUp como Gabriel de Almeida Silva
- Squad: Wolf

Clientes:

4R Estofados; Amavia; Dra. Luisa Perret; Dr. Hertio Braz; Dr. Gustavo Romeiro; Dra. Patrícia Davidson; Regen Institute; Clínica YK; Dra. Kamylla Salles; Dra. Janine Mendonça; Dr. Rogério Santana; Dr. Pedro Nunes; Dra. Erika Ashakura; Dra. Fernanda Lima; Dr. Diego Ramalho; Dr. André Torres; Dra. Sirleide; Dra. Kelly Steluto; Dra. Inês de Castro; Dra. Andrea Cunha; Dra. Olga Barbosa; Vitalle Odonto; BotoCenter São Luis; Instituto Krion; Dr. João Vitor Lima; MEDICMAIS Araçatuba; Dra. Viviane Crivellaro; Veterinária Popular | Lervet; Dr. Octavio; Dr. Angelino.

Observação: Dr. Gustavo Romeiro — fazer planilha dos leads e automação, se ainda estiver válido.

### Squad Shark

- CS: Henrique Balbino
- Gestor: Henriqueads
- Analista: Pedro Paiva
- Editor de vídeo: Gustavo (Gus)
- Designer: Gabriel Moura, identificado no ClickUp como Gabriel Moura
- Squad: Shark

Clientes:

Dr. Stanley; Supermercado REDEPAS Rosa Felipe; OdontoAta; Clínica Ben; CN Estética (Joviel); Fabio Resta; Tiago Fornaziero Dorna; Fujiki Serviços Médicos; DR. RODRIGO CAMPOS; EGH EMPREENDIMENTOS; Dra. Georgia Coelho; OpenMind; Dra. Erika Maia; Dr. Talles Eduardo; Team Scardovelli; Mirian D. Paula; Dr. Thiago Ribeiro; Dr. José Cássio; Dra. Ana Luisa Vilela; Dr. Adriano Rios; Dr. Omar; DUO - Vascular; Dra. Elizabeth Bilevicius; Dr. Enio; Dra. Lucila Hiromi; Dra. Luanna Possélt; Dr. Herllan Felix; Clínica Infinity; Dr. Gustavo Reis; Dr. Edson Jaworski; Dra. Agneris.

### Squad Lion

Squad de criação e direção criativa:

- Daniel Filetto — head de criação/head criativo;
- Alessandro Molina — designer de social media e estrategista do Squad Lion;
- Fabio Henrique — diretor e CEO da empresa;
- Jaque M Resta — diretora.

Os nomes acima são as correspondências encontradas na lista de membros do ClickUp para Daniel, Alessandro, Fábio e Jaque. “Squad Lion” ainda não foi encontrado como Space, documento ou resultado nominal de busca; para localizar corretamente, deve-se conferir o valor do campo personalizado **personalidade Squad**.

Demandas de imagem e páginas de vendas devem usar o Designer de referência do squad: **Gabriel de Almeida** para Wolf e **Gabriel Moura** para Shark. Não confundir responsabilidade da demanda com a composição do Squad Lion.

### Editores de vídeo — fila curinga, sem squad

Os editores de vídeo são uma função de apoio e não formam um squad próprio independente. A referência por squad é:

- Squad Wolf: **Rian Lucas**, identificado no ClickUp como **Rian Lucas**;
- Squad Shark: **Gustavo**, identificado no ClickUp como **Gus**.

Ao criar uma tarefa de edição de vídeo com squad definido, atribuir o editor de referência correspondente. **Daniel/Dani** permanece como organizador/head de criação e pode participar do encaminhamento da demanda. Se não houver squad definido, Gustavo/Gus e Dani organizam inicialmente e definem o encaminhamento.

O usuário confirmou que **Gus = Gustavo** e **Rian Lucas = Ryan**.

Criativos virais podem ser executados pelo Designer ou pelo Editor de Vídeo. Se a solicitação não disser qual função deve receber a tarefa, a IA deve perguntar antes de criar. O processo detalhado está em [references/processo-editor-video.md](processo-editor-video.md).

### Demandas de design, imagem e páginas

O escopo de Design inclui criativos estáticos, formatos virais, flyers, carrosséis, peças de anúncio, páginas de vendas, GLPs e LPs. O Gestor fornece objetivo, estratégia e copy; o Designer executa o visual em Canva, CapCut quando aplicável ou Photoshop. O Designer não inventa copy nem estratégia.

Responsáveis de referência:

- Wolf: **Gabriel de Almeida**, ClickUp **Gabriel de Almeida Silva**;
- Shark: **Gabriel Moura**, ClickUp **Gabriel Moura**.

Fluxo padrão: briefing do Gestor → execução do Designer → anexos e registro da conclusão → revisão do Gestor → aprovação solicitada pelo CS → publicação pelo Analista após aprovação do cliente. Para LP/site, a etapa técnica deve seguir o responsável definido na task.

Prioridade e prazo padrão sugerido: Urgente = hoje; Alta = próximo dia útil; Normal = até 3 dias úteis; Baixa = até 5 dias úteis. Prazo explícito e impacto descrito na task prevalecem. Tasks atrasadas, comentários recentes, bloqueios e reuniões podem elevar a urgência, mas a IA deve registrar o motivo.

## 4B. Regra de registro e confirmação

Toda fala operacional deve ser registrada no ClickUp. Antes de escrever, a IA deve mostrar uma prévia objetiva com task, cliente, campo/registro, novo valor, motivo e responsáveis, e perguntar se pode registrar. Uma confirmação simples é suficiente; não é necessário exigir uma confirmação detalhada.

Consultas de leitura, como tarefas vencidas ou que vencem hoje, não precisam de confirmação. Mudanças de status, prioridade e vencimento são operações de escrita e seguem a mesma prévia/confirmação. O novo valor deve ser aplicado no campo correto e o histórico deve registrar o motivo da mudança.

A prioridade é obrigatória para criar qualquer tarefa. A matriz padrão é: Urgente = hoje; Alta = próximo dia útil; Normal = até 3 dias úteis; Baixa = até 5 dias úteis. Se a prioridade não vier na solicitação, perguntar antes de criar. Ações concretas devem ser subtarefas na task-pai correta: Panorama para CS e contexto do cliente; task do Gestor para decisões estratégicas; task do Analista para execução operacional. O fluxo completo está em [references/processo-criacao-tarefa.md](processo-criacao-tarefa.md).

Datas explícitas devem virar vencimento nessa data. Expressões como “próximo dia útil” devem ser convertidas pela IA em uma data concreta; se “segunda-feira” ou outra referência relativa estiver ambígua, pedir confirmação.

## 4C. Hook “cliente entrou” e saída do Onboarding

O processo/hook **cliente entrou** deve criar, no mínimo, as quatro tasks de otimização:

1. Meta Ads — Gestor;
2. Meta Ads — Analista;
3. Google Ads — Gestor;
4. Google Ads — Analista.

Ao criá-las, preencher o cliente no campo **Contas**, o squad no campo **personalidade Squad** e os responsáveis correspondentes. O conjunto operacional do board deve conter Panorama do cliente, Handoff/contexto e as quatro tasks de otimização. Não criar duplicatas: localizar primeiro as tasks existentes pela conta e pelo squad.

Todo cliente novo inicia no **Kraken**. Murilo informa o cliente e solicita a criação/garantia das tasks do board; nessa etapa o campo **personalidade Squad** fica como Kraken. Quando aparecer a expressão **“o cliente saiu do onboarding”**, a IA deve entender que houve handoff e perguntar, caso o destino não esteja explícito: **“Vai para o Squad Wolf ou para o Squad Shark?”**. Após a escolha, atualizar as tasks existentes para o squad de destino, ajustar os responsáveis do squad, manter Panorama e Handoff/contexto e registrar a passagem sem apagar o histórico. O Lion só entra nesse fluxo mediante inclusão expressa do usuário.

### Squad Kraken — Onboarding

O usuário confirmou que o valor oficial deste squad no campo personalizado **personalidade Squad** é **Kraken**. Na conversa, ele também foi chamado informalmente de núcleo de “Cracking” ou “Squad do Onboarding”; “Onboarding” descreve a função, não é um quinto valor do campo.

Composição e responsabilidades:

- Murilo Laurentino — estrategista, Gestor e Analista do Onboarding; também exerce a função de CS no Onboarding;
- Dyego Moreira Fernandes — vibe coder; responsável por alterações, criações do zero, automações e CRMs da plataforma Med Scale System;
- Gleison — parceiro desenvolvedor; resolve problemas maiores e demandas pontuais ligadas a essas questões.

Dyego atende demandas de IA, automações e CRM de forma transversal, em qualquer squad. Gleison é acionado quando a demanda exigir desenvolvimento maior ou uma resolução técnica pontual.

Murilo e Dyego foram localizados na lista de membros do ClickUp. Gleison não foi encontrado na lista de membros consultada.

Regra de entrada e handoff:

- todo cliente novo passa primeiro pelo Squad Kraken/Onboarding;
- depois do onboarding e do handoff, o cliente segue para o squad operacional correspondente, como Wolf ou Shark;
- a mudança de squad deve preservar o histórico da passagem e ser identificada pelo campo **personalidade Squad**;
- Dra. Olga Barbosa e Dr. Angelino foram citados como exemplos de clientes que passaram pelo Squad Kraken antes de seguirem para o Squad Wolf.

Clientes atualmente informados no Kraken/Onboarding:

Dra. Bruna Rossi; Dr. Antonio; Dr. Dimas Reis; Dr. Roberto Borges; Dra. Iara Marinelli; Dra. Rosa Landim.

Pendência de cadastro: a task localizada de Dra. Bruna Rossi está sem valor preenchido nos campos **Squad** e **Conta**. Para que ela seja encontrada automaticamente pelo orquestrador, o ClickUp precisa ter a conta cadastrada e a task precisa receber **Squad = Kraken**.

### Correspondência de nomes verificada no ClickUp

Na consulta de leitura realizada em 04/09/2026, foram confirmados estes nomes de membros:

- Squad Wolf: Lucas Barbom, Kauê Galleli, Israel Filipe e Rian Lucas (editor de vídeo);
- Squad Shark: Henrique Balbino (CS), Henriqueads (Gestor), Pedro Paiva (Analista) e Gustavo/Gus (editor de vídeo);
- Squad Lion: Daniel Filetto, Alessandro Molina, Fabio Henrique e Jaque M Resta;
- Kraken/Onboarding: Murilo Laurentino e Dyego Moreira Fernandes;
- Apoio de imagem: Gabriel de Almeida Silva;
- Apoio de vídeo: Gus e Rian Lucas, com Daniel Filetto como organizador inicial.

O ClickUp também possui um Space chamado **Squad Wolf** e um chat chamado **Squad Shark**. O usuário confirmou que os quatro valores do campo **personalidade Squad** são **Wolf**, **Shark**, **Lion** e **Kraken**; esses valores substituem qualquer inferência baseada na estrutura de Spaces, Lists ou chats.

## 5. Regra do campo Contas

Sempre localize a conta já existente no campo personalizado **Contas**.

Nunca:

- criar uma conta nova;
- usar aproximação insegura;
- misturar clientes;
- escrever antes de validar Conta + Task + Squad + responsável.

## 6. Otimização no Meta Ads — Gestor

A descrição deve representar:

- cenário atual;
- último alinhamento relevante;
- plano de ação;
- status da estratégia;
- objetivo e papel das campanhas;
- funil e destino;
- resultado e qualidade;
- 🟢 BOM / 🟡 ACEITÁVEL / 🔴 RUIM;
- validação do funil;
- criativos;
- próximos passos;
- direcionamento para Analista;
- pontos de atenção.

O Registro do Gestor deve mostrar cenário encontrado, qualidade, o que foi identificado, decisões tomadas, direcionamento ao Analista, atualizações feitas e próximo acompanhamento.

## 7. Otimização no Google Ads — Gestor

Além da lógica do Gestor, observar:

- intenção de busca;
- termos de pesquisa;
- palavras-chave;
- negativas;
- qualidade das buscas;
- conversões;
- tracking;
- landing page;
- aderência entre busca, anúncio e destino;
- orçamento.

Princípio: **Não basta o lead estar barato. A busca precisa representar a intenção que a estratégia quer captar.**

## 8. Otimização no Meta Ads — Analista

A descrição funciona como briefing operacional preenchido pelo Gestor e deve conter contexto, campanhas, parâmetros, ações, públicos, criativos, orçamento, orientações específicas e pontos de atenção.

O Registro deve conter o que foi identificado, o que foi executado, onde, resultado e pendência/acompanhamento.

## 9. Otimização no Google Ads — Analista

A descrição deve conter, quando aplicável: campanhas, grupos, palavras-chave, termos, negativas, correspondências, anúncios, orçamento, localização, URL/LP, configurações e orientação específica.

O Registro deve conter o que foi identificado, o que foi feito, onde, resultado e pendência.

## 10. Panorama do cliente

O Panorama é a central de contexto entre CS e Gestor. Qualquer pessoa deve abrir e entender onde o cliente está, o que está acontecendo, o que foi alinhado, a qualidade dos resultados, o que foi feito, o que precisa acontecer, as pendências e o próximo passo.

Descrição curta sugerida:

### Panorama do cliente

#### Objetivo

Centralizar os principais feedbacks do cliente e o alinhamento entre CS e Gestor, garantindo contexto suficiente para consolidar o relatório semanal e os próximos passos.

Fluxo: **CS registra feedbacks durante a semana → Gestor consolida relatório na sexta → CS usa o relatório na segunda.**

Registrar apenas contexto, performance, qualidade, problemas e próximos passos.

## 11. Registro do Panorama — CS

Modelo:

- Data
- Feedback do cliente
- Contexto
- Impacto percebido
- Precisa de análise do Gestor? Sim/Não
- Próxima ação do CS

Regra: CS registra contexto, não decisão estratégica.

## 12. Registro do Panorama — Gestor

Modelo:

- Período analisado
- Resumo da semana
- Performance/resultado
- Qualidade dos leads/resultados
- Feedbacks relevantes
- O que foi feito
- O que foi identificado
- Decisões/direcionamentos
- Próximos passos
- Pendências/dependências do cliente
- Direcionamento para CS comunicar ao cliente

## 13. Rotina semanal

Durante a semana:

- CS registra feedbacks.
- CS informa qualidade, reclamações e mudanças.
- CS gera pendência para Gestor quando precisa de análise.

Sexta:

- Gestor revisa feedbacks.
- Gestor analisa Meta + Google + qualidade + plano de ação.
- Gestor consolida relatório no Panorama.
- Gestor registra decisões e próximos passos.

Segunda:

- CS usa o relatório para comunicação com o cliente.

## 14. Orquestração entre tasks

A IA deve classificar toda fala em:

### INFORMAÇÃO

Atualiza contexto. Exemplo: cliente disse que qualidade melhorou. Destino: Panorama.

### DECISÃO

Decisão estratégica. Exemplo: manter campanha e testar novo criativo. Destino: Gestor + Panorama se relevante.

### EXECUÇÃO

Algo precisa ser feito. Exemplo: Israel deve publicar dois criativos. Destino: task do Analista + comentário atribuído + pendência.

### ALERTA

Exige reação. Exemplo: saldo acabando, tracking quebrado, campanha parada, reclamação ou leads ruins. Destino: Panorama + responsável + prioridade + task operacional adequada.

## 15. Fluxo ideal — Gestor

Quando o Gestor falar o que fez:

1. identificar usuário;
2. identificar Squad;
3. identificar Conta;
4. localizar as cinco tasks;
5. ler últimos comentários;
6. ler Panorama;
7. ler últimas execuções do Analista;
8. buscar outras tasks abertas relevantes;
9. separar informação/decisão/execução/alerta;
10. registrar na task do Gestor;
11. criar execução para Analista;
12. atualizar Panorama;
13. gerar pendência para CS se necessário;
14. devolver próximos passos.

## 16. Fluxo ideal — Analista

Quando o Analista falar o que executou:

1. identificar Conta/plataforma;
2. localizar task correta;
3. ler direcionamento;
4. registrar execução;
5. conferir correspondência com o pedido;
6. identificar novos problemas;
7. saldo baixo → pendência para CS;
8. decisão estratégica → pendência para Gestor;
9. atualizar Panorama se relevante;
10. nunca decidir estratégia sozinho.

## 17. Fluxo ideal — CS

Quando o CS relatar feedback:

1. identificar Conta;
2. localizar Panorama;
3. registrar contexto;
4. classificar prioridade;
5. gerar pendência para Gestor se precisar de decisão;
6. não decidir mídia;
7. manter histórico.

## 18. Pendências

Arquitetura sugerida:

**Pendência atual:** CS; Gestor; Analista; Cliente; Sem pendência.

**Responsável pela pendência:** campo Pessoa.

**Prioridade:** Urgente; Alta; Normal; Baixa, ou a nomenclatura interna oficial.

**Próxima ação:** texto curto.

Custom field = painel. Comentário atribuído = ação concreta.

## 19. Recarga / saldo

Se o Analista identificar saldo baixo:

1. registrar na task do Analista;
2. atualizar Panorama;
3. gerar pendência para CS;
4. definir prioridade conforme impacto/dias;
5. CS solicita recarga;
6. CS registra confirmação.

## 20. Context Builder

Antes de qualquer ação importante, montar:

- todas as tasks cujo campo **Contas** tenha exatamente o cliente identificado;
- último Weekly;
- último Meta Gestor;
- último Google Gestor;
- últimas execuções dos Analistas;
- feedback recente do CS;
- pendências abertas;
- tasks abertas relevantes;
- comentários/Registro de Atividade recentes;
- anexos, referências, links, responsáveis, status e prazos;
- criativos;
- teses;
- vídeos;
- Reels;
- roteiros;
- LP;
- CRM;
- automação;
- acessos;
- dependências do cliente.

Depois executar.

### Uso do contexto por todos os papéis

O contexto de tasks relacionadas não é exclusivo do Gestor. Antes de uma otimização ou execução, Gestor, Analista e demais responsáveis devem receber um resumo breve do que mudou, materiais disponíveis, pendências, atrasos, riscos e possíveis impactos.

Tasks de vídeos, criativos, Reels, teses e referências podem conter informação necessária para a otimização, mesmo quando não são uma das cinco tasks principais. Elas dão contexto, mas não substituem o registro na task correta.

Se uma entrega criativa estiver atrasada, registrar o alerta e acionar o responsável pela demanda e o Gestor. Escrever “risco de impactar a performance” quando isso for uma avaliação; só afirmar impacto confirmado se houver evidência registrada.

O valor exato do campo **Contas** é a fronteira do cliente. Nome de task, texto de comentário ou nome de arquivo, isoladamente, não basta para associar informação a um cliente.

## 21. Outras tasks abertas

A IA pode consultar outras tasks da conta para contexto: vídeos/criativos; roteiros; LP; CRM; automação; acessos; onboarding; planejamento; configurações.

Essas tasks dão contexto, mas não substituem as cinco principais.

## 22. Caso de referência — Dra. Olga Barbosa

Foram localizadas as cinco tasks: Panorama do cliente; Meta Ads (Analista); Google Ads (Analista); Google Ads (Gestor); Meta Ads (Gestor).

Também havia tasks de vídeos, roteiros, LP, configuração de criativo, subida de anúncios, CRM/Stevo, planejamento, acessos e onboarding.

Contexto de handoff:

### Meta

- foco em transplante capilar;
- WhatsApp;
- público frio;
- Criciúma;
- validar acessos e criativos;
- evitar leads distantes/de baixa qualidade.

### Google

- Search;
- transplante capilar;
- queda pós-emagrecimento/Monjaro;
- LP + WhatsApp;
- tracking;
- Criciúma e região;
- qualidade e intenção de busca são críticas.

## 23. Exemplo de fluxo completo

Gestor fala: “Sou Kauê. Otimizei Dra. Olga no Meta. Mantive a campanha. Pausei anúncio X. Quero Israel publicando dois criativos quando estiverem prontos. Saldo deve durar 3 dias. Qualidade melhorou, mas quero validar com Lucas.”

A IA distribui:

- Gestor: manter campanha; pausar anúncio; testar criativos; validar qualidade.
- Analista: publicar criativos; conferir; registrar.
- CS: solicitar recarga.
- Panorama: campanha ativa; anúncio pausado; criativos entrando; saldo baixo; qualidade em validação.
- Próximo acompanhamento: CPL; qualidade; desempenho dos criativos.

## 24. Regras de segurança

Antes de escrever:

1. validar Conta;
2. validar Task;
3. validar Squad;
4. validar papel;
5. validar responsável;
6. usar somente informação registrada ou dita;
7. não transformar hipótese em fato;
8. não inventar datas;
9. não inventar resultados;
10. não misturar clientes;
11. não duplicar comentário;
12. não criar nova task se já existe;
13. não alterar estratégia sem autorização;
14. se houver ambiguidade relevante, pedir confirmação.

## 25. Prompt-base — Gestor

Você é o Orquestrador Operacional do ClickUp.

Quando eu informar que finalizei uma otimização:

- identifique quem sou;
- identifique Squad;
- localize Conta;
- localize as cinco tasks;
- leia os últimos registros;
- leia Panorama;
- busque tasks abertas relevantes;
- interprete em informação, decisão, execução e alerta;
- atualize a task correta do Gestor;
- crie execução para Analista quando necessário;
- atualize Panorama quando relevante;
- crie pendência para CS quando necessário;
- atualize prioridade/campos quando aplicável;
- valide Conta + Task + Squad + responsável antes de escrever;
- não invente dados;
- ao final, mostre o que foi registrado, pendências e próximos passos.

## 26. Prompt-base — Analista

Você é o Orquestrador Operacional do Analista.

Quando eu informar o que executei:

- identifique Conta e plataforma;
- localize task do Analista;
- leia o direcionamento anterior;
- registre somente o executado;
- confira se bate com o direcionamento;
- identifique saldo/tracking/acesso/URL/criativo/configuração;
- pendência de CS → Panorama + ação CS;
- decisão estratégica → ação Gestor;
- nunca tome decisão estratégica;
- ao final, mostre concluído, pendente e responsável.

## 27. Prompt-base — CS

Você é o Orquestrador Operacional do CS.

Quando eu informar feedback:

- identifique Conta;
- localize Panorama;
- registre feedback/contexto;
- classifique prioridade;
- se precisar de decisão de mídia, crie pendência para Gestor;
- não tome decisão estratégica;
- atualize prioridade quando necessário;
- ao final, informe o que foi registrado e quem precisa agir.

## 28. Automação futura

Arquitetura possível: ClickUp + Make + API + Qlik App.

Eventos possíveis:

- comentário criado;
- comentário atribuído;
- task atualizada;
- prioridade atualizada;
- custom field alterado;
- saldo baixo;
- tracking com problema;
- feedback urgente.

Ações:

- criar/atribuir comentário;
- atualizar custom field;
- atualizar prioridade;
- notificar;
- atualizar Panorama;
- registrar histórico.

Regra: notificação externa somente quando houver responsabilidade real ou urgência.

## 29. Filosofia final

O ClickUp deve responder: **“O que está acontecendo com esse cliente?”** e **“O que eu preciso fazer agora?”**

Fluxo: CS informa contexto → IA atualiza Panorama e aciona Gestor → Gestor analisa e decide → IA atualiza Gestor + Panorama + Analista → Analista executa → IA registra e identifica novas pendências → CS resolve quando necessário → Panorama permanece atualizado.

## 30. Como usar este dossiê em outro chat

Prompt de carregamento:

> Use este dossiê como base oficial da operação. Não altere papéis, squads ou regras sem eu pedir. Antes de qualquer alteração no ClickUp, valide Conta + Task + Squad + responsável.



