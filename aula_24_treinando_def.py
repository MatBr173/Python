"""Criar um código onde demonstre quais produtos estão ou não na promoção"""

def compra_de_produtos(produtos):
    if produtos >= 50:
        valor = (20 / 100) * produtos
        valor_desconto = produtos - valor
        return valor_desconto
    else:
        return produtos

valor_produto_1 = 25.4
valor_produto_2 = 65.0

valor_a_ser_pago_1 = compra_de_produtos(valor_produto_1)
valor_a_ser_pago_2 = compra_de_produtos(valor_produto_2)

print(f"Produto 1: R${valor_a_ser_pago_1:.2f}")
print(f"Produto 2: R${valor_a_ser_pago_2:.2f}")
