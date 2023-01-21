# Defini uma célula
def linha(d):
    return "+" + d*"-"+"+"

  # Define uma coluna, o final de uma celula 
def coluna():
  return "|"

  # Cria uma variável que recebe uma coluna 
c=coluna()

#cria linha 1 da tabela 
print("{} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {} {:} {}" .format(linha(24),linha(14),linha(12),linha(15),linha(16),linha(13),"\n"+c,' Lista	de	Produtos |',c,'QTD Entradas |',c,'QTD Saídas |',c,'Saldo Estoque |',c,'Preço Unitário |',c,'Subtotal    |'))

#cria linha 2 da tabela 
print("%s %s %s %s %s %s %s %24s %s %14s %s %12s %s %15s %s %16s %s %10s %24s %s %s %14s %s %12s %s %15s %s %16s %s %13s" % (linha(24),linha(14),linha(12),linha(15),linha(16),linha(13),"\n"+c,"Azeite de Oliva Extra |",c,"100 |",c,"40 |",c,"60 |",c,"R$ 21,90 |",c,"R$ 1.314,00 |","\n"+c,"Virgem LAT 500ml       |",c,c,c,c,c,c,c,c,c,c))

#cria linha 3 da tabela 
print("%s %s %s %s %s %s %s %s %6s %s %14s %s %12s %s %15s %s %16s %s %10s %24s %s %12s %s %14s %s %12s %s %15s %s %16s %s %13s"%(linha(24),linha(14),linha(12),linha(15),linha(16),linha(13),"\n"+c,"Castanha	do Pará",c,c,"100 |",c, "5 |",c, "95 |", c, "R$ 6,00 |",c, "R$ 300,00   |","\n"+c,"Granel [gr]",c,c,c,c,c,c,c,c,c,c,c))

#cria linha 4 da tabela 
print("%s %s %s %s %s %s %s %s %0s %s %14s %s %12s %s %15s %s %16s %s %10s %24s %s %17s %s %14s %s %12s %s %15s %s %16s %s %13s"%(linha(24),linha(14),linha(12),linha(15),linha(16),linha(13),"\n"+c,"Paçoca de Amendoim CXA",c,c,"100 |",c, "8 |",c, "92 |", c, "R$ 1,50 |",c, "R$ 30,00    |","\n"+c,"30 UND",c,c,c,c,c,c,c,c,c,c,c))

#cria linha 5 da tabela 
print("%s %s %s %s %s %s %s %s %s %14s %s %12s %s %15s %s %16s %s %10s %24s %s %18s %s %14s %s %12s %s %15s %s %16s %s %13s"%(linha(24),linha(14),linha(12),linha(15),linha(16),linha(13),"\n"+c,"Panetone sem Gluten CXA|",c,"100 |",c, "60 |",c, "40 |", c, "R$ 17,30 |",c, "R$ 692,00   |","\n"+c,"1 UND",c,c,c,c,c,c,c,c,c,c,c))

#cria linha 6 da tabela 
print("%s %s %s %s %s %s %s %s %5s %s %14s %s %12s %s %15s %s %16s %s %10s %24s %s %10s %-1s %14s %s %12s %s %15s %s %16s %s %13s"%(linha(24),linha(14),linha(12),linha(15),linha(16),linha(13),"\n"+c,"Pão Sirio Integral",c,c,"100 |",c, "70 |",c, "30 |", c, "R$ 5,90 |",c, "R$ 177,00   |","\n"+c,"Saco com 500g",c,c,c,c,c,c,c,c,c,c,c))

#cria linha 7 da tabela 
print("%s %s %s %s %s %s %s %s %s %14s %s %12s %s %15s %s %16s %s %10s %24s %s %17s %s %14s %s %12s %s %15s %s %16s %s %13s"%(linha(24),linha(14),linha(12),linha(15),linha(16),linha(13),"\n"+c,"Polpa de Açai Natural  |",c,"100 |",c, "1 |",c, "99 |", c, "R$ 7,10 |",c, "R$ 639,00   |","\n"+c,"PCT 5L",c,c,c,c,c,c,c,c,c,c,c))

#cria linha 8 da tabela 
print("%s %s %s %s %s %s %s %s %10s %s %14s %s %12s %s %15s %s %16s %s %10s %24s %s %15s %-1s %14s %s %12s %s %15s %s %16s %s %13s"%(linha(24),linha(14),linha(12),linha(15),linha(16),linha(13),"\n"+c,"Queijo Vegano",c,c,"100 |",c, "30 |",c, "70 |", c, "R$ 25,00 |",c, "R$ 1.750,00 |","\n"+c,"PCT 450g",c,c,c,c,c,c,c,c,c,c,c))

#cria linha 9 da tabela 
print("%s %s %s %s %s %s %s %24s %s %14s %s %12s %s %15s %s %14s %s %13s "%(linha(24),linha(14),linha(12),linha(15),linha(16),linha(13),"\n"+c,c,c,c,c,c,c,c,c, "Total",c, "| R$ 5.774,00 |")) 

# Linha final da tabela
print("%s %s %s %s %s %s " %(linha(24),linha(14),linha(12),linha(15),linha(16),linha(13)))