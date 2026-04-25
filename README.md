# Hello GitHub - Tutorial Git

Repositório para praticar os comandos básicos do Git.

## 10 Comandos Básicos do Git

### 1. Clone o repositório
```bash
git clone https://github.com/IA-para-DEVs-SD/hello-github.git
```
Copia um repositório remoto para sua máquina local.

```mermaid
graph LR
    A[Repositório Remoto<br/>GitHub] -->|git clone| B[Repositório Local<br/>Sua Máquina]
    style A fill:#ff6b6b
    style B fill:#51cf66
```

### 2. Verifique o status dos arquivos
```bash
git status
```
Mostra quais arquivos foram modificados, adicionados ou estão prontos para commit.

```mermaid
graph TB
    A[git status] --> B{Verifica Estado}
    B --> C[Arquivos Modificados]
    B --> D[Arquivos em Stage]
    B --> E[Arquivos Não Rastreados]
    style A fill:#4dabf7
    style C fill:#ffd43b
    style D fill:#51cf66
    style E fill:#ff8787
```

### 3. Adicione arquivos ao stage
```bash
git add .
# ou adicione arquivo específico
git add arquivo.txt
```
Prepara os arquivos modificados para serem commitados.

```mermaid
graph LR
    A[Arquivos Modificados] -->|git add| B[Área de Stage<br/>Preparado para Commit]
    style A fill:#ffd43b
    style B fill:#51cf66
```

### 4. Faça um commit das alterações
```bash
git commit -m "Sua mensagem aqui"
```
Salva as alterações no repositório local com uma mensagem descritiva.

```mermaid
graph LR
    A[Área de Stage] -->|git commit -m| B[Repositório Local<br/>Histórico Salvo]
    style A fill:#51cf66
    style B fill:#4dabf7
```

### 5. Envie as alterações para o GitHub
```bash
git push
```
Envia seus commits locais para o repositório remoto.

```mermaid
graph LR
    A[Repositório Local<br/>Seus Commits] -->|git push| B[Repositório Remoto<br/>GitHub]
    style A fill:#4dabf7
    style B fill:#ff6b6b
```

### 6. Baixe as alterações do GitHub
```bash
git pull
```
Baixa e integra as alterações do repositório remoto para seu repositório local.

```mermaid
graph LR
    A[Repositório Remoto<br/>GitHub] -->|git pull| B[Repositório Local<br/>Atualizado]
    style A fill:#ff6b6b
    style B fill:#4dabf7
```

### 7. Veja o histórico de commits
```bash
git log
# ou versão resumida
git log --oneline
```
Exibe o histórico de commits do projeto.

```mermaid
graph TB
    A[git log] --> B[Histórico de Commits]
    B --> C[Commit 3: Mensagem]
    B --> D[Commit 2: Mensagem]
    B --> E[Commit 1: Mensagem]
    style A fill:#4dabf7
    style B fill:#845ef7
    style C fill:#e0e0e0
    style D fill:#e0e0e0
    style E fill:#e0e0e0
```

### 8. Crie uma nova branch
```bash
git branch nome-da-branch
# ou crie e mude para a branch
git checkout -b nome-da-branch
```
Cria um novo ramo de desenvolvimento.

```mermaid
graph LR
    A[Branch Principal<br/>master/main] -->|git branch| B[Nova Branch<br/>feature]
    style A fill:#4dabf7
    style B fill:#845ef7
```

### 9. Mude de branch
```bash
git checkout nome-da-branch
```
Alterna entre diferentes branches do projeto.

```mermaid
graph LR
    A[Branch Atual<br/>master] -->|git checkout| B[Outra Branch<br/>feature]
    style A fill:#4dabf7
    style B fill:#845ef7
```

### 10. Mescle branches
```bash
git merge nome-da-branch
```
Integra as alterações de uma branch em outra.

```mermaid
graph TB
    A[Branch Feature] -->|git merge| C[Branch Master<br/>Código Integrado]
    B[Branch Master] -->|git merge| C
    style A fill:#845ef7
    style B fill:#4dabf7
    style C fill:#51cf66
```

## Exercício Prático

1. Clone este repositório
2. Crie uma nova branch com `git checkout -b minha-branch`
3. Modifique o arquivo `hello.py`
4. Use `git status` para ver as mudanças
5. Adicione as mudanças com `git add .`
6. Faça commit com `git commit -m "Mensagem descritiva"`
7. Volte para a branch principal com `git checkout master`
8. Mescle suas alterações com `git merge minha-branch`
9. Envie para o GitHub com `git push`
10. Veja o histórico com `git log --oneline`

## Dicas Importantes

- Sempre use `git status` antes de fazer commit
- Escreva mensagens de commit claras e descritivas
- Faça `git pull` antes de começar a trabalhar para ter a versão mais recente
- Use branches para desenvolver novas funcionalidades

Boa prática! 🚀
