CREATE TABLE TESTE(
	[%OURORECEBIDO] FLOAT
)


CREATE VIEW [Vw_Fato] AS
	SELECT 
		[gameid]
		,[datacompleteness]
		,[league]
		,[split]
		,[playoffs]
		,CONVERT (DATE, [date]) AS [date]
		,[game]
		,[patch] 
		,[side] 
		,[position] 
		,[playername]
		,[playerid]
		,[teamname]
		,[teamid]
		,[champion]
		,[ban1]
		,[ban2]
		,[ban3]
		,[ban4]
		,[ban5]
		,FORMAT(DATEADD(SECOND,CAST([gamelength] AS INT),0), 'mm:ss') AS [gamelength]
		,[result] 
		,CAST ([kills] AS INT) AS [kills]
		,CAST ([deaths] AS INT) AS [deaths]
		,CAST ([assists] AS INT) AS [assists]
		,CAST([teamkills] AS INT) AS [teamkills]
		,CAST([teamdeaths] AS INT) AS [teamdeaths]
		,CAST([doublekills] AS INT) AS [doublekills]
		,CAST([triplekills] AS INT) AS [triplekills]
		,CAST([quadrakills] AS INT) AS [quadrakills]
		, CAST([pentakills] AS INT) AS [pentakills]
		,[firstblood]
		,[firstbloodkill]
		,[firstbloodassist]
		,[firstbloodvictim]
		,CAST([team kpm] AS FLOAT) AS [team kpm]
		,CAST([ckpm] AS FLOAT) AS [ckpm]
		,[firstdragon]
		,CAST([dragons] AS INT) AS [dragons]
		,CAST([opp_dragons] AS INT) AS [opp_dragons]
		,CAST([elementaldrakes] AS INT) AS [elementaldrakes]
		,CAST([opp_elementaldrakes] AS INT) AS [opp_elementaldrakes]
		,CAST([infernals] AS INT) AS [infernals]
		,CAST([mountains] AS INT) AS [mountains]
		,CAST([clouds] AS INT) AS [clouds]
		,CAST([oceans] AS INT) AS [oceans]
		,CAST([chemtechs] AS INT) AS [chemtechs]
		,CAST([hextechs] AS INT) AS [hextechs]
		,CAST([elders] AS INT) AS [elders]
		,CAST([opp_elders] AS INT) AS [opp_elders]
		,[firstherald]
		,CAST([heralds] AS INT) AS [heralds]
		,CAST([opp_heralds] AS INT) AS [opp_heralds]
		,[firstbaron]
		,CAST([barons] AS INT) AS [barons]
		,CAST([opp_barons] AS INT) AS [opp_barons]
		,[firsttower]
		,CAST([towers] AS INT) AS [towers]
		,CAST([opp_towers] AS INT) AS [opp_towers]
		,[firstmidtower]
		,[firsttothreetowers]
		,CAST([turretplates] AS INT) AS [turretplates]
		,CAST([opp_turretplates] AS INT) AS [opp_turretplates]
		,CAST([inhibitors] AS INT) AS[inhibitors]
		,CAST([opp_inhibitors] AS INT) AS[opp_inhibitors]
		,CAST([damagetochampions] AS FLOAT) AS [damagetochampions]
		,CAST([dpm] AS FLOAT) AS[dpm]
		,CAST([damageshare] AS FLOAT) AS[damageshare]
		,CAST([damagetakenperminute] AS FLOAT) AS[damagetakenperminute]
		,CAST([damagemitigatedperminute] AS FLOAT) AS[damamitigatedperminute]
		,CAST([wardsplaced] AS INT) AS[wardsplaced]
		,CAST([wpm] AS FLOAT) AS[wpm]
		,CAST([wardskilled] AS INT) AS[wardskilled]
		,CAST([wcpm] AS FLOAT) AS[wcpm]
		,CAST([controlwardsbought] AS INT) AS[controlwardsbought]
		,CAST([visionscore] AS INT) AS[visionscore]
		,CAST([vspm] AS FLOAT) AS[vspm]
		,CAST([totalgold] AS INT) AS[totalgold]
		,CAST([earnedgold] AS INT) AS [earnedgold]
		,CAST([earned gpm] AS FLOAT) AS[earned gpm]
		,CAST([earnedgoldshare] AS FLOAT) AS[earnedgoldshare]
		,CAST([goldspent] AS INT) AS[goldspent]
		,CAST([gspd] AS FLOAT) AS[gspd]
		,CAST ([total cs] AS INT) AS[total cs]
		,CAST ([minionkills] AS INT) AS[minionkills]
		,CAST ([monsterkills] AS INT) AS[monsterkills]
		,CAST ([monsterkillsownjungle] AS INT) AS[monsterkillsownjungle]
		,CAST ([monsterkillsenemyjungle] AS INT) AS[monsterkillsenemyjungle]
		,CAST([cspm] AS FLOAT) AS[cspm]
		,CAST ([goldat10] AS INT) AS[goldat10]
		,CAST ([xpat10] AS INT) AS[xpat10]
		,CAST ([csat10] AS INT) AS[csat10]
		,CAST ([opp_goldat10] AS INT) AS[opp_goldat10]
		,CAST ([opp_xpat10] AS INT) AS[opp_xpat10]
		,CAST ([opp_csat10] AS INT) AS[opp_csat10]
		,CAST ([golddiffat10] AS INT) AS[golddiffat10]
		,CAST ([xpdiffat10] AS INT) AS[xpdiffat10]
		,CAST ([csdiffat10] AS INT) AS[csdiffat10]
		,CAST ([killsat10] AS INT) AS[killsat10]
		,CAST ([assistsat10] AS INT) AS[assistsat10]
		,CAST ([deathsat10] AS INT) AS[deathsat10]
		,CAST ([opp_killsat10] AS INT) AS[opp_killsat10]
		,CAST ([opp_assistsat10] AS INT) AS[opp_assistsat10]
		,CAST ([opp_deathsat10] AS INT) AS[opp_deathsat10]
		,CAST ([goldat15] AS INT) AS[goldat15]
		,CAST ([xpat15] AS INT) AS[xpat15]
		,CAST ([csat15] AS INT) AS[csat15]
		,CAST ([opp_goldat15] AS INT) AS[opp_goldat15]
		,CAST ([opp_xpat15] AS INT) AS[opp_xpat15]
		,CAST ([opp_csat15] AS INT) AS[opp_csat15]
		,CAST ([golddiffat15] AS INT) AS[golddiffat15]
		,CAST ([xpdiffat15] AS INT) AS[xpdiffat15]
		,CAST ([csdiffat15] AS INT) AS[csdiffat15]
		,CAST ([killsat15] AS INT) AS[killsat15]
		,CAST ([assistsat15] AS INT) AS[assistsat15]
		,CAST ([deathsat15] AS INT) AS[deathsat15]
		,CAST ([opp_killsat15] AS INT) AS[opp_killsat15]
		,CAST ([opp_assistsat15] AS INT) AS[opp_assistsat15]
		,CAST ([opp_deathsat15] AS INT) AS[opp_deathsat15]
	FROM [dbo].[DADOS_PARTIDAS_2023]


ALTER TABLE [dbo].[FatoPartida]
ALTER COLUMN [TempoPartida] NVARCHAR (4000)


CREATE TABLE FatoPartida(
	IDPartida VARCHAR (50) NOT NULL
	,DadosCompletos VARCHAR (50) NULL
	,IDLiga INT NULL
	,LigaTemporada VARCHAR (50) NULL
	,Playoff VARCHAR (50) NULL
	,DataPartida VARCHAR (50) NULL
	,Jogo VARCHAR (50) NULL
	,Patch VARCHAR (50) NULL
	,Lado VARCHAR (50) NULL
	,Posicao VARCHAR (50) NULL
	,IDJogador INT NULL
	,IDEquipe INT NULL
	,Campeao VARCHAR (50) NULL
	,PrimeiroBan VARCHAR (50) NULL
	,SegundoBan VARCHAR (50) NULL
	,TerceiroBan VARCHAR (50) NULL
	,QuartoBan VARCHAR (50) NULL
	,QuintoBan VARCHAR (50) NULL
	,TempoPartida VARCHAR(4000) NULL
	,Resultado VARCHAR (50) NULL
	,Abates INT
	,Mortes INT
	,Assistencias INT
	,EquipeAbates INT
	,EquipeMortes INT
	,DoubleKills INT
	,TripleKills INT
	,QuadraKills INT
	,PentaKills INT
	,PrimeiroAbate VARCHAR (50) NULL
	,PrimeiroAbate_Abatedor VARCHAR (50) NULL
	,PrimeiroAbate_Assist VARCHAR (50) NULL
	,PrimeiroAbate_Vitima VARCHAR (50) NULL
	,[Equipe_Abates/Min] FLOAT
	,[Equipe_AbatesCamp/Min] INT
	,DragaoPrimeiro VARCHAR (50) NULL
	,DragaoAbates INT
	,Adv_DragaoAbates INT
	,DragaoAbateElemental INT
	,Adv_DragaoAbateElemental INT
	,DragaoAbate_Infernal INT
	,DragaoAbate_Montanha INT
	,DragaoAbate_Nuvens INT
	,DragaoAbate_Oceano INT
	,DragaoAbate_Quimtech INT
	,DragaoAbate_Hextech INT
	,DragaoAbate_Anciao INT
	,Adv_DragaoAbate_Anciao INT
	,ArautoPrimeiro VARCHAR (50) NULL
	,ArautosAbate INT
	,BaraoPrimeiro VARCHAR(50)
	,BaraoAbate INT
	,TorrePrimeira VARCHAR (50) NULL
	,TorreDestruida INT
	,Adv_TorreDestruida INT
	,TorreMidPrimeiro VARCHAR (50) NULL
	,TorreTresPrimeiro VARCHAR (50) NULL
	,TorreBarricadasDestruidas INT
	,Adv_TorreBarricadasDestruidas INT
	,Inibidores INT
	,Adv_Inibidores INT
	,DanoACampeoes FLOAT
	,[Dano/Min] FLOAT
	,[%ParticipDano] FLOAT
	,[DanoRecebido/Min] FLOAT
	,[DanoMitigado/Min] FLOAT
	,[WardsPosicionadas] INT
	,[WardsPorisionadas/Min] FLOAT
	,[WardsRemovidas] INT
	,[WardsControlePosicionadas/Min] FLOAT
	,[WardsControleCompradas] INT
	,[PlacarVisao] INT
	,[PlacarVisao/Min] FLOAT
	,OuroTotal INT
	,OuroRecebido INT
	,[OuroRecebido/Min] FLOAT
	,[%OuroRecebidoParticip] FLOAT
	,OuroGasto INT
	,[OuroGasto/Dano] FLOAT
	,FarmTotal INT
	,Farm_MinionAbate INT
	,Farm_MonstrosAbate INT
	,Farm_MonstrosSelvaAliadaAbate INT
	,Farm_MonstrosSelvaAdvAbate INT
	,[Farm/Min] FLOAT
	,Ouro_10min INT
	,XP_10min INT
	,Farm_10min INT
	,Adv_Ouro_10min INT
	,Adv_XP_10min INT
	,Adv_Farm_10min INT
	,OuroDiff_10min INT
	,XPDiff_10min INT
	,FarmDiff_10min INT
	,Abates_10min INT
	,Assistencias_10min INT
	,Mortes_10min INT
	,Adv_Abates_10min INT
	,Adv_Assistencias_10min INT
	,Adv_Mortes_10min INT
	,Ouro_15min INT
	,XP_15min INT
	,Farm_15min INT
	,Adv_Ouro_15min INT
	,Adv_XP_15min INT
	,Adv_Farm_15min INT
	,OuroDiff_15min INT
	,XPDiff_15min INT
	,FarmDiff_15min INT
	,Abates_15min INT
	,Assistencias_15min INT
	,Mortes_15min INT
	,Adv_Abates_15min INT
	,Adv_Assistencia_15min INT
	,Adv_Mortes_15min INT
)
alter table [dbo].[FatoPartida]
add CONSTRAINT [PK_FatoPedido_IDPedido] PRIMARY KEY CLUSTERED 
(
	[IDPartida] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
 

ALTER TABLE [dbo].[FatoPartida]
ALTER COLUMN [TempoPartida] NVARCHAR(4000)
--ALTER COLUMN [DataPartida] INT

ALTER TABLE [dbo].[DimLiga] DROP CONSTRAINt [PK_DimLiga_IDLiga] ;
ALTER TABLE[dbo].[FatoPartida] DROP CONSTRAINT[PK_FatoPedido_IDPedido]

ALTER TABLE [dbo].[FatoPartida]  WITH CHECK ADD  CONSTRAINT [FK_FatoPartida_DimLiga] FOREIGN KEY([IDLiga])
REFERENCES [dbo].[DimLiga] ([IDLiga])
GO
ALTER TABLE [dbo].[FatoPartida] CHECK CONSTRAINT [FK_FatoPartida_DimLiga]


ALTER TABLE [dbo].[FatoPartida]  WITH CHECK ADD  CONSTRAINT [FK_FatoPartida_DimJogador] FOREIGN KEY([IDJogador])
REFERENCES [dbo].[DimJogador] ([IDJogador])
GO
ALTER TABLE [dbo].[FatoPartida] CHECK CONSTRAINT [FK_FatoPartida_DimJogador]


ALTER TABLE [dbo].[FatoPartida]  WITH CHECK ADD  CONSTRAINT [FK_FatoPedido_DimEquipe] FOREIGN KEY([IDEquipe])
REFERENCES [dbo].[DimEquipe] ([IDEquipe])
GO
ALTER TABLE [dbo].[FatoPartida] CHECK CONSTRAINT [FK_FatoPartida_DimEquipe]


ALTER TABLE [dbo].[FatoPartida]  WITH CHECK ADD  CONSTRAINT [FK_FatoPartida_DimDate] FOREIGN KEY([DataPartida])
REFERENCES [dbo].[DimDate] ([DateKey])
GO
ALTER TABLE [dbo].[FatoPartida] CHECK CONSTRAINT [FK_FatoPartida_DimDate]
----------------------------------------------------------
--------------CRIACAO TABELAS DIMENSOES-------------------
----------------------------------------------------------

CREATE TABLE DimLiga (
	IDLiga INT IDENTITY (1,1) NOT NULL
	,Liga VARCHAR (50) NULL

 CONSTRAINT [PK_DimLiga_IDLiga] PRIMARY KEY CLUSTERED (
	[IDLiga] ASC
	)
	WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]


CREATE TABLE DimJogador(
	IDJogador INT IDENTITY (1,1) NOT NULL
	,IDAlternativo_Jogador VARCHAR(50)
	,NickJogador VARCHAR(50)
 CONSTRAINT [PK_DimJogador_IDJogador] PRIMARY KEY CLUSTERED (
	[IDJogador] ASC
	)
	WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]


CREATE TABLE DimEquipe(
	IDEquipe INT IDENTITY (1,1) NOT NULL
	,IDEquipe_Alternativo VARCHAR(50) NULL
	,NomeEquipe VARCHAR(50) NULL
	CONSTRAINT [PK_DimEquipe_IDEquipe] PRIMARY KEY CLUSTERED (
	[IDEquipe] ASC
	)
	WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

----------------------------------------------------------
----------------------------------------------------------
----------------------------------------------------------



----------------------------------------------------------
------------------CRIANDO AS VIEWS------------------------
----------------------------------------------------------


CREATE VIEW [Vw_DimLiga] AS
	SELECT DISTINCT
		DENSE_RANK() OVER (ORDER BY [league]) AS ID_League
		,[league]
	FROM [dbo].[DADOS_PARTIDAS_2023]



CREATE VIEW [Vw_DimJogador] AS
	SELECT DISTINCT
		DENSE_RANK() OVER (ORDER BY [playerid]) AS ID_Jogador
		,[playerid]
		,[playername]
		FROM [dbo].[DADOS_PARTIDAS_2023]



CREATE VIEW [Vw_DimEquipe] AS
	SELECT DISTINCT
		DENSE_RANK() OVER (ORDER BY [teamid]) AS IDEquipe
		,[teamid]
		,[teamname]
		FROM [dbo].[DADOS_PARTIDAS_2023]

-------------------------------------------------------------
-------------------------------------------------------------
-------------------------------------------------------------