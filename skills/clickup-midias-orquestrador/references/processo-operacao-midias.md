# Processo da operação de mídia paga

## Pacote padrão do cliente

Cada cliente deve ser localizado pelo valor exato do campo **Conta** e ter, quando aplicável, estas cinco tasks principais:

1. Panorama do cliente;
2. Otimização no Meta Ads (Gestor);
3. Otimização no Google Ads (Gestor);
4. Otimização no Meta Ads (Analista);
5. Otimização no Google Ads (Analista).

As cinco tasks formam o pacote operacional, mas não pertencem todas ao mesmo papel:

- CS é o dono do contexto, comunicação e acompanhamento no Panorama;
- Gestor é o dono de estratégia, decisão e direcionamento nas tasks de Gestor;
- Analista é o dono da execução e conferência nas tasks de Analista.

## CS — contexto e sucesso do cliente

O CS é a ponte entre cliente e equipe. Ele deve:

- realizar reuniões, ligações e alinhamentos;
- registrar feedback, qualidade dos leads, vendas, agendamentos, reclamações e mudanças de prioridade;
- manter o Panorama atualizado;
- apresentar ao cliente o que foi executado e o próximo passo;
- fazer o acompanhamento semanal e o segundo acompanhamento no meio da semana, quando houver métrica ou pendência relevante;
- cobrar informações, aprovações, materiais, acessos e recargas;
- comunicar ao Gestor qualquer informação que possa exigir decisão de mídia.

O CS não deve decidir estratégia de Meta ou Google. Quando precisar de uma decisão, registra o contexto no Panorama e cria uma subtarefa para o Gestor na task de plataforma correspondente.

### Subtarefas do CS

Usar o Panorama para ações concretas de comunicação, por exemplo:

- solicitar aprovação de criativo;
- cobrar gravação ou material;
- confirmar verba ou recarga;
- perguntar sobre qualidade dos leads;
- confirmar disponibilidade para reunião;
- pedir acesso, documento ou informação do cliente.

Cada subtarefa deve ter ação clara, responsável CS, prioridade, vencimento e próximo passo.

## Gestor — estratégia e direcionamento

O Gestor é responsável pelas tasks de Meta Ads e Google Ads com a indicação **Gestor**. Ele deve:

- analisar o cenário e o objetivo do cliente;
- consultar Panorama, histórico, criativos, LP, CRM, qualidade dos leads e registros do Analista;
- tomar decisões estratégicas de campanha, funil, verba, copy, público, teste e prioridade;
- transformar hipóteses em direcionamentos claros;
- delegar execuções ao Analista por subtarefa ou comentário atribuído;
- acompanhar se o Analista executou e conferiu;
- registrar decisão, motivo, impacto esperado, risco, resultado e próximo acompanhamento;
- revisar peças, LPs e copies antes de o CS encaminhar para aprovação do cliente;
- informar ao CS o que deve ser comunicado ao cliente.

Se o Gestor estiver em dúvida entre estratégia e execução, a IA deve separar as duas partes: decisão fica na task do Gestor; execução vira subtarefa na task do Analista.

## Analista — execução e conferência

O Analista é responsável pelas tasks de Meta Ads e Google Ads com a indicação **Analista**. Ele deve:

- ler o direcionamento do Gestor antes de executar;
- conferir conta, campanha, conjunto, anúncio, termos, criativos, orçamento, tracking e status;
- executar a mudança solicitada;
- registrar exatamente o que foi alterado e onde;
- conferir se a alteração foi publicada ou aplicada;
- informar resultado inicial, impedimento, saldo, acesso, política ou qualquer risco;
- sinalizar ao Gestor e ao CS quando uma pendência afetar prazo, verba ou qualidade.

O Analista pode sugerir melhorias, mas deve identificá-las como **sugestão**, não como decisão aprovada. Ele não deve mudar sozinho estratégia, objetivo, orçamento, público ou estrutura relevante sem direcionamento do Gestor.

### Subtarefas do Analista

Quando o Gestor decidir uma ação, criar a subtarefa na task da plataforma do Analista, com:

- ação operacional;
- referência ao direcionamento do Gestor;
- cliente e Conta;
- prioridade e vencimento;
- critério de conclusão;
- responsável Analista.

Se o Analista precisar de resposta ou material do cliente, ele não deve deixar a demanda solta: registra o bloqueio na sua task e cria uma subtarefa no Panorama para o CS cobrar.

## Como a IA deve lembrar cada papel

A IA deve funcionar como uma trava de organização e avisar quando a fala estiver no lugar errado:

- CS relatou problema de campanha: registrar contexto no Panorama e encaminhar decisão ao Gestor;
- Gestor descreveu uma alteração de conta: registrar decisão no Gestor e criar execução para o Analista;
- Analista propôs mudança estratégica: registrar como sugestão e solicitar decisão do Gestor;
- Analista precisa cobrar o cliente: criar subtarefa no Panorama para o CS;
- Designer ou Editor recebeu pedido sem briefing: perguntar os campos faltantes ao solicitante/Gestor;
- qualquer pessoa informou prazo sem prioridade: perguntar a prioridade antes de criar;
- qualquer pessoa enviou imagem, PDF ou vídeo: localizar a task correta antes de anexar.

O lembrete deve ser objetivo e respeitoso, explicando onde a informação será registrada e quem precisa agir. A IA não deve bloquear uma consulta de leitura; deve bloquear apenas a criação ou atualização ambígua.

## Registro e circulação da informação

- Panorama: visão geral, contexto do cliente, feedback, qualidade, pendências e próximo passo;
- Gestor: análise, decisão, estratégia, direcionamento e revisão;
- Analista: execução, conferência, resultado técnico e impedimentos;
- comentários atribuídos: ação concreta com dono;
- subtarefas: acompanhamento de ações que precisam de prazo e responsável.

Uma informação pode ser replicada entre Panorama, Gestor e Analista quando tiver impacto em mais de um papel, mas cada registro deve ter finalidade diferente. Não copiar o mesmo texto sem adaptar ao papel.

## Fluxo padrão de uma demanda

```text
Contexto ou pedido do cliente
        ↓
CS registra no Panorama
        ↓
Gestor analisa e decide
        ↓
Analista executa e confere
        ↓
Gestor avalia o resultado
        ↓
CS comunica o cliente e registra o retorno
```

Quando a demanda for criativo ou página, seguir o fluxo específico de Design/Editor: briefing → execução → revisão do Gestor → aprovação do CS/cliente → publicação ou disponibilização.

## Limites da automação

A IA pode localizar, resumir, criar prévias, registrar comentários, criar subtarefas, atualizar status e organizar responsáveis quando a ação estiver autorizada. Ela não deve transformar uma sugestão em decisão, nem esconder uma pendência porque uma task foi concluída.



