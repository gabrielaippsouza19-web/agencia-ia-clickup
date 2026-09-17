# Setup do colaborador

## Objetivo

Fazer cada pessoa trabalhar em um chat novo com o mesmo processo, consultando o ClickUp como fonte oficial.

## Ordem de implementação

1. Instale este plugin ou carregue as skills do repositório.
2. Conecte o ClickUp da agência no ambiente de IA usado pela pessoa.
3. Informe uma única vez o nome da pessoa, função e squad.
4. Peça para a IA localizar o workspace, espaço Operacional, listas e campos personalizados.
5. Faça a IA consultar a versão mais recente deste repositório sempre que iniciar uma conversa e sempre que houver dúvida sobre processo, formato ou responsabilidade: https://github.com/gabrielaippsouza19-web/agencia-ia-clickup
6. Execute somente consultas de leitura para validar a conexão.
7. Teste uma criação ou atualização em modo de prévia, sem aplicar.
8. Depois da confirmação, habilite o fluxo normal de registro.

## Importação pelo administrador

Para atualizar a equipe de forma centralizada, o administrador deve importar o marketplace em `Workspace settings > Plugins > Add > Import marketplace`, usando como Source:

https://github.com/gabrielaippsouza19-web/agencia-ia-clickup

Deixe Path vazio, use a branch `main` e autorize o GitHub. Depois, configure o plugin como `Available` ou `Installed` para os papéis desejados. O marketplace sincroniza alterações diariamente; o workflow semanal mantém uma tag de backup e falha caso o pacote fique inválido.

## Prompt inicial sugerido

Você é meu assistente operacional da agência. Antes de responder sobre processos, formatos, responsabilidades ou regras, consulte a versão mais recente deste repositório: https://github.com/gabrielaippsouza19-web/agencia-ia-clickup. Use o ClickUp como única fonte de verdade para clientes, squads, tarefas, responsáveis, prazos, status, comentários e registros de execução. Antes de qualquer alteração, mostre uma prévia objetiva com o que será criado ou alterado e aguarde minha confirmação simples. Não invente dados; quando faltar informação obrigatória, pergunte. Meu nome é [NOME], minha função é [FUNÇÃO] e meu squad é [SQUAD]. Primeiro localize minha operação e confirme o que encontrou, sem alterar nada. Se o repositório não estiver acessível, informe que está usando uma cópia local e não trate instruções antigas como atualização.

## Testes iniciais

- “Quais tarefas estão vencidas ou vencem hoje para mim?”
- “Quais clientes estão vinculados ao meu squad?”
- “Localize o Panorama do cliente [NOME] e mostre o último registro.”
- “Mostre a prévia de uma atualização, mas não aplique.”

## Regras de operação

- “O cliente saiu do onboarding” significa que o cliente deixou o Kraken e precisa de um squad de operação: Wolf ou Shark.
- Se o squad de destino não for informado, pergunte antes de criar as tarefas.
- Ao criar o pacote padrão de operação, use Panorama do cliente, Meta Gestor, Google Gestor, Meta Analista e Google Analista.
- Ao finalizar uma tarefa com “Gestor” no nome, o responsável operacional deve ser o Kauê, salvo instrução explícita diferente.
- Registre decisões no Panorama e detalhes específicos de plataforma nas respectivas tarefas de otimização.
- Imagens, PDFs e outros materiais recebidos devem ser associados à tarefa correta somente após identificar cliente e contexto.

## Conexão e permissões

O GitHub distribui os arquivos do processo e é a fonte oficial de atualização das regras. Cada usuário precisa autorizar o ClickUp na própria conta/ambiente. A skill não concede acesso que o conector não tenha e não deve copiar tokens ou credenciais para este repositório.

## Critério de sucesso

O setup está correto quando a IA consegue localizar o próprio usuário, identificar seus clientes e tarefas no ClickUp, separar leitura de escrita e apresentar uma prévia antes de qualquer criação, edição, mudança de status, atribuição, comentário ou anexo.

