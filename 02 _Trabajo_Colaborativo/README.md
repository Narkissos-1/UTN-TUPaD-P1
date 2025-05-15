
# Preguntas sobre Git y GitHub

1. **¿Qué es GitHub?**  
Es una plataforma para guardar y colaborar en proyectos con control de versiones usando Git.

2. **¿Cómo crear un repositorio en GitHub?**  
Entrás a GitHub, hacés clic en "New" o "Nuevo repositorio", completás los datos y lo creás.

3. **¿Cómo crear una rama en Git?**  
Usás el comando: `git branch nombre-de-la-rama`

4. **¿Cómo cambiar a una rama en Git?**  
Usás: `git checkout nombre-de-la-rama`

5. **¿Cómo fusionar ramas en Git?**  
Primero cambiás a la rama principal y luego hacés: `git merge nombre-de-la-rama`

6. **¿Cómo crear un commit en Git?**  
Primero hacés `git add archivo` y después `git commit -m "Mensaje"`

7. **¿Cómo enviar un commit a GitHub?**  
Después del commit hacés: `git push`

8. **¿Qué es un repositorio remoto?**  
Es una versión del repositorio guardada en línea (como en GitHub).

9. **¿Cómo agregar un repositorio remoto a Git?**  
`git remote add origin URL-del-repositorio`

10. **¿Cómo empujar cambios a un repositorio remoto?**  
`git push origin nombre-de-la-rama`

11. **¿Cómo tirar de cambios de un repositorio remoto?**  
`git pull origin nombre-de-la-rama`

12. **¿Qué es un fork de repositorio?**  
Es una copia de otro repositorio en tu cuenta de GitHub para poder modificarlo.

13. **¿Cómo crear un fork de un repositorio?**  
En la página del repositorio, hacés clic en "Fork".

14. **¿Cómo enviar una solicitud de extracción (pull request) a un repositorio?**  
Desde tu fork, hacés clic en "Compare & pull request" y seguís los pasos.

15. **¿Cómo aceptar una solicitud de extracción?**  
El dueño del repositorio entra a "Pull requests", revisa y acepta con "Merge pull request".

16. **¿Qué es una etiqueta en Git?**  
Es una marca que se usa para señalar versiones específicas del proyecto.

17. **¿Cómo crear una etiqueta en Git?**  
`git tag nombre-de-la-etiqueta`

18. **¿Cómo enviar una etiqueta a GitHub?**  
`git push origin nombre-de-la-etiqueta`

19. **¿Qué es un historial de Git?**  
Es el registro de todos los commits realizados en el proyecto.

20. **¿Cómo ver el historial de Git?**  
`git log`

21. **¿Cómo buscar en el historial de Git?**  
Podés usar: `git log --grep="texto"`

22. **¿Cómo borrar el historial de Git?**  
No se recomienda. Pero podés reiniciar el repo con: `git init` (destruye el historial anterior).

23. **¿Qué es un repositorio privado en GitHub?**  
Es un repositorio que solo pueden ver las personas autorizadas.

24. **¿Cómo crear un repositorio privado en GitHub?**  
Al crear el repositorio, marcás la opción "Private".

25. **¿Cómo invitar a alguien a un repositorio privado en GitHub?**  
Desde "Settings" > "Collaborators", agregás al usuario.

26. **¿Qué es un repositorio público en GitHub?**  
Es un repositorio que cualquiera puede ver.

27. **¿Cómo crear un repositorio público en GitHub?**  
Cuando lo creás, elegís la opción "Public".

28. **¿Cómo compartir un repositorio público en GitHub?**  
Copiás la URL del repositorio y la pasás.
