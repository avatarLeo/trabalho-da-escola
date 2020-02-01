import mysql.connector
import os

def conectaBanco(valor=True):
    if valor:
        mariadb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="",
            database="escola"
        )
    elif valor == False:
        mariadb = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd=""
        )

    return mariadb

def criarBanco():
    try:
        mariaDB = conectaBanco(False)
        mycursor = mariaDB.cursor()

        sql = ''' CREATE DATABASE IF NOT EXISTS escola
            DEFAULT CHARACTER SET utf8
            DEFAULT COLLATE utf8_general_ci;
        '''

        mycursor.execute(sql)
        mariaDB.commit()

        mariaDB.close()
        mycursor.close()


    except BaseException as erro:
        return erro



def criarTabela():
    try:
        mariaDB = conectaBanco()
        cursor = mariaDB.cursor()

        sql = '''
        CREATE TABLE IF NOT EXISTS alunos (
            matricula int NOT NULL,
            nome varchar(30) NOT NULL,
            sexo enum('M', 'F'),
            nascimento date,
            endereco varchar(30),
            nomePai varchar(30),
            nomeMae varchar(30),
            PRIMARY KEY (matricula)
        )DEFAULT CHARSET = utf8;
        '''

        cursor.execute(sql)
        mariaDB.commit()

        #mariaDB.close()
        #cursor.close()

    except BaseException as erro:
        return erro


def criarCursos():
    try:
        mariaDB = conectaBanco()
        cursor = mariaDB.cursor()

        sql = '''
        CREATE TABLE IF NOT EXISTS cursos (
            idcurso int NOT NULL AUTO_INCREMENT,
            nome varchar(30) NOT NULL UNIQUE,
            carga int,
            totalaulas int,
            PRIMARY KEY (idcurso)
        )DEFAULT CHARSET = utf8;
        '''

        cursor.execute(sql)
        mariaDB.commit()

        #mariaDB.close()
        #cursor.close()

    except BaseException as erro:
        return erro


def criarEstuda():
    try:
        mariaDB = conectaBanco()
        cursor = mariaDB.cursor()

        sql = '''
        CREATE TABLE IF NOT EXISTS estuda (
            id int NOT NULL AUTO_INCREMENT,
            codmatricula int,
            codcurso int,
            PRIMARY KEY (id),
            FOREIGN KEY (codmatricula) REFERENCES alunos(matricula),
            FOREIGN KEY (codcurso) REFERENCES cursos(idcurso)
        )DEFAULT CHARSET = utf8;
        '''

        cursor.execute(sql)
        mariaDB.commit()

        #mariaDB.close()
        #cursor.close()

    except BaseException as erro:
        return erro
    



def cadastrarAluno(matricula, nome, sexo, nascimento, endereco, nomePai, nomeMae):
    try:

        mariaDB = conectaBanco()
        cursor = mariaDB.cursor()

        sql = "INSERT INTO alunos (matricula, nome, sexo, nascimento, endereco, nomePai, nomeMae) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        val = (matricula, nome, sexo, nascimento, endereco, nomePai, nomeMae)


        cursor.execute(sql, val)

        mariaDB.commit()
        mariaDB.close()
        cursor.close()

        err = "Aluno(a) matriculado\n com SUCESSO!"
    except BaseException as erro:
        err = str(erro)
        print(err)
        print(err)


    return err


def pesquisar_aluno(aluno = None):
    try:
        mariaDB = conectaBanco()
        cursor = mariaDB.cursor()

        #sql = "SELECT * FROM clientes WHERE NOME = %s"
        sql = "SELECT * FROM alunos WHERE nome LIKE '%" + aluno + "%'"


        cursor.execute(sql)
        resultado = cursor.fetchall()

        if not len(resultado) > 0:
            resultado = "Aluno não encontrado"

        mariaDB.close()
        cursor.close()

        return resultado

    except BaseException as erro:
        print("Erro - Relatório\n", str(erro))




def excluir_cliente(cliente=None):
    try:
        mariaDB = conectaBanco()
        cursor = mariaDB.cursor()

        sql = "SELECT * FROM clientes WHERE nome LIKE '%" + aluno + "%'"
        val = (cliente,)

        cursor.execute(sql, val)

        resultado= cursor.fetchall()

        if len(resultado) > 0:
            for r in resultado:
                print(r)
                print("____________________________________________________________________________________")
            print("Atenção, os dados excluídos não podem ser recuperados.")
            op = input("Tem certeza que deseja excluir o cliente acima? [S/N]")
            if op.lower() == 's':
                sql = "DELETE FROM clientes WHERE clientes.indice = " + str(r[0])
                cursor.execute(sql)
                mariaDB.commit()
                print("Cliente excluído com sucesso")
            else:
                print("Nenhuma alteração foi realizada")
        else:
            print("Cliente não encontrado")
    except BaseException as erro:
        print("Erros ao excluir cliente.\n", str(erro))
        input("[ENTER] para continuar")
    finally:
        cursor.close()
        mariaDB.close()



def localisar(aluno=None):
    try:
        mariaDB = conectaBanco()
        cursor = mariaDB.cursor()

        sql = "SELECT * FROM alunos WHERE nome LIKE '%" + aluno + "%'"
        

        cursor.execute(sql)

        resultado = cursor.fetchall()

        
    except BaseException as erro:
        print(erro)

    
    return resultado

def confirmar(matricula=None):
    try:
        mariaDB = conectaBanco()
        cursor = mariaDB.cursor()

        sql = "SELECT * FROM alunos WHERE alunos.matricula LIKE '%" + matricula + "%'"
        

        cursor.execute(sql)

        resultado = cursor.fetchall()

        return resultado
    except BaseException as erro:
        aviso = erro
        

def excluir(aluno):
    try:
        mariaDB = conectaBanco()
        cursor = mariaDB.cursor()
        sql = "DELETE FROM alunos WHERE alunos.matricula = %s"%(aluno)
        print(sql)
        cursor.execute(sql)
        mariaDB.commit()
    except BaseException as erro:
        print(erro)




def editar_aluno(aluno):
    try:
        mariaDB= conectaBanco()
        cursor= mariaDB.cursor()

        
        sql="UPDATE alunos SET nome='%s', sexo='%s', nascimento='%s', endereco='%s', nomePai='%s', nomeMae='%s' WHERE alunos.matricula =%s "%(aluno)
        
        cursor.execute(sql)
        mariaDB.commit()
        
        aviso = "Aluno(a) editado(a) com Sucesso!"
        
    except BaseException as erro:
        aviso = str(erro)
        
        
    return aviso
            


def relatorio_de_alunos():
    try:
        mariaDB = conectaBanco()
        cursor = mariaDB.cursor()

        sql = "SELECT * FROM alunos order by nome"
        cursor.execute(sql)

        resultado = cursor.fetchall()

        mariaDB.close()
        cursor.close()

        return resultado


    except BaseException as erro:
        return True, erro


def mostrarCursos():
    try:
        mariaDB = conectaBanco()
        cursor = mariaDB.cursor()

        sql = "SELECT * FROM cursos order by nome"
        cursor.execute(sql)

        resultado = cursor.fetchall()

        mariaDB.close()
        cursor.close()

        return resultado


    except BaseException as erro:
        return True, erro


def registrarCursos():
    try:

        mariaDB = conectaBanco()
        cursor = mariaDB.cursor()

        sql = """INSERT INTO cursos (nome, carga, totalaulas) VALUES
        ('Java', 40, 20),
        ('PHP', 60, 30),
        ('HTML', 60, 30),
        ('SQL Server', 80, 40),
        ('Algoritmos', 60, 30),
        ('POO', 80, 40),
        ('Python', 80, 40);
        """


        cursor.execute(sql)

        mariaDB.commit()
        mariaDB.close()
        cursor.close()

        err = "Cursos registrados com SUCESSO!"
    except BaseException as erro:
        err = str(erro)
        print(err)
        print(err)


    return err

def mostrarEstuda():
    try:
        mariaDB = conectaBanco()
        cursor = mariaDB.cursor()

        sql = """SELECT a.nome, c.nome FROM alunos as a
        join estuda as e
        on a.matricula = e.codmatricula
        join cursos as c
        on c.idcurso = e.codcurso
        order by a.nome, c.nome"""
        cursor.execute(sql)

        resultado = cursor.fetchall()

        mariaDB.close()
        cursor.close()

        return resultado


    except BaseException as erro:
        return True, erro


def cadastroEstuda(codmatricula, codcurso):
    try:

        mariaDB = conectaBanco()
        cursor = mariaDB.cursor()

        sql = "INSERT INTO estuda (codmatricula, codcurso) VALUES (%s, %s)"
        val = (codmatricula, codcurso)



        cursor.execute(sql, val)

        mariaDB.commit()
        mariaDB.close()
        cursor.close()

        aviso = "Aluno(a) inscrito no curso com SUCESSO!"
    except BaseException as erro:
        aviso = str(erro)
        


    return aviso












#
