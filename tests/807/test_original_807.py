import pytest
import importlib

test_cases = [
	('Fui devagar, mas ou o pé ou o espelho traiu-me. Este pode ser que não fosse; era um espelhinho de pataca (perdoai a barateza), comprado a um mascate italiano, moldura tosca, argolinha de latão, pendente da parede, entre as duas janelas.', 2),
	('D. Fortunata, que estava no quintal, nem esperou que eu lhe perguntasse pela filha. Está na sala, penteando o cabelo, disse-me; vá devagarzinho para lhe pregar um susto.', 3),
	('Neste direi somente que, passados alguns dias do ajuste com o agregado, fui ver a minha amiga; eram dez horas da manhã.', 1),
	('É o que contarei no outro capítulo.', 1),
	('Caso houve, porém, no qual não sei se aprendeu ou ensinou, ou se fez ambas as coisas, como eu.', 1),
	('CAPÍTULO XXXII OLHOS DE RESSACA Tudo era matéria às curiosidades de Capitu.', 1),
	('Tudo era matéria às curiosidades de Capitu, mobílias antigas, alfaias velhas, costumes, notícias de Itaguaí, a infância e a mocidade de minha mãe, um dito daqui, uma lembrança dali, um adágio dacolá...', 1),
	('Ouvindo falar várias vezes da Maioridade, teimou um dia em saber o que fora este acontecimento; disseram-lho, e achou que o Imperador fizera muito bem em querer subir ao trono aos quinze anos.', 1),
	('Nascera muito depois daquelas festas célebres.', 1),
	('Queria a notícia das tribunas da Capela Imperial e dos salões dos bailes.', 1),
	('Sabia já o que os pais lhe haviam dito, mas naturalmente tinha para si que eles pouco mais conheceriam do que o que se passou nas ruas.', 1),
	('Foi pelas festas da Coroação. Oh! conte-me as festas da Coroação!', 3),
	('São jóias viúvas, como eu, Capitu. Quando é que botou estas?', 2),
	('A pérola de César acendia os olhos de Capitu. Foi nessa ocasião que ela perguntou a minha mãe por que é que já não usava as jóias do retrato; referia-se ao que estava na sala, com o de meu pai; tinha um grande colar, um diadema e brincos.', 2),
	('José Dias, não tendo presente o valor do sestércio, respondeu entusiasmado: É o maior homem da história!', 1),
	('E quanto valia cada sestércio?', 1),
	('Ficou muito tempo com a cara virada para ele. Um homem que podia tudo! que fazia tudo! Um homem que dava a uma senhora uma pérola do valor de seis milhões de sestércios!', 4),
	('José Dias dava-lhe essas notícias com certo orgulho de erudito. A erudição deste não avultava muito mais que a sua homeopatia de Cantagalo. Um dia, Capitu quis saber o que eram as figuras da sala de visitas. O agregado disse-lho sumariamente, demorando-se um pouco mais em César, com exclamações e latins: César! Júlio César! Grande homem! Tu quoque, Brute? Capitu não achava bonito o perfil de César, mas as ações citadas por José Dias davam-lhe gestos de admiração.', 8),
	('Mas, não tendo ela rudimento algum de arte, e havendo feito aquilo de memória em poucos minutos, achei que era obra de muito merecimento; descontai-me a idade e a simpatia. Ainda assim, estou que aprenderia facilmente pintura, como aprendeu música mais tarde... Já então namorava o piano da nossa casa, velho traste inútil, apenas de estimação... Lia os nossos romances, folheava os nossos livros de gravuras, querendo saber das ruínas, das pessoas, das campanhas, o nome, a história, o lugar.', 4),
	('Um dia fui achá-la desenhando a lápis um retrato; dava os últimos rasgos, e pediu-me que esperasse para ver se estava parecido. Era o de meu pai, copiado da tela que minha mãe tinha na sala e que ainda agora está comigo. Perfeição não era; ao contrário, os olhos saíram esbugalhados, e os cabelos eram pequenos círculos uns sobre outros.', 3),
	('Tio Cosme ensinou-lhe gamão. Anda apanhar um capotinho, Capitu, dizia-lhe ele. Capitu obedecia e jogava com facilidade, com atenção, não sei se diga com amor.', 3),
	('No colégio onde, desde os sete anos, aprendera a ler, escrever e contar, francês, doutrina e obras de agulha, não aprendeu, por exemplo, a fazer renda; por isso mesmo, quis que prima Justina lhe ensinasse. Se não estudou latim com o Padre Cabral foi porque o padre, depois de lhe propor gracejando, acabou dizendo que latim não era língua de meninas. Capitu confessou-me um dia que esta razão acendeu nela o desejo de o saber. Em compensação, quis aprender inglês com um velho professor amigo do pai e parceiro deste ao solo, mas não foi adiante.', 4),
	('As curiosidades de Capitu dão para um capítulo. Eram de vária espécie, explicáveis e inexplicáveis, assim úteis como inúteis, umas graves, outras frívolas; gostava de saber tudo.', 2),
	('Preciso tirar um cochilo. Meus Deus! Que horas são? Vou perder a minha aula...', 4)
]

@pytest.mark.parametrize("a, output", test_cases)

def test_conta_frases(a, output, solution):
	imp = importlib.import_module(solution)
	assert imp.conta_frases(a) == output
