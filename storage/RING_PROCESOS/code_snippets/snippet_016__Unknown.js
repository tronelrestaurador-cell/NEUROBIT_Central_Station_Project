javascript






















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



27



28



29



30



31



32



33





34





35



36



37



38



39



40



41



42



43



44



45



46



47



48





49



50



51



52



53



54



55





56



57



58



59





60



61





62



63



64



65





66



67



68





69



70



71



72



73



74





75



76



77



78



79



80



81



82





83



84





85



86



87





88



89



90



91



92



93



94





95



96



97



98





99



100



101



102



103





104



105



106



107



108



109



110



111





112



113





114



115





116



117





118



119



120



121



122



123





124





125



126



127



128



129



130



131



132



133





134



135



136













































































































































































































































































































































































































































































































































































































































































































































































































































































// control.js - Gestión de nodos mediante pestañas

const nodeManager = {

    nodes: {},

    initialize: function() {

        // Detectar si esta es la pestaña principal

        if (!localStorage.getItem('mainNode')) {

            localStorage.setItem('mainNode', Date.now().toString());

            this.isMainNode = true;

            document.title = "✧ ESTACIÓN PRINCIPAL - The Sofistas ✧";

        } else {

            this.isMainNode = false;

            const nodeId = 'node_' + Math.random().toString(36).substr(2, 5);

            this.registerNode(nodeId);

            document.title = `✧ NODO ${nodeId} ✧`;

        }

        

        // Comunicación entre pestañas mediante localStorage

        window.addEventListener('storage', this.handleStorageEvent.bind(this));

        

        // Enviar estado inicial si es nodo principal

        if (this.isMainNode) {

            this.broadcastSystemState();

        }

        

        // Configurar botón de procesamiento

        document.getElementById('processBtn').addEventListener('click', () => {

            this.processMessage();

        });

        

        // Actualizar estado cada 5 segundos

        setInterval(() => this.updateNodeStatus(), 5000);

    },

    

    registerNode: function(nodeId) {

        const nodeInfo = {

            id: nodeId,

            timestamp: Date.now(),

            role: this.assignRoleBasedOnTime(),

            status: 'activo'

        };

        

        // Guardar en localStorage para que otros nodos lo detecten

        localStorage.setItem(`node_${nodeId}`, JSON.stringify(nodeInfo));

        this.nodes[nodeId] = nodeInfo;

        

        return nodeInfo;

    },

    

    assignRoleBasedOnTime: function() {

        // Asignación de roles basada en momento de conexión (fractal)

        const second = new Date().getSeconds();

        const roles = ['validator', 'expander', 'dispatcher', 'sender'];

        return roles[second % roles.length];

    },

    

    processMessage: function() {

        const message = document.getElementById('messageInput').value;

        const tags = message.match(/#\w+:\w+/g) || [];

        

        if (this.isMainNode) {

            // Distribuir trabajo a nodos especializados

            tags.forEach(tag => {

                const role = tag.split(':')[0].replace('#', '');

                this.delegateTask(role, { message, tag });

            });

        } else {

            // Procesar localmente si este nodo tiene el rol adecuado

            const myRole = Object.values(this.nodes).find(n => n.id === Object.keys(this.nodes)[0])?.role;

            if (tags.some(tag => tag.includes(myRole))) {

                this.localProcess(message, tags);

            }

        }

    },

    

    delegateTask: function(role, taskData) {

        // Simular delegación a nodos específicos

        console.log(`[DELEGACIÓN] Rol ${role} - Tarea:`, taskData);

        

        // En implementación real, esto usaría IndexedDB o API de comunicación

        localStorage.setItem(`task_${role}_${Date.now()}`, JSON.stringify(taskData));

    },

    

    localProcess: function(message, tags) {

        // Procesamiento local simulado

        const result = {

            original: message,

            processed_by: Object.keys(this.nodes)[0],

            expansions: tags.map(tag => ({

                tag: tag,

                expanded: `${message} [Procesado por nodo ${tag}]`

            })),

            timestamp: Date.now()

        };

        

        document.getElementById('resultOutput').textContent = 

            JSON.stringify(result, null, 2);

    },

    

    updateNodeStatus: function() {

        // Actualizar visualización de nodos activos

        const statusDiv = document.getElementById('nodeStatus');

        let html = '<ul>';

        

        Object.values(this.nodes).forEach(node => {

            html += `<li>NODO ${node.id}: <span class="${node.status}">${node.role.toUpperCase()}</span></li>`;

        });

        

        html += '</ul>';

        statusDiv.innerHTML = html;

    },

    

    handleStorageEvent: function(e) {

        // Manejar eventos de otras pestañas

        if (e.key && e.key.startsWith('node_')) {

            const nodeId = e.key.replace('node_', '');

            if (e.newValue) {

                this.nodes[nodeId] = JSON.parse(e.newValue);

            } else {

                delete this.nodes[nodeId];

            }

        }

    },

    

    broadcastSystemState: function() {

        localStorage.setItem('systemState', JSON.stringify({

            mainNode: localStorage.getItem('mainNode'),

            timestamp: Date.now(),

            activeNodes: Object.keys(this.nodes).length

        }));

    }

};



// Iniciar al cargar la página

document.addEventListener('DOMContentLoaded', () => {

    nodeManager.initialize();

});
