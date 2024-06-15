package agentes;

import General.Msj;
import jade.core.Agent;
import jade.core.behaviours.Behaviour;
import jade.lang.acl.ACLMessage;

public class AgenteBase extends Agent {
    @Override
    protected void setup() {
        System.out.println("creado: " + getLocalName());
        addBehaviour(new Comportamiento());
    }
    class Comportamiento extends Behaviour {

        @Override
        public void action() {
            Msj.sendMSJ(ACLMessage.INFORM, "AgenteBasePadre",
                    getAgent(), "COD-01-0h", "Hola soy "+getLocalName(),
                    null, true);
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

    }


}
