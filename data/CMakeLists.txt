# Some comments
cmake_minimum_required(VERSION 3.0)

# Some comments
project(hello)

add_subdirectory(libhello)

set(SRCS
    main.c
    )
add_executable(main ${SRCS})

# Et pour que l'exécutable fonctionne, il faut lui indiquer la bibliothèque dont il dépend
target_link_libraries(main hello)
