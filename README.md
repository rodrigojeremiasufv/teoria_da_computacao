# Repositório referente à disciplina "SIN132: Introdução à Teoria da Computação".
Este repositório tem como objetivo disponibilizar o trabalho desenvolvido ao decorrer da disciplina "Introdução à Teoria da Computação", realizado pelo aluno Rodrigo Jeremias Mendes, matrícula 6315, [email](rodrigo.jeremias@ufv.br).
### Como Executar?
Para executar a verificação de um autômato, certifique-se que o python esteja instalado e execute:

```
python3 main.py <arquivo_automato.txt> <arquivo_strings.txt>
exemplo: python3 main.py automato.txt testes.txt
```

Para verificara a igualdade entre dois automatos, execute:

```
python3 igualdade.py <arquivo_automato.txt> <arquivo_automato2.txt>
exemplo: python3 igualdade.py automato.txt automato2.txt
```

### TODO:
- [x] Criar uma aplicação capaz de receber como entrada um Autômato Finito Determinístico (AFD) ou Não-Determinístico (AFN).
- [x] Converter uma AFN para AFD caso necessário.
- [x] Simular a aceitação de palavras.
- [ ] Demonstrar equivalencia entre AFD e AFN.
- [ ] Minimizar AFDs.
- [ ] Front-end.
- [ ] Tratamento de Erros e correções.
- [ ] Testes.
- [x] Criação de autômatos por arquivos. 

