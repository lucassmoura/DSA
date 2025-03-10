
import cx_Oracle
import pandas as pd
import os

OraclHost = os.environ.get('OraclHost')
OraclPsw = os.environ.get('OraclPsw')


cx_Oracle.init_oracle_client(lib_dir="C:/oracle/instantclient_19_6")
dsn_tns = cx_Oracle.makedsn(OraclHost, '1521', service_name='X98PAZ_999999_PP') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
conn = cx_Oracle.connect(user='USR_QLIK_AGR', password=OraclPsw, dsn=dsn_tns) # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'

c = conn.cursor()



dup_vencer = c.execute('''SELECT '03' AS CodEmp,
        TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
        SUM(E1_SALDO) as Valor,
        'CNH' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '1.DUPLICATAS A VENCER' AS  SUBGRUPO

FROM siga_producao12.SE1030 SE 
LEFT JOIN  SIGA_PRODUCAO12.sa1030 SA ON A1_COD = E1_CLIENTE AND A1_LOJA = E1_LOJA 
WHERE
(

(A1_XEMPGRU = '1' AND substr(E1_TIPO,0,2)  IN ( 'NF','DP','NP','FT','BC') ) OR

(substr(E1_TIPO,0,2)  IN('CC','CD')  OR E1_TIPO='BON') OR 

(substr(E1_TIPO,0,2)  IN('NF','DP','NP','FT','BC','CH','FI') AND E1_XTPFIMA IN (' ','U','R') AND A1_XEMPGRU<>'1' AND TO_DATE(e1_vencrea, 'YYYYMMDD')>= SYSDATE-60)

)

AND 

E1_SALDO>0  AND se.d_e_l_e_t_=' ' AND sa.d_e_l_e_t_=' '  AND E1_SITUACA NOT IN ('O','Q') AND TRIM(e1_vencrea) IS NOT NULL
 
UNION ALL

SELECT '27' AS CodEmp,
        TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
        SUM(E1_SALDO) as Valor,
        'OUTROS' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '1.DUPLICATAS A VENCER' AS  SUBGRUPO

FROM siga_producao12.SE1270 SE 
LEFT JOIN  SIGA_PRODUCAO12.sa1270 SA ON A1_COD = E1_CLIENTE AND A1_LOJA = E1_LOJA 
WHERE
(

(A1_XEMPGRU = '1' AND substr(E1_TIPO,0,2)  IN ( 'NF','DP','NP','FT','BC') ) OR

(substr(E1_TIPO,0,2)  IN('CC','CD')  OR E1_TIPO='BON') OR 

(substr(E1_TIPO,0,2)  IN('NF','DP','NP','FT','BC','CH','FI') AND E1_XTPFIMA IN (' ','U','R') AND A1_XEMPGRU<>'1' AND e1_vencrea>= to_CHAR(SYSDATE-60,'YYYYMMDD')))

AND 

E1_SALDO>0  AND se.d_e_l_e_t_=' ' AND sa.d_e_l_e_t_=' '  AND E1_SITUACA NOT IN ('O','Q') 

UNION ALL

SELECT '04' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) AS Valor,
         'CNH' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '1.DUPLICATAS A VENCER' AS  SUBGRUPO
FROM siga_producao12.SE1040 SE 
LEFT JOIN  SIGA_PRODUCAO12.sa1040 SA ON A1_COD = E1_CLIENTE AND A1_LOJA = E1_LOJA
WHERE
(

(A1_XEMPGRU = '1' AND substr(E1_TIPO,0,2)  IN ( 'NF','DP','NP','FT','BC') ) OR

(substr(E1_TIPO,0,2)  IN('CC','CD')  OR E1_TIPO='BON') OR 

(substr(E1_TIPO,0,2)  IN('NF','DP','NP','FT','BC','CH','FI') AND E1_XTPFIMA IN (' ','U','R') AND A1_XEMPGRU<>'1' AND TO_DATE(e1_vencrea, 'YYYYMMDD')>= SYSDATE-60)

)

AND 

E1_SALDO>0  AND se.d_e_l_e_t_=' '  AND sa.d_e_l_e_t_=' ' AND E1_SITUACA NOT IN ('O','Q') AND TRIM(e1_vencrea) IS NOT NULL

UNION ALL

SELECT '01' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA, 
    SUM(E1_SALDO) as Valor,
         'AGCO' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '1.DUPLICATAS A VENCER' AS  SUBGRUPO

    FROM siga_producao12.SE1010 SE 
LEFT JOIN  SIGA_PRODUCAO12.SA1080   SA ON A1_COD = E1_CLIENTE AND A1_LOJA = E1_LOJA
WHERE
(

(A1_XEMPGRU = '1' AND substr(E1_TIPO,0,2)  IN ( 'NF','DP','NP','FT','BC') ) OR

(substr(E1_TIPO,0,2)  IN('CC','CD')  OR E1_TIPO='BON') OR 

(substr(E1_TIPO,0,2)  IN('NF','DP','NP','FT','BC','CH','FI') AND E1_XTPFIMA IN (' ','U','R') AND A1_XEMPGRU<>'1' AND TO_DATE(e1_vencrea, 'YYYYMMDD')>= SYSDATE-60)

)

AND 

E1_SALDO>0  AND se.d_e_l_e_t_=' '  AND sa.d_e_l_e_t_=' ' AND E1_SITUACA NOT IN ('O','Q') AND TRIM(e1_vencrea) IS NOT NULL

UNION ALL

SELECT '08' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) as Valor,
     'AGCO' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '1.DUPLICATAS A VENCER' AS  SUBGRUPO
FROM siga_producao12.SE1080 SE 
LEFT JOIN  SIGA_PRODUCAO12.sa1080 SA ON A1_COD = E1_CLIENTE AND A1_LOJA = E1_LOJA
WHERE
(

(A1_XEMPGRU = '1' AND substr(E1_TIPO,0,2)  IN ( 'NF','DP','NP','FT','BC') ) OR

(substr(E1_TIPO,0,2)  IN('CC','CD')  OR E1_TIPO='BON') OR 

(substr(E1_TIPO,0,2)  IN('NF','DP','NP','FT','BC','CH','FI') AND E1_XTPFIMA IN (' ','U','R') AND A1_XEMPGRU<>'1' AND TO_DATE(e1_vencrea, 'YYYYMMDD')>= SYSDATE-60)

)

AND 

E1_SALDO>0  AND se.d_e_l_e_t_=' '  AND sa.d_e_l_e_t_=' ' AND E1_SITUACA NOT IN ('O','Q') AND TRIM(e1_vencrea) IS NOT NULL

UNION ALL

SELECT '24' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) as Valor,
         'AGCO' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '1.DUPLICATAS A VENCER' AS  SUBGRUPO
FROM siga_producao12.SE1240 SE 
LEFT JOIN  SIGA_PRODUCAO12.sa1240 SA ON A1_COD = E1_CLIENTE AND A1_LOJA = E1_LOJA
WHERE
(

(A1_XEMPGRU = '1' AND substr(E1_TIPO,0,2)  IN ( 'NF','DP','NP','FT','BC') ) OR

(substr(E1_TIPO,0,2)  IN('CC','CD')  OR E1_TIPO='BON') OR 

(substr(E1_TIPO,0,2)  IN('NF','DP','NP','FT','BC','CH','FI') AND E1_XTPFIMA IN (' ','U','R') AND A1_XEMPGRU<>'1' AND TO_DATE(e1_vencrea, 'YYYYMMDD')>= SYSDATE-60)

)

AND 

E1_SALDO>0  AND se.d_e_l_e_t_=' '  AND sa.d_e_l_e_t_=' ' AND E1_SITUACA NOT IN ('O','Q') AND TRIM(e1_vencrea) IS NOT NULL

UNION ALL

SELECT '11' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO)as Valor,
    'CNH' AS COMARCA,
    '2.CONTAS A RECEBER' AS GRUPO,
    '1.DUPLICATAS A VENCER' AS  SUBGRUPO

    FROM siga_producao12.SE1110 SE 
LEFT JOIN  SIGA_PRODUCAO12.sa1110 SA ON A1_COD = E1_CLIENTE AND A1_LOJA = E1_LOJA
WHERE
(

(A1_XEMPGRU = '1' AND substr(E1_TIPO,0,2)  IN ( 'NF','DP','NP','FT','BC') ) OR

(substr(E1_TIPO,0,2)  IN('CC','CD')  OR E1_TIPO='BON') OR 

(substr(E1_TIPO,0,2)  IN('NF','DP','NP','FT','BC','CH','FI') AND E1_XTPFIMA IN (' ','U','R') AND A1_XEMPGRU<>'1' AND TO_DATE(e1_vencrea, 'YYYYMMDD')>= SYSDATE-60)

)

AND 

E1_SALDO>0  AND se.d_e_l_e_t_=' ' AND sa.d_e_l_e_t_=' ' AND E1_SITUACA NOT IN ('O','Q') AND TRIM(e1_vencrea) IS NOT NULL
UNION ALL

SELECT '06' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) as Valor,
         'CNH' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '1.DUPLICATAS A VENCER' AS  SUBGRUPO
FROM siga_producao12.SE1060 SE 
LEFT JOIN  SIGA_PRODUCAO12.sa1060 SA ON A1_COD = E1_CLIENTE AND A1_LOJA = E1_LOJA
WHERE
(

(A1_XEMPGRU = '1' AND substr(E1_TIPO,0,2)  IN ( 'NF','DP','NP','FT','BC') ) OR

(substr(E1_TIPO,0,2)  IN('CC','CD')  OR E1_TIPO='BON') OR 

(substr(E1_TIPO,0,2)  IN('NF','DP','NP','FT','BC','CH','FI') AND E1_XTPFIMA IN (' ','U','R') AND A1_XEMPGRU<>'1' AND TO_DATE(e1_vencrea, 'YYYYMMDD')>= SYSDATE-60)

)

AND 

E1_SALDO>0  AND se.d_e_l_e_t_=' ' AND sa.d_e_l_e_t_=' ' AND E1_SITUACA NOT IN ('O','Q') AND TRIM(e1_vencrea) IS NOT NULL

UNION ALL

SELECT '23' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
        SUM(E1_SALDO) as Valor,
             'CNH' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '1.DUPLICATAS A VENCER' AS  SUBGRUPO
FROM siga_producao12.SE1230 SE 
LEFT JOIN  SIGA_PRODUCAO12.sa1230 SA ON A1_COD = E1_CLIENTE AND A1_LOJA = E1_LOJA
WHERE
(

(A1_XEMPGRU = '1' AND substr(E1_TIPO,0,2)  IN ( 'NF','DP','NP','FT','BC') ) OR

(substr(E1_TIPO,0,2)  IN('CC','CD')  OR E1_TIPO='BON') OR 

(substr(E1_TIPO,0,2)  IN('NF','DP','NP','FT','BC','CH','FI') AND E1_XTPFIMA IN (' ','U','R') AND A1_XEMPGRU<>'1' AND TO_DATE(e1_vencrea, 'YYYYMMDD')>= SYSDATE-60)

)

AND 

E1_SALDO>0  AND se.d_e_l_e_t_=' ' AND sa.d_e_l_e_t_=' ' AND E1_SITUACA NOT IN ('O','Q') AND TRIM(e1_vencrea) IS NOT NULL

UNION ALL

SELECT '07' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) as Valor,
         'CNH' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '1.DUPLICATAS A VENCER' AS  SUBGRUPO
FROM siga_producao12.SE1070 SE 
LEFT JOIN  SIGA_PRODUCAO12.sa1070 SA ON A1_COD = E1_CLIENTE AND A1_LOJA = E1_LOJA
WHERE
(

(A1_XEMPGRU = '1' AND substr(E1_TIPO,0,2)  IN ( 'NF','DP','NP','FT','BC') ) OR

(substr(E1_TIPO,0,2)  IN('CC','CD')  OR E1_TIPO='BON') OR 

(substr(E1_TIPO,0,2)  IN('NF','DP','NP','FT','BC','CH','FI') AND E1_XTPFIMA IN (' ','U','R') AND A1_XEMPGRU<>'1' AND TO_DATE(e1_vencrea, 'YYYYMMDD')>= SYSDATE-60)

)

AND 

E1_SALDO>0  AND se.d_e_l_e_t_=' ' AND sa.d_e_l_e_t_=' ' AND E1_SITUACA NOT IN ('O','Q') AND TRIM(e1_vencrea) IS NOT NULL

UNION ALL

SELECT '25' AS CodEmp,
        TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
        SUM(E1_SALDO) as Valor,
        'OUTROS' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '1.DUPLICATAS A VENCER' AS  SUBGRUPO

FROM siga_producao12.SE1250 SE 
LEFT JOIN  SIGA_PRODUCAO12.sa1250 SA ON A1_COD = E1_CLIENTE AND A1_LOJA = E1_LOJA 
WHERE
(

(A1_XEMPGRU = '1' AND substr(E1_TIPO,0,2)  IN ( 'NF','DP','NP','FT','BC') ) OR

(substr(E1_TIPO,0,2)  IN('CC','CD')  OR E1_TIPO='BON') OR 

(substr(E1_TIPO,0,2)  IN('NF','DP','NP','FT','BC','CH','FI') AND E1_XTPFIMA IN (' ','U','R') AND A1_XEMPGRU<>'1' AND e1_vencrea>= to_CHAR(SYSDATE-60,'YYYYMMDD')))

AND 

E1_SALDO>0  AND se.d_e_l_e_t_=' ' AND sa.d_e_l_e_t_=' '  AND E1_SITUACA NOT IN ('O','Q') 
''')

dup_vencer = pd.DataFrame(dup_vencer,columns=['CodEmp','DATA','VALOR','COMARCA','GRUPO','SUBGRUPO'])
dup_vencer['DATA'] = pd.to_datetime(dup_vencer['DATA']).apply(lambda x: x.date())


# In[4]:


dup_vencidas = c.execute('''SELECT 
    '03' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) as Valor,
         'CNH' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '2.DUPLICATAS VENCIDAS' AS  SUBGRUPO
    FROM siga_producao12.SE1030 SE 
LEFT JOIN  SIGA_PRODUCAO12.sa1030 SA ON A1_COD = E1_CLIENTE AND A1_LOJA = E1_LOJA
WHERE A1_XEMPGRU <> '1' AND substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC','CH','FI' ) AND 
 E1_XTPFIMA IN (' ','U','R') AND  e1_vencrea <= to_char(SYSDATE-60,'YYYYMMDD')  
AND E1_SALDO>0  AND se.d_e_l_e_t_=' '  AND sa.d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R')AND  TRIM(e1_vencrea) IS NOT NULL 

UNION ALL 

SELECT '01' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) as Valor,
         'AGCO' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '2.DUPLICATAS VENCIDAS' AS  SUBGRUPO
    FROM siga_producao12.SE1010 SE 
LEFT JOIN  SIGA_PRODUCAO12.sa1080 SA ON A1_COD = E1_CLIENTE AND A1_LOJA = E1_LOJA
WHERE A1_XEMPGRU <> '1' AND substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC','CH','FI' ) AND 
 E1_XTPFIMA IN (' ','U','R') AND  e1_vencrea <= to_char(SYSDATE-60,'YYYYMMDD')  
AND E1_SALDO>0  AND se.d_e_l_e_t_=' '  AND sa.d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R')AND  TRIM(e1_vencrea) IS NOT NULL 

UNION ALL 

SELECT '08' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) as Valor,
         'AGCO' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '2.DUPLICATAS VENCIDAS' AS  SUBGRUPO
    FROM siga_producao12.SE1080 SE 
LEFT JOIN  SIGA_PRODUCAO12.sa1080 SA ON A1_COD = E1_CLIENTE AND A1_LOJA = E1_LOJA
WHERE A1_XEMPGRU <> '1' AND substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC','CH','FI' ) AND 
 E1_XTPFIMA IN (' ','U','R') AND  e1_vencrea <= to_char(SYSDATE-60,'YYYYMMDD')  
AND E1_SALDO>0  AND se.d_e_l_e_t_=' '  AND sa.d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R')AND  TRIM(e1_vencrea) IS NOT NULL 


UNION ALL 

SELECT '24' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) as Valor,
         'AGCO' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '2.DUPLICATAS VENCIDAS' AS  SUBGRUPO
    FROM siga_producao12.SE1240 SE 
LEFT JOIN  SIGA_PRODUCAO12.sa1240 SA ON A1_COD = E1_CLIENTE AND A1_LOJA = E1_LOJA
WHERE A1_XEMPGRU <> '1' AND substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC','CH','FI' ) AND 
 E1_XTPFIMA IN (' ','U','R') AND  e1_vencrea <= to_char(SYSDATE-60,'YYYYMMDD')
AND E1_SALDO>0  AND se.d_e_l_e_t_=' '  AND sa.d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R')AND  TRIM(e1_vencrea) IS NOT NULL 



UNION ALL 

SELECT '04' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) as Valor,
         'CNH' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '2.DUPLICATAS VENCIDAS' AS  SUBGRUPO
    FROM siga_producao12.SE1040 SE 
LEFT JOIN  SIGA_PRODUCAO12.sa1040 SA ON A1_COD = E1_CLIENTE AND A1_LOJA = E1_LOJA
WHERE A1_XEMPGRU <> '1' AND substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC','CH' ,'FI') AND 
 E1_XTPFIMA IN (' ','U','R') AND  e1_vencrea <= to_char(SYSDATE-60,'YYYYMMDD')  
AND E1_SALDO>0  AND se.d_e_l_e_t_=' '  AND sa.d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R')AND  TRIM(e1_vencrea) IS NOT NULL 


UNION ALL 

SELECT '11' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) as Valor,
         'CNH' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '2.DUPLICATAS VENCIDAS' AS  SUBGRUPO
    FROM siga_producao12.SE1110 SE 
LEFT JOIN  SIGA_PRODUCAO12.sa1110 SA ON A1_COD = E1_CLIENTE AND A1_LOJA = E1_LOJA
WHERE A1_XEMPGRU <> '1' AND substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC','CH','FI' ) AND 
 E1_XTPFIMA IN (' ','U','R') AND  e1_vencrea <= to_char(SYSDATE-60,'YYYYMMDD')  
AND E1_SALDO>0  AND se.d_e_l_e_t_=' '  AND sa.d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R')AND  TRIM(e1_vencrea) IS NOT NULL 
 


UNION ALL 

SELECT '06' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) as Valor,
         'CNH' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '2.DUPLICATAS VENCIDAS' AS  SUBGRUPO
    FROM siga_producao12.SE1060 SE 
LEFT JOIN  SIGA_PRODUCAO12.sa1060 SA ON A1_COD = E1_CLIENTE AND A1_LOJA = E1_LOJA
WHERE A1_XEMPGRU <> '1' AND substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC','CH','FI' ) AND 
 E1_XTPFIMA IN (' ','U','R') AND  e1_vencrea <= to_char(SYSDATE-60,'YYYYMMDD')  
AND E1_SALDO>0  AND se.d_e_l_e_t_=' '  AND sa.d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R')AND  TRIM(e1_vencrea) IS NOT NULL 


UNION ALL 

SELECT '23' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) as Valor,
         'CNH' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '2.DUPLICATAS VENCIDAS' AS  SUBGRUPO
    FROM siga_producao12.SE1230 SE 
LEFT JOIN  SIGA_PRODUCAO12.sa1230 SA ON A1_COD = E1_CLIENTE AND A1_LOJA = E1_LOJA
WHERE A1_XEMPGRU <> '1' AND substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC','CH','FI' ) AND 
 E1_XTPFIMA IN ('','U','R') AND A1_XEMPGRU<>'1' AND  e1_vencrea <= to_char(SYSDATE-60,'YYYYMMDD')  
AND E1_SALDO>0  AND se.d_e_l_e_t_=' '  AND sa.d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R')AND  TRIM(e1_vencrea) IS NOT NULL 

UNION ALL 

SELECT '07' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) as Valor,
         'CNH' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '2.DUPLICATAS VENCIDAS' AS  SUBGRUPO
    FROM siga_producao12.SE1070 SE 
LEFT JOIN  SIGA_PRODUCAO12.sa1070 SA ON A1_COD = E1_CLIENTE AND A1_LOJA = E1_LOJA
WHERE A1_XEMPGRU <> '1' AND substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC','CH' ,'FI') AND 
 E1_XTPFIMA IN (' ','U','R') AND  e1_vencrea <= to_char(SYSDATE-60,'YYYYMMDD')  
AND E1_SALDO>0  AND se.d_e_l_e_t_=' '  AND sa.d_e_l_e_t_=' '  AND sa.d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R')AND  TRIM(e1_vencrea) IS NOT NULL 
 
UNION ALL 
SELECT 
    '27' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) as Valor,
         'OUTROS' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '2.DUPLICATAS VENCIDAS' AS  SUBGRUPO
    FROM siga_producao12.SE1270 SE 
LEFT JOIN  SIGA_PRODUCAO12.sa1270 SA ON A1_COD = E1_CLIENTE AND A1_LOJA = E1_LOJA
WHERE A1_XEMPGRU <> '1' AND substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC','CH','FI' ) AND 
 E1_XTPFIMA IN (' ','U','R') AND  e1_vencrea <= to_char(SYSDATE-60,'YYYYMMDD')  
AND E1_SALDO>0  AND se.d_e_l_e_t_=' '  AND sa.d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R')

UNION ALL 

SELECT 
    '25' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) as Valor,
         'OUTROS' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '2.DUPLICATAS VENCIDAS' AS  SUBGRUPO
    FROM siga_producao12.SE1250 SE 
LEFT JOIN  SIGA_PRODUCAO12.sa1250 SA ON A1_COD = E1_CLIENTE AND A1_LOJA = E1_LOJA
WHERE A1_XEMPGRU <> '1' AND substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC','CH','FI' ) AND 
 E1_XTPFIMA IN (' ','U','R') AND  e1_vencrea <= to_char(SYSDATE-60,'YYYYMMDD')  
AND E1_SALDO>0  AND se.d_e_l_e_t_=' '  AND sa.d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R')

''')

dup_vencidas = pd.DataFrame(dup_vencidas,columns=['CodEmp','DATA','VALOR','COMARCA','GRUPO','SUBGRUPO'])
dup_vencidas['DATA'] = pd.to_datetime(dup_vencidas['DATA']).apply(lambda x: x.date())


# In[5]:


fin_avencer = c.execute('''SELECT '04' AS CodEmp,
        TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
        SUM(E1_SALDO) AS VALOR,
        'CNH' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '4.FINANCIAMENTO A VENCER' AS SUBGRUPO
FROM siga_producao12.SE1040 SE 
where  E1_XTPFIMA IN ('F','C')and   substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC')  AND E1_SALDO>0  AND d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R') 
And TO_DATE(e1_vencrea, 'YYYYMMDD') >= SYSDATE-1 AND TRIM(e1_vencrea) IS NOT NULL

UNION ALL

SELECT '03' AS CodEmp,
        TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
        SUM(E1_SALDO) AS VALOR,
        'CNH' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '4.FINANCIAMENTO A VENCER' AS SUBGRUPO
FROM siga_producao12.SE1030 SE 
where  E1_XTPFIMA IN ('F','C')and   substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC')  AND E1_SALDO>0  AND d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R') 
And TO_DATE(e1_vencrea, 'YYYYMMDD') >= SYSDATE-1 AND TRIM(e1_vencrea) IS NOT NULL

UNION ALL

SELECT '01' AS CodEmp,
        TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
        SUM(E1_SALDO) AS VALOR,
        'AGCO' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '4.FINANCIAMENTO A VENCER' AS SUBGRUPO
FROM siga_producao12.SE1010 SE 
where  E1_XTPFIMA IN ('F','C')and   substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC','FI' )  AND E1_SALDO>0  AND d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R') 
And TO_DATE(e1_vencrea, 'YYYYMMDD') >= SYSDATE-1 AND TRIM(e1_vencrea) IS NOT NULL

UNION ALL

SELECT '08' AS CodEmp,
        TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
        SUM(E1_SALDO) AS VALOR,
        'AGCO' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '4.FINANCIAMENTO A VENCER' AS SUBGRUPO
FROM siga_producao12.SE1080 SE 
where  E1_XTPFIMA IN ('F','C')and   substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC' )  AND E1_SALDO>0  AND d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R') 
And TO_DATE(e1_vencrea, 'YYYYMMDD') >= SYSDATE-1 AND TRIM(e1_vencrea) IS NOT NULL
UNION ALL

SELECT '24' AS CodEmp,
        TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
        SUM(E1_SALDO) AS VALOR,
        'AGCO' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '4.FINANCIAMENTO A VENCER' AS SUBGRUPO
FROM siga_producao12.SE1240 SE 
where  E1_XTPFIMA IN ('F','C')and   substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC')  AND E1_SALDO>0  AND d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R') 
And TO_DATE(e1_vencrea, 'YYYYMMDD') >= SYSDATE-1 AND TRIM(e1_vencrea) IS NOT NULL
UNION ALL

SELECT '11' AS CodEmp,
        TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
        SUM(E1_SALDO) AS VALOR,
        'CNH' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '4.FINANCIAMENTO A VENCER' AS SUBGRUPO
FROM siga_producao12.SE1110 SE 
where  E1_XTPFIMA IN ('F','C')and   substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC' )  AND E1_SALDO>0  AND d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R') 
And TO_DATE(e1_vencrea, 'YYYYMMDD') >= SYSDATE-1 AND TRIM(e1_vencrea) IS NOT NULL

UNION ALL

SELECT '06' AS CodEmp,
        TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
        SUM(E1_SALDO) AS VALOR,
        'CNH' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '4.FINANCIAMENTO A VENCER' AS SUBGRUPO
FROM siga_producao12.SE1060 SE 
where  E1_XTPFIMA IN ('F','C')and   substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC' )  AND E1_SALDO>0  AND d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R') 
And TO_DATE(e1_vencrea, 'YYYYMMDD') >= SYSDATE-1 AND TRIM(e1_vencrea) IS NOT NULL
UNION ALL

SELECT '23' AS CodEmp,
        TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
        SUM(E1_SALDO) AS VALOR,
        'CNH' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '4.FINANCIAMENTO A VENCER' AS SUBGRUPO
FROM siga_producao12.SE1230 SE 
where  E1_XTPFIMA IN ('F','C')and   substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC' )  AND E1_SALDO>0  AND d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R') 
And TO_DATE(e1_vencrea, 'YYYYMMDD') >= SYSDATE-1 AND TRIM(e1_vencrea) IS NOT NULL

UNION ALL

SELECT '07' AS CodEmp,
        TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
        SUM(E1_SALDO) AS VALOR,
        'CNH' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '4.FINANCIAMENTO A VENCER' AS SUBGRUPO
FROM siga_producao12.SE1070 SE 
where  E1_XTPFIMA IN ('F','C')and   substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC')  AND E1_SALDO>0  AND d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R') 
And TO_DATE(e1_vencrea, 'YYYYMMDD') >= SYSDATE-1 AND TRIM(e1_vencrea) IS NOT NULL
UNION ALL 

SELECT '25' AS CodEmp,
        TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
        SUM(E1_SALDO) AS VALOR,
        'OUTROS' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '4.FINANCIAMENTO A VENCER' AS SUBGRUPO
FROM siga_producao12.SE1250 SE 
where  E1_XTPFIMA IN ('F','C')and   substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC')  AND E1_SALDO>0  AND d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R') 
And e1_vencrea >= TO_CHAR(SYSDATE-1,'YYYYMMDD')
UNION ALL 
SELECT '27' AS CodEmp,
        TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
        SUM(E1_SALDO) AS VALOR,
        'OUTROS' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '4.FINANCIAMENTO A VENCER' AS SUBGRUPO
FROM siga_producao12.SE1270 SE 
where  E1_XTPFIMA IN ('F','C')and   substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC')  AND E1_SALDO>0  AND d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R') 
And e1_vencrea >= TO_CHAR(SYSDATE-1,'YYYYMMDD')
''')

fin_avencer = pd.DataFrame(fin_avencer,columns=['CodEmp','DATA','VALOR','COMARCA','GRUPO','SUBGRUPO'])
fin_avencer['DATA'] = pd.to_datetime(fin_avencer['DATA']).apply(lambda x: x.date())


# In[6]:


fin_vencidas = c.execute('''SELECT '04' AS CodEmp,
        TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
        SUM(E1_SALDO) AS VALOR,
        'CNH' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '3.FINANCIAMENTO VENCIDOS' AS SUBGRUPO
FROM siga_producao12.SE1040 SE 
where  E1_XTPFIMA IN ('F','C')and   substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC' )  AND E1_SALDO>0  AND d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R') 
And TO_DATE(e1_vencrea, 'YYYYMMDD') < SYSDATE-1 AND TRIM(e1_vencrea) IS NOT NULL

UNION ALL

SELECT '03' AS CodEmp,
        TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
        SUM(E1_SALDO) AS VALOR,
        'CNH' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '3.FINANCIAMENTO VENCIDOS' AS SUBGRUPO
FROM siga_producao12.SE1030 SE 
where  E1_XTPFIMA IN ('F','C')and   substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC' )  AND E1_SALDO>0  AND d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R') 
And TO_DATE(e1_vencrea, 'YYYYMMDD') < SYSDATE-1 AND TRIM(e1_vencrea) IS NOT NULL

UNION ALL

SELECT '01' AS CodEmp,
        TO_DATE(SYSDATE,'DD/MM/YY') AS DATA,
        SUM(E1_SALDO) AS VALOR,
        'AGCO' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '3.FINANCIAMENTO VENCIDOS' AS SUBGRUPO
FROM siga_producao12.SE1010 SE 
where  E1_XTPFIMA IN ('F','C')and   substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC' )  AND E1_SALDO>0  AND d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R') 
And TO_DATE(e1_vencrea, 'YYYYMMDD') < SYSDATE-1 AND TRIM(e1_vencrea) IS NOT NULL

UNION ALL

SELECT '08' AS CodEmp,
        TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
        SUM(E1_SALDO) AS VALOR,
        'AGCO' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '3.FINANCIAMENTO VENCIDOS' AS SUBGRUPO
FROM siga_producao12.SE1080 SE 
where  E1_XTPFIMA IN ('F','C')and   substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC' )  AND E1_SALDO>0  AND d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R') 
And TO_DATE(e1_vencrea, 'YYYYMMDD') < SYSDATE-1 AND TRIM(e1_vencrea) IS NOT NULL
UNION ALL

SELECT '24' AS CodEmp,
        TO_DATE(SYSDATE,'DD/MM/YY') AS DATA,
        SUM(E1_SALDO) AS VALOR,
        'AGCO' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '3.FINANCIAMENTO VENCIDOS' AS SUBGRUPO
FROM siga_producao12.SE1240 SE 
where  E1_XTPFIMA IN ('F','C')and   substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC' )  AND E1_SALDO>0  AND d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R') 
And TO_DATE(e1_vencrea, 'YYYYMMDD') < SYSDATE-1 AND TRIM(e1_vencrea) IS NOT NULL
UNION ALL

SELECT '11' AS CodEmp,
         TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
        SUM(E1_SALDO) AS VALOR,
        'CNH' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '3.FINANCIAMENTO VENCIDOS' AS SUBGRUPO
FROM siga_producao12.SE1110 SE 
where  E1_XTPFIMA IN ('F','C')and   substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC' )  AND E1_SALDO>0  AND d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R') 
And TO_DATE(e1_vencrea, 'YYYYMMDD') < SYSDATE-1 AND TRIM(e1_vencrea) IS NOT NULL

UNION ALL

SELECT '06' AS CodEmp,
        TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
        SUM(E1_SALDO) AS VALOR,
        'CNH' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '3.FINANCIAMENTO VENCIDOS' AS SUBGRUPO
FROM siga_producao12.SE1060 SE 
where  E1_XTPFIMA IN ('F','C')and   substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC')  AND E1_SALDO>0  AND d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R') 
And TO_DATE(e1_vencrea, 'YYYYMMDD') < SYSDATE-1 AND TRIM(e1_vencrea) IS NOT NULL
UNION ALL

SELECT '23' AS CodEmp,
        TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
        SUM(E1_SALDO) AS VALOR,
        'CNH' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '3.FINANCIAMENTO VENCIDOS' AS SUBGRUPO
FROM siga_producao12.SE1230 SE 
where  E1_XTPFIMA IN ('F','C')and  E1_TIPO IN ( 'NF','DP','NP','FT','BC' )  AND E1_SALDO>0  AND d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R') 
And TO_DATE(e1_vencrea, 'YYYYMMDD') < SYSDATE-1 AND TRIM(e1_vencrea) IS NOT NULL

UNION ALL

SELECT '07' AS CodEmp,
        TO_DATE(SYSDATE,'DD/MM/YY') AS DATA,
        SUM(E1_SALDO) AS VALOR,
        'CNH' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '3.FINANCIAMENTO VENCIDOS' AS SUBGRUPO
FROM siga_producao12.SE1070 SE 
where  E1_XTPFIMA IN ('F','C')and  E1_TIPO IN ( 'NF','DP','NP','FT','BC' )  AND E1_SALDO>0  AND d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R') 
And TO_DATE(e1_vencrea, 'YYYYMMDD') < SYSDATE-1 AND TRIM(e1_vencrea) IS NOT NULL
UNION ALL
SELECT '27' AS CodEmp,
        TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
        SUM(E1_SALDO) AS VALOR,
        'OUTROS' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '3.FINANCIAMENTO VENCIDOS' AS SUBGRUPO
FROM siga_producao12.SE1270 SE 
where  E1_XTPFIMA IN ('F','C')and   substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC' )  AND E1_SALDO>0  AND d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R') 
And e1_vencrea< TO_CHAR(SYSDATE-1,'YYYYMMDD')  

UNION ALL 
SELECT '25' AS CodEmp,
        TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
        SUM(E1_SALDO) AS VALOR,
        'OUTROS' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '3.FINANCIAMENTO VENCIDOS' AS SUBGRUPO
FROM siga_producao12.SE1250 SE 
where  E1_XTPFIMA IN ('F','C')and   substr(E1_TIPO,0,2) IN ( 'NF','DP','NP','FT','BC' )  AND E1_SALDO>0  AND d_e_l_e_t_=' ' AND E1_SITUACA NOT IN( '6','M','N','O','P','Q','R') 
And e1_vencrea< TO_CHAR(SYSDATE-1,'YYYYMMDD')  

''')

fin_vencidas = pd.DataFrame(fin_vencidas,columns=['CodEmp','DATA','VALOR','COMARCA','GRUPO','SUBGRUPO'])
fin_vencidas['DATA'] = pd.to_datetime(fin_vencidas['DATA']).apply(lambda x: x.date())


# In[7]:


juri = c.execute('''SELECT '07' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY') AS DATA,
    SUM(E1_SALDO) as Valor,
         'CNH' AS COMARCA,
        '9.JURIDICOS' AS GRUPO,
        'AÇÕES' AS  SUBGRUPO
FROM siga_producao12.SE1070 SE 
WHERE  substr(E1_TIPO,0,2) IN('NF','DP','NP','FT','BC','FI')  AND 
E1_SALDO>0  AND se.d_e_l_e_t_=' ' AND E1_SITUACA IN( '6','M','N','P','R') AND e1_vencrea <= to_char(SYSDATE-60,'YYYYMMDD')  
AND TRIM(e1_vencrea) IS NOT NULL

UNION ALL 

SELECT '01' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) as Valor,
         'AGCO' AS COMARCA,
        '9.JURIDICOS' AS GRUPO,
        'AÇÕES' AS  SUBGRUPO
FROM siga_producao12.SE1010 SE 
WHERE  substr(E1_TIPO,0,2) IN('NF','DP','NP','FT','BC','FI')  AND 
E1_SALDO>0  AND se.d_e_l_e_t_=' ' AND E1_SITUACA IN( '5','6','M','N','P','R') AND e1_vencrea <= to_char(SYSDATE-60,'YYYYMMDD') 
AND TRIM(e1_vencrea) IS NOT NULL
UNION ALL 

SELECT '08' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) as Valor,
         'AGCO' AS COMARCA,
        '9.JURIDICOS' AS GRUPO,
        'AÇÕES' AS  SUBGRUPO
FROM siga_producao12.SE1080 SE 
WHERE  substr(E1_TIPO,0,2) IN('NF','DP','NP','FT','BC','FI')  AND 
E1_SALDO>0  AND se.d_e_l_e_t_=' ' AND E1_SITUACA IN( '5','6','M','N','P','R') AND e1_vencrea <= to_char(SYSDATE-60,'YYYYMMDD') 
AND TRIM(e1_vencrea) IS NOT NULL
UNION ALL 

SELECT '24' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY') AS DATA,
    SUM(E1_SALDO) as Valor,
         'AGCO' AS COMARCA,
        '9.JURIDICOS' AS GRUPO,
        'AÇÕES' AS  SUBGRUPO
FROM siga_producao12.SE1240 SE 
WHERE  substr(E1_TIPO,0,2) IN('NF','DP','NP','FT','BC','FI')  AND 
E1_SALDO>0  AND se.d_e_l_e_t_=' ' AND E1_SITUACA IN( '5','6','M','N','P','R') AND e1_vencrea <= to_char(SYSDATE-60,'YYYYMMDD') 
AND TRIM(e1_vencrea) IS NOT NULL
UNION ALL 
SELECT '03' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) as Valor,
         'CNH' AS COMARCA,
        '9.JURIDICOS' AS GRUPO,
        'AÇÕES' AS  SUBGRUPO
FROM siga_producao12.SE1030 SE 
WHERE  substr(E1_TIPO,0,2) IN('NF','DP','NP','FT','BC','FI')  AND 
E1_SALDO>0  AND se.d_e_l_e_t_=' ' AND E1_SITUACA IN( '5','6','M','N','P','R') AND e1_vencrea <= to_char(SYSDATE-60,'YYYYMMDD') 

UNION ALL 
SELECT '04' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) as Valor,
         'CNH' AS COMARCA,
        '9.JURIDICOS' AS GRUPO,
        'AÇÕES' AS  SUBGRUPO
FROM siga_producao12.SE1040 SE 
WHERE  substr(E1_TIPO,0,2) IN('NF','DP','NP','FT','BC','FI')  AND 
E1_SALDO>0  AND se.d_e_l_e_t_=' ' AND E1_SITUACA IN( '5','6','M','N','P','R') AND e1_vencrea <= to_char(SYSDATE-60,'YYYYMMDD') 
AND TRIM(e1_vencrea) IS NOT NULL
UNION ALL
SELECT '06' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) as Valor,
         'CNH' AS COMARCA,
        '9.JURIDICOS' AS GRUPO,
        'AÇÕES' AS  SUBGRUPO
FROM siga_producao12.SE1060 SE 
WHERE  substr(E1_TIPO,0,2) IN('NF','DP','NP','FT','BC','FI')  AND 
E1_SALDO>0  AND se.d_e_l_e_t_=' ' AND E1_SITUACA IN( '5','6','M','N','P','R') AND e1_vencrea <= to_char(SYSDATE-60,'YYYYMMDD') 
AND TRIM(e1_vencrea) IS NOT NULL
UNION ALL 

SELECT '11' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) as Valor,
         'CNH' AS COMARCA,
        '9.JURIDICOS' AS GRUPO,
        'AÇÕES' AS  SUBGRUPO
FROM siga_producao12.SE1110 SE 
WHERE  substr(E1_TIPO,0,2) IN('NF','DP','NP','FT','BC','FI')  AND 
E1_SALDO>0  AND se.d_e_l_e_t_=' ' AND E1_SITUACA IN( '5','6','M','N','P','R') AND e1_vencrea <= to_char(SYSDATE-60,'YYYYMMDD') 
AND TRIM(e1_vencrea) IS NOT NULL
UNION ALL 
SELECT '23' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) as Valor,
         'CNH' AS COMARCA,
        '9.JURIDICOS' AS GRUPO,
        'AÇÕES' AS  SUBGRUPO
FROM siga_producao12.SE1230 SE 
WHERE  substr(E1_TIPO,0,2) IN('NF','DP','NP','FT','BC','FI')  AND 
E1_SALDO>0  AND se.d_e_l_e_t_=' ' AND E1_SITUACA IN( '5','6','M','N','P','R') AND e1_vencrea <= to_char(SYSDATE-60,'YYYYMMDD') 
UNION ALL 

 
SELECT '27' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) as Valor,
         'OUTROS' AS COMARCA,
        '9.JURIDICOS' AS GRUPO,
        'AÇÕES' AS  SUBGRUPO
FROM siga_producao12.SE1270 SE 
WHERE  substr(E1_TIPO,0,2) IN('NF','DP','NP','FT','BC','FI')  AND 
E1_SALDO>0  AND se.d_e_l_e_t_=' ' AND E1_SITUACA IN( '5','6','M','N','P','R') AND e1_vencrea <= to_char(SYSDATE-60,'YYYYMMDD') 
 UNION ALL 
 
  
SELECT '25' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) as Valor,
         'OUTROS' AS COMARCA,
        '9.JURIDICOS' AS GRUPO,
        'AÇÕES' AS  SUBGRUPO
FROM siga_producao12.SE1250 SE 
WHERE  substr(E1_TIPO,0,2) IN('NF','DP','NP','FT','BC','FI')  AND 
E1_SALDO>0  AND se.d_e_l_e_t_=' ' AND E1_SITUACA IN( '5','6','M','N','P','R') AND e1_vencrea <= to_char(SYSDATE-60,'YYYYMMDD') 

''')

juri = pd.DataFrame(juri,columns=['CodEmp','DATA','VALOR','COMARCA','GRUPO','SUBGRUPO'])
juri['DATA'] = pd.to_datetime(juri['DATA']).apply(lambda x: x.date())


# In[8]:


PC = c.execute(''' 
SELECT '03' as CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM((E2_SALDO+e2_acresc)-e2_decresc)  as VALOR, 
    'CNH' AS COMARCA,
        '4.CONTAS A PAGAR'  AS GRUPO,
        'FORNECEDOR / PEÇAS' AS  SUBGRUPO
        FROM  SIGA_PRODUCAO12.SE2030 e21
WHERE EXISTS(SELECT 
DISTINCT  E2_NUM, E2_LOJA,e2_prefixo,E2_FORNECE, E2_SALDO,E2_PARCELA
FROM SIGA_PRODUCAO12.SE2030 e2
LEFT JOIN SIGA_PRODUCAO12.SD1030 D1 ON
   D1_DOC = E2_NUM AND D1_FORNECE = E2_FORNECE AND SUBSTR(e2.e2_prefixo,0,2) = D1_FILIAL AND D1_LOJA = E2_LOJA
   LEFT JOIN SIGA_PRODUCAO12.SB1040   D1 ON
   D1_COD = B1_COD 
WHERE E2.D_E_L_E_T_=' ' and e2_saldo>0 AND TO_DATE(e2.e2_emissao, 'YYYYMMDD') <= SYSDATE
AND E2_NATUREZ IN( '0201001','0201002','0102003','0101001','0201003','0201004','0201005','0201006','0201007','0201008','0201009','0201010') 
AND  E2_TIPO IN('NF','DP','FT')AND B1_TIPO IN ('ME')
AND
e21.E2_FORNECE = e2.E2_FORNECE 
AND e2.e2_prefixo = e21.e2_prefixo 
AND e21.E2_LOJA = e2.E2_LOJA AND
e21.E2_NUM = e2.E2_NUM)

UNION ALL


SELECT '01' as CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM((E2_SALDO+e2_acresc)-e2_decresc)  as VALOR, 
    'AGCO' AS COMARCA,
        '4.CONTAS A PAGAR'  AS GRUPO,
        'FORNECEDOR / PEÇAS' AS  SUBGRUPO
        FROM  SIGA_PRODUCAO12.SE2010 e21
WHERE EXISTS(SELECT 
DISTINCT  E2_NUM, E2_LOJA,e2_prefixo,E2_FORNECE, E2_SALDO,E2_PARCELA
FROM SIGA_PRODUCAO12.SE2010 e2
LEFT JOIN SIGA_PRODUCAO12.SD1010 D1 ON
   D1_DOC = E2_NUM AND D1_FORNECE = E2_FORNECE AND SUBSTR(e2.e2_prefixo,0,2) = D1_FILIAL AND D1_LOJA = E2_LOJA
   LEFT JOIN SIGA_PRODUCAO12.SB1040   D1 ON
   D1_COD = B1_COD 
WHERE E2.D_E_L_E_T_=' ' and e2_saldo>0 AND TO_DATE(e2.e2_emissao, 'YYYYMMDD') <= SYSDATE
AND E2_NATUREZ IN( '0201001','0201002','0101001','0201003','0201004','0201005','0201006','0201007','0201008','0201009','0201010') 
AND  E2_TIPO IN('NF','DP','FT')AND B1_TIPO IN ('ME')
AND
e21.E2_FORNECE = e2.E2_FORNECE 
AND e2.e2_prefixo = e21.e2_prefixo 
AND e21.E2_LOJA = e2.E2_LOJA AND
e21.E2_NUM = e2.E2_NUM)

UNION ALL


SELECT '04' as CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM((E2_SALDO+e2_acresc)-e2_decresc)  as VALOR, 
    'CNH' AS COMARCA,
        '4.CONTAS A PAGAR'  AS GRUPO,
        'FORNECEDOR / PEÇAS' AS  SUBGRUPO
        FROM  SIGA_PRODUCAO12.SE2040 e21
WHERE EXISTS(SELECT 
DISTINCT  E2_NUM, E2_LOJA,e2_prefixo,E2_FORNECE, E2_SALDO,E2_PARCELA
FROM SIGA_PRODUCAO12.SE2040 e2
LEFT JOIN SIGA_PRODUCAO12.SD1040 D1 ON
   D1_DOC = E2_NUM AND D1_FORNECE = E2_FORNECE AND SUBSTR(e2.e2_prefixo,0,2) = D1_FILIAL AND D1_LOJA = E2_LOJA
   LEFT JOIN SIGA_PRODUCAO12.SB1040   D1 ON
   D1_COD = B1_COD 
WHERE E2.D_E_L_E_T_=' ' and e2_saldo>0 AND TO_DATE(e2.e2_emissao, 'YYYYMMDD') <= SYSDATE
AND E2_NATUREZ IN( '0201001','0201002','0101001','0102003','0201003','0201004','0201005','0201006','0201007','0201008','0201009','0201010') 
AND  E2_TIPO IN('NF','DP','FT')AND B1_TIPO IN ('ME')
AND
e21.E2_FORNECE = e2.E2_FORNECE 
AND e2.e2_prefixo = e21.e2_prefixo 
AND e21.E2_LOJA = e2.E2_LOJA AND
e21.E2_NUM = e2.E2_NUM)
UNION ALL


SELECT '06' as CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM((E2_SALDO+e2_acresc)-e2_decresc)  as VALOR, 
    'CNH' AS COMARCA,
        '4.CONTAS A PAGAR'  AS GRUPO,
        'FORNECEDOR / PEÇAS' AS  SUBGRUPO
        FROM  SIGA_PRODUCAO12.SE2060 e21
WHERE EXISTS(SELECT 
DISTINCT  E2_NUM, E2_LOJA,e2_prefixo,E2_FORNECE, E2_SALDO,E2_PARCELA
FROM SIGA_PRODUCAO12.SE2060 e2
LEFT JOIN SIGA_PRODUCAO12.SD1060 D1 ON
   D1_DOC = E2_NUM AND D1_FORNECE = E2_FORNECE AND SUBSTR(e2.e2_prefixo,0,2) = D1_FILIAL AND D1_LOJA = E2_LOJA
   LEFT JOIN SIGA_PRODUCAO12.SB1060   D1 ON
   D1_COD = B1_COD 
WHERE E2.D_E_L_E_T_=' ' and e2_saldo>0 AND TO_DATE(e2.e2_emissao, 'YYYYMMDD') <= SYSDATE
AND E2_NATUREZ IN( '0201001','0201002','0101001','0102003','0201003','0201004','0201005','0201006','0201007','0201008','0201009','0201010') 
AND  E2_TIPO IN('NF','DP','FT')AND B1_TIPO IN ('ME')
AND
e21.E2_FORNECE = e2.E2_FORNECE 
AND e2.e2_prefixo = e21.e2_prefixo 
AND e21.E2_LOJA = e2.E2_LOJA AND
e21.E2_NUM = e2.E2_NUM)


UNION ALL


SELECT '08' as CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM((E2_SALDO+e2_acresc)-e2_decresc)  as VALOR, 
    'CNH' AS COMARCA,
        '4.CONTAS A PAGAR'  AS GRUPO,
        'FORNECEDOR / PEÇAS' AS  SUBGRUPO
        FROM  SIGA_PRODUCAO12.SE2080 e21
WHERE EXISTS(SELECT 
DISTINCT  E2_NUM, E2_LOJA,e2_prefixo,E2_FORNECE, E2_SALDO,E2_PARCELA
FROM SIGA_PRODUCAO12.SE2080 e2
LEFT JOIN SIGA_PRODUCAO12.SD1080 D1 ON
   D1_DOC = E2_NUM AND D1_FORNECE = E2_FORNECE AND SUBSTR(e2.e2_prefixo,0,2) = D1_FILIAL AND D1_LOJA = E2_LOJA
   LEFT JOIN SIGA_PRODUCAO12.SB1040   D1 ON
   D1_COD = B1_COD 
WHERE E2.D_E_L_E_T_=' ' and e2_saldo>0 AND TO_DATE(e2.e2_emissao, 'YYYYMMDD') <= SYSDATE
AND E2_NATUREZ IN( '0201001','0201002','0101001','0201003','0201004','0201005','0201006','0201007','0201008','0201009','0201010') 
AND  E2_TIPO IN('NF','DP','FT')AND B1_TIPO IN ('ME')
AND
e21.E2_FORNECE = e2.E2_FORNECE 
AND e2.e2_prefixo = e21.e2_prefixo 
AND e21.E2_LOJA = e2.E2_LOJA AND
e21.E2_NUM = e2.E2_NUM)

UNION ALL


SELECT '11' as CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM((E2_SALDO+e2_acresc)-e2_decresc)  as VALOR, 
    'CNH' AS COMARCA,
        '4.CONTAS A PAGAR'  AS GRUPO,
        'FORNECEDOR / PEÇAS' AS  SUBGRUPO
        FROM  SIGA_PRODUCAO12.SE2110 e21
WHERE EXISTS(SELECT 
DISTINCT  E2_NUM, E2_LOJA,e2_prefixo,E2_FORNECE, E2_SALDO,E2_PARCELA
FROM SIGA_PRODUCAO12.SE2110 e2
LEFT JOIN SIGA_PRODUCAO12.SD1110 D1 ON
   D1_DOC = E2_NUM AND D1_FORNECE = E2_FORNECE AND SUBSTR(e2.e2_prefixo,0,2) = D1_FILIAL AND D1_LOJA = E2_LOJA
   LEFT JOIN SIGA_PRODUCAO12.SB1040   D1 ON
   D1_COD = B1_COD 
WHERE E2.D_E_L_E_T_=' ' and e2_saldo>0 AND TO_DATE(e2.e2_emissao, 'YYYYMMDD') <= SYSDATE
AND E2_NATUREZ IN( '0201001','0201002','0102003','0101001','0201003','0201004','0201005','0201006','0201007','0201008','0201009','0201010') 
AND  E2_TIPO IN('NF','DP','FT')AND B1_TIPO IN ('ME')
AND
e21.E2_FORNECE = e2.E2_FORNECE 
AND e2.e2_prefixo = e21.e2_prefixo 
AND e21.E2_LOJA = e2.E2_LOJA AND
e21.E2_NUM = e2.E2_NUM)

UNION ALL


SELECT '07' as CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM((E2_SALDO+e2_acresc)-e2_decresc)  as VALOR, 
    'CNH' AS COMARCA,
        '4.CONTAS A PAGAR'  AS GRUPO,
        'FORNECEDOR / PEÇAS' AS  SUBGRUPO
        FROM  SIGA_PRODUCAO12.SE2070 e21
WHERE EXISTS(SELECT 
DISTINCT  E2_NUM, E2_LOJA,e2_prefixo,E2_FORNECE, E2_SALDO,E2_PARCELA
FROM SIGA_PRODUCAO12.SE2070 e2
LEFT JOIN SIGA_PRODUCAO12.SD1070 D1 ON
   D1_DOC = E2_NUM AND D1_FORNECE = E2_FORNECE AND SUBSTR(e2.e2_prefixo,0,2) = D1_FILIAL AND D1_LOJA = E2_LOJA
   LEFT JOIN SIGA_PRODUCAO12.SB1070   D1 ON
   D1_COD = B1_COD 
WHERE E2.D_E_L_E_T_=' ' and e2_saldo>0 AND TO_DATE(e2.e2_emissao, 'YYYYMMDD') <= SYSDATE
AND E2_NATUREZ IN( '0201001','0201002','0101001','0201003','0201004','0201005','0201006','0201007','0201008','0201009','0201010') 
AND  E2_TIPO IN('NF','DP','FT')AND B1_TIPO IN ('ME')
AND
e21.E2_FORNECE = e2.E2_FORNECE 
AND e2.e2_prefixo = e21.e2_prefixo 
AND e21.E2_LOJA = e2.E2_LOJA AND
e21.E2_NUM = e2.E2_NUM)

UNION ALL


SELECT '23' as CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM((E2_SALDO+e2_acresc)-e2_decresc)  as VALOR, 
    'CNH' AS COMARCA,
        '4.CONTAS A PAGAR'  AS GRUPO,
        'FORNECEDOR / PEÇAS' AS  SUBGRUPO
        FROM  SIGA_PRODUCAO12.SE2230 e21
WHERE EXISTS(SELECT 
DISTINCT  E2_NUM, E2_LOJA,e2_prefixo,E2_FORNECE, E2_SALDO,E2_PARCELA
FROM SIGA_PRODUCAO12.SE2230 e2
LEFT JOIN SIGA_PRODUCAO12.SD1230 D1 ON
   D1_DOC = E2_NUM AND D1_FORNECE = E2_FORNECE AND SUBSTR(e2.e2_prefixo,0,2) = D1_FILIAL AND D1_LOJA = E2_LOJA
   LEFT JOIN SIGA_PRODUCAO12.SB1230   D1 ON
   D1_COD = B1_COD 
WHERE E2.D_E_L_E_T_=' ' and e2_saldo>0 AND TO_DATE(e2.e2_emissao, 'YYYYMMDD') <= SYSDATE
AND E2_NATUREZ IN( '0201001','0201002','0101001','0102003','0201003','0201004','0201005','0201006','0201007','0201008','0201009','0201010') 
AND  E2_TIPO IN('NF','DP','FT')AND B1_TIPO IN ('ME')
AND
e21.E2_FORNECE = e2.E2_FORNECE 
AND e2.e2_prefixo = e21.e2_prefixo 
AND e21.E2_LOJA = e2.E2_LOJA AND
e21.E2_NUM = e2.E2_NUM)
UNION ALL
SELECT '27' as CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM((E2_SALDO+e2_acresc)-e2_decresc)  as VALOR, 
    'OUTROS' AS COMARCA,
        '4.CONTAS A PAGAR'  AS GRUPO,
        'FORNECEDOR / PEÇAS' AS  SUBGRUPO
        FROM  SIGA_PRODUCAO12.SE2270 e21
WHERE EXISTS(SELECT 
DISTINCT  E2_NUM, E2_LOJA,e2_prefixo,E2_FORNECE, E2_SALDO,E2_PARCELA
FROM SIGA_PRODUCAO12.SE2270 e2
LEFT JOIN SIGA_PRODUCAO12.SD1270 D1 ON
   D1_DOC = E2_NUM AND D1_FORNECE = E2_FORNECE AND SUBSTR(e2.e2_prefixo,0,2) = D1_FILIAL AND D1_LOJA = E2_LOJA
   LEFT JOIN SIGA_PRODUCAO12.SB1270   D1 ON
   D1_COD = B1_COD 
WHERE E2.D_E_L_E_T_=' ' and e2_saldo>0 AND e2.e2_emissao <=TO_CHAR(SYSDATE, 'YYYYMMDD')  
AND E2_NATUREZ IN( '0201001','0201002','0101001','0102003','0201003','0201004','0201005','0201006','0201007','0201008','0201009','0201010') 
AND  E2_TIPO IN('NF','DP','FT')AND B1_TIPO IN ('ME')
AND
e21.E2_FORNECE = e2.E2_FORNECE 
AND e2.e2_prefixo = e21.e2_prefixo 
AND e21.E2_LOJA = e2.E2_LOJA AND
e21.E2_NUM = e2.E2_NUM)

UNION ALL

SELECT '25' as CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM((E2_SALDO+e2_acresc)-e2_decresc)  as VALOR, 
    'OUTROS' AS COMARCA,
        '4.CONTAS A PAGAR'  AS GRUPO,
        'FORNECEDOR / PEÇAS' AS  SUBGRUPO
        FROM  SIGA_PRODUCAO12.SE2250 e21
WHERE EXISTS(SELECT 
DISTINCT  E2_NUM, E2_LOJA,e2_prefixo,E2_FORNECE, E2_SALDO,E2_PARCELA
FROM SIGA_PRODUCAO12.SE2250 e2
LEFT JOIN SIGA_PRODUCAO12.SD1250 D1 ON
   D1_DOC = E2_NUM AND D1_FORNECE = E2_FORNECE AND SUBSTR(e2.e2_prefixo,0,2) = D1_FILIAL AND D1_LOJA = E2_LOJA
   LEFT JOIN SIGA_PRODUCAO12.SB1040   D1 ON
   D1_COD = B1_COD 
WHERE E2.D_E_L_E_T_=' ' and e2_saldo>0 AND e2.e2_emissao <=TO_CHAR(SYSDATE, 'YYYYMMDD')  
AND E2_NATUREZ IN( '0201001','0201002','0101001','0102003','0201003','0201004','0201005','0201006','0201007','0201008','0201009','0201010') 
AND  E2_TIPO IN('NF','DP','FT')AND B1_TIPO IN ('ME')
AND
e21.E2_FORNECE = e2.E2_FORNECE 
AND e2.e2_prefixo = e21.e2_prefixo 
AND e21.E2_LOJA = e2.E2_LOJA AND
e21.E2_NUM = e2.E2_NUM)

UNION ALL


SELECT '24' as CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM((E2_SALDO+e2_acresc)-e2_decresc)  as VALOR, 
    'AGCO' AS COMARCA,
        '4.CONTAS A PAGAR'  AS GRUPO,
        'FORNECEDOR / PEÇAS' AS  SUBGRUPO
        FROM  SIGA_PRODUCAO12.SE2240 e21
WHERE EXISTS(SELECT 
DISTINCT  E2_NUM, E2_LOJA,e2_prefixo,E2_FORNECE, E2_SALDO,E2_PARCELA
FROM SIGA_PRODUCAO12.SE2240 e2
LEFT JOIN SIGA_PRODUCAO12.SD1240 D1 ON
   D1_DOC = E2_NUM AND D1_FORNECE = E2_FORNECE AND SUBSTR(e2.e2_prefixo,0,2) = D1_FILIAL AND D1_LOJA = E2_LOJA
   LEFT JOIN SIGA_PRODUCAO12.SB1040   D1 ON
   D1_COD = B1_COD 
WHERE E2.D_E_L_E_T_=' ' and e2_saldo>0 AND TO_DATE(e2.e2_emissao, 'YYYYMMDD') <= SYSDATE
AND E2_NATUREZ IN( '0201001','0201002','0101001','0201003','0201004','0201005','0201006','0201007','0201008','0201009','0201010') 
AND  E2_TIPO IN('NF','DP','FT')AND B1_TIPO IN ('ME')
AND
e21.E2_FORNECE = e2.E2_FORNECE 
AND e2.e2_prefixo = e21.e2_prefixo 
AND e21.E2_LOJA = e2.E2_LOJA AND
e21.E2_NUM = e2.E2_NUM)
UNION ALL

SELECT '03' as CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM((E2_SALDO+e2_acresc)-e2_decresc)  as VALOR, 
    'CNH' AS COMARCA,
        '4.CONTAS A PAGAR'  AS GRUPO,
        'MAQUINAS / WHOLESALE' AS  SUBGRUPO
        FROM  SIGA_PRODUCAO12.SE2030 e21
WHERE EXISTS(SELECT 
DISTINCT  E2_NUM, E2_LOJA,e2_prefixo,E2_FORNECE, E2_SALDO,E2_PARCELA
FROM SIGA_PRODUCAO12.SE2030 e2
LEFT JOIN SIGA_PRODUCAO12.SD1030 D1 ON
   D1_DOC = E2_NUM AND D1_FORNECE = E2_FORNECE AND SUBSTR(e2.e2_prefixo,0,2) = D1_FILIAL AND D1_LOJA = E2_LOJA
   LEFT JOIN SIGA_PRODUCAO12.SB1040   D1 ON
   D1_COD = B1_COD 
WHERE  ((B1_TIPO IN ('PV') and E2.D_E_L_E_T_=' ' and e2_saldo>0 AND TO_DATE(e2.e2_emissao, 'YYYYMMDD') <= SYSDATE
AND E2_NATUREZ IN( '0205097','0201001','0201002','0101001','0102003','0201003','0201004','0201005','0201006','0201007','0201008','0201009','0201010') 
AND  E2_TIPO IN('NF','DP','FT')) OR  (  E2.D_E_L_E_T_=' ' and e2_saldo>0 AND TO_DATE(e2.e2_emissao, 'YYYYMMDD') <= SYSDATE
AND E2_NATUREZ IN( '0205097','0201001','0201002','0101001','0102003','0201003','0201004','0201005','0201006','0201007','0201008','0201009','0201010') 
AND  E2_TIPO IN('NF','DP','FT') AND E2_HIST = 'WHOLESALE' AND E2_SALDO>0))
AND
e21.E2_FORNECE = e2.E2_FORNECE 
AND e2.e2_prefixo = e21.e2_prefixo 
AND e21.E2_LOJA = e2.E2_LOJA AND
e21.E2_NUM = e2.E2_NUM) 

UNION ALL


SELECT '01' as CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM((E2_SALDO+e2_acresc)-e2_decresc)  as VALOR, 
    'AGCO' AS COMARCA,
        '4.CONTAS A PAGAR'  AS GRUPO,
        'MAQUINAS / WHOLESALE' AS  SUBGRUPO
        FROM  SIGA_PRODUCAO12.SE2010 e21
WHERE EXISTS(SELECT 
DISTINCT  E2_NUM, E2_LOJA,e2_prefixo,E2_FORNECE, E2_SALDO,E2_PARCELA
FROM SIGA_PRODUCAO12.SE2010 e2
LEFT JOIN SIGA_PRODUCAO12.SD1010 D1 ON
   D1_DOC = E2_NUM AND D1_FORNECE = E2_FORNECE AND SUBSTR(e2.e2_prefixo,0,2) = D1_FILIAL AND D1_LOJA = E2_LOJA
   LEFT JOIN SIGA_PRODUCAO12.SB1040   D1 ON
   D1_COD = B1_COD 
WHERE E2.D_E_L_E_T_=' ' and e2_saldo>0 AND TO_DATE(e2.e2_emissao, 'YYYYMMDD') <= SYSDATE
AND E2_NATUREZ IN( '0201001','0201002','0101001','0201003','0201004','0201005','0201006','0201007','0201008','0201009','0201010') 
AND  E2_TIPO IN('NF','DP','FT')AND B1_TIPO IN ('PV')
AND
e21.E2_FORNECE = e2.E2_FORNECE 
AND e2.e2_prefixo = e21.e2_prefixo 
AND e21.E2_LOJA = e2.E2_LOJA AND
e21.E2_NUM = e2.E2_NUM)

UNION ALL 

SELECT '27' as CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM((E2_SALDO+e2_acresc)-e2_decresc)  as VALOR, 
    'OUTROS' AS COMARCA,
        '4.CONTAS A PAGAR'  AS GRUPO,
        'MAQUINAS / WHOLESALE' AS  SUBGRUPO
        FROM  SIGA_PRODUCAO12.SE2270 e21
WHERE EXISTS(SELECT 
DISTINCT  E2_NUM, E2_LOJA,e2_prefixo,E2_FORNECE, E2_SALDO,E2_PARCELA
FROM SIGA_PRODUCAO12.SE2270 e2
LEFT JOIN SIGA_PRODUCAO12.SD1270 D1 ON
   D1_DOC = E2_NUM AND D1_FORNECE = E2_FORNECE AND SUBSTR(e2.e2_prefixo,0,2) = D1_FILIAL AND D1_LOJA = E2_LOJA
   LEFT JOIN SIGA_PRODUCAO12.SB1270   D1 ON
   D1_COD = B1_COD 
WHERE E2.D_E_L_E_T_=' ' and e2_saldo>0 AND TO_DATE(e2.e2_emissao, 'YYYYMMDD') <= SYSDATE
AND E2_NATUREZ IN( '0201001','0201002','0101001','0201003','0201004','0201005','0201006','0201007','0201008','0201009','0201010') 
AND  E2_TIPO IN('NF','DP','FT')AND B1_TIPO IN ('PV')
AND
e21.E2_FORNECE = e2.E2_FORNECE 
AND e2.e2_prefixo = e21.e2_prefixo 
AND e21.E2_LOJA = e2.E2_LOJA AND
e21.E2_NUM = e2.E2_NUM)

UNION ALL

SELECT '25' as CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM((E2_SALDO+e2_acresc)-e2_decresc)  as VALOR, 
    'OUTROS' AS COMARCA,
        '4.CONTAS A PAGAR'  AS GRUPO,
        'MAQUINAS / WHOLESALE' AS  SUBGRUPO
        FROM  SIGA_PRODUCAO12.SE2250 e21
WHERE EXISTS(SELECT 
DISTINCT  E2_NUM, E2_LOJA,e2_prefixo,E2_FORNECE, E2_SALDO,E2_PARCELA
FROM SIGA_PRODUCAO12.SE2250 e2
LEFT JOIN SIGA_PRODUCAO12.SD1250 D1 ON
   D1_DOC = E2_NUM AND D1_FORNECE = E2_FORNECE AND SUBSTR(e2.e2_prefixo,0,2) = D1_FILIAL AND D1_LOJA = E2_LOJA
   LEFT JOIN SIGA_PRODUCAO12.SB1040   D1 ON
   D1_COD = B1_COD 
WHERE E2.D_E_L_E_T_=' ' and e2_saldo>0 AND TO_DATE(e2.e2_emissao, 'YYYYMMDD') <= SYSDATE
AND E2_NATUREZ IN( '0201001','0201002','0101001','0201003','0201004','0201005','0201006','0201007','0201008','0201009','0201010') 
AND  E2_TIPO IN('NF','DP','FT')AND B1_TIPO IN ('PV')
AND
e21.E2_FORNECE = e2.E2_FORNECE 
AND e2.e2_prefixo = e21.e2_prefixo 
AND e21.E2_LOJA = e2.E2_LOJA AND
e21.E2_NUM = e2.E2_NUM)
UNION ALL


SELECT '04' as CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM((E2_SALDO+e2_acresc)-e2_decresc)  as VALOR, 
    'CNH' AS COMARCA,
        '4.CONTAS A PAGAR'  AS GRUPO,
        'MAQUINAS / WHOLESALE' AS  SUBGRUPO
        FROM  SIGA_PRODUCAO12.SE2040 e21
WHERE EXISTS(SELECT 
DISTINCT  E2_NUM, E2_LOJA,e2_prefixo,E2_FORNECE, E2_SALDO,E2_PARCELA
FROM SIGA_PRODUCAO12.SE2040 e2
LEFT JOIN SIGA_PRODUCAO12.SD1040 D1 ON
   D1_DOC = E2_NUM AND D1_FORNECE = E2_FORNECE AND SUBSTR(e2.e2_prefixo,0,2) = D1_FILIAL AND D1_LOJA = E2_LOJA
   LEFT JOIN SIGA_PRODUCAO12.SB1040   D1 ON
   D1_COD = B1_COD 
WHERE  ((B1_TIPO IN ('PV') and E2.D_E_L_E_T_=' ' and e2_saldo>0 AND TO_DATE(e2.e2_emissao, 'YYYYMMDD') <= SYSDATE
AND E2_NATUREZ IN('0205097', '0201001','0201002','0101001','0102003','0201003','0201004','0201005','0201006','0201007','0201008','0201009','0201010') 
AND  E2_TIPO IN('NF','DP','FT')) OR  (  E2.D_E_L_E_T_=' ' and e2_saldo>0 AND TO_DATE(e2.e2_emissao, 'YYYYMMDD') <= SYSDATE
AND E2_NATUREZ IN( '0205097','0201001','0201002','0101001','0102003','0201003','0201004','0201005','0201006','0201007','0201008','0201009','0201010') 
AND  E2_TIPO IN('NF','DP','FT') AND E2_HIST = 'WHOLESALE' AND E2_SALDO>0))
AND
e21.E2_FORNECE = e2.E2_FORNECE 
AND e2.e2_prefixo = e21.e2_prefixo 
AND e21.E2_LOJA = e2.E2_LOJA AND
e21.E2_NUM = e2.E2_NUM) 
UNION ALL


SELECT '06' as CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM((E2_SALDO+e2_acresc)-e2_decresc)  as VALOR, 
    'CNH' AS COMARCA,
        '4.CONTAS A PAGAR'  AS GRUPO,
        'MAQUINAS / WHOLESALE' AS  SUBGRUPO
        FROM  SIGA_PRODUCAO12.SE2060 e21
WHERE EXISTS(SELECT 
DISTINCT  E2_NUM, E2_LOJA,e2_prefixo,E2_FORNECE, E2_SALDO,E2_PARCELA
FROM SIGA_PRODUCAO12.SE2060 e2
LEFT JOIN SIGA_PRODUCAO12.SD1060 D1 ON
   D1_DOC = E2_NUM AND D1_FORNECE = E2_FORNECE AND SUBSTR(e2.e2_prefixo,0,2) = D1_FILIAL AND D1_LOJA = E2_LOJA
   LEFT JOIN SIGA_PRODUCAO12.SB1060   D1 ON
   D1_COD = B1_COD 
WHERE  ((B1_TIPO IN ('PV') and E2.D_E_L_E_T_=' ' and e2_saldo>0 AND TO_DATE(e2.e2_emissao, 'YYYYMMDD') <= SYSDATE
AND E2_NATUREZ IN('0205097', '0201001','0201002','0101001','0102003','0201003','0201004','0201005','0201006','0201007','0201008','0201009','0201010') 
AND  E2_TIPO IN('NF','DP','FT')) OR  (  E2.D_E_L_E_T_=' ' and e2_saldo>0 AND TO_DATE(e2.e2_emissao, 'YYYYMMDD') <= SYSDATE
AND E2_NATUREZ IN('0205097', '0201001','0201002','0101001','0102003','0201003','0201004','0201005','0201006','0201007','0201008','0201009','0201010') 
AND  E2_TIPO IN('NF','DP','FT') AND E2_HIST = 'WHOLESALE' AND E2_SALDO>0))
AND
e21.E2_FORNECE = e2.E2_FORNECE 
AND e2.e2_prefixo = e21.e2_prefixo 
AND e21.E2_LOJA = e2.E2_LOJA AND
e21.E2_NUM = e2.E2_NUM) 


UNION ALL


SELECT '08' as CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM((E2_SALDO+e2_acresc)-e2_decresc)  as VALOR, 
    'CNH' AS COMARCA,
        '4.CONTAS A PAGAR'  AS GRUPO,
        'MAQUINAS / WHOLESALE' AS  SUBGRUPO
        FROM  SIGA_PRODUCAO12.SE2080 e21
WHERE EXISTS(SELECT 
DISTINCT  E2_NUM, E2_LOJA,e2_prefixo,E2_FORNECE, E2_SALDO,E2_PARCELA
FROM SIGA_PRODUCAO12.SE2080 e2
LEFT JOIN SIGA_PRODUCAO12.SD1080 D1 ON
   D1_DOC = E2_NUM AND D1_FORNECE = E2_FORNECE AND SUBSTR(e2.e2_prefixo,0,2) = D1_FILIAL AND D1_LOJA = E2_LOJA
   LEFT JOIN SIGA_PRODUCAO12.SB1040   D1 ON
   D1_COD = B1_COD 
WHERE E2.D_E_L_E_T_=' ' and e2_saldo>0 AND TO_DATE(e2.e2_emissao, 'YYYYMMDD') <= SYSDATE
AND E2_NATUREZ IN( '0201001','0201002','0101001','0102003','0201003','0201004','0201005','0201006','0201007','0201008','0201009','0201010') 
AND  E2_TIPO IN('NF','DP','FT')AND B1_TIPO IN ('PV')
AND
e21.E2_FORNECE = e2.E2_FORNECE 
AND e2.e2_prefixo = e21.e2_prefixo 
AND e21.E2_LOJA = e2.E2_LOJA AND
e21.E2_NUM = e2.E2_NUM)

UNION ALL


SELECT '11' as CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM((E2_SALDO+e2_acresc)-e2_decresc)  as VALOR, 
    'CNH' AS COMARCA,
        '4.CONTAS A PAGAR'  AS GRUPO,
        'MAQUINAS / WHOLESALE' AS  SUBGRUPO
        FROM  SIGA_PRODUCAO12.SE2110 e21
WHERE EXISTS(SELECT 
DISTINCT  E2_NUM, E2_LOJA,e2_prefixo,E2_FORNECE, E2_SALDO,E2_PARCELA
FROM SIGA_PRODUCAO12.SE2110 e2
LEFT JOIN SIGA_PRODUCAO12.SD1110 D1 ON
   D1_DOC = E2_NUM AND D1_FORNECE = E2_FORNECE AND SUBSTR(e2.e2_prefixo,0,2) = D1_FILIAL AND D1_LOJA = E2_LOJA
   LEFT JOIN SIGA_PRODUCAO12.SB1040   D1 ON
   D1_COD = B1_COD 
WHERE E2.D_E_L_E_T_=' ' and e2_saldo>0 AND TO_DATE(e2.e2_emissao, 'YYYYMMDD') <= SYSDATE
AND E2_NATUREZ IN( '0205097','0201001','0201002','0101001','0102003','0201003','0201004','0201005','0201006','0201007','0201008','0201009','0201010') 
AND  E2_TIPO IN('NF','DP','FT')AND B1_TIPO IN ('PV')
AND
e21.E2_FORNECE = e2.E2_FORNECE 
AND e2.e2_prefixo = e21.e2_prefixo 
AND e21.E2_LOJA = e2.E2_LOJA AND
e21.E2_NUM = e2.E2_NUM)

UNION ALL


SELECT '07' as CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM((E2_SALDO+e2_acresc)-e2_decresc)  as VALOR, 
    'CNH' AS COMARCA,
        '4.CONTAS A PAGAR'  AS GRUPO,
        'MAQUINAS / WHOLESALE' AS  SUBGRUPO
        FROM  SIGA_PRODUCAO12.SE2070 e21
WHERE EXISTS(SELECT 
DISTINCT  E2_NUM, E2_LOJA,e2_prefixo,E2_FORNECE, E2_SALDO,E2_PARCELA
FROM SIGA_PRODUCAO12.SE2070 e2
LEFT JOIN SIGA_PRODUCAO12.SD1070 D1 ON
   D1_DOC = E2_NUM AND D1_FORNECE = E2_FORNECE AND SUBSTR(e2.e2_prefixo,0,2) = D1_FILIAL AND D1_LOJA = E2_LOJA
   LEFT JOIN SIGA_PRODUCAO12.SB1070   D1 ON
   D1_COD = B1_COD 
WHERE E2.D_E_L_E_T_=' ' and e2_saldo>0 AND TO_DATE(e2.e2_emissao, 'YYYYMMDD') <= SYSDATE
AND E2_NATUREZ IN( '0201001','0201002','0101001','0102003','0201003','0201004','0201005','0201006','0201007','0201008','0201009','0201010') 
AND  E2_TIPO IN('NF','DP','FT')AND B1_TIPO IN ('PV')
AND
e21.E2_FORNECE = e2.E2_FORNECE 
AND e2.e2_prefixo = e21.e2_prefixo 
AND e21.E2_LOJA = e2.E2_LOJA AND
e21.E2_NUM = e2.E2_NUM)

UNION ALL


SELECT '23' as CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM((E2_SALDO+e2_acresc)-e2_decresc)  as VALOR, 
    'CNH' AS COMARCA,
        '4.CONTAS A PAGAR'  AS GRUPO,
        'MAQUINAS / WHOLESALE' AS  SUBGRUPO
        FROM  SIGA_PRODUCAO12.SE2230 e21
WHERE EXISTS(SELECT 
DISTINCT  E2_NUM, E2_LOJA,e2_prefixo,E2_FORNECE, E2_SALDO,E2_PARCELA
FROM SIGA_PRODUCAO12.SE2230 e2
LEFT JOIN SIGA_PRODUCAO12.SD1230 D1 ON
   D1_DOC = E2_NUM AND D1_FORNECE = E2_FORNECE AND SUBSTR(e2.e2_prefixo,0,2) = D1_FILIAL AND D1_LOJA = E2_LOJA
   LEFT JOIN SIGA_PRODUCAO12.SB1230   D1 ON
   D1_COD = B1_COD 
WHERE E2.D_E_L_E_T_=' ' and e2_saldo>0 AND TO_DATE(e2.e2_emissao, 'YYYYMMDD') <= SYSDATE
AND E2_NATUREZ IN( '0201001','0201002','0101001','0102003','0201003','0201004','0201005','0201006','0201007','0201008','0201009','0201010') 
AND  E2_TIPO IN('NF','DP','FT')AND B1_TIPO IN ('PV')
AND
e21.E2_FORNECE = e2.E2_FORNECE 
AND e2.e2_prefixo = e21.e2_prefixo 
AND e21.E2_LOJA = e2.E2_LOJA AND
e21.E2_NUM = e2.E2_NUM)


UNION ALL


SELECT '24' as CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM((E2_SALDO+e2_acresc)-e2_decresc)  as VALOR, 
    'AGCO' AS COMARCA,
        '4.CONTAS A PAGAR'  AS GRUPO,
        'MAQUINAS / WHOLESALE' AS  SUBGRUPO
        FROM  SIGA_PRODUCAO12.SE2240 e21
WHERE EXISTS(SELECT 
DISTINCT  E2_NUM, E2_LOJA,e2_prefixo,E2_FORNECE, E2_SALDO,E2_PARCELA
FROM SIGA_PRODUCAO12.SE2240 e2
LEFT JOIN SIGA_PRODUCAO12.SD1240 D1 ON
   D1_DOC = E2_NUM AND D1_FORNECE = E2_FORNECE AND SUBSTR(e2.e2_prefixo,0,2) = D1_FILIAL AND D1_LOJA = E2_LOJA
   LEFT JOIN SIGA_PRODUCAO12.SB1040   D1 ON
   D1_COD = B1_COD 
WHERE E2.D_E_L_E_T_=' ' and e2_saldo>0 AND TO_DATE(e2.e2_emissao, 'YYYYMMDD') <= SYSDATE
AND E2_NATUREZ IN( '0201001','0201002','0101001','0201003','0201004','0201005','0201006','0201007','0201008','0201009','0201010') 
AND  E2_TIPO IN('NF','DP','FT')AND B1_TIPO IN ('PV')    
AND
e21.E2_FORNECE = e2.E2_FORNECE 
AND e2.e2_prefixo = e21.e2_prefixo 
AND e21.E2_LOJA = e2.E2_LOJA AND
e21.E2_NUM = e2.E2_NUM)

''')

PC = pd.DataFrame(PC,columns=['CodEmp','DATA','VALOR','COMARCA','GRUPO','SUBGRUPO'])
PC['DATA'] = pd.to_datetime(PC['DATA']).apply(lambda x: x.date())


MsPws = os.environ.get('MsPws')

import pymysql

conn = pymysql.connect(host='10.1.20.159',
                       port=3306,
                       user='admin_dw', 
                       passwd=MsPws,  
                       db='qlikviewdb',
                       charset='utf8')
my = conn.cursor()


dup_vencer.fillna(0,inplace=True)

cols = ",".join([str(i) for i in dup_vencer.columns.tolist()])

# Insert DataFrame recrds one by one.
for i,row in dup_vencer.iterrows():

    sql = "INSERT INTO financeiro_pos (" +cols +''') VALUES (''' + "%s,"*(len(row)-1) + '''%s)'''
    my.execute(sql, tuple(row))
    conn.commit()


# In[23]:


dup_vencidas.fillna(0,inplace=True)

cols = ",".join([str(i) for i in dup_vencidas.columns.tolist()])

# Insert DataFrame recrds one by one.
for i,row in dup_vencidas.iterrows():

    sql = "INSERT INTO financeiro_pos (" +cols +''') VALUES (''' + "%s,"*(len(row)-1) + '''%s)'''
    my.execute(sql, tuple(row))
    conn.commit()


# In[24]:


juri.fillna(0,inplace=True)

cols = ",".join([str(i) for i in juri.columns.tolist()])

# Insert DataFrame recrds one by one.
for i,row in juri.iterrows():

    sql = "INSERT INTO financeiro_pos (" +cols +''') VALUES (''' + "%s,"*(len(row)-1) + '''%s)'''
    my.execute(sql, tuple(row))
    conn.commit()


# In[25]:


fin_avencer.fillna(0,inplace=True)

cols = ",".join([str(i) for i in fin_avencer.columns.tolist()])

# Insert DataFrame recrds one by one.
for i,row in fin_avencer.iterrows():

    sql = "INSERT INTO financeiro_pos (" +cols +''') VALUES (''' + "%s,"*(len(row)-1) + '''%s)'''
    my.execute(sql, tuple(row))
    conn.commit()



fin_vencidas.fillna(0,inplace=True)

cols = ",".join([str(i) for i in fin_vencidas.columns.tolist()])

# Insert DataFrame recrds one by one.
for i,row in fin_vencidas.iterrows():

    sql = "INSERT INTO financeiro_pos (" +cols +''') VALUES (''' + "%s,"*(len(row)-1) + '''%s)'''
    my.execute(sql, tuple(row))
    conn.commit()


# In[27]:




# In[28]:


PC.fillna(0,inplace=True)

cols = ",".join([str(i) for i in PC.columns.tolist()])

# Insert DataFrame recrds one by one.
for i,row in PC.iterrows():

    sql = "INSERT INTO financeiro_pos (" +cols +''') VALUES (''' + "%s,"*(len(row)-1) + '''%s)'''
    my.execute(sql, tuple(row))
    conn.commit()

conn.close()




## MOVIMENTO SK 
OraclHostSK = os.environ.get('OraclHostSK')
OraclPswSK = os.environ.get('OraclPswSK')
import cx_Oracle
import pandas as pd
#cx_Oracle.init_oracle_client(lib_dir="C:/oracle/instantclient_19_6")
dsn_tnssk = cx_Oracle.makedsn(OraclHostSK, '1521', service_name='W8PATW_999999_PP_high.paas.oracle.com') # if needed, place an 'r' before any parameter in order to address special characters such as '\'.
connsk = cx_Oracle.connect(user='USR_QLIK_AGR', password=OraclPswSK, dsn=dsn_tnssk) # if needed, place an 'r' before any parameter in order to address special characters such as '\'. For example, if your user name contains '\', you'll need to place 'r' before the user name: user=r'User Name'

Csk = connsk.cursor()



dup_vencer = Csk.execute('''
SELECT '09' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) as Valor,
         'SK AUTOMOTIVE' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '1.DUPLICATAS A VENCER' AS  SUBGRUPO FROM siga_prdsk12_new.SE1090
WHERE  

TRIM(e1_vencrea) IS NOT NULL and
TO_DATE(e1_vencrea, 'YYYYMMDD')>= SYSDATE
AND e1_fluxo='S' AND
E1_SALDO>0  AND d_e_l_e_t_=' '

UNION ALL

SELECT '09' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) as Valor,
         'SK AUTOMOTIVE' AS COMARCA,
        '2.CONTAS A RECEBER' AS GRUPO,
        '2.DUPLICATAS VENCIDAS' AS  SUBGRUPO FROM siga_prdsk12_new.SE1090
WHERE 
(substr(E1_TIPO,0,2)  IN('NF','DP','NP','FT') AND
TO_DATE(e1_vencrea, 'YYYYMMDD')<= SYSDATE-1 and TO_DATE(e1_vencrea, 'YYYYMMDD')>= TO_DATE('20160101', 'YYYYMMDD')) and 
E1_SALDO>0  AND d_e_l_e_t_=' 'AND TRIM(e1_vencrea) IS NOT NULL 
''')

dup_vencer = pd.DataFrame(dup_vencer,columns=['CodEmp','DATA','VALOR','COMARCA','GRUPO','SUBGRUPO'])
dup_vencer['DATA'] = pd.to_datetime(dup_vencer['DATA']).apply(lambda x: x.date())

juri = Csk.execute('''
SELECT '09' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY')  AS DATA,
    SUM(E1_SALDO) as Valor,
         'SK AUTOMOTIVE' AS COMARCA,
        '9.JURIDICOS' AS GRUPO,
        'AÇÕES' AS  SUBGRUPO
        FROM siga_prdsk12_new.SE1090
WHERE 
(substr(E1_TIPO,0,2)  IN('NF','DP','NP','FT','BC','CH') AND TO_DATE(e1_vencrea, 'YYYYMMDD')<=  TO_DATE('20160101', 'YYYYMMDD'))
AND 
E1_SALDO>0  AND d_e_l_e_t_=' ' AND E1_SITUACA NOT IN ('O','Q') AND TRIM(e1_vencrea) IS NOT NULL ''')

juri = pd.DataFrame(juri,columns=['CodEmp','DATA','VALOR','COMARCA','GRUPO','SUBGRUPO'])
juri['DATA'] = pd.to_datetime(juri['DATA']).apply(lambda x: x.date())

cppecas = Csk.execute('''SELECT '09' AS CodEmp,
    TO_DATE(SYSDATE,'DD/MM/YY') AS DATA,
    SUM(E2_SALDO) as Valor,
         'SK AUTOMOTIVE' AS COMARCA,
        '4.CONTAS A PAGAR' AS GRUPO,
        'FORNECEDOR / PEÇAS' AS  SUBGRUPO
FROM SIGA_PRDSK12_NEW.se2090
WHERE e2_naturez IN( '0102003','0201005','0201003','0201004') AND d_e_l_e_t_=' ' AND E2_SALDO>0  AND E2_TIPO<>'NDF' and TO_DATE(e2_vencrea, 'YYYYMMDD')>=SYSDATE AND e2_fornece<>'214642' ''')

cppecas = pd.DataFrame(cppecas,columns=['CodEmp','DATA','VALOR','COMARCA','GRUPO','SUBGRUPO'])
cppecas['DATA'] = pd.to_datetime(cppecas['DATA']).apply(lambda x: x.date())

import pymysql

conn = pymysql.connect(host='10.1.20.159',
                       port=3306,
                       user='admin_dw', 
                       passwd=MsPws,  
                       db='qlikviewdb',
                       charset='utf8'
					   )
my = conn.cursor()

 
    
dup_vencer.fillna(0,inplace=True)

cols = ",".join([str(i) for i in dup_vencer.columns.tolist()])

# Insert DataFrame recrds one by one.
for i,row in dup_vencer.iterrows():

    sql = "INSERT INTO financeiro_pos (" +cols +''') VALUES (''' + "%s,"*(len(row)-1) + '''%s)'''
    my.execute(sql, tuple(row))
    conn.commit()

juri.fillna(0,inplace=True) 

cols = ",".join([str(i) for i in juri.columns.tolist()])

# Insert DataFrame recrds one by one.
for i,row in juri.iterrows():

    sql = "INSERT INTO financeiro_pos (" +cols +''') VALUES (''' + "%s,"*(len(row)-1) + '''%s)'''
    my.execute(sql, tuple(row))
    conn.commit()
    
    


cppecas.fillna(0,inplace=True)

cols = ",".join([str(i) for i in cppecas.columns.tolist()])

# Insert DataFrame recrds one by one.
for i,row in cppecas.iterrows():

    sql = "INSERT INTO financeiro_pos (" +cols +''') VALUES (''' + "%s,"*(len(row)-1) + '''%s)'''
    my.execute(sql, tuple(row))
    conn.commit()
conn.close()

