package agentes;

import General.Contenedor;
import jade.core.Agent;
import jade.core.behaviours.Behaviour;
import jade.lang.acl.ACLMessage;

public class AgenteBasePadre extends Agent {
    @Override
    protected void setup() {
        System.out.println("creado: " + getLocalName());
        addBehaviour(new Comportamiento());
    }
    class Comportamiento extends Behaviour {

        @Override
        public void action() {
            ACLMessage acl = blockingReceive();
            System.out.println(acl.getContent());
            doDelete();
        }
        @Override
        public boolean done() {
            return true;
        }
    }
    @Override
    protected void takeDown() {
        Contenedor c = (Contenedor) getArguments()[0];
        c.crearHijo("HijoNUevo",new Object[]{c});
        System.out.println("hijo creado");

    }


}
