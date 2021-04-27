***
# GIT COMMANDS
***

1. [Firts steps in git](#firts-steps-in-git) 
2. Creating Alias to commands
3. Creating my firts project in git
4. Add files to stage
5. Ignoring files
6. "Diff" Command
7. Commits
8. Logs
9. Reverse Commits
10. Rename or Move
11. Branches
12. Tags

***
# GITHUB
***

1. Firts steps
2. Clone Command
3. PULL PUSH & FETCH

***
***

## FIRTS STEPS IN GIT

Firts commands 

+git config --global user.name "nickname"
+git config --global user.email "email.com"

Location

+ git config --global -e	//para saber el usuario registrado en la maquina.
+ git config --global -l // Sin peligro a modificar el archivo.

## CREATING ALIAS TO COMMANDS

+git config --global alias.lg "log --oneline --decorate --all --graph"
+git lg

+git config --global alias-s "status -s -b"
+git s

Location

+ git config --global -e
+ git config --global -l	//mas seguro, solo muestra lista y no hay peligro de modificar algo	

## CREATING MY FIRTS PROJECT IN GIT

+ git -- version
+ git help
+ git init	// iniciar proyecto en git
+ git status
+ git status -s -b

## ADD FILES TO STAGE

+ git add .  	// agregar todos los archivos o poner el nombre del archivo
+ git add nombredelarchivo
+ git add *.png	//agrega todos los archivos con eza extension
+ git add carpeta/ 	//se agregan todos lo archivos contenidos en la carpeta
+ git add carpeta/*.txt	//agrega todos los acrchivos con esa entension que esten 					en la carpeta
+ git add -A 	//agrega todos los archivos
+ git add --all
+ git add "*.txt"	/agrega todos los cambios en archivos con esa extension
+ git add *.txt		/agrega todos del directorio actual
+ git add lista_de_archivos
+ git add -u	//actualiza todo, recomendable si haces cambios fuera de git
+ git reset nombredel_archivo_a_excluir_del:_commit

## INGORING FILES

Crear archivo en la raiz del proyecto .gitignore
hacer listado de archivos a ignorar en git
*.log
archivo.txt
carpeta/

no aparecen los archivos pero si el .gitignore, hay que agregarlo y hacer el commit

## DIFF COMMAND

Show the diferents betwen files

+ git diff
+ git diff --staged

## COMMITS

+ git commit -m "comentario solicitado por git"
+ git commit -am "comentario"	//se agrega y guarda el commit, solo de archivos con 				seguimiento que en algun momento se agregaron con add.
+ git commit --amend -m "mensaje"	/arregla un commit con un mensaje mas especifico o 						sin errores
+ git reset --soft HEAD^ 	//otra forma de volver a hacer commit guardando cambios o 					 solo cambiando el mensaje sin hacer mas logs de commits
+ git reset --soft ID_de_punto_a_restaurar // soft no destruye nada
+ git reset --hard ID_de_punto_a_restaurar	//hard destruye todo lo superior al punto 							especificado

## LOGS

+ git log	//muestra los cambios en el proyecto
+ git log --oneline	//mas resumido
+ git --oneline --decorate --all --graph	//solo info importante y muestra 							ramas

## REVERSE COMMITS

+ git reglog		//logs mas profundos
+ git reset --hard ID_de_punto_a_restaurar
+ git checkout -- .	// para revertir un cambio en todos los archivos
+ git checkout 

## RENAME OR MOVE

+ git mv name_archivo  new_name_archivo		//renombra el archivo o lo mueve
+ git rm name_archivo	//eliminar archivo

## BRANCHES

MERGE- Union de ramas

	-FAST-FORWARD
    + Cuando no hay ningun cambio en la rama master.	
	-UNIONES AUTOMATICAS
		+ GIT Detecta que no hay modificaciones en lineas iguales, sin confilctos.
	-MANUAL
		+ Git Detecta conflictos y es necesaria la intervencion humana.
		
Crear Branch

+ git config --global init.defaultBranch <name>	//cambiar el default nombre de la rama master
+ git branch nombre_branch	//crear branch
+ git checkout -b name_branch	//crear branch y te mueves de inmediato
+ git branch	//ver en que rama estamos

Moverse a otra rama

+ git checkout name_branch	//te mueve de rama
+ git diff name_rama master	//diferencias entre una rama y la master

UNIR RAMAS

+ git merge name_branch		//para unir las ramas con la master
+ git branch -m <name>	//remonbrar una rama
+ git branch -d name_branch	//elimina la rama -d (delete)

## TAGS

Son una referencia a un commit especifico, es usado para marcar versiones.

+ git tag name_tag
+ git tag		//ver tags
+ git tag -d name_tag	//eliminar tag

+ git tag -a tag_name -m "comentario del tag o version"

+ git tag -a tag_name hash_commit -m "comentario"	//para poner un tag en commits 							anteriores

+ git show tag_name	//ver comentarios del tag


***
***

# GITHUB

***
***

# FIRTS STEPS

Es una plataforma de desarrollo colaborativo de software para alojar proyectos.

Repositorio Remoto.

+ git remote add origin _url_	//para subir un repositorio a github
    + add 	agregar un repositorio
    + origin	nombre del repositorio, se puede cambiar
varios repositorios en un mismo repositorio

+ git remote -v	//muestra como se liga al github

# CLONE COMMAND

+ git clone _url_ 	//hace un clone del repositorio desde github.
+ git clone _url_ name_repositorio	//hace un clone desde github pero con un nombre especificado.

# PULL PUSH & FETCH

+ git push -u origin master	//-u para poner la rama por defecto y no es necesario 				especificar la rama en push posteriores

+ git pull	//si hiciste el -u ya no es necesario poner la rama

+ git fecth	//actualiza todo como un pull pero sin modificar nuestros cambios

+ git push --tags	//sube todos los tags.



