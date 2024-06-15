package agentes;

import General.Msj;
import jade.core.Agent;
import jade.core.behaviours.Behaviour;
import jade.lang.acl.ACLMessage;

public class AgenteHijo extends Agent {
    @Override
    protected void setup() {
        System.out.println("creado: " + getLocalName());
        addBehaviour(new Comportamiento());
    }
    class Comportamiento extends Behaviour {

        @Override
        public void action() {
            System.out.println("te envio mi mensaje");
            Msj.sendMSJ(ACLMessage.INFORM, "AgenteBase",
                    getAgent(), "COD-01-0h", "Hola soy "+getLocalName(),
                    null, true);

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
