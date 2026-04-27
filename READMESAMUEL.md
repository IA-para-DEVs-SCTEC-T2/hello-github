# Aprendendo o Kiro

Guia prático em português para usar o Kiro no dia a dia do desenvolvimento.

---

## O que é o Kiro?

O Kiro é um IDE com IA integrada. Diferente de um simples assistente de chat, ele tem acesso direto ao seu projeto — lê arquivos, escreve código, roda comandos e entende o contexto do que você está construindo.

---

## Modos de Operação

### Autopilot
O Kiro age de forma autônoma: lê, cria e modifica arquivos sem pedir confirmação a cada passo. Ideal para tarefas maiores onde você quer velocidade.

### Supervised
O Kiro mostra as mudanças antes de aplicar, e você pode reverter qualquer alteração. Ideal quando quer mais controle sobre o que está sendo feito.

---

## Como Conversar com o Kiro

### Contexto de arquivos
Use `#` para referenciar arquivos ou pastas diretamente no chat:

- `#File` — inclui um arquivo específico no contexto
- `#Folder` — inclui uma pasta inteira
- `#Problems` — mostra os erros do arquivo atual
- `#Terminal` — inclui a saída do terminal
- `#Git Diff` — inclui as mudanças não commitadas

**Exemplo:**
```
Revise o #File src/calculator.py e corrija os erros em #Problems
```

### Imagens e documentos
Arraste uma imagem ou PDF direto no chat, ou clique no ícone de anexo. O Kiro consegue ler e interpretar o conteúdo.

---

## Specs — Desenvolvimento Estruturado

Specs são a forma de construir features complexas de forma incremental com o Kiro.

O fluxo é:
1. Você descreve a feature
2. O Kiro gera os **requisitos**
3. Você revisa e aprova
4. O Kiro gera o **design técnico**
5. Você revisa e aprova
6. O Kiro gera as **tarefas de implementação**
7. Você executa tarefa por tarefa

Specs ficam salvas em `.kiro/specs/` e podem referenciar outros arquivos com:
```
#[[file:caminho/do/arquivo]]
```

---

## Hooks — Automação por Eventos

Hooks disparam ações automaticamente quando algo acontece no IDE.

### Eventos disponíveis
| Evento | Quando dispara |
|---|---|
| `fileEdited` | Ao salvar um arquivo |
| `fileCreated` | Ao criar um arquivo |
| `fileDeleted` | Ao deletar um arquivo |
| `promptSubmit` | Ao enviar uma mensagem |
| `agentStop` | Quando o agente termina |
| `preToolUse` | Antes de uma ferramenta ser usada |
| `postToolUse` | Após uma ferramenta ser usada |
| `preTaskExecution` | Antes de uma tarefa de spec iniciar |
| `postTaskExecution` | Após uma tarefa de spec ser concluída |
| `userTriggered` | Acionado manualmente pelo usuário |

### Ações disponíveis
- `askAgent` — envia uma instrução ao agente
- `runCommand` — executa um comando shell

### Exemplo: rodar lint ao salvar
```json
{
  "name": "Lint ao Salvar",
  "version": "1.0.0",
  "when": {
    "type": "fileEdited",
    "patterns": ["*.ts", "*.tsx"]
  },
  "then": {
    "type": "runCommand",
    "command": "npm run lint"
  }
}
```

### Exemplo: rodar testes após spec concluída
```json
{
  "name": "Testes Pós-Tarefa",
  "version": "1.0.0",
  "when": {
    "type": "postTaskExecution"
  },
  "then": {
    "type": "runCommand",
    "command": "pytest --tb=short"
  }
}
```

Hooks ficam em `.kiro/hooks/` e podem ser gerenciados pelo painel "Agent Hooks" no Explorer, ou pela paleta de comandos buscando `Open Kiro Hook UI`.

---

## Steering — Contexto Persistente

Steering são arquivos Markdown em `.kiro/steering/` que o Kiro lê automaticamente para entender padrões, convenções e informações do projeto.

### Tipos de inclusão
- **Sempre** (padrão) — incluído em toda conversa
- **Por arquivo** — incluído quando um arquivo específico está no contexto:
  ```
  ---
  inclusion: fileMatch
  fileMatchPattern: 'src/**/*.py'
  ---
  ```
- **Manual** — incluído só quando você chama com `#`:
  ```
  ---
  inclusion: manual
  ---
  ```

### Exemplo de uso
Crie `.kiro/steering/padroes.md` com as convenções do seu time:
```markdown
- Sempre usar type hints em Python
- Testes ficam em tests/ com prefixo test_
- Commits seguem Conventional Commits
```

---

## MCP — Model Context Protocol

MCP permite conectar o Kiro a servidores externos que adicionam novas ferramentas e capacidades.

Configuração fica em `.kiro/settings/mcp.json` (workspace) ou `~/.kiro/settings/mcp.json` (global).

### Exemplo
```json
{
  "mcpServers": {
    "meu-servidor": {
      "command": "uvx",
      "args": ["nome-do-pacote@latest"],
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

---

## Dicas Práticas

- Seja específico no que pede — quanto mais contexto, melhor o resultado
- Use `#File` para focar o Kiro no arquivo certo
- Para projetos novos, peça uma Spec antes de sair codando
- Use Steering para não repetir as mesmas instruções toda hora
- Hooks são ótimos para automatizar lint, testes e formatação
- No modo Supervised, revise sempre antes de aceitar mudanças grandes
