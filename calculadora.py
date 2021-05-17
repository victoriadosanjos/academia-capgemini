#script python

investimento = float(input('Digite o valor investido: '))

## Calculo de( 30 pessoas visualizam o anúncio original (não compartilhado) a cada R$ 1,00 investido. )
visualizacaoOriginal = int(investimento * 30)

## Calculo de ( a cada 100 pessoas que visualizam o anúncio 12 clicam nele. ) 
## Pegamos a porcentagem da quantidade de conversão em cliques
cliques = int(visualizacaoOriginal * 0.12)

## Calculo de (a cada 20 pessoas que clicam no anúncio 3 compartilham nas redes sociais.) | 
# o mesmo anúncio é compartilhado no máximo 4 vezes em sequência
compartilhamento = int((cliques * 0.15) * 4)

## Calculo de ( cada compartilhamento nas redes sociais gera 40 novas visualizações. )
novasVisualizacoes = int(compartilhamento * 40)

## Quantidade aproximada de visualizacao (considerando o anuncio original + os compartilhados) 
visualizacaoTotal = int(novasVisualizacoes + visualizacaoOriginal)

print(f'Valor investido : R$ {investimento: .2f}')
print(f'Visualizacao original : {visualizacaoOriginal}')
print(f'Quantidade de cliques : {cliques}')
print(f'Quantidade de compartilhamento : {compartilhamento}')
print(f'Quantidade de novas visualizacoes : {novasVisualizacoes}')
print(f'Quantidade total de visualizacoes : {visualizacaoTotal}')