create database Projeto_integrador;

use Projeto_integrador;

create table Produtos(
	cod_pro int(10) not null,
	nome varchar(40) not null,
	descricao varchar(200) not null,
	CP int(30) not null,
	CF_p int(30) not null,
	IV_p int(30) not null,
	CM_p int(30) not null,
	ML int(30) not null,
	primary key(cod_pro)
)default charset = utf8mb4;

select * from Produtos;

#inserir dados
insert into Produtos(cod_pro, nome, descricao, CP, CF_p, IV_p, CM_p, ML)VALUES 
(111,"Copo da Ponte Preta", "Copo plástico com capacidade de 500 ML.perfeito para os torcedores apaixonados pela Macaca!","1000.00","100","100","100","100"),
(222,"Camisa do Corinthians","O sagrado manto alvinegro, oferece uma qualidade e conforto que todos os torcedores merecem","10000.00","100","100","100","1000"),
(333,"Bola de Futebol","Ela é fabricada com couro sintético e consiste de várias camadas revestidas com uma cobertura à prova d’água.Cor:Vermelho e Branco","50.00","10","10","10","10"),
(444,"Raquete de beach tennis","Construção : Carbono Frame.Carbono 3K Face.Cor:Preto e Branco","500.00","20","20","20","20");

#listar dados
select*from Produtos;

#Deletar dado
Delete from Produtos
where cod_pro = 444;

#Alterar dados#
#Adicionar coluna
alter table Produtos
add column(Data_Fabricação date);

#Excluir coluna
alter table Produtos
drop column Data_Fabricação;