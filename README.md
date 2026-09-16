# Agência IA + ClickUp

Pacote interno de processos e skills para a operação de mídia paga da agência.

## O que este pacote faz

- Usa o ClickUp como fonte oficial de clientes, squads, tarefas, responsáveis, prazos e histórico.
- Orquestra CS, gestor, analista, designer e editor de vídeo.
- Padroniza criação, revisão, aprovação, execução e registro de tarefas.
- Reconhece o onboarding pelo Squad Kraken e a saída pelo comando “o cliente saiu do onboarding”.
- Mantém o contexto do cliente no Panorama e separa estratégia, execução e comunicação.
- Formata tasks de vídeo sem inventar informações obrigatórias.

## O que este pacote não faz

- Não inclui token, senha ou credencial do ClickUp.
- Não substitui a conexão do ClickUp feita por cada colaborador.
- Não altera tarefas sem apresentar o plano e obter confirmação simples do usuário.
- Não transforma uma skill de distribuição em sincronização automática entre contas.

## Instalação rápida

1. Abra este repositório no ambiente de IA utilizado pela pessoa.
2. Instale ou carregue o plugin/skills a partir do GitHub.
3. Conecte o ClickUp na conta individual da pessoa.
4. Faça o setup inicial seguindo [`SETUP.md`](SETUP.md).
5. Rode os testes de leitura antes de permitir atualizações.

## Estrutura

- `.codex-plugin/plugin.json`: manifesto do plugin.
- `skills/clickup-midias-orquestrador/`: skill principal da operação.
- `skills/formatar-task-editor-video/`: formatação de tasks de vídeo.
- `SETUP.md`: instalação, conexão e testes iniciais.

## Regra de segurança operacional

Toda alteração no ClickUp deve ser apresentada antes no chat com cliente, tarefa, campos, responsáveis, prazo, status, comentário e anexos previstos. A alteração só deve ser feita após confirmação do usuário.

