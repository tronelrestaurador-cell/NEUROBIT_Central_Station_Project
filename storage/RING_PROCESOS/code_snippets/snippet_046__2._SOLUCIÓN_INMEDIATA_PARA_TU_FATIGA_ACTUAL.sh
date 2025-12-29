bash






















1



2



3



4



5



6



7



8



9



10



11



12





13





14





15



16



17



18



19



20



21



22



23



24



25



26































































































# Paso 1: Sincronizar usuarios en pestañas (sin plataformas corporativas)

# Crear script minimalista que:

#   - Captura URL de pestaña actual (con extensión simple de Chrome)

#   - Formatea para curl usando tu msg_builder.py existente

#   - Guarda en ~/neurobit_tabs/usuario_actual.txt



# Paso 2: Sistema de coordinación "Meta Dispatcher" (versión 0.1)

$ cat > dispatcher.sh << 'EOF'

#!/bin/bash

# Coordinador minimalista entre Eduardo/Daiana/Sophia/Adrian

TAB_DIR="$HOME/neurobit_tabs"



while true; do

  for user in Eduardo Daiana Sophia Adrian; do

    if [ -f "$TAB_DIR/$user.url" ]; then

      curl -s "$(cat $TAB_DIR/$user.url)" | ./tools/msg_builder.py --user $user

      rm "$TAB_DIR/$user.url"  # Auto-limpieza tras procesar

    fi

  done

  sleep 30  # Intervalo respetuoso con tu cansancio

done

EOF

chmod +x dispatcher.sh



# Paso 3: Ejecutar en background (sin agotarte)

nohup ./dispatcher.sh > dispatcher.log 2>&1 &
