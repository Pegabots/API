# API Pegabot

![Maintained? yes](https://img.shields.io/badge/Maintained%3F-yes-green.svg)
![Ask me anything](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)

Neste repositório encontra-se o código da API do Pegabot, capaz de buscar informações do usuário por meio da API do Twitter, bem como fazer requisições de análise ao Motor Pegabot.

## Background

Quando chamada, a API busca no banco de dados aquele usuário. Caso ele já tenha sido analisado e essa análise tenha ocorrido em menos de 30 dias, o valor da análise é retornado sem que uma nova análise seja feita. Caso contrário, é feita uma requisição ao Motor Pegabot, que analisa aquele perfil e retorna o resultado dessa análise. O valor é então, salvo no banco de dados e retornado à aplicação que fez a requisição.

## Código de Conduta

Observe nosso nosso [Código de Conduta](./CODE_OF_CONDUCT.md) na hora de realizar interações aqui no repositório. O objetivo é promover um espaço saudável de desenvolvimento.

## Contribuindo

Encorajamos todos os interessados a contribuírem para o projeto. Se você quiser mais informações, acesse [contribuindo para o projeto](/CONTRIBUTING.md) para entender como você pode contribuir.

## Versão

O Projeto será mantido sob as diretrizes de versão semântica, tanto quanto possível. Os lançamentos serão numerados com o seguinte formato:

`<major>.<minor>.<patch>`

Para obter mais informações sobre SemVer, visite http://semver.org.

## Licença

Este projeto é gratuito e de código aberto. Você pode usá-lo para projetos comerciais, projetos de código aberto ou praticamente o que você quiser. Você pode ver [aqui](/LICENSE) qual é a Licensa utilizada no projeto.


## Agradecimentos

Agradecimentos aos desenvolvedores **[@blckjzz](https://github.com/blckjzz)** e **[@otaviouss](https://github.com/otaviouss)**.



