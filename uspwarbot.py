class Pais:
	def Pais():
		self.nome
		self.populacao
		self.poder_ataque
		self.poder_defesa
		self.fertilidade

	def atacar(pais_inimigo):
		poder_efetivo = self.poder_ataque - pais_inimigo.poder_defesa
		perda_nossa_efetiva = self.poder_defesa - pais_inimigo.poder_defesa
		
		pais_inimigo.morrer(poder_efetivo * self.populacao)
		self.morrer(perda_nossa_efetiva * pais_inimigo.populacao)

	def morrer(numero_pessoas):
		self.populacao -= numero_pessoas

	def update():
		self.populacao += fertilidade * self.populacao
W
